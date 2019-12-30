import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from testc.regression.helper import RegressionHelper
from testc.regression.helper import RegressionBase
from testc.regression.helper import regressionLogger

# define which classes within the module should be visible for testing
__all__ = ["Tutorial3c219"]

# in order to skip the test execution
# @unittest.skip("reason")
class Tutorial3c219(RegressionBase):

	# this method is executed just once and before for all tests
	# rather than for every test like setUp, useful for data
	# setup, e.g.: copy data, use ```this_class``` instead of ```self```
	# for this method, it is and instance of this class, this is managed
	# by the pytunit testing framework
	@classmethod
	def setUpClass(class_instance):
		#class_instance.cexec_module = 
		
		# this should be done in a different way...
		relative_data_path = "/home/casa/data/trunk/regression/3C129"
		test_data = []
		test_data.append("%s/%s" % (relative_data_path, "AT166_1"))
		test_data.append("%s/%s" % (relative_data_path, "AT166_2"))
		test_data.append("%s/%s" % (relative_data_path, "AT166_3"))
		RegressionHelper.data_copy(test_data)

	# Define all your setup here, beware that this method
	# is execute before each test_* method defined for this
	# class
	def setUp(self):
		pass

	# this method is excuted after every test_* method
	# defined in this class
	def tearDown(self):
		pass

	# this method is executed just once and after for all tests
	# rather than for every test like setUp
	@classmethod
	def tearDownClass(class_instance):
		pass

	# this is predifined but not mandatory, you can define
	# your tests methods by adding the prefix ```test_```
	# in order to skip the test execution, uncomment
	#@unittest.skip("reason")
	def test_execution(self):
		"""Testing execution of exec_3c129_tutorial
		"""
		self.execute("casapy_3c129_tutorial")