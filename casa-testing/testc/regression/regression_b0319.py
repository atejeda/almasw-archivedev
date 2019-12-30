import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from testc.regression.helper import RegressionHelper
from testc.regression.helper import RegressionBase
from testc.regression.helper import regressionLogger

__all__ = ["B0319"]

class B0319(RegressionBase):

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
		self.execute("casapy_b0319")