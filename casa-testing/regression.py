import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"
assert globals().has_key("IPython"), "IPython environment is needed for this module (%s)" % __file__
assert globals().has_key("casa"), "CASA environment is needed for this module (%s)" % __file__

import os

from testc.regression.helper import regressionExecutor

# configure regression tests to execute
regressions = []

# configure guides tests to execute
guides = []
guides.append("regression_EVLA3BitTutorialG192")

# test the regression
for test in regressions:
	regressionExecutor(test)

# test the guides
for test in guides:
	regressionExecutor(test, guide = True)

