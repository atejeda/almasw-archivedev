import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from testc.regression.helper import RegressionHelper
from testc.regression.helper import RegressionBase
from testc.regression.helper import regressionLogger

__all__ = ["Coordsystest"]

class Coordsystest(RegressionBase):

	@classmethod
	def setUpClass(class_instance):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@classmethod
	def tearDownClass(class_instance):
		pass
		
	def test_execution(self):
		#self.execute("exec_coordsystest")
		self.execute("casapy_coordsystest")