"""
PsProfile / GLPv3 / github.com/atejeda

This module is a nose plugin to profile a given pid and generate json data with
the profile data.

In order to integrate it to your test cases see the following code snippet:

	default_argv = [	test_module_path,
						test_module_uri,
						"-d",
						"-s",
						"--verbosity=%s" % verbosity,
						"--with-psprofile",
						"--psprofile-file=%s.json" % test
					]

	nose.run(argv = default_argv, addplugins = [psprofile.PSProfile()])

Within a script should be execute same as above, for more info why
see: http://code.google.com/p/python-nose/issues/detail?id=105

	"*ALSO NOTE* that if you pass a unittest.TestSuite
	instance as the suite, context fixtures at the class, module and
	package level will not be used, and many plugin hooks will not
	be called. If you want normal nose behavior, either pass a list
	of tests, or a fully-configured `nose.suite.ContextSuite`_."

The module relies on the psutil module, for more info about it, take a look to the pip site.
"""

import sys

assert sys.version >= '2', "Python 2 or greater is supported"

import os
import time
import threading
import logging
import json
import traceback

from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Manager

import psutil

import nose
from nose.plugins import Plugin

__test__ = False
__all__ = ["PSProfile" ]

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

name = 'psprofile'

class PSProfile(Plugin):

	name = 'psprofile'
	score = 1
		
	def options(self, parser, env = os.environ):
		logger.debug("options(self, parser, env = os.environ):...")
		
		parser.add_option(
			"--psprofile-file", 
			action = "store", 
			default = env.get("NOSE_PSP_FILE", "psprofile.json"), 
			dest = "psp_file", 
			metavar="FILE",
			help = "By Default a psprofile.json is generated in the current working directory")

		Plugin.options(self, parser, env)

	def configure(self, options, conf):
		logger.debug("configure(self, options, conf):...")
		super(PSProfile, self).configure(options, conf)
		
		if not self.enabled:
			logger.debug("plugin not enabled")
			return
		
		self.__profile_data = {}
		self.__psp_report = options.psp_file

	def prepareTestCase(self, test):
		
		pid = os.getpid()

		self.testname = test.test._testMethodName
		logger.debug("prepareTestCase(self, test):... %s [%s]" % (self.testname, pid))
		
		# setup the multiprocessing proxy objects
		self.__process_manager = Manager()
		self.__process_event = self.__process_manager.Event()
		self.__process_data = self.__process_manager.dict()

		# LBYP approach here
		self.__process_data['ioc'] = []
		self.__process_data['fds'] = []
		self.__process_data['mem'] = []
		self.__process_data['time'] = []
		self.__process_data['cpu'] = []

		self.__process = Process(target = PSProfile.profile, args = (pid, self.__process_data, self.__process_event))

	def startTest(self, test):
		self.__process_event.clear()
		self.__process.start()
		logger.debug("startTest(self, test):... %s" % self.testname)
		
	def stopTest(self, test):
		logger.debug("stopTest(self, test):... %s" % self.testname)
		self.__process_event.set()
		self.__process.join()
		self.__profile_data[self.testname] = dict(self.__process_data)

	def report(self, stream):
		logger.debug("report(self, stream):...")
		json_report = json.dumps(self.__profile_data)
		
		self.write_report(json_report)

		if self.conf.verbosity > 4:
			stream.writeln(str(json_report))

	def write_report(self, json_report):
		""" write a report, a .json file with json data
		"""
		report_file_path = self.__psp_report
		with open(report_file_path, 'w') as report_file:
			report_file.write(json_report)

		print "-"*70
		print "PROFILE: %s" % self.__psp_report
		print "-"*70

	def finalize(self, result):
		logger.debug("finalize(self, result):...")

	@staticmethod
	def profile(pid, data, event, interval = 1):
		"""
		PSProfile.profile is executed in a multiprocessing context, the method
		can be executed or not within a nose environment.
		
		data -- is a DictProxy type object instance
		event -- is a flag to stop or not the process
		
		The data is written by proxy using objects once the process is about
		to finish.

		If the process to profile isn't alive, it will finish the process
		"""

		# the method code can be improved, but DictProxy isn't very flexible

		ps = psutil.Process(pid)

		ioc = []
		fds = []
		mem = []
		stamp = []
		cpu = []

		while not event.is_set():
			if ps.status():
				ioc.append(ps.io_counters())
				fds.append(ps.num_fds())
				mem.append(ps.memory_info())
				stamp.append(time.time())
				cpu.append(ps.cpu_percent(interval = interval))
			else:
				event.set()
				logger.debug("process to profile is not alive, about to finish this process [%s]" % os.getpid())

		data['ioc'] = ioc
		data['fds'] = fds
		data['mem'] = mem
		data['time'] = stamp
		data['cpu'] = cpu

# not used in the plugin, for testing purposes only
class PSProfileThread(threading.Thread):
	"""
	This class does the same as PSProfile intented
	to be used in non GIL blocker python modules/classes.
	"""

	def __init__(self, pid, interval = 1):
		super(PSProfileThread, self).__init__()

		self.__pid = pid
		self.__interval = interval
		self.__cpu = []
		self.__ioc = []
		self.__fds = []
		self.__mem = []
		self.__time = []
		self.__ps = psutil.Process(self.__pid)
		self.__stop_profiler = threading.Event()
				
	def join(self, timeout = None):
		"""When join is triggered, also stop the thread, a timeout
		can be specified
		"""
		self.stop_profiler.set()
		super(PSProfileThread, self).join(timeout)

	def __gather_data(self):
		"""Gather IO counters, file descriptors, ress and virt memory, time
		as ctime and cpu
		"""
		logger.debug("getting data...")
		self.__time.append(time.time())
		try:
			self.__ioc.append(self.__ps.io_counters())
			self.__fds.append(self.__ps.num_fds())
			self.__mem.append(self.__ps.memory_info())
			self.__cpu.append(self.__ps.cpu_percent(interval = self.__interval))
		except:
			logger.debug("problem gathering data for ts: %s" % self.__time[-1:])

	def profile_data(self):
		"""Retrieve the profile data gathered during the
		living-thread nor process
		"""
		return { 
			"cpu"  : self.__cpu,
			"ioc"  : self.__ioc,
			"fds"  : self.__fds,
			"mem"  : self.__mem,
			"time" : self.__time
			}

	def run(self):
		while not self.__stop_profiler.isSet():
			if self.__ps.status():
				self.__gather_data()
			else:
				logger.debug("process [%s] is not alive" % self.__pid)
				self.join()

if __name__ == "__main__":
	assert sys.argv[1], "An argument is needed, the pid of the process"

	profiler = PSProfileThread(int(sys.argv[1]))
	profiler.start_profiler()
	profiler.join()

	print json.dumps(profiler.profile_data())