#!/usr/bin/env python
"""
This module is the core module of the testing 'framework'.

Exported classes:

RegressionBase -- Inherits from unittest.TestCase, this class is the base testing class for the regression test classes,
the class defines helper methods to be used within the class, e.g.: the execute method will execute a casapy executable
python script.

RegressionHelper -- Defines static helper methods to be used, e.g.: data management.

regressionLogger -- A python logger

RegressionRunner -- Class to locate and execute the testing classes by using nose, within casa:
> from regression_utils import RegressionRunner
> RegressionRunner.execute_regression("regression_b0319")
"""

import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import string
import importlib
import inspect
import shutil
import logging
import hashlib
import threading
import imp
from contextlib import contextmanager
from contextlib import closing
from functools import wraps

import unittest
import nose

from testc.nose.plugin import psprofile
from testc import regression

import coverage

__test__ = False
__all__ = ["RegressionHelper", "RegressionBase", "regressionExecutor", "regressionLogger", "injectMod", "injectEnv"]

regressionLogger = logging.getLogger("RegressionLogger")

cover_packages = [
	# casa
	"casac",
	# tools
	"accum", "applycal", "asdmsummary", "autoclean", "bandpass", "blcal", "boxit", "browsetable", "calstat",
	"clean", "clearcal", "clearplot", "clearstat", "cvel", "deconvolve", "exportfits", "exportuvfits", "feather",
	"find",	"fixvis", "flagdata", "flagmanager", "fluxscale", "ft", "gaincal", "gencal", "hanningsmooth", "hanningsmooth2",
	"imcontsub", "imfit", "imhead", "immath", "immoments", "importasdm", "importfits", "importgmrt", "importuvfits",
	"importvla", "imregrid", "imsmooth", "imstat", "imval", "imview", "listcal", "listhistory", "listobs", "listvis",
	"mosaic", "msmoments", "mstransform", "msview", "partition", "plotants", "plotcal", "plotms", "polcal", "rmtables",
	"setjy", "simalma", "simobserve", "simanalyze", "smoothcal", "specfit", "split", "split2", "uvcontsub", "uvmodelfit",
	"uvsub", "viewer", "vishead", "visstat", "widefield", 
	# asap
	"sdcal", "sdsmooth", "sdbaseline", "sdbaseline2", "sdreduce", "sdcoadd", "sdsave", "sdscale", "sdfit", "sdplot", "sdstat",
	"sdlist", "sdflag", "sdflag2", "sdtpimaging", "sdmath", "sdimaging", "sdimprocess"
]

def injectMod(module, method = True):
	def test_injection(func):
		def wrapped(*args, **kwargs):
			testc_file, testc_path, testc_desc = imp.find_module("testc")
			module_paths = sys.path + [os.path.join(testc_path, "regression"), os.path.join(testc_path, "guide")] 			
			module_file, module_path, module_desc = imp.find_module(module, module_paths)

			if method:
				module_object = imp.load_module(module, module_file, module_path, module_desc)
				if isinstance(method, str):
					method_object = getattr(module_object, method)
				else:
					method_object = getattr(module_object, func.__name__)
				method_object()
			else:
				casa_globals = dict(globals().items() + RegressionHelper.casa_console_globals().items())
				execfile(module_path, custom_globals, locals())
			
			return func(*args, **kwargs)
		return wraps(func)(wrapped)
	return test_injection

def injectEnv(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		casa_globals = dict(RegressionHelper.casa_console_globals().items() + func.func_globals.items())
		# see http://snipplr.com/view/17819/
		return type(func)(func.func_code, casa_globals)(*args, **kwargs)
	return wrapper

@contextmanager
@injectEnv
def msHandler(file):
	exception = None
	table_instance = tbtool()
	table_instance.open(file)
	
	try:		
		yield table_instance
	except Exception, e:
		exception = e

	try:
		table_instance.close()
	except: 
		pass

	try:
		del table_instance
	except:
		pass

	if exception:
		raise exception

class RegressionHelper():

	def __init__(self):
		raise NotImplementedError("This class only implements static methods")

	@staticmethod
	def casapath():
		return os.environ.get("CASAPATH", "unset").split()[0]

	@staticmethod
	def assert_file(file):
		assert os.access(file, os.F_OK), "%s not exists" % file
		
	@staticmethod
	def assert_files(files, basepath = ""):
		for file in files:
			RegressionHelper.assert_file("%s/%s" % (basepath, file))
		
	@staticmethod
	def locate_data(file):
		# TODO: implement this 
		# module_path =  RegressionHelper.base_path(importlib.import_module(self.__module__).__file__)
		# index_file = file if file else 
		pass

	@staticmethod
	def assertenvvar(envvar):
		assert os.getenv(envvar), "The envvar %s is not defined" % envvar
	
	# deprecated
	@staticmethod
	def base_path(file):
		return os.path.dirname(file)

	@staticmethod
	def data_copy(array_path, destination = os.getcwd()):
		"""Given an array of paths, it will iterate and copy all to the
		current working directory, which is where casapy is executed
		"""
		for data_path in array_path:
			RegressionHelper.assert_file(data_path)
			if os.path.isdir(data_path):
				shutil.copytree(data_path, destination)
			else:
				shutil.copy(data_path, destination)

	@staticmethod
	def data_remove(array_path):
		"""Given an array of paths, it will iterate and delete them
		"""
		for data_path in array_path:
			RegressionHelper.assert_file(data_path)
			regressionLogger.debug("data_remove %s" % data_path)
			if os.path.isdir(data_path):
				shutil.rmtree(data_path, True)
			else:
				os.remove(data_path)

	@staticmethod
	def md5sum(objinst, on_memory = False):
		"""Whatever fits in the current rss memory, bigger files
		should be read in chunks of 129KB (to be implemented) if is
		needed
		"""
		digest = None

		if not on_memory:
			RegressionHelper.assert_file(objinst)
			with open(objinst, 'r') as to_hash:
				digest = hashlib.md5(to_hash.read()).hexdigest()
		else:
			digest = hashlib.md5(objinst).hexdigest()

		return digest

	@staticmethod
	def casa_console_globals():
		"""Return the CASA globals of the ipython console frame stack
		"""
		_stack = inspect.stack()
		_stack_flag = -1
		_stack_frame = None
		_stack_frame_globals = None

		for _stack_level in _stack:
			_stack_flag += 1
			if(string.find(_stack_level[1], "ipython console")):
				_stack_frame = sys._getframe(_stack_flag)
				_stack_frame_globals = _stack_frame.f_globals

		assert _stack_frame_globals, "No ipython console globals defined"
		return _stack_frame_globals

class RegressionBase(unittest.TestCase):

	def setUp(self):
		"""All the custom setup should be implemented by the developer
		"""
		self.casapy_script = None

	def tearDown(self):
		pass

	def __script_path(self, script_module_path, script):
		"""Return the absolute path of the script
		"""
		RegressionHelper.assert_file(script_module_path)
		path_script = "%s/%s.py" % (script_module_path, script)
		RegressionHelper.assert_file(path_script)
		return path_script

	def __class_module_path(self):
		"""Return the class module path (where is located), this method
		is intended to be used by child classes to resolve where
		the class extended is locate, will return the base path
		"""
		module_path =  os.path.dirname(importlib.import_module(self.__module__).__file__)
		RegressionHelper.assert_file(module_path)
		return module_path

	def execute(self, casapy_script, import_module = False, custom_globals = None):

		if import_module:
			importlib.import_module("%s" % casapy_script)
		else:
			console_frame_globals = RegressionHelper.casa_console_globals()
			console_frame_globals = dict(console_frame_globals.items() + custom_globals.items()) if custom_globals else console_frame_globals
			cexec_script = self.__script_path(self.__class_module_path(), casapy_script)
			execfile(cexec_script, console_frame_globals)

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

def regressionExecutor(test, custom_argv = None, guide = False, verbosity = 2):
	"""Execute the regression test by using nose with the nose arguments
	and with -d -s -v and --with-xunit (xml generation)
	"""
	# use imp instead of fixed package uri? not sure yet - atejeda
	test_package = "testc.regression" if not guide else "testc.guide"
	test_module_uri = "%s.%s" % (test_package, test)
	test_module = importlib.import_module(test_module_uri)
	test_module_path = os.path.dirname(test_module.__file__)

	RegressionHelper.assertenvvar("CASAROOT")

	default_argv = [ 
					test_module_path,
					test_module_uri,
					"-d",
					"-s",
					"--verbosity=%s" % verbosity,
					"--with-xunit",
					"--xunit-file=%s/xunit_%s.xml" % (os.getcwd(), test),
					"--with-psprofile",
					"--psprofile-file=%s/profile_%s.json" % (os.getcwd(), test)
					]

	test_argv = custom_argv if custom_argv else default_argv


	py_coverage_tree = [ "%s/lib/python/__casac__" % os.getenv("CASAROOT") ]

	coverage_instance = coverage.coverage(branch=True, source=py_coverage_tree)
	coverage_instance.start()

	nose.run(argv = test_argv, addplugins = [psprofile.PSProfile()])

	coverage_instance.xml_report(outfile="%s/coverage_%s.xml" % (os.getcwd(), test))
	coverage_instance.stop()
	
	del coverage_instance
	del test_module

if __name__ == "__main__":
	assert sys.argv[1], "an argument is needed, e.g.: regression_3c129_tutorial"
	regressionExecutor(sys.argv[1])
