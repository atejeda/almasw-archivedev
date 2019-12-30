"""
This is NOT a generated module
all modified changes will be kept.
"""

import sys

# assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"
# assert globals().has_key("IPython"), "IPython environment is needed for this module (%s)" % __file__
# assert globals().has_key("casa"), "CASA environment is needed for this module (%s)" % __file__

import os
import time

from testc.regression.helper import RegressionHelper
from testc.regression.helper import RegressionBase
from testc.regression.helper import regressionLogger
from testc.regression.helper import msHandler

from numpy import count_nonzero

__test__ = False

def setjy_common(measet, checksum_ref):
	with msHandler(measet) as table:
		source_model = table.getcell('SOURCE_MODEL', 0)
		assert source_model, "no model defined at SOURCE.SOURCE_MODEL[0]"
		checksum = RegressionHelper.md5sum(source_model, on_memory = True)
		assert checksum == checksum_ref, "different data, checksum computed is %s" % checksum

def applycal_common(measet, field_id, checksum_ref):
	column = "CORRECTED_DATA"

	with msHandler(measet) as table:
		assert table.iscelldefined(column), "no %s column is defined" % column
		corrected_data_table = table.query('FIELD_ID == %s' % field_id, columns = '%s' % column)
		corrected_data_rows = corrected_data_table.getcol(column)
		checksum = RegressionHelper.md5sum(corrected_data_rows, on_memory = True)
		del corrected_data_table
		del corrected_data_rows
		assert checksum == checksum_ref, "different data, checksum computed is %s" % checksum

def test_00_splitting_fields_for_analysis():
	"""post method for "splitting fields for analysis"
	"""
	RegressionHelper.assert_file("%s/G192_6s.ms" % os.getcwd())

def test_01_listobs_on_the_initial_data_set():
	"""post method for "listobs on the initial data set"
	"""
	listobs_file = "%s/G192_listobs.txt" % os.getcwd()
	RegressionHelper.assert_file(listobs_file)

	remove = []
	remove.append(listobs_file)
	remove.append("%s/listobs.last" % os.getcwd())
	#RegressionHelper.data_remove(remove)

def test_02_flag_table_plot():
	"""post method for "flag table plot"
	"""
	RegressionHelper.assert_file("%s/PlotG192_flagcmd_4.1.png" % os.getcwd())

# the number of FLAG_ROWS (2909568) doesn't match to the expected one
def test_03_bandpass_calibrator_analysis_flagging():
	"""post method for "bandpass calibrator analysis flagging"
	"""
	measet = "%s/G192_6s.ms" % os.getcwd()
	
	with msHandler(measet) as table:
		nrows = count_nonzero(table.getcol("FLAG_ROW"))
		assert nrows, "no FLAG_ROWS in %s" % measet
		assert nrows == 2909568, "the number of FLAG_ROWS (%s) doesn't match to the expected one" % nrows

# the number of FLAG_ROWS (2909568) doesn't match to the expected one
def test_04_rfi_phase_calibrator_flagging():
	"""post method for "RFI phase calibrator flagging"
	"""
	measet = "%s/G192_6s.ms" % os.getcwd()
	
	with msHandler(measet) as table:
		nrows = count_nonzero(table.getcol("FLAG_ROW"))
		assert nrows, "no FLAG_ROWS in %s" % measet
		assert nrows == 2909568, "the number of FLAG_ROWS (%s) doesn't match to the expected one" % nrows
	
def test_05_splitting_good_and_bad_data():
	"""post method for "splitting good and bad data"
	"""
	# dont delete G192_flagged_6s.ms all the tests relies on the
	# the dataset with the the flagged data
	measet = "G192_flagged_6s.ms"
	RegressionHelper.assert_file("%s/%s" % (os.getcwd(), measet))

def test_06_split_and_flagged_listobs():
	"""post method for "split and flagged listobs"
	"""
	listobs_file = "%s/G192_flagged_listobs.txt" % os.getcwd()
	RegressionHelper.assert_file(listobs_file)

# must be string or buffer, not dict
def test_07_model_for_the_flux_calibrator():
	"""post method for "model for the flux calibrator"
	"""
	measet = "%s/G192_flagged_6s.ms/SOURCE" % os.getcwd()
	checksum_ref = ""
	setjy_common(measet, checksum_ref)

def test_08_determining_antenna_position_corrections():
	"""post method for "determining antenna position corrections"
	"""
	produced_files = []
	produced_files.append("calG192.antpos")
	produced_files.append("calG192.antpos/table.dat")
	produced_files.append("calG192.antpos/table.lock")
	produced_files.append("calG192.antpos/ANTENNA")
	produced_files.append("calG192.antpos/ANTENNA/table.dat")
	produced_files.append("calG192.antpos/ANTENNA/table.lock")
	produced_files.append("calG192.antpos/ANTENNA/table.info")
	produced_files.append("calG192.antpos/ANTENNA/table.f0")
	produced_files.append("calG192.antpos/SPECTRAL_WINDOW")
	produced_files.append("calG192.antpos/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.antpos/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.antpos/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.antpos/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.antpos/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.antpos/HISTORY")
	produced_files.append("calG192.antpos/HISTORY/table.dat")
	produced_files.append("calG192.antpos/HISTORY/table.lock")
	produced_files.append("calG192.antpos/HISTORY/table.info")
	produced_files.append("calG192.antpos/HISTORY/table.f0")
	produced_files.append("calG192.antpos/FIELD")
	produced_files.append("calG192.antpos/FIELD/table.dat")
	produced_files.append("calG192.antpos/FIELD/table.lock")
	produced_files.append("calG192.antpos/FIELD/table.f0i")
	produced_files.append("calG192.antpos/FIELD/table.info")
	produced_files.append("calG192.antpos/FIELD/table.f0")
	produced_files.append("calG192.antpos/table.f0i")
	produced_files.append("calG192.antpos/table.info")
	produced_files.append("calG192.antpos/OBSERVATION")
	produced_files.append("calG192.antpos/OBSERVATION/table.dat")
	produced_files.append("calG192.antpos/OBSERVATION/table.lock")
	produced_files.append("calG192.antpos/OBSERVATION/table.info")
	produced_files.append("calG192.antpos/OBSERVATION/table.f0")
	produced_files.append("calG192.antpos/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_09_generating_gaincurve_calibration():
	"""post method for "generating gaincurve calibration"
	"""
	produced_files = []
	produced_files.append("calG192.gaincurve")
	produced_files.append("calG192.gaincurve/table.dat")
	produced_files.append("calG192.gaincurve/table.lock")
	produced_files.append("calG192.gaincurve/ANTENNA")
	produced_files.append("calG192.gaincurve/ANTENNA/table.dat")
	produced_files.append("calG192.gaincurve/ANTENNA/table.lock")
	produced_files.append("calG192.gaincurve/ANTENNA/table.info")
	produced_files.append("calG192.gaincurve/ANTENNA/table.f0")
	produced_files.append("calG192.gaincurve/SPECTRAL_WINDOW")
	produced_files.append("calG192.gaincurve/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.gaincurve/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.gaincurve/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.gaincurve/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.gaincurve/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.gaincurve/HISTORY")
	produced_files.append("calG192.gaincurve/HISTORY/table.dat")
	produced_files.append("calG192.gaincurve/HISTORY/table.lock")
	produced_files.append("calG192.gaincurve/HISTORY/table.info")
	produced_files.append("calG192.gaincurve/HISTORY/table.f0")
	produced_files.append("calG192.gaincurve/FIELD")
	produced_files.append("calG192.gaincurve/FIELD/table.dat")
	produced_files.append("calG192.gaincurve/FIELD/table.lock")
	produced_files.append("calG192.gaincurve/FIELD/table.f0i")
	produced_files.append("calG192.gaincurve/FIELD/table.info")
	produced_files.append("calG192.gaincurve/FIELD/table.f0")
	produced_files.append("calG192.gaincurve/table.f0i")
	produced_files.append("calG192.gaincurve/table.info")
	produced_files.append("calG192.gaincurve/OBSERVATION")
	produced_files.append("calG192.gaincurve/OBSERVATION/table.dat")
	produced_files.append("calG192.gaincurve/OBSERVATION/table.lock")
	produced_files.append("calG192.gaincurve/OBSERVATION/table.info")
	produced_files.append("calG192.gaincurve/OBSERVATION/table.f0")
	produced_files.append("calG192.gaincurve/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

# error: global name 'SPWs' is not defined
def test_10_generate_atmospheric_opacity_calibration():
	"""post method for "generate atmospheric opacity calibration"
	"""
	produced_files = []
	produced_files.append("calG192.opacity")
	produced_files.append("calG192.opacity/table.dat")
	produced_files.append("calG192.opacity/table.lock")
	produced_files.append("calG192.opacity/ANTENNA")
	produced_files.append("calG192.opacity/ANTENNA/table.dat")
	produced_files.append("calG192.opacity/ANTENNA/table.lock")
	produced_files.append("calG192.opacity/ANTENNA/table.info")
	produced_files.append("calG192.opacity/ANTENNA/table.f0")
	produced_files.append("calG192.opacity/SPECTRAL_WINDOW")
	produced_files.append("calG192.opacity/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.opacity/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.opacity/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.opacity/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.opacity/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.opacity/HISTORY")
	produced_files.append("calG192.opacity/HISTORY/table.dat")
	produced_files.append("calG192.opacity/HISTORY/table.lock")
	produced_files.append("calG192.opacity/HISTORY/table.info")
	produced_files.append("calG192.opacity/HISTORY/table.f0")
	produced_files.append("calG192.opacity/FIELD")
	produced_files.append("calG192.opacity/FIELD/table.dat")
	produced_files.append("calG192.opacity/FIELD/table.lock")
	produced_files.append("calG192.opacity/FIELD/table.f0i")
	produced_files.append("calG192.opacity/FIELD/table.info")
	produced_files.append("calG192.opacity/FIELD/table.f0")
	produced_files.append("calG192.opacity/table.f0i")
	produced_files.append("calG192.opacity/table.info")
	produced_files.append("calG192.opacity/OBSERVATION")
	produced_files.append("calG192.opacity/OBSERVATION/table.dat")
	produced_files.append("calG192.opacity/OBSERVATION/table.lock")
	produced_files.append("calG192.opacity/OBSERVATION/table.info")
	produced_files.append("calG192.opacity/OBSERVATION/table.f0")
	produced_files.append("calG192.opacity/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_11_generate_requantizer_gains_corrections():
	"""post method for "generate requantizer gains corrections"
	"""
	produced_files = []
	produced_files.append("calG192.requantizer")
	produced_files.append("calG192.requantizer/table.dat")
	produced_files.append("calG192.requantizer/table.lock")
	produced_files.append("calG192.requantizer/ANTENNA")
	produced_files.append("calG192.requantizer/ANTENNA/table.dat")
	produced_files.append("calG192.requantizer/ANTENNA/table.lock")
	produced_files.append("calG192.requantizer/ANTENNA/table.info")
	produced_files.append("calG192.requantizer/ANTENNA/table.f0")
	produced_files.append("calG192.requantizer/SPECTRAL_WINDOW")
	produced_files.append("calG192.requantizer/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.requantizer/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.requantizer/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.requantizer/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.requantizer/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.requantizer/HISTORY")
	produced_files.append("calG192.requantizer/HISTORY/table.dat")
	produced_files.append("calG192.requantizer/HISTORY/table.lock")
	produced_files.append("calG192.requantizer/HISTORY/table.info")
	produced_files.append("calG192.requantizer/HISTORY/table.f0")
	produced_files.append("calG192.requantizer/FIELD")
	produced_files.append("calG192.requantizer/FIELD/table.dat")
	produced_files.append("calG192.requantizer/FIELD/table.lock")
	produced_files.append("calG192.requantizer/FIELD/table.f0i")
	produced_files.append("calG192.requantizer/FIELD/table.info")
	produced_files.append("calG192.requantizer/FIELD/table.f0")
	produced_files.append("calG192.requantizer/table.f0i")
	produced_files.append("calG192.requantizer/table.info")
	produced_files.append("calG192.requantizer/OBSERVATION")
	produced_files.append("calG192.requantizer/OBSERVATION/table.dat")
	produced_files.append("calG192.requantizer/OBSERVATION/table.lock")
	produced_files.append("calG192.requantizer/OBSERVATION/table.info")
	produced_files.append("calG192.requantizer/OBSERVATION/table.f0")
	produced_files.append("calG192.requantizer/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_12_phase_only_calibration():
	"""post method for "phase only calibration"
	"""
	produced_files = []
	produced_files.append("calG192.G0")
	produced_files.append("calG192.G0/table.dat")
	produced_files.append("calG192.G0/table.lock")
	produced_files.append("calG192.G0/ANTENNA")
	produced_files.append("calG192.G0/ANTENNA/table.dat")
	produced_files.append("calG192.G0/ANTENNA/table.lock")
	produced_files.append("calG192.G0/ANTENNA/table.info")
	produced_files.append("calG192.G0/ANTENNA/table.f0")
	produced_files.append("calG192.G0/SPECTRAL_WINDOW")
	produced_files.append("calG192.G0/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G0/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G0/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G0/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G0/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G0/HISTORY")
	produced_files.append("calG192.G0/HISTORY/table.dat")
	produced_files.append("calG192.G0/HISTORY/table.lock")
	produced_files.append("calG192.G0/HISTORY/table.info")
	produced_files.append("calG192.G0/HISTORY/table.f0")
	produced_files.append("calG192.G0/FIELD")
	produced_files.append("calG192.G0/FIELD/table.dat")
	produced_files.append("calG192.G0/FIELD/table.lock")
	produced_files.append("calG192.G0/FIELD/table.f0i")
	produced_files.append("calG192.G0/FIELD/table.info")
	produced_files.append("calG192.G0/FIELD/table.f0")
	produced_files.append("calG192.G0/table.f0i")
	produced_files.append("calG192.G0/table.info")
	produced_files.append("calG192.G0/OBSERVATION")
	produced_files.append("calG192.G0/OBSERVATION/table.dat")
	produced_files.append("calG192.G0/OBSERVATION/table.lock")
	produced_files.append("calG192.G0/OBSERVATION/table.info")
	produced_files.append("calG192.G0/OBSERVATION/table.f0")
	produced_files.append("calG192.G0/table.f0")
	
	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_13_residual_delays():
	"""post method for "residual delays"
	"""
	produced_files = []
	produced_files.append("calG192.K0")
	produced_files.append("calG192.K0/table.dat")
	produced_files.append("calG192.K0/table.lock")
	produced_files.append("calG192.K0/ANTENNA")
	produced_files.append("calG192.K0/ANTENNA/table.dat")
	produced_files.append("calG192.K0/ANTENNA/table.lock")
	produced_files.append("calG192.K0/ANTENNA/table.info")
	produced_files.append("calG192.K0/ANTENNA/table.f0")
	produced_files.append("calG192.K0/SPECTRAL_WINDOW")
	produced_files.append("calG192.K0/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.K0/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.K0/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.K0/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.K0/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.K0/HISTORY")
	produced_files.append("calG192.K0/HISTORY/table.dat")
	produced_files.append("calG192.K0/HISTORY/table.lock")
	produced_files.append("calG192.K0/HISTORY/table.info")
	produced_files.append("calG192.K0/HISTORY/table.f0")
	produced_files.append("calG192.K0/FIELD")
	produced_files.append("calG192.K0/FIELD/table.dat")
	produced_files.append("calG192.K0/FIELD/table.lock")
	produced_files.append("calG192.K0/FIELD/table.f0i")
	produced_files.append("calG192.K0/FIELD/table.info")
	produced_files.append("calG192.K0/FIELD/table.f0")
	produced_files.append("calG192.K0/table.f0i")
	produced_files.append("calG192.K0/table.info")
	produced_files.append("calG192.K0/OBSERVATION")
	produced_files.append("calG192.K0/OBSERVATION/table.dat")
	produced_files.append("calG192.K0/OBSERVATION/table.lock")
	produced_files.append("calG192.K0/OBSERVATION/table.info")
	produced_files.append("calG192.K0/OBSERVATION/table.f0")
	produced_files.append("calG192.K0/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_14_antenna_bandpasses():
	"""post method for "antenna bandpasses"
	"""
	produced_files = []
	produced_files.append("calG192.B0")
	produced_files.append("calG192.B0/table.dat")
	produced_files.append("calG192.B0/table.lock")
	produced_files.append("calG192.B0/ANTENNA")
	produced_files.append("calG192.B0/ANTENNA/table.dat")
	produced_files.append("calG192.B0/ANTENNA/table.lock")
	produced_files.append("calG192.B0/ANTENNA/table.info")
	produced_files.append("calG192.B0/ANTENNA/table.f0")
	produced_files.append("calG192.B0/SPECTRAL_WINDOW")
	produced_files.append("calG192.B0/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.B0/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.B0/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.B0/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.B0/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.B0/HISTORY")
	produced_files.append("calG192.B0/HISTORY/table.dat")
	produced_files.append("calG192.B0/HISTORY/table.lock")
	produced_files.append("calG192.B0/HISTORY/table.info")
	produced_files.append("calG192.B0/HISTORY/table.f0")
	produced_files.append("calG192.B0/FIELD")
	produced_files.append("calG192.B0/FIELD/table.dat")
	produced_files.append("calG192.B0/FIELD/table.lock")
	produced_files.append("calG192.B0/FIELD/table.f0i")
	produced_files.append("calG192.B0/FIELD/table.info")
	produced_files.append("calG192.B0/FIELD/table.f0")
	produced_files.append("calG192.B0/table.f0i")
	produced_files.append("calG192.B0/table.info")
	produced_files.append("calG192.B0/OBSERVATION")
	produced_files.append("calG192.B0/OBSERVATION/table.dat")
	produced_files.append("calG192.B0/OBSERVATION/table.lock")
	produced_files.append("calG192.B0/OBSERVATION/table.info")
	produced_files.append("calG192.B0/OBSERVATION/table.f0")
	produced_files.append("calG192.B0/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_15_flux_and_bandpass_calibrators_gain():
	"""post method for "flux and bandpass calibrators gain"
	"""
	produced_files = []
	produced_files.append("calG192.G1")
	produced_files.append("calG192.G1/table.dat")
	produced_files.append("calG192.G1/table.lock")
	produced_files.append("calG192.G1/ANTENNA")
	produced_files.append("calG192.G1/ANTENNA/table.dat")
	produced_files.append("calG192.G1/ANTENNA/table.lock")
	produced_files.append("calG192.G1/ANTENNA/table.info")
	produced_files.append("calG192.G1/ANTENNA/table.f0")
	produced_files.append("calG192.G1/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1/HISTORY")
	produced_files.append("calG192.G1/HISTORY/table.dat")
	produced_files.append("calG192.G1/HISTORY/table.lock")
	produced_files.append("calG192.G1/HISTORY/table.info")
	produced_files.append("calG192.G1/HISTORY/table.f0")
	produced_files.append("calG192.G1/FIELD")
	produced_files.append("calG192.G1/FIELD/table.dat")
	produced_files.append("calG192.G1/FIELD/table.lock")
	produced_files.append("calG192.G1/FIELD/table.f0i")
	produced_files.append("calG192.G1/FIELD/table.info")
	produced_files.append("calG192.G1/FIELD/table.f0")
	produced_files.append("calG192.G1/table.f0i")
	produced_files.append("calG192.G1/table.info")
	produced_files.append("calG192.G1/OBSERVATION")
	produced_files.append("calG192.G1/OBSERVATION/table.dat")
	produced_files.append("calG192.G1/OBSERVATION/table.lock")
	produced_files.append("calG192.G1/OBSERVATION/table.info")
	produced_files.append("calG192.G1/OBSERVATION/table.f0")
	produced_files.append("calG192.G1/table.f0")

def test_16_bandpass_calibrator_gain_amplitudes_scaling():
	"""post method for "bandpass calibrator gain amplitudes scaling"
	"""
	RegressionHelper.assert_file("%s/3C84.fluxinfo" % os.getcwd())

# must be string or buffer, not dict
def test_17_spectral_information():
	"""post method for "spectral information"
	"""
	measet = "%s/G192_flagged_6s.ms/SOURCE" % os.getcwd()
	checksum_ref = ""
	setjy_common(measet, checksum_ref)

def test_18_phase_only_recalibration():
	"""post method for "phase only recalibration"
	"""
	produced_files = []
	produced_files.append("calG192.G0.b")
	produced_files.append("calG192.G0.b/table.dat")
	produced_files.append("calG192.G0.b/table.lock")
	produced_files.append("calG192.G0.b/ANTENNA")
	produced_files.append("calG192.G0.b/ANTENNA/table.dat")
	produced_files.append("calG192.G0.b/ANTENNA/table.lock")
	produced_files.append("calG192.G0.b/ANTENNA/table.info")
	produced_files.append("calG192.G0.b/ANTENNA/table.f0")
	produced_files.append("calG192.G0.b/SPECTRAL_WINDOW")
	produced_files.append("calG192.G0.b/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G0.b/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G0.b/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G0.b/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G0.b/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G0.b/HISTORY")
	produced_files.append("calG192.G0.b/HISTORY/table.dat")
	produced_files.append("calG192.G0.b/HISTORY/table.lock")
	produced_files.append("calG192.G0.b/HISTORY/table.info")
	produced_files.append("calG192.G0.b/HISTORY/table.f0")
	produced_files.append("calG192.G0.b/FIELD")
	produced_files.append("calG192.G0.b/FIELD/table.dat")
	produced_files.append("calG192.G0.b/FIELD/table.lock")
	produced_files.append("calG192.G0.b/FIELD/table.f0i")
	produced_files.append("calG192.G0.b/FIELD/table.info")
	produced_files.append("calG192.G0.b/FIELD/table.f0")
	produced_files.append("calG192.G0.b/table.f0i")
	produced_files.append("calG192.G0.b/table.info")
	produced_files.append("calG192.G0.b/OBSERVATION")
	produced_files.append("calG192.G0.b/OBSERVATION/table.dat")
	produced_files.append("calG192.G0.b/OBSERVATION/table.lock")
	produced_files.append("calG192.G0.b/OBSERVATION/table.info")
	produced_files.append("calG192.G0.b/OBSERVATION/table.f0")
	produced_files.append("calG192.G0.b/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_19_residual_delays_recalibration():
	"""post method for "residual delays recalibration"
	"""
	produced_files = []
	produced_files.append("calG192.K0.b")
	produced_files.append("calG192.K0.b/table.dat")
	produced_files.append("calG192.K0.b/table.lock")
	produced_files.append("calG192.K0.b/ANTENNA")
	produced_files.append("calG192.K0.b/ANTENNA/table.dat")
	produced_files.append("calG192.K0.b/ANTENNA/table.lock")
	produced_files.append("calG192.K0.b/ANTENNA/table.info")
	produced_files.append("calG192.K0.b/ANTENNA/table.f0")
	produced_files.append("calG192.K0.b/SPECTRAL_WINDOW")
	produced_files.append("calG192.K0.b/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.K0.b/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.K0.b/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.K0.b/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.K0.b/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.K0.b/HISTORY")
	produced_files.append("calG192.K0.b/HISTORY/table.dat")
	produced_files.append("calG192.K0.b/HISTORY/table.lock")
	produced_files.append("calG192.K0.b/HISTORY/table.info")
	produced_files.append("calG192.K0.b/HISTORY/table.f0")
	produced_files.append("calG192.K0.b/FIELD")
	produced_files.append("calG192.K0.b/FIELD/table.dat")
	produced_files.append("calG192.K0.b/FIELD/table.lock")
	produced_files.append("calG192.K0.b/FIELD/table.f0i")
	produced_files.append("calG192.K0.b/FIELD/table.info")
	produced_files.append("calG192.K0.b/FIELD/table.f0")
	produced_files.append("calG192.K0.b/table.f0i")
	produced_files.append("calG192.K0.b/table.info")
	produced_files.append("calG192.K0.b/OBSERVATION")
	produced_files.append("calG192.K0.b/OBSERVATION/table.dat")
	produced_files.append("calG192.K0.b/OBSERVATION/table.lock")
	produced_files.append("calG192.K0.b/OBSERVATION/table.info")
	produced_files.append("calG192.K0.b/OBSERVATION/table.f0")
	produced_files.append("calG192.K0.b/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_20_antenna_bandpasses_recalibration():
	"""post method for "antenna bandpasses recalibration"
	"""
	produced_files = []
	produced_files.append("calG192.B0.b")
	produced_files.append("calG192.B0.b/table.dat")
	produced_files.append("calG192.B0.b/table.lock")
	produced_files.append("calG192.B0.b/ANTENNA")
	produced_files.append("calG192.B0.b/ANTENNA/table.dat")
	produced_files.append("calG192.B0.b/ANTENNA/table.lock")
	produced_files.append("calG192.B0.b/ANTENNA/table.info")
	produced_files.append("calG192.B0.b/ANTENNA/table.f0")
	produced_files.append("calG192.B0.b/SPECTRAL_WINDOW")
	produced_files.append("calG192.B0.b/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.B0.b/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.B0.b/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.B0.b/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.B0.b/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.B0.b/HISTORY")
	produced_files.append("calG192.B0.b/HISTORY/table.dat")
	produced_files.append("calG192.B0.b/HISTORY/table.lock")
	produced_files.append("calG192.B0.b/HISTORY/table.info")
	produced_files.append("calG192.B0.b/HISTORY/table.f0")
	produced_files.append("calG192.B0.b/FIELD")
	produced_files.append("calG192.B0.b/FIELD/table.dat")
	produced_files.append("calG192.B0.b/FIELD/table.lock")
	produced_files.append("calG192.B0.b/FIELD/table.f0i")
	produced_files.append("calG192.B0.b/FIELD/table.info")
	produced_files.append("calG192.B0.b/FIELD/table.f0")
	produced_files.append("calG192.B0.b/table.f0i")
	produced_files.append("calG192.B0.b/table.info")
	produced_files.append("calG192.B0.b/OBSERVATION")
	produced_files.append("calG192.B0.b/OBSERVATION/table.dat")
	produced_files.append("calG192.B0.b/OBSERVATION/table.lock")
	produced_files.append("calG192.B0.b/OBSERVATION/table.info")
	produced_files.append("calG192.B0.b/OBSERVATION/table.f0")
	produced_files.append("calG192.B0.b/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_21_compute_gain_phases_using_3c147():
	"""post method for "compute gain phases using 3C147"
	"""
	produced_files = []
	produced_files.append("calG192.G1.int")
	produced_files.append("calG192.G1.int/table.dat")
	produced_files.append("calG192.G1.int/table.lock")
	produced_files.append("calG192.G1.int/ANTENNA")
	produced_files.append("calG192.G1.int/ANTENNA/table.dat")
	produced_files.append("calG192.G1.int/ANTENNA/table.lock")
	produced_files.append("calG192.G1.int/ANTENNA/table.info")
	produced_files.append("calG192.G1.int/ANTENNA/table.f0")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.int/HISTORY")
	produced_files.append("calG192.G1.int/HISTORY/table.dat")
	produced_files.append("calG192.G1.int/HISTORY/table.lock")
	produced_files.append("calG192.G1.int/HISTORY/table.info")
	produced_files.append("calG192.G1.int/HISTORY/table.f0")
	produced_files.append("calG192.G1.int/FIELD")
	produced_files.append("calG192.G1.int/FIELD/table.dat")
	produced_files.append("calG192.G1.int/FIELD/table.lock")
	produced_files.append("calG192.G1.int/FIELD/table.f0i")
	produced_files.append("calG192.G1.int/FIELD/table.info")
	produced_files.append("calG192.G1.int/FIELD/table.f0")
	produced_files.append("calG192.G1.int/table.f0i")
	produced_files.append("calG192.G1.int/table.info")
	produced_files.append("calG192.G1.int/OBSERVATION")
	produced_files.append("calG192.G1.int/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.int/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.int/OBSERVATION/table.info")
	produced_files.append("calG192.G1.int/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.int/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_22_compute_gain_phases_using_j0603_174():
	"""post method for "compute gain phases using J0603+174"
	"""
	produced_files = []
	produced_files.append("calG192.G1.int")
	produced_files.append("calG192.G1.int/table.dat")
	produced_files.append("calG192.G1.int/table.lock")
	produced_files.append("calG192.G1.int/ANTENNA")
	produced_files.append("calG192.G1.int/ANTENNA/table.dat")
	produced_files.append("calG192.G1.int/ANTENNA/table.lock")
	produced_files.append("calG192.G1.int/ANTENNA/table.info")
	produced_files.append("calG192.G1.int/ANTENNA/table.f0")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.int/HISTORY")
	produced_files.append("calG192.G1.int/HISTORY/table.dat")
	produced_files.append("calG192.G1.int/HISTORY/table.lock")
	produced_files.append("calG192.G1.int/HISTORY/table.info")
	produced_files.append("calG192.G1.int/HISTORY/table.f0")
	produced_files.append("calG192.G1.int/FIELD")
	produced_files.append("calG192.G1.int/FIELD/table.dat")
	produced_files.append("calG192.G1.int/FIELD/table.lock")
	produced_files.append("calG192.G1.int/FIELD/table.f0i")
	produced_files.append("calG192.G1.int/FIELD/table.info")
	produced_files.append("calG192.G1.int/FIELD/table.f0")
	produced_files.append("calG192.G1.int/table.f0i")
	produced_files.append("calG192.G1.int/table.info")
	produced_files.append("calG192.G1.int/OBSERVATION")
	produced_files.append("calG192.G1.int/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.int/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.int/OBSERVATION/table.info")
	produced_files.append("calG192.G1.int/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.int/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_23_compute_gain_phases_using_3c84():
	"""post method for "compute gain phases using 3C84"
	"""
	produced_files = []
	produced_files.append("calG192.G1.int")
	produced_files.append("calG192.G1.int/table.dat")
	produced_files.append("calG192.G1.int/table.lock")
	produced_files.append("calG192.G1.int/ANTENNA")
	produced_files.append("calG192.G1.int/ANTENNA/table.dat")
	produced_files.append("calG192.G1.int/ANTENNA/table.lock")
	produced_files.append("calG192.G1.int/ANTENNA/table.info")
	produced_files.append("calG192.G1.int/ANTENNA/table.f0")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.int/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.int/HISTORY")
	produced_files.append("calG192.G1.int/HISTORY/table.dat")
	produced_files.append("calG192.G1.int/HISTORY/table.lock")
	produced_files.append("calG192.G1.int/HISTORY/table.info")
	produced_files.append("calG192.G1.int/HISTORY/table.f0")
	produced_files.append("calG192.G1.int/FIELD")
	produced_files.append("calG192.G1.int/FIELD/table.dat")
	produced_files.append("calG192.G1.int/FIELD/table.lock")
	produced_files.append("calG192.G1.int/FIELD/table.f0i")
	produced_files.append("calG192.G1.int/FIELD/table.info")
	produced_files.append("calG192.G1.int/FIELD/table.f0")
	produced_files.append("calG192.G1.int/table.f0i")
	produced_files.append("calG192.G1.int/table.info")
	produced_files.append("calG192.G1.int/OBSERVATION")
	produced_files.append("calG192.G1.int/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.int/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.int/OBSERVATION/table.info")
	produced_files.append("calG192.G1.int/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.int/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_24_applying_phase_calibration():
	"""post method for "applying phase calibration"
	"""
	produced_files = []
	produced_files.append("calG192.G1.inf")
	produced_files.append("calG192.G1.inf/table.dat")
	produced_files.append("calG192.G1.inf/table.lock")
	produced_files.append("calG192.G1.inf/ANTENNA")
	produced_files.append("calG192.G1.inf/ANTENNA/table.dat")
	produced_files.append("calG192.G1.inf/ANTENNA/table.lock")
	produced_files.append("calG192.G1.inf/ANTENNA/table.info")
	produced_files.append("calG192.G1.inf/ANTENNA/table.f0")
	produced_files.append("calG192.G1.inf/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.inf/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.inf/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.inf/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.inf/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.inf/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.inf/HISTORY")
	produced_files.append("calG192.G1.inf/HISTORY/table.dat")
	produced_files.append("calG192.G1.inf/HISTORY/table.lock")
	produced_files.append("calG192.G1.inf/HISTORY/table.info")
	produced_files.append("calG192.G1.inf/HISTORY/table.f0")
	produced_files.append("calG192.G1.inf/FIELD")
	produced_files.append("calG192.G1.inf/FIELD/table.dat")
	produced_files.append("calG192.G1.inf/FIELD/table.lock")
	produced_files.append("calG192.G1.inf/FIELD/table.f0i")
	produced_files.append("calG192.G1.inf/FIELD/table.info")
	produced_files.append("calG192.G1.inf/FIELD/table.f0")
	produced_files.append("calG192.G1.inf/table.f0i")
	produced_files.append("calG192.G1.inf/table.info")
	produced_files.append("calG192.G1.inf/OBSERVATION")
	produced_files.append("calG192.G1.inf/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.inf/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.inf/OBSERVATION/table.info")
	produced_files.append("calG192.G1.inf/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.inf/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_25_3c147_scan_solving_amplitudes():
	"""post method for "3C147 scan solving amplitudes"
	"""
	produced_files = []
	produced_files.append("calG192.G2")
	produced_files.append("calG192.G2/table.dat")
	produced_files.append("calG192.G2/table.lock")
	produced_files.append("calG192.G2/ANTENNA")
	produced_files.append("calG192.G2/ANTENNA/table.dat")
	produced_files.append("calG192.G2/ANTENNA/table.lock")
	produced_files.append("calG192.G2/ANTENNA/table.info")
	produced_files.append("calG192.G2/ANTENNA/table.f0")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G2/HISTORY")
	produced_files.append("calG192.G2/HISTORY/table.dat")
	produced_files.append("calG192.G2/HISTORY/table.lock")
	produced_files.append("calG192.G2/HISTORY/table.info")
	produced_files.append("calG192.G2/HISTORY/table.f0")
	produced_files.append("calG192.G2/FIELD")
	produced_files.append("calG192.G2/FIELD/table.dat")
	produced_files.append("calG192.G2/FIELD/table.lock")
	produced_files.append("calG192.G2/FIELD/table.f0i")
	produced_files.append("calG192.G2/FIELD/table.info")
	produced_files.append("calG192.G2/FIELD/table.f0")
	produced_files.append("calG192.G2/table.f0i")
	produced_files.append("calG192.G2/table.info")
	produced_files.append("calG192.G2/OBSERVATION")
	produced_files.append("calG192.G2/OBSERVATION/table.dat")
	produced_files.append("calG192.G2/OBSERVATION/table.lock")
	produced_files.append("calG192.G2/OBSERVATION/table.info")
	produced_files.append("calG192.G2/OBSERVATION/table.f0")
	produced_files.append("calG192.G2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_26_j0603_174__scan_solving_amplitudes():
	"""post method for "J0603+174  scan solving amplitudes"
	"""
	produced_files = []
	produced_files.append("calG192.G2")
	produced_files.append("calG192.G2/table.dat")
	produced_files.append("calG192.G2/table.lock")
	produced_files.append("calG192.G2/ANTENNA")
	produced_files.append("calG192.G2/ANTENNA/table.dat")
	produced_files.append("calG192.G2/ANTENNA/table.lock")
	produced_files.append("calG192.G2/ANTENNA/table.info")
	produced_files.append("calG192.G2/ANTENNA/table.f0")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G2/HISTORY")
	produced_files.append("calG192.G2/HISTORY/table.dat")
	produced_files.append("calG192.G2/HISTORY/table.lock")
	produced_files.append("calG192.G2/HISTORY/table.info")
	produced_files.append("calG192.G2/HISTORY/table.f0")
	produced_files.append("calG192.G2/FIELD")
	produced_files.append("calG192.G2/FIELD/table.dat")
	produced_files.append("calG192.G2/FIELD/table.lock")
	produced_files.append("calG192.G2/FIELD/table.f0i")
	produced_files.append("calG192.G2/FIELD/table.info")
	produced_files.append("calG192.G2/FIELD/table.f0")
	produced_files.append("calG192.G2/table.f0i")
	produced_files.append("calG192.G2/table.info")
	produced_files.append("calG192.G2/OBSERVATION")
	produced_files.append("calG192.G2/OBSERVATION/table.dat")
	produced_files.append("calG192.G2/OBSERVATION/table.lock")
	produced_files.append("calG192.G2/OBSERVATION/table.info")
	produced_files.append("calG192.G2/OBSERVATION/table.f0")
	produced_files.append("calG192.G2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

# TODO: check this one
def test_27_3c84_scan_solving_amplitudes():
	"""post method for "3C84 scan solving amplitudes"
	"""
	produced_files = []
	produced_files.append("calG192.G2")
	produced_files.append("calG192.G2/table.dat")
	produced_files.append("calG192.G2/table.lock")
	produced_files.append("calG192.G2/ANTENNA")
	produced_files.append("calG192.G2/ANTENNA/table.dat")
	produced_files.append("calG192.G2/ANTENNA/table.lock")
	produced_files.append("calG192.G2/ANTENNA/table.info")
	produced_files.append("calG192.G2/ANTENNA/table.f0")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G2/HISTORY")
	produced_files.append("calG192.G2/HISTORY/table.dat")
	produced_files.append("calG192.G2/HISTORY/table.lock")
	produced_files.append("calG192.G2/HISTORY/table.info")
	produced_files.append("calG192.G2/HISTORY/table.f0")
	produced_files.append("calG192.G2/FIELD")
	produced_files.append("calG192.G2/FIELD/table.dat")
	produced_files.append("calG192.G2/FIELD/table.lock")
	produced_files.append("calG192.G2/FIELD/table.f0i")
	produced_files.append("calG192.G2/FIELD/table.info")
	produced_files.append("calG192.G2/FIELD/table.f0")
	produced_files.append("calG192.G2/table.f0i")
	produced_files.append("calG192.G2/table.info")
	produced_files.append("calG192.G2/OBSERVATION")
	produced_files.append("calG192.G2/OBSERVATION/table.dat")
	produced_files.append("calG192.G2/OBSERVATION/table.lock")
	produced_files.append("calG192.G2/OBSERVATION/table.info")
	produced_files.append("calG192.G2/OBSERVATION/table.f0")
	produced_files.append("calG192.G2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_28_using_fluxscale_to_transfer_the_amplitude_solutions():
	"""post method for "using fluxscale to transfer the amplitude solutions"
	"""
	produced_files = []
	produced_files.append("calG192.F2")
	produced_files.append("calG192.F2/table.dat")
	produced_files.append("calG192.F2/table.lock")
	produced_files.append("calG192.F2/ANTENNA")
	produced_files.append("calG192.F2/ANTENNA/table.dat")
	produced_files.append("calG192.F2/ANTENNA/table.lock")
	produced_files.append("calG192.F2/ANTENNA/table.info")
	produced_files.append("calG192.F2/ANTENNA/table.f0")
	produced_files.append("calG192.F2/SPECTRAL_WINDOW")
	produced_files.append("calG192.F2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.F2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.F2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.F2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.F2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.F2/HISTORY")
	produced_files.append("calG192.F2/HISTORY/table.dat")
	produced_files.append("calG192.F2/HISTORY/table.lock")
	produced_files.append("calG192.F2/HISTORY/table.info")
	produced_files.append("calG192.F2/HISTORY/table.f0")
	produced_files.append("calG192.F2/FIELD")
	produced_files.append("calG192.F2/FIELD/table.dat")
	produced_files.append("calG192.F2/FIELD/table.lock")
	produced_files.append("calG192.F2/FIELD/table.f0i")
	produced_files.append("calG192.F2/FIELD/table.info")
	produced_files.append("calG192.F2/FIELD/table.f0")
	produced_files.append("calG192.F2/table.f0i")
	produced_files.append("calG192.F2/table.info")
	produced_files.append("calG192.F2/OBSERVATION")
	produced_files.append("calG192.F2/OBSERVATION/table.dat")
	produced_files.append("calG192.F2/OBSERVATION/table.lock")
	produced_files.append("calG192.F2/OBSERVATION/table.info")
	produced_files.append("calG192.F2/OBSERVATION/table.f0")
	produced_files.append("calG192.F2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

# different data, checksum computed is 3b96fa951412a6022104d9d700e5a43e
def test_29_3c147_accumulated_calibration():
	"""post method for "3C147 accumulated calibration"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()
	field_id = 0
	checksum_ref= "3b96fa951412a6022104d9d700e5a43e"

	applycal_common(measet, field_id, checksum_ref)

# fix memory issues related to the checksum
def test_30_gain_accumulated_calibration():
	"""post method for "gain accumulated calibration"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()
	field_id = 1
	checksum_ref= ""

	#applycal_common(measet, field_id, checksum_ref)

# fix memory issues related to the checksum
def test_31_g192_accumulated_calibration():
	"""post method for "G192 accumulated calibration"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()	
	field_id = 2
	checksum_ref= ""

	#applycal_common(measet, field_id, checksum_ref)

# fix memory issues related to the checksum
def test_32_3c84_accumulated_calibration():
	"""post method for "3C84 accumulated calibration"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()	
	field_id = 3
	checksum_ref= ""

	#applycal_common(measet, field_id, checksum_ref)

def test_33_flagging_isolated_rfi():
	"""post method for "flagging isolated RFI"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()
	
	with msHandler(measet) as table:
		nrows = count_nonzero(table.getcol("FLAG_ROW"))
		assert nrows, "no FLAG_ROWS in %s" % measet
		assert nrows == -1, "the number of FLAG_ROWS (%s) doesn't match to the expected one" % nrows

def test_34_baseline_flagging():
	"""post method for "baseline flagging"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()
	
	with msHandler(measet) as table:
		nrows = count_nonzero(table.getcol("FLAG_ROW"))
		assert nrows, "no FLAG_ROWS in %s" % measet
		assert nrows == 30912, "the number of FLAG_ROWS (%s) doesn't match to the expected one" % nrows

def test_35_3c147_density_model():
	"""post method for "3C147 density model"
	"""
	measet = "%s/G192_flagged_6s.ms/SOURCE" % os.getcwd()
	checksum_ref = ""
	setjy_common(measet, checksum_ref)

def test_36_3c84_spectral_information_column():
	"""post method for "3C84 spectral information column"
	"""
	measet = "%s/G192_flagged_6s.ms/SOURCE" % os.getcwd()
	checksum_ref = ""
	setjy_common(measet, checksum_ref)

def test_37_initial_phase_calibration():
	"""post method for "initial phase calibration"
	"""
	produced_files = []
	produced_files.append("calG192.G0.b.2")
	produced_files.append("calG192.G0.b.2/table.dat")
	produced_files.append("calG192.G0.b.2/table.lock")
	produced_files.append("calG192.G0.b.2/ANTENNA")
	produced_files.append("calG192.G0.b.2/ANTENNA/table.dat")
	produced_files.append("calG192.G0.b.2/ANTENNA/table.lock")
	produced_files.append("calG192.G0.b.2/ANTENNA/table.info")
	produced_files.append("calG192.G0.b.2/ANTENNA/table.f0")
	produced_files.append("calG192.G0.b.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G0.b.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G0.b.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G0.b.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G0.b.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G0.b.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G0.b.2/HISTORY")
	produced_files.append("calG192.G0.b.2/HISTORY/table.dat")
	produced_files.append("calG192.G0.b.2/HISTORY/table.lock")
	produced_files.append("calG192.G0.b.2/HISTORY/table.info")
	produced_files.append("calG192.G0.b.2/HISTORY/table.f0")
	produced_files.append("calG192.G0.b.2/FIELD")
	produced_files.append("calG192.G0.b.2/FIELD/table.dat")
	produced_files.append("calG192.G0.b.2/FIELD/table.lock")
	produced_files.append("calG192.G0.b.2/FIELD/table.f0i")
	produced_files.append("calG192.G0.b.2/FIELD/table.info")
	produced_files.append("calG192.G0.b.2/FIELD/table.f0")
	produced_files.append("calG192.G0.b.2/table.f0i")
	produced_files.append("calG192.G0.b.2/table.info")
	produced_files.append("calG192.G0.b.2/OBSERVATION")
	produced_files.append("calG192.G0.b.2/OBSERVATION/table.dat")
	produced_files.append("calG192.G0.b.2/OBSERVATION/table.lock")
	produced_files.append("calG192.G0.b.2/OBSERVATION/table.info")
	produced_files.append("calG192.G0.b.2/OBSERVATION/table.f0")
	produced_files.append("calG192.G0.b.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_38_delay_calibration():
	"""post method for "delay calibration"
	"""
	produced_files = []
	produced_files.append("calG192.K0.b.2")
	produced_files.append("calG192.K0.b.2/table.dat")
	produced_files.append("calG192.K0.b.2/table.lock")
	produced_files.append("calG192.K0.b.2/ANTENNA")
	produced_files.append("calG192.K0.b.2/ANTENNA/table.dat")
	produced_files.append("calG192.K0.b.2/ANTENNA/table.lock")
	produced_files.append("calG192.K0.b.2/ANTENNA/table.info")
	produced_files.append("calG192.K0.b.2/ANTENNA/table.f0")
	produced_files.append("calG192.K0.b.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.K0.b.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.K0.b.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.K0.b.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.K0.b.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.K0.b.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.K0.b.2/HISTORY")
	produced_files.append("calG192.K0.b.2/HISTORY/table.dat")
	produced_files.append("calG192.K0.b.2/HISTORY/table.lock")
	produced_files.append("calG192.K0.b.2/HISTORY/table.info")
	produced_files.append("calG192.K0.b.2/HISTORY/table.f0")
	produced_files.append("calG192.K0.b.2/FIELD")
	produced_files.append("calG192.K0.b.2/FIELD/table.dat")
	produced_files.append("calG192.K0.b.2/FIELD/table.lock")
	produced_files.append("calG192.K0.b.2/FIELD/table.f0i")
	produced_files.append("calG192.K0.b.2/FIELD/table.info")
	produced_files.append("calG192.K0.b.2/FIELD/table.f0")
	produced_files.append("calG192.K0.b.2/table.f0i")
	produced_files.append("calG192.K0.b.2/table.info")
	produced_files.append("calG192.K0.b.2/OBSERVATION")
	produced_files.append("calG192.K0.b.2/OBSERVATION/table.dat")
	produced_files.append("calG192.K0.b.2/OBSERVATION/table.lock")
	produced_files.append("calG192.K0.b.2/OBSERVATION/table.info")
	produced_files.append("calG192.K0.b.2/OBSERVATION/table.f0")
	produced_files.append("calG192.K0.b.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_39_bandpass_calibration():
	"""post method for "bandpass calibration"
	"""
	produced_files = []
	produced_files.append("calG192.B0.b.2")
	produced_files.append("calG192.B0.b.2/table.dat")
	produced_files.append("calG192.B0.b.2/table.lock")
	produced_files.append("calG192.B0.b.2/ANTENNA")
	produced_files.append("calG192.B0.b.2/ANTENNA/table.dat")
	produced_files.append("calG192.B0.b.2/ANTENNA/table.lock")
	produced_files.append("calG192.B0.b.2/ANTENNA/table.info")
	produced_files.append("calG192.B0.b.2/ANTENNA/table.f0")
	produced_files.append("calG192.B0.b.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.B0.b.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.B0.b.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.B0.b.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.B0.b.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.B0.b.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.B0.b.2/HISTORY")
	produced_files.append("calG192.B0.b.2/HISTORY/table.dat")
	produced_files.append("calG192.B0.b.2/HISTORY/table.lock")
	produced_files.append("calG192.B0.b.2/HISTORY/table.info")
	produced_files.append("calG192.B0.b.2/HISTORY/table.f0")
	produced_files.append("calG192.B0.b.2/FIELD")
	produced_files.append("calG192.B0.b.2/FIELD/table.dat")
	produced_files.append("calG192.B0.b.2/FIELD/table.lock")
	produced_files.append("calG192.B0.b.2/FIELD/table.f0i")
	produced_files.append("calG192.B0.b.2/FIELD/table.info")
	produced_files.append("calG192.B0.b.2/FIELD/table.f0")
	produced_files.append("calG192.B0.b.2/table.f0i")
	produced_files.append("calG192.B0.b.2/table.info")
	produced_files.append("calG192.B0.b.2/OBSERVATION")
	produced_files.append("calG192.B0.b.2/OBSERVATION/table.dat")
	produced_files.append("calG192.B0.b.2/OBSERVATION/table.lock")
	produced_files.append("calG192.B0.b.2/OBSERVATION/table.info")
	produced_files.append("calG192.B0.b.2/OBSERVATION/table.f0")
	produced_files.append("calG192.B0.b.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_40_phase_gain_calibration_field_0():
	"""post method for "phase gain calibration field 0"
	"""
	produced_files = []
	produced_files.append("calG192.G1.int.2")
	produced_files.append("calG192.G1.int.2/table.dat")
	produced_files.append("calG192.G1.int.2/table.lock")
	produced_files.append("calG192.G1.int.2/ANTENNA")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.dat")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.lock")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.info")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.f0")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.int.2/HISTORY")
	produced_files.append("calG192.G1.int.2/HISTORY/table.dat")
	produced_files.append("calG192.G1.int.2/HISTORY/table.lock")
	produced_files.append("calG192.G1.int.2/HISTORY/table.info")
	produced_files.append("calG192.G1.int.2/HISTORY/table.f0")
	produced_files.append("calG192.G1.int.2/FIELD")
	produced_files.append("calG192.G1.int.2/FIELD/table.dat")
	produced_files.append("calG192.G1.int.2/FIELD/table.lock")
	produced_files.append("calG192.G1.int.2/FIELD/table.f0i")
	produced_files.append("calG192.G1.int.2/FIELD/table.info")
	produced_files.append("calG192.G1.int.2/FIELD/table.f0")
	produced_files.append("calG192.G1.int.2/table.f0i")
	produced_files.append("calG192.G1.int.2/table.info")
	produced_files.append("calG192.G1.int.2/OBSERVATION")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.info")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.int.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_41_phase_gain_calibration_field_1():
	"""post method for "phase gain calibration field 1"
	"""
	produced_files = []
	produced_files.append("calG192.G1.int.2")
	produced_files.append("calG192.G1.int.2/table.dat")
	produced_files.append("calG192.G1.int.2/table.lock")
	produced_files.append("calG192.G1.int.2/ANTENNA")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.dat")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.lock")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.info")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.f0")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.int.2/HISTORY")
	produced_files.append("calG192.G1.int.2/HISTORY/table.dat")
	produced_files.append("calG192.G1.int.2/HISTORY/table.lock")
	produced_files.append("calG192.G1.int.2/HISTORY/table.info")
	produced_files.append("calG192.G1.int.2/HISTORY/table.f0")
	produced_files.append("calG192.G1.int.2/FIELD")
	produced_files.append("calG192.G1.int.2/FIELD/table.dat")
	produced_files.append("calG192.G1.int.2/FIELD/table.lock")
	produced_files.append("calG192.G1.int.2/FIELD/table.f0i")
	produced_files.append("calG192.G1.int.2/FIELD/table.info")
	produced_files.append("calG192.G1.int.2/FIELD/table.f0")
	produced_files.append("calG192.G1.int.2/table.f0i")
	produced_files.append("calG192.G1.int.2/table.info")
	produced_files.append("calG192.G1.int.2/OBSERVATION")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.info")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.int.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_42_phase_gain_calibration_field_3():
	"""post method for "phase gain calibration field 3"
	"""
	produced_files = []
	produced_files.append("calG192.G1.int.2")
	produced_files.append("calG192.G1.int.2/table.dat")
	produced_files.append("calG192.G1.int.2/table.lock")
	produced_files.append("calG192.G1.int.2/ANTENNA")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.dat")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.lock")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.info")
	produced_files.append("calG192.G1.int.2/ANTENNA/table.f0")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.int.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.int.2/HISTORY")
	produced_files.append("calG192.G1.int.2/HISTORY/table.dat")
	produced_files.append("calG192.G1.int.2/HISTORY/table.lock")
	produced_files.append("calG192.G1.int.2/HISTORY/table.info")
	produced_files.append("calG192.G1.int.2/HISTORY/table.f0")
	produced_files.append("calG192.G1.int.2/FIELD")
	produced_files.append("calG192.G1.int.2/FIELD/table.dat")
	produced_files.append("calG192.G1.int.2/FIELD/table.lock")
	produced_files.append("calG192.G1.int.2/FIELD/table.f0i")
	produced_files.append("calG192.G1.int.2/FIELD/table.info")
	produced_files.append("calG192.G1.int.2/FIELD/table.f0")
	produced_files.append("calG192.G1.int.2/table.f0i")
	produced_files.append("calG192.G1.int.2/table.info")
	produced_files.append("calG192.G1.int.2/OBSERVATION")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.info")
	produced_files.append("calG192.G1.int.2/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.int.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_43_phase_gain_calibration_infinite_solution_interval():
	"""post method for "phase gain calibration infinite solution interval"
	"""
	produced_files = []
	produced_files.append("calG192.G1.inf.2")
	produced_files.append("calG192.G1.inf.2/table.dat")
	produced_files.append("calG192.G1.inf.2/table.lock")
	produced_files.append("calG192.G1.inf.2/ANTENNA")
	produced_files.append("calG192.G1.inf.2/ANTENNA/table.dat")
	produced_files.append("calG192.G1.inf.2/ANTENNA/table.lock")
	produced_files.append("calG192.G1.inf.2/ANTENNA/table.info")
	produced_files.append("calG192.G1.inf.2/ANTENNA/table.f0")
	produced_files.append("calG192.G1.inf.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G1.inf.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G1.inf.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G1.inf.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G1.inf.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G1.inf.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G1.inf.2/HISTORY")
	produced_files.append("calG192.G1.inf.2/HISTORY/table.dat")
	produced_files.append("calG192.G1.inf.2/HISTORY/table.lock")
	produced_files.append("calG192.G1.inf.2/HISTORY/table.info")
	produced_files.append("calG192.G1.inf.2/HISTORY/table.f0")
	produced_files.append("calG192.G1.inf.2/FIELD")
	produced_files.append("calG192.G1.inf.2/FIELD/table.dat")
	produced_files.append("calG192.G1.inf.2/FIELD/table.lock")
	produced_files.append("calG192.G1.inf.2/FIELD/table.f0i")
	produced_files.append("calG192.G1.inf.2/FIELD/table.info")
	produced_files.append("calG192.G1.inf.2/FIELD/table.f0")
	produced_files.append("calG192.G1.inf.2/table.f0i")
	produced_files.append("calG192.G1.inf.2/table.info")
	produced_files.append("calG192.G1.inf.2/OBSERVATION")
	produced_files.append("calG192.G1.inf.2/OBSERVATION/table.dat")
	produced_files.append("calG192.G1.inf.2/OBSERVATION/table.lock")
	produced_files.append("calG192.G1.inf.2/OBSERVATION/table.info")
	produced_files.append("calG192.G1.inf.2/OBSERVATION/table.f0")
	produced_files.append("calG192.G1.inf.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_44_amplitude_calibration_solutions_field_0():
	"""post method for "amplitude calibration solutions field 0"
	"""
	produced_files = []
	produced_files.append("calG192.G2")
	produced_files.append("calG192.G2/table.dat")
	produced_files.append("calG192.G2/table.lock")
	produced_files.append("calG192.G2/ANTENNA")
	produced_files.append("calG192.G2/ANTENNA/table.dat")
	produced_files.append("calG192.G2/ANTENNA/table.lock")
	produced_files.append("calG192.G2/ANTENNA/table.info")
	produced_files.append("calG192.G2/ANTENNA/table.f0")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G2/HISTORY")
	produced_files.append("calG192.G2/HISTORY/table.dat")
	produced_files.append("calG192.G2/HISTORY/table.lock")
	produced_files.append("calG192.G2/HISTORY/table.info")
	produced_files.append("calG192.G2/HISTORY/table.f0")
	produced_files.append("calG192.G2/FIELD")
	produced_files.append("calG192.G2/FIELD/table.dat")
	produced_files.append("calG192.G2/FIELD/table.lock")
	produced_files.append("calG192.G2/FIELD/table.f0i")
	produced_files.append("calG192.G2/FIELD/table.info")
	produced_files.append("calG192.G2/FIELD/table.f0")
	produced_files.append("calG192.G2/table.f0i")
	produced_files.append("calG192.G2/table.info")
	produced_files.append("calG192.G2/OBSERVATION")
	produced_files.append("calG192.G2/OBSERVATION/table.dat")
	produced_files.append("calG192.G2/OBSERVATION/table.lock")
	produced_files.append("calG192.G2/OBSERVATION/table.info")
	produced_files.append("calG192.G2/OBSERVATION/table.f0")
	produced_files.append("calG192.G2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_45_amplitude_calibration_solutions_field_1():
	"""post method for "amplitude calibration solutions field 1"
	"""
	produced_files = []
	produced_files.append("calG192.G2")
	produced_files.append("calG192.G2/table.dat")
	produced_files.append("calG192.G2/table.lock")
	produced_files.append("calG192.G2/ANTENNA")
	produced_files.append("calG192.G2/ANTENNA/table.dat")
	produced_files.append("calG192.G2/ANTENNA/table.lock")
	produced_files.append("calG192.G2/ANTENNA/table.info")
	produced_files.append("calG192.G2/ANTENNA/table.f0")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G2/HISTORY")
	produced_files.append("calG192.G2/HISTORY/table.dat")
	produced_files.append("calG192.G2/HISTORY/table.lock")
	produced_files.append("calG192.G2/HISTORY/table.info")
	produced_files.append("calG192.G2/HISTORY/table.f0")
	produced_files.append("calG192.G2/FIELD")
	produced_files.append("calG192.G2/FIELD/table.dat")
	produced_files.append("calG192.G2/FIELD/table.lock")
	produced_files.append("calG192.G2/FIELD/table.f0i")
	produced_files.append("calG192.G2/FIELD/table.info")
	produced_files.append("calG192.G2/FIELD/table.f0")
	produced_files.append("calG192.G2/table.f0i")
	produced_files.append("calG192.G2/table.info")
	produced_files.append("calG192.G2/OBSERVATION")
	produced_files.append("calG192.G2/OBSERVATION/table.dat")
	produced_files.append("calG192.G2/OBSERVATION/table.lock")
	produced_files.append("calG192.G2/OBSERVATION/table.info")
	produced_files.append("calG192.G2/OBSERVATION/table.f0")
	produced_files.append("calG192.G2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_46_amplitude_calibration_solutions_field_3():
	"""post method for "amplitude calibration solutions field 3"
	"""
	produced_files = []
	produced_files.append("calG192.G2")
	produced_files.append("calG192.G2/table.dat")
	produced_files.append("calG192.G2/table.lock")
	produced_files.append("calG192.G2/ANTENNA")
	produced_files.append("calG192.G2/ANTENNA/table.dat")
	produced_files.append("calG192.G2/ANTENNA/table.lock")
	produced_files.append("calG192.G2/ANTENNA/table.info")
	produced_files.append("calG192.G2/ANTENNA/table.f0")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.G2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.G2/HISTORY")
	produced_files.append("calG192.G2/HISTORY/table.dat")
	produced_files.append("calG192.G2/HISTORY/table.lock")
	produced_files.append("calG192.G2/HISTORY/table.info")
	produced_files.append("calG192.G2/HISTORY/table.f0")
	produced_files.append("calG192.G2/FIELD")
	produced_files.append("calG192.G2/FIELD/table.dat")
	produced_files.append("calG192.G2/FIELD/table.lock")
	produced_files.append("calG192.G2/FIELD/table.f0i")
	produced_files.append("calG192.G2/FIELD/table.info")
	produced_files.append("calG192.G2/FIELD/table.f0")
	produced_files.append("calG192.G2/table.f0i")
	produced_files.append("calG192.G2/table.info")
	produced_files.append("calG192.G2/OBSERVATION")
	produced_files.append("calG192.G2/OBSERVATION/table.dat")
	produced_files.append("calG192.G2/OBSERVATION/table.lock")
	produced_files.append("calG192.G2/OBSERVATION/table.info")
	produced_files.append("calG192.G2/OBSERVATION/table.f0")
	produced_files.append("calG192.G2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_47_flux_calibration_solutions():
	"""post method for "flux calibration solutions"
	"""
	produced_files = []
	produced_files.append("calG192.F2.2")
	produced_files.append("calG192.F2.2/table.dat")
	produced_files.append("calG192.F2.2/table.lock")
	produced_files.append("calG192.F2.2/ANTENNA")
	produced_files.append("calG192.F2.2/ANTENNA/table.dat")
	produced_files.append("calG192.F2.2/ANTENNA/table.lock")
	produced_files.append("calG192.F2.2/ANTENNA/table.info")
	produced_files.append("calG192.F2.2/ANTENNA/table.f0")
	produced_files.append("calG192.F2.2/SPECTRAL_WINDOW")
	produced_files.append("calG192.F2.2/SPECTRAL_WINDOW/table.dat")
	produced_files.append("calG192.F2.2/SPECTRAL_WINDOW/table.lock")
	produced_files.append("calG192.F2.2/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("calG192.F2.2/SPECTRAL_WINDOW/table.info")
	produced_files.append("calG192.F2.2/SPECTRAL_WINDOW/table.f0")
	produced_files.append("calG192.F2.2/HISTORY")
	produced_files.append("calG192.F2.2/HISTORY/table.dat")
	produced_files.append("calG192.F2.2/HISTORY/table.lock")
	produced_files.append("calG192.F2.2/HISTORY/table.info")
	produced_files.append("calG192.F2.2/HISTORY/table.f0")
	produced_files.append("calG192.F2.2/FIELD")
	produced_files.append("calG192.F2.2/FIELD/table.dat")
	produced_files.append("calG192.F2.2/FIELD/table.lock")
	produced_files.append("calG192.F2.2/FIELD/table.f0i")
	produced_files.append("calG192.F2.2/FIELD/table.info")
	produced_files.append("calG192.F2.2/FIELD/table.f0")
	produced_files.append("calG192.F2.2/table.f0i")
	produced_files.append("calG192.F2.2/table.info")
	produced_files.append("calG192.F2.2/OBSERVATION")
	produced_files.append("calG192.F2.2/OBSERVATION/table.dat")
	produced_files.append("calG192.F2.2/OBSERVATION/table.lock")
	produced_files.append("calG192.F2.2/OBSERVATION/table.info")
	produced_files.append("calG192.F2.2/OBSERVATION/table.f0")
	produced_files.append("calG192.F2.2/table.f0")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_48_apply_calibration_tables_field_0():
	"""post method for "apply calibration tables field 0"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()		
	field_id = 0
	checksum_ref= "f3ef0bb78677a022831e39aa268f3771"

	applycal_common(measet, field_id, checksum_ref)

def test_49_apply_calibration_tables_field_1():
	"""post method for "apply calibration tables field 1"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()	
	field_id = 1
	checksum_ref= ""

	#applycal_common(measet, field_id, checksum_ref)

def test_50_apply_calibration_tables_field_2():
	"""post method for "apply calibration tables field 2"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()	
	field_id = 2
	checksum_ref= ""

	#applycal_common(measet, field_id, checksum_ref)

def test_51_apply_calibration_tables_field_3():
	"""post method for "apply calibration tables field 3"
	"""
	measet = "%s/G192_flagged_6s.ms" % os.getcwd()	
	field_id = 3
	checksum_ref= ""

	#applycal_common(measet, field_id, checksum_ref)

def test_52_splitting_calibrated_data_3c147():
	"""post method for "splitting calibrated data 3C147"
	"""
	produced_files = []
	produced_files.append("3C147_split_6s.ms")
	produced_files.append("3C147_split_6s.ms/table.f19")
	produced_files.append("3C147_split_6s.ms/table.f2")
	produced_files.append("3C147_split_6s.ms/table.dat")
	produced_files.append("3C147_split_6s.ms/table.lock")
	produced_files.append("3C147_split_6s.ms/FLAG_CMD")
	produced_files.append("3C147_split_6s.ms/FLAG_CMD/table.dat")
	produced_files.append("3C147_split_6s.ms/FLAG_CMD/table.lock")
	produced_files.append("3C147_split_6s.ms/FLAG_CMD/table.info")
	produced_files.append("3C147_split_6s.ms/FLAG_CMD/table.f0")
	produced_files.append("3C147_split_6s.ms/SYSPOWER")
	produced_files.append("3C147_split_6s.ms/SYSPOWER/table.dat")
	produced_files.append("3C147_split_6s.ms/SYSPOWER/table.lock")
	produced_files.append("3C147_split_6s.ms/SYSPOWER/table.f0i")
	produced_files.append("3C147_split_6s.ms/SYSPOWER/table.info")
	produced_files.append("3C147_split_6s.ms/SYSPOWER/table.f0")
	produced_files.append("3C147_split_6s.ms/STATE")
	produced_files.append("3C147_split_6s.ms/STATE/table.dat")
	produced_files.append("3C147_split_6s.ms/STATE/table.lock")
	produced_files.append("3C147_split_6s.ms/STATE/table.info")
	produced_files.append("3C147_split_6s.ms/STATE/table.f0")
	produced_files.append("3C147_split_6s.ms/FEED")
	produced_files.append("3C147_split_6s.ms/FEED/table.dat")
	produced_files.append("3C147_split_6s.ms/FEED/table.lock")
	produced_files.append("3C147_split_6s.ms/FEED/table.f0i")
	produced_files.append("3C147_split_6s.ms/FEED/table.info")
	produced_files.append("3C147_split_6s.ms/FEED/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f10")
	produced_files.append("3C147_split_6s.ms/ANTENNA")
	produced_files.append("3C147_split_6s.ms/ANTENNA/table.dat")
	produced_files.append("3C147_split_6s.ms/ANTENNA/table.lock")
	produced_files.append("3C147_split_6s.ms/ANTENNA/table.info")
	produced_files.append("3C147_split_6s.ms/ANTENNA/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f18")
	produced_files.append("3C147_split_6s.ms/table.f20")
	produced_files.append("3C147_split_6s.ms/table.f12")
	produced_files.append("3C147_split_6s.ms/table.f11")
	produced_files.append("3C147_split_6s.ms/SPECTRAL_WINDOW")
	produced_files.append("3C147_split_6s.ms/SPECTRAL_WINDOW/table.dat")
	produced_files.append("3C147_split_6s.ms/SPECTRAL_WINDOW/table.lock")
	produced_files.append("3C147_split_6s.ms/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("3C147_split_6s.ms/SPECTRAL_WINDOW/table.info")
	produced_files.append("3C147_split_6s.ms/SPECTRAL_WINDOW/table.f0")
	produced_files.append("3C147_split_6s.ms/HISTORY")
	produced_files.append("3C147_split_6s.ms/HISTORY/table.dat")
	produced_files.append("3C147_split_6s.ms/HISTORY/table.lock")
	produced_files.append("3C147_split_6s.ms/HISTORY/table.info")
	produced_files.append("3C147_split_6s.ms/HISTORY/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f23")
	produced_files.append("3C147_split_6s.ms/table.f20_TSM0")
	produced_files.append("3C147_split_6s.ms/table.f16")
	produced_files.append("3C147_split_6s.ms/table.f1")
	produced_files.append("3C147_split_6s.ms/FIELD")
	produced_files.append("3C147_split_6s.ms/FIELD/table.dat")
	produced_files.append("3C147_split_6s.ms/FIELD/table.lock")
	produced_files.append("3C147_split_6s.ms/FIELD/table.f0i")
	produced_files.append("3C147_split_6s.ms/FIELD/table.info")
	produced_files.append("3C147_split_6s.ms/FIELD/table.f0")
	produced_files.append("3C147_split_6s.ms/DATA_DESCRIPTION")
	produced_files.append("3C147_split_6s.ms/DATA_DESCRIPTION/table.dat")
	produced_files.append("3C147_split_6s.ms/DATA_DESCRIPTION/table.lock")
	produced_files.append("3C147_split_6s.ms/DATA_DESCRIPTION/table.info")
	produced_files.append("3C147_split_6s.ms/DATA_DESCRIPTION/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f14")
	produced_files.append("3C147_split_6s.ms/table.f6")
	produced_files.append("3C147_split_6s.ms/SORTED_TABLE")
	produced_files.append("3C147_split_6s.ms/SORTED_TABLE/table.dat")
	produced_files.append("3C147_split_6s.ms/SORTED_TABLE/table.info")
	produced_files.append("3C147_split_6s.ms/POINTING")
	produced_files.append("3C147_split_6s.ms/POINTING/table.dat")
	produced_files.append("3C147_split_6s.ms/POINTING/table.lock")
	produced_files.append("3C147_split_6s.ms/POINTING/table.f0i")
	produced_files.append("3C147_split_6s.ms/POINTING/table.info")
	produced_files.append("3C147_split_6s.ms/POINTING/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f3")
	produced_files.append("3C147_split_6s.ms/table.f15")
	produced_files.append("3C147_split_6s.ms/table.f22")
	produced_files.append("3C147_split_6s.ms/table.f4")
	produced_files.append("3C147_split_6s.ms/table.f22_TSM1")
	produced_files.append("3C147_split_6s.ms/table.f5")
	produced_files.append("3C147_split_6s.ms/table.info")
	produced_files.append("3C147_split_6s.ms/PROCESSOR")
	produced_files.append("3C147_split_6s.ms/PROCESSOR/table.dat")
	produced_files.append("3C147_split_6s.ms/PROCESSOR/table.lock")
	produced_files.append("3C147_split_6s.ms/PROCESSOR/table.info")
	produced_files.append("3C147_split_6s.ms/PROCESSOR/table.f0")
	produced_files.append("3C147_split_6s.ms/POLARIZATION")
	produced_files.append("3C147_split_6s.ms/POLARIZATION/table.dat")
	produced_files.append("3C147_split_6s.ms/POLARIZATION/table.lock")
	produced_files.append("3C147_split_6s.ms/POLARIZATION/table.f0i")
	produced_files.append("3C147_split_6s.ms/POLARIZATION/table.info")
	produced_files.append("3C147_split_6s.ms/POLARIZATION/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f21_TSM1")
	produced_files.append("3C147_split_6s.ms/table.f21")
	produced_files.append("3C147_split_6s.ms/table.f8")
	produced_files.append("3C147_split_6s.ms/table.f23_TSM1")
	produced_files.append("3C147_split_6s.ms/SYSCAL")
	produced_files.append("3C147_split_6s.ms/SYSCAL/table.dat")
	produced_files.append("3C147_split_6s.ms/SYSCAL/table.lock")
	produced_files.append("3C147_split_6s.ms/SYSCAL/table.f0i")
	produced_files.append("3C147_split_6s.ms/SYSCAL/table.info")
	produced_files.append("3C147_split_6s.ms/SYSCAL/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f17")
	produced_files.append("3C147_split_6s.ms/SOURCE")
	produced_files.append("3C147_split_6s.ms/SOURCE/table.dat")
	produced_files.append("3C147_split_6s.ms/SOURCE/table.lock")
	produced_files.append("3C147_split_6s.ms/SOURCE/table.f0i")
	produced_files.append("3C147_split_6s.ms/SOURCE/table.info")
	produced_files.append("3C147_split_6s.ms/SOURCE/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f9")
	produced_files.append("3C147_split_6s.ms/CALDEVICE")
	produced_files.append("3C147_split_6s.ms/CALDEVICE/table.dat")
	produced_files.append("3C147_split_6s.ms/CALDEVICE/table.lock")
	produced_files.append("3C147_split_6s.ms/CALDEVICE/table.f0i")
	produced_files.append("3C147_split_6s.ms/CALDEVICE/table.info")
	produced_files.append("3C147_split_6s.ms/CALDEVICE/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f17_TSM1")
	produced_files.append("3C147_split_6s.ms/table.f13")
	produced_files.append("3C147_split_6s.ms/OBSERVATION")
	produced_files.append("3C147_split_6s.ms/OBSERVATION/table.dat")
	produced_files.append("3C147_split_6s.ms/OBSERVATION/table.lock")
	produced_files.append("3C147_split_6s.ms/OBSERVATION/table.info")
	produced_files.append("3C147_split_6s.ms/OBSERVATION/table.f0")
	produced_files.append("3C147_split_6s.ms/WEATHER")
	produced_files.append("3C147_split_6s.ms/WEATHER/table.dat")
	produced_files.append("3C147_split_6s.ms/WEATHER/table.lock")
	produced_files.append("3C147_split_6s.ms/WEATHER/table.info")
	produced_files.append("3C147_split_6s.ms/WEATHER/table.f0")
	produced_files.append("3C147_split_6s.ms/table.f7")

	RegressionHelper.assert_files(produced_files, os.getcwd())


	outputvis = "3C147_split_6s.ms"
	RegressionHelper.assert_file("%s/%s" % (os.getcwd(), outputvis))

	remove = []
	remove.append("%s/%s" % (os.getcwd(), outputvis))
	#RegressionHelper.data_remove(remove)

def test_53_splitting_calibrated_data_j0603_174():
	"""post method for "splitting calibrated data J0603+174"
	"""
	produced_files = []
	produced_files.append("J0603_split_6s.ms")
	produced_files.append("J0603_split_6s.ms/table.f19")
	produced_files.append("J0603_split_6s.ms/table.f2")
	produced_files.append("J0603_split_6s.ms/table.dat")
	produced_files.append("J0603_split_6s.ms/table.lock")
	produced_files.append("J0603_split_6s.ms/FLAG_CMD")
	produced_files.append("J0603_split_6s.ms/FLAG_CMD/table.dat")
	produced_files.append("J0603_split_6s.ms/FLAG_CMD/table.lock")
	produced_files.append("J0603_split_6s.ms/FLAG_CMD/table.info")
	produced_files.append("J0603_split_6s.ms/FLAG_CMD/table.f0")
	produced_files.append("J0603_split_6s.ms/SYSPOWER")
	produced_files.append("J0603_split_6s.ms/SYSPOWER/table.dat")
	produced_files.append("J0603_split_6s.ms/SYSPOWER/table.lock")
	produced_files.append("J0603_split_6s.ms/SYSPOWER/table.f0i")
	produced_files.append("J0603_split_6s.ms/SYSPOWER/table.info")
	produced_files.append("J0603_split_6s.ms/SYSPOWER/table.f0")
	produced_files.append("J0603_split_6s.ms/STATE")
	produced_files.append("J0603_split_6s.ms/STATE/table.dat")
	produced_files.append("J0603_split_6s.ms/STATE/table.lock")
	produced_files.append("J0603_split_6s.ms/STATE/table.info")
	produced_files.append("J0603_split_6s.ms/STATE/table.f0")
	produced_files.append("J0603_split_6s.ms/FEED")
	produced_files.append("J0603_split_6s.ms/FEED/table.dat")
	produced_files.append("J0603_split_6s.ms/FEED/table.lock")
	produced_files.append("J0603_split_6s.ms/FEED/table.f0i")
	produced_files.append("J0603_split_6s.ms/FEED/table.info")
	produced_files.append("J0603_split_6s.ms/FEED/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f10")
	produced_files.append("J0603_split_6s.ms/ANTENNA")
	produced_files.append("J0603_split_6s.ms/ANTENNA/table.dat")
	produced_files.append("J0603_split_6s.ms/ANTENNA/table.lock")
	produced_files.append("J0603_split_6s.ms/ANTENNA/table.info")
	produced_files.append("J0603_split_6s.ms/ANTENNA/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f18")
	produced_files.append("J0603_split_6s.ms/table.f20")
	produced_files.append("J0603_split_6s.ms/table.f12")
	produced_files.append("J0603_split_6s.ms/table.f11")
	produced_files.append("J0603_split_6s.ms/SPECTRAL_WINDOW")
	produced_files.append("J0603_split_6s.ms/SPECTRAL_WINDOW/table.dat")
	produced_files.append("J0603_split_6s.ms/SPECTRAL_WINDOW/table.lock")
	produced_files.append("J0603_split_6s.ms/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("J0603_split_6s.ms/SPECTRAL_WINDOW/table.info")
	produced_files.append("J0603_split_6s.ms/SPECTRAL_WINDOW/table.f0")
	produced_files.append("J0603_split_6s.ms/HISTORY")
	produced_files.append("J0603_split_6s.ms/HISTORY/table.dat")
	produced_files.append("J0603_split_6s.ms/HISTORY/table.lock")
	produced_files.append("J0603_split_6s.ms/HISTORY/table.info")
	produced_files.append("J0603_split_6s.ms/HISTORY/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f23")
	produced_files.append("J0603_split_6s.ms/table.f20_TSM0")
	produced_files.append("J0603_split_6s.ms/table.f16")
	produced_files.append("J0603_split_6s.ms/table.f1")
	produced_files.append("J0603_split_6s.ms/FIELD")
	produced_files.append("J0603_split_6s.ms/FIELD/table.dat")
	produced_files.append("J0603_split_6s.ms/FIELD/table.lock")
	produced_files.append("J0603_split_6s.ms/FIELD/table.f0i")
	produced_files.append("J0603_split_6s.ms/FIELD/table.info")
	produced_files.append("J0603_split_6s.ms/FIELD/table.f0")
	produced_files.append("J0603_split_6s.ms/DATA_DESCRIPTION")
	produced_files.append("J0603_split_6s.ms/DATA_DESCRIPTION/table.dat")
	produced_files.append("J0603_split_6s.ms/DATA_DESCRIPTION/table.lock")
	produced_files.append("J0603_split_6s.ms/DATA_DESCRIPTION/table.info")
	produced_files.append("J0603_split_6s.ms/DATA_DESCRIPTION/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f14")
	produced_files.append("J0603_split_6s.ms/table.f6")
	produced_files.append("J0603_split_6s.ms/SORTED_TABLE")
	produced_files.append("J0603_split_6s.ms/SORTED_TABLE/table.dat")
	produced_files.append("J0603_split_6s.ms/SORTED_TABLE/table.info")
	produced_files.append("J0603_split_6s.ms/POINTING")
	produced_files.append("J0603_split_6s.ms/POINTING/table.dat")
	produced_files.append("J0603_split_6s.ms/POINTING/table.lock")
	produced_files.append("J0603_split_6s.ms/POINTING/table.f0i")
	produced_files.append("J0603_split_6s.ms/POINTING/table.info")
	produced_files.append("J0603_split_6s.ms/POINTING/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f3")
	produced_files.append("J0603_split_6s.ms/table.f15")
	produced_files.append("J0603_split_6s.ms/table.f22")
	produced_files.append("J0603_split_6s.ms/table.f4")
	produced_files.append("J0603_split_6s.ms/table.f22_TSM1")
	produced_files.append("J0603_split_6s.ms/table.f5")
	produced_files.append("J0603_split_6s.ms/table.info")
	produced_files.append("J0603_split_6s.ms/PROCESSOR")
	produced_files.append("J0603_split_6s.ms/PROCESSOR/table.dat")
	produced_files.append("J0603_split_6s.ms/PROCESSOR/table.lock")
	produced_files.append("J0603_split_6s.ms/PROCESSOR/table.info")
	produced_files.append("J0603_split_6s.ms/PROCESSOR/table.f0")
	produced_files.append("J0603_split_6s.ms/POLARIZATION")
	produced_files.append("J0603_split_6s.ms/POLARIZATION/table.dat")
	produced_files.append("J0603_split_6s.ms/POLARIZATION/table.lock")
	produced_files.append("J0603_split_6s.ms/POLARIZATION/table.f0i")
	produced_files.append("J0603_split_6s.ms/POLARIZATION/table.info")
	produced_files.append("J0603_split_6s.ms/POLARIZATION/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f21_TSM1")
	produced_files.append("J0603_split_6s.ms/table.f21")
	produced_files.append("J0603_split_6s.ms/table.f8")
	produced_files.append("J0603_split_6s.ms/table.f23_TSM1")
	produced_files.append("J0603_split_6s.ms/SYSCAL")
	produced_files.append("J0603_split_6s.ms/SYSCAL/table.dat")
	produced_files.append("J0603_split_6s.ms/SYSCAL/table.lock")
	produced_files.append("J0603_split_6s.ms/SYSCAL/table.f0i")
	produced_files.append("J0603_split_6s.ms/SYSCAL/table.info")
	produced_files.append("J0603_split_6s.ms/SYSCAL/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f17")
	produced_files.append("J0603_split_6s.ms/SOURCE")
	produced_files.append("J0603_split_6s.ms/SOURCE/table.dat")
	produced_files.append("J0603_split_6s.ms/SOURCE/table.lock")
	produced_files.append("J0603_split_6s.ms/SOURCE/table.f0i")
	produced_files.append("J0603_split_6s.ms/SOURCE/table.info")
	produced_files.append("J0603_split_6s.ms/SOURCE/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f9")
	produced_files.append("J0603_split_6s.ms/CALDEVICE")
	produced_files.append("J0603_split_6s.ms/CALDEVICE/table.dat")
	produced_files.append("J0603_split_6s.ms/CALDEVICE/table.lock")
	produced_files.append("J0603_split_6s.ms/CALDEVICE/table.f0i")
	produced_files.append("J0603_split_6s.ms/CALDEVICE/table.info")
	produced_files.append("J0603_split_6s.ms/CALDEVICE/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f17_TSM1")
	produced_files.append("J0603_split_6s.ms/table.f13")
	produced_files.append("J0603_split_6s.ms/OBSERVATION")
	produced_files.append("J0603_split_6s.ms/OBSERVATION/table.dat")
	produced_files.append("J0603_split_6s.ms/OBSERVATION/table.lock")
	produced_files.append("J0603_split_6s.ms/OBSERVATION/table.info")
	produced_files.append("J0603_split_6s.ms/OBSERVATION/table.f0")
	produced_files.append("J0603_split_6s.ms/WEATHER")
	produced_files.append("J0603_split_6s.ms/WEATHER/table.dat")
	produced_files.append("J0603_split_6s.ms/WEATHER/table.lock")
	produced_files.append("J0603_split_6s.ms/WEATHER/table.info")
	produced_files.append("J0603_split_6s.ms/WEATHER/table.f0")
	produced_files.append("J0603_split_6s.ms/table.f7")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_54_splitting_calibrated_data_g192():
	"""post method for "splitting calibrated data G192"
	"""
	produced_files = []
	produced_files.append("G192_split_6s.ms")
	produced_files.append("G192_split_6s.ms/table.f19")
	produced_files.append("G192_split_6s.ms/table.f2")
	produced_files.append("G192_split_6s.ms/table.dat")
	produced_files.append("G192_split_6s.ms/table.lock")
	produced_files.append("G192_split_6s.ms/FLAG_CMD")
	produced_files.append("G192_split_6s.ms/FLAG_CMD/table.dat")
	produced_files.append("G192_split_6s.ms/FLAG_CMD/table.lock")
	produced_files.append("G192_split_6s.ms/FLAG_CMD/table.info")
	produced_files.append("G192_split_6s.ms/FLAG_CMD/table.f0")
	produced_files.append("G192_split_6s.ms/SYSPOWER")
	produced_files.append("G192_split_6s.ms/SYSPOWER/table.dat")
	produced_files.append("G192_split_6s.ms/SYSPOWER/table.lock")
	produced_files.append("G192_split_6s.ms/SYSPOWER/table.f0i")
	produced_files.append("G192_split_6s.ms/SYSPOWER/table.info")
	produced_files.append("G192_split_6s.ms/SYSPOWER/table.f0")
	produced_files.append("G192_split_6s.ms/STATE")
	produced_files.append("G192_split_6s.ms/STATE/table.dat")
	produced_files.append("G192_split_6s.ms/STATE/table.lock")
	produced_files.append("G192_split_6s.ms/STATE/table.info")
	produced_files.append("G192_split_6s.ms/STATE/table.f0")
	produced_files.append("G192_split_6s.ms/FEED")
	produced_files.append("G192_split_6s.ms/FEED/table.dat")
	produced_files.append("G192_split_6s.ms/FEED/table.lock")
	produced_files.append("G192_split_6s.ms/FEED/table.f0i")
	produced_files.append("G192_split_6s.ms/FEED/table.info")
	produced_files.append("G192_split_6s.ms/FEED/table.f0")
	produced_files.append("G192_split_6s.ms/table.f10")
	produced_files.append("G192_split_6s.ms/ANTENNA")
	produced_files.append("G192_split_6s.ms/ANTENNA/table.dat")
	produced_files.append("G192_split_6s.ms/ANTENNA/table.lock")
	produced_files.append("G192_split_6s.ms/ANTENNA/table.info")
	produced_files.append("G192_split_6s.ms/ANTENNA/table.f0")
	produced_files.append("G192_split_6s.ms/table.f18")
	produced_files.append("G192_split_6s.ms/table.f20")
	produced_files.append("G192_split_6s.ms/table.f12")
	produced_files.append("G192_split_6s.ms/table.f11")
	produced_files.append("G192_split_6s.ms/SPECTRAL_WINDOW")
	produced_files.append("G192_split_6s.ms/SPECTRAL_WINDOW/table.dat")
	produced_files.append("G192_split_6s.ms/SPECTRAL_WINDOW/table.lock")
	produced_files.append("G192_split_6s.ms/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("G192_split_6s.ms/SPECTRAL_WINDOW/table.info")
	produced_files.append("G192_split_6s.ms/SPECTRAL_WINDOW/table.f0")
	produced_files.append("G192_split_6s.ms/HISTORY")
	produced_files.append("G192_split_6s.ms/HISTORY/table.dat")
	produced_files.append("G192_split_6s.ms/HISTORY/table.lock")
	produced_files.append("G192_split_6s.ms/HISTORY/table.info")
	produced_files.append("G192_split_6s.ms/HISTORY/table.f0")
	produced_files.append("G192_split_6s.ms/table.f23")
	produced_files.append("G192_split_6s.ms/table.f20_TSM0")
	produced_files.append("G192_split_6s.ms/table.f16")
	produced_files.append("G192_split_6s.ms/table.f1")
	produced_files.append("G192_split_6s.ms/FIELD")
	produced_files.append("G192_split_6s.ms/FIELD/table.dat")
	produced_files.append("G192_split_6s.ms/FIELD/table.lock")
	produced_files.append("G192_split_6s.ms/FIELD/table.f0i")
	produced_files.append("G192_split_6s.ms/FIELD/table.info")
	produced_files.append("G192_split_6s.ms/FIELD/table.f0")
	produced_files.append("G192_split_6s.ms/DATA_DESCRIPTION")
	produced_files.append("G192_split_6s.ms/DATA_DESCRIPTION/table.dat")
	produced_files.append("G192_split_6s.ms/DATA_DESCRIPTION/table.lock")
	produced_files.append("G192_split_6s.ms/DATA_DESCRIPTION/table.info")
	produced_files.append("G192_split_6s.ms/DATA_DESCRIPTION/table.f0")
	produced_files.append("G192_split_6s.ms/table.f14")
	produced_files.append("G192_split_6s.ms/table.f6")
	produced_files.append("G192_split_6s.ms/SORTED_TABLE")
	produced_files.append("G192_split_6s.ms/SORTED_TABLE/table.dat")
	produced_files.append("G192_split_6s.ms/SORTED_TABLE/table.info")
	produced_files.append("G192_split_6s.ms/POINTING")
	produced_files.append("G192_split_6s.ms/POINTING/table.dat")
	produced_files.append("G192_split_6s.ms/POINTING/table.lock")
	produced_files.append("G192_split_6s.ms/POINTING/table.f0i")
	produced_files.append("G192_split_6s.ms/POINTING/table.info")
	produced_files.append("G192_split_6s.ms/POINTING/table.f0")
	produced_files.append("G192_split_6s.ms/table.f3")
	produced_files.append("G192_split_6s.ms/table.f15")
	produced_files.append("G192_split_6s.ms/table.f22")
	produced_files.append("G192_split_6s.ms/table.f4")
	produced_files.append("G192_split_6s.ms/table.f22_TSM1")
	produced_files.append("G192_split_6s.ms/table.f5")
	produced_files.append("G192_split_6s.ms/table.info")
	produced_files.append("G192_split_6s.ms/PROCESSOR")
	produced_files.append("G192_split_6s.ms/PROCESSOR/table.dat")
	produced_files.append("G192_split_6s.ms/PROCESSOR/table.lock")
	produced_files.append("G192_split_6s.ms/PROCESSOR/table.info")
	produced_files.append("G192_split_6s.ms/PROCESSOR/table.f0")
	produced_files.append("G192_split_6s.ms/POLARIZATION")
	produced_files.append("G192_split_6s.ms/POLARIZATION/table.dat")
	produced_files.append("G192_split_6s.ms/POLARIZATION/table.lock")
	produced_files.append("G192_split_6s.ms/POLARIZATION/table.f0i")
	produced_files.append("G192_split_6s.ms/POLARIZATION/table.info")
	produced_files.append("G192_split_6s.ms/POLARIZATION/table.f0")
	produced_files.append("G192_split_6s.ms/table.f21_TSM1")
	produced_files.append("G192_split_6s.ms/table.f21")
	produced_files.append("G192_split_6s.ms/table.f8")
	produced_files.append("G192_split_6s.ms/table.f23_TSM1")
	produced_files.append("G192_split_6s.ms/SYSCAL")
	produced_files.append("G192_split_6s.ms/SYSCAL/table.dat")
	produced_files.append("G192_split_6s.ms/SYSCAL/table.lock")
	produced_files.append("G192_split_6s.ms/SYSCAL/table.f0i")
	produced_files.append("G192_split_6s.ms/SYSCAL/table.info")
	produced_files.append("G192_split_6s.ms/SYSCAL/table.f0")
	produced_files.append("G192_split_6s.ms/table.f17")
	produced_files.append("G192_split_6s.ms/SOURCE")
	produced_files.append("G192_split_6s.ms/SOURCE/table.dat")
	produced_files.append("G192_split_6s.ms/SOURCE/table.lock")
	produced_files.append("G192_split_6s.ms/SOURCE/table.f0i")
	produced_files.append("G192_split_6s.ms/SOURCE/table.info")
	produced_files.append("G192_split_6s.ms/SOURCE/table.f0")
	produced_files.append("G192_split_6s.ms/table.f9")
	produced_files.append("G192_split_6s.ms/CALDEVICE")
	produced_files.append("G192_split_6s.ms/CALDEVICE/table.dat")
	produced_files.append("G192_split_6s.ms/CALDEVICE/table.lock")
	produced_files.append("G192_split_6s.ms/CALDEVICE/table.f0i")
	produced_files.append("G192_split_6s.ms/CALDEVICE/table.info")
	produced_files.append("G192_split_6s.ms/CALDEVICE/table.f0")
	produced_files.append("G192_split_6s.ms/table.f17_TSM1")
	produced_files.append("G192_split_6s.ms/table.f13")
	produced_files.append("G192_split_6s.ms/OBSERVATION")
	produced_files.append("G192_split_6s.ms/OBSERVATION/table.dat")
	produced_files.append("G192_split_6s.ms/OBSERVATION/table.lock")
	produced_files.append("G192_split_6s.ms/OBSERVATION/table.info")
	produced_files.append("G192_split_6s.ms/OBSERVATION/table.f0")
	produced_files.append("G192_split_6s.ms/WEATHER")
	produced_files.append("G192_split_6s.ms/WEATHER/table.dat")
	produced_files.append("G192_split_6s.ms/WEATHER/table.lock")
	produced_files.append("G192_split_6s.ms/WEATHER/table.info")
	produced_files.append("G192_split_6s.ms/WEATHER/table.f0")
	produced_files.append("G192_split_6s.ms/table.f7")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_55_splitting_calibrated_data_3c84():
	"""post method for "splitting calibrated data 3C84"
	"""
	produced_files = []
	produced_files.append("3C84_split_6s.ms")
	produced_files.append("3C84_split_6s.ms/table.f19")
	produced_files.append("3C84_split_6s.ms/table.f2")
	produced_files.append("3C84_split_6s.ms/table.dat")
	produced_files.append("3C84_split_6s.ms/table.lock")
	produced_files.append("3C84_split_6s.ms/FLAG_CMD")
	produced_files.append("3C84_split_6s.ms/FLAG_CMD/table.dat")
	produced_files.append("3C84_split_6s.ms/FLAG_CMD/table.lock")
	produced_files.append("3C84_split_6s.ms/FLAG_CMD/table.info")
	produced_files.append("3C84_split_6s.ms/FLAG_CMD/table.f0")
	produced_files.append("3C84_split_6s.ms/SYSPOWER")
	produced_files.append("3C84_split_6s.ms/SYSPOWER/table.dat")
	produced_files.append("3C84_split_6s.ms/SYSPOWER/table.lock")
	produced_files.append("3C84_split_6s.ms/SYSPOWER/table.f0i")
	produced_files.append("3C84_split_6s.ms/SYSPOWER/table.info")
	produced_files.append("3C84_split_6s.ms/SYSPOWER/table.f0")
	produced_files.append("3C84_split_6s.ms/STATE")
	produced_files.append("3C84_split_6s.ms/STATE/table.dat")
	produced_files.append("3C84_split_6s.ms/STATE/table.lock")
	produced_files.append("3C84_split_6s.ms/STATE/table.info")
	produced_files.append("3C84_split_6s.ms/STATE/table.f0")
	produced_files.append("3C84_split_6s.ms/FEED")
	produced_files.append("3C84_split_6s.ms/FEED/table.dat")
	produced_files.append("3C84_split_6s.ms/FEED/table.lock")
	produced_files.append("3C84_split_6s.ms/FEED/table.f0i")
	produced_files.append("3C84_split_6s.ms/FEED/table.info")
	produced_files.append("3C84_split_6s.ms/FEED/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f10")
	produced_files.append("3C84_split_6s.ms/ANTENNA")
	produced_files.append("3C84_split_6s.ms/ANTENNA/table.dat")
	produced_files.append("3C84_split_6s.ms/ANTENNA/table.lock")
	produced_files.append("3C84_split_6s.ms/ANTENNA/table.info")
	produced_files.append("3C84_split_6s.ms/ANTENNA/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f18")
	produced_files.append("3C84_split_6s.ms/table.f20")
	produced_files.append("3C84_split_6s.ms/table.f12")
	produced_files.append("3C84_split_6s.ms/table.f11")
	produced_files.append("3C84_split_6s.ms/SPECTRAL_WINDOW")
	produced_files.append("3C84_split_6s.ms/SPECTRAL_WINDOW/table.dat")
	produced_files.append("3C84_split_6s.ms/SPECTRAL_WINDOW/table.lock")
	produced_files.append("3C84_split_6s.ms/SPECTRAL_WINDOW/table.f0i")
	produced_files.append("3C84_split_6s.ms/SPECTRAL_WINDOW/table.info")
	produced_files.append("3C84_split_6s.ms/SPECTRAL_WINDOW/table.f0")
	produced_files.append("3C84_split_6s.ms/HISTORY")
	produced_files.append("3C84_split_6s.ms/HISTORY/table.dat")
	produced_files.append("3C84_split_6s.ms/HISTORY/table.lock")
	produced_files.append("3C84_split_6s.ms/HISTORY/table.info")
	produced_files.append("3C84_split_6s.ms/HISTORY/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f23")
	produced_files.append("3C84_split_6s.ms/table.f20_TSM0")
	produced_files.append("3C84_split_6s.ms/table.f16")
	produced_files.append("3C84_split_6s.ms/table.f1")
	produced_files.append("3C84_split_6s.ms/FIELD")
	produced_files.append("3C84_split_6s.ms/FIELD/table.dat")
	produced_files.append("3C84_split_6s.ms/FIELD/table.lock")
	produced_files.append("3C84_split_6s.ms/FIELD/table.f0i")
	produced_files.append("3C84_split_6s.ms/FIELD/table.info")
	produced_files.append("3C84_split_6s.ms/FIELD/table.f0")
	produced_files.append("3C84_split_6s.ms/DATA_DESCRIPTION")
	produced_files.append("3C84_split_6s.ms/DATA_DESCRIPTION/table.dat")
	produced_files.append("3C84_split_6s.ms/DATA_DESCRIPTION/table.lock")
	produced_files.append("3C84_split_6s.ms/DATA_DESCRIPTION/table.info")
	produced_files.append("3C84_split_6s.ms/DATA_DESCRIPTION/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f14")
	produced_files.append("3C84_split_6s.ms/table.f6")
	produced_files.append("3C84_split_6s.ms/SORTED_TABLE")
	produced_files.append("3C84_split_6s.ms/SORTED_TABLE/table.dat")
	produced_files.append("3C84_split_6s.ms/SORTED_TABLE/table.info")
	produced_files.append("3C84_split_6s.ms/POINTING")
	produced_files.append("3C84_split_6s.ms/POINTING/table.dat")
	produced_files.append("3C84_split_6s.ms/POINTING/table.lock")
	produced_files.append("3C84_split_6s.ms/POINTING/table.f0i")
	produced_files.append("3C84_split_6s.ms/POINTING/table.info")
	produced_files.append("3C84_split_6s.ms/POINTING/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f3")
	produced_files.append("3C84_split_6s.ms/table.f15")
	produced_files.append("3C84_split_6s.ms/table.f22")
	produced_files.append("3C84_split_6s.ms/table.f4")
	produced_files.append("3C84_split_6s.ms/table.f22_TSM1")
	produced_files.append("3C84_split_6s.ms/table.f5")
	produced_files.append("3C84_split_6s.ms/table.info")
	produced_files.append("3C84_split_6s.ms/PROCESSOR")
	produced_files.append("3C84_split_6s.ms/PROCESSOR/table.dat")
	produced_files.append("3C84_split_6s.ms/PROCESSOR/table.lock")
	produced_files.append("3C84_split_6s.ms/PROCESSOR/table.info")
	produced_files.append("3C84_split_6s.ms/PROCESSOR/table.f0")
	produced_files.append("3C84_split_6s.ms/POLARIZATION")
	produced_files.append("3C84_split_6s.ms/POLARIZATION/table.dat")
	produced_files.append("3C84_split_6s.ms/POLARIZATION/table.lock")
	produced_files.append("3C84_split_6s.ms/POLARIZATION/table.f0i")
	produced_files.append("3C84_split_6s.ms/POLARIZATION/table.info")
	produced_files.append("3C84_split_6s.ms/POLARIZATION/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f21_TSM1")
	produced_files.append("3C84_split_6s.ms/table.f21")
	produced_files.append("3C84_split_6s.ms/table.f8")
	produced_files.append("3C84_split_6s.ms/table.f23_TSM1")
	produced_files.append("3C84_split_6s.ms/SYSCAL")
	produced_files.append("3C84_split_6s.ms/SYSCAL/table.dat")
	produced_files.append("3C84_split_6s.ms/SYSCAL/table.lock")
	produced_files.append("3C84_split_6s.ms/SYSCAL/table.f0i")
	produced_files.append("3C84_split_6s.ms/SYSCAL/table.info")
	produced_files.append("3C84_split_6s.ms/SYSCAL/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f17")
	produced_files.append("3C84_split_6s.ms/SOURCE")
	produced_files.append("3C84_split_6s.ms/SOURCE/table.dat")
	produced_files.append("3C84_split_6s.ms/SOURCE/table.lock")
	produced_files.append("3C84_split_6s.ms/SOURCE/table.f0i")
	produced_files.append("3C84_split_6s.ms/SOURCE/table.info")
	produced_files.append("3C84_split_6s.ms/SOURCE/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f9")
	produced_files.append("3C84_split_6s.ms/CALDEVICE")
	produced_files.append("3C84_split_6s.ms/CALDEVICE/table.dat")
	produced_files.append("3C84_split_6s.ms/CALDEVICE/table.lock")
	produced_files.append("3C84_split_6s.ms/CALDEVICE/table.f0i")
	produced_files.append("3C84_split_6s.ms/CALDEVICE/table.info")
	produced_files.append("3C84_split_6s.ms/CALDEVICE/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f17_TSM1")
	produced_files.append("3C84_split_6s.ms/table.f13")
	produced_files.append("3C84_split_6s.ms/OBSERVATION")
	produced_files.append("3C84_split_6s.ms/OBSERVATION/table.dat")
	produced_files.append("3C84_split_6s.ms/OBSERVATION/table.lock")
	produced_files.append("3C84_split_6s.ms/OBSERVATION/table.info")
	produced_files.append("3C84_split_6s.ms/OBSERVATION/table.f0")
	produced_files.append("3C84_split_6s.ms/WEATHER")
	produced_files.append("3C84_split_6s.ms/WEATHER/table.dat")
	produced_files.append("3C84_split_6s.ms/WEATHER/table.lock")
	produced_files.append("3C84_split_6s.ms/WEATHER/table.info")
	produced_files.append("3C84_split_6s.ms/WEATHER/table.f0")
	produced_files.append("3C84_split_6s.ms/table.f7")

	RegressionHelper.assert_files(produced_files, os.getcwd())

def test_56_single_spectral_window_cleaning():
	"""post method for "single spectral window cleaning"
	"""
	raise NotImplementedError("post test method not implemented")

def test_57_lower_frequency_baseband_cleaning():
	"""post method for "lower frequency baseband cleaning"
	"""
	raise NotImplementedError("post test method not implemented")

def test_58_upper_frequency_baseband_cleaning():
	"""post method for "upper frequency baseband cleaning"
	"""
	raise NotImplementedError("post test method not implemented")

def test_59_basebands_mfs_taylor_cleaning():
	"""post method for "basebands mfs taylor cleaning"
	"""
	raise NotImplementedError("post test method not implemented")

def test_60_spectral_index_image_filtering():
	"""post method for "spectral index image filtering"
	"""
	outfile = "imgG192_6s_spw0-63_mfs2.image.alpha.filtered"
	RegressionHelper.assert_file("%s/%s" % (os.getcwd(), outfile))

def test_61_spectral_index_probable_errors_filtering():
	"""post method for "spectral index probable errors filtering"
	"""
	outfile = "imgG192_6s_spw0-63_mfs2.image.alpha.error.filtered"
	RegressionHelper.assert_file("%s/%s" % (os.getcwd(), outfile))

def test_62_intensity_weighted_mean_spectral_analysis():
	"""post method for "intensity weighted mean spectral analysis"
	"""
	outfile_tt1 = "imgG192_6s_spw0-63_mfs2.image.tt1.filtered"
	outfile_tt0 = "imgG192_6s_spw0-63_mfs2.image.tt0.filtered"
	
	RegressionHelper.assert_file("%s/%s" % (os.getcwd(), outfile_tt1))
	RegressionHelper.assert_file("%s/%s" % (os.getcwd(), outfile_tt0))


# temporal mapping shift

# test_27_using_fluxscale_to_transfer_the_amplitude_solutions	= test_28_using_fluxscale_to_transfer_the_amplitude_solutions
# test_28_3c147_accumulated_calibration	= test_29_3c147_accumulated_calibration
# test_29_gain_accumulated_calibration	= test_30_gain_accumulated_calibration
# test_30_g192_accumulated_calibration	= test_31_g192_accumulated_calibration
# test_31_3c84_accumulated_calibration	= test_32_3c84_accumulated_calibration
# test_32_flagging_isolated_rfi	= test_33_flagging_isolated_rfi
# test_33_baseline_flagging	= test_34_baseline_flagging
# test_34_3c147_density_model	= test_35_3c147_density_model
# test_35_3c84_spectral_information_column	= test_36_3c84_spectral_information_column
# test_36_initial_phase_calibration	= test_37_initial_phase_calibration
# test_37_delay_calibration	= test_38_delay_calibration
# test_38_bandpass_calibration	= test_39_bandpass_calibration
# test_39_phase_gain_calibration_field_0	= test_40_phase_gain_calibration_field_0
# test_40_phase_gain_calibration_field_1	= test_41_phase_gain_calibration_field_1
# test_41_phase_gain_calibration_field_3	= test_42_phase_gain_calibration_field_3
# test_42_phase_gain_calibration_infinite_solution_interval	= test_43_phase_gain_calibration_infinite_solution_interval
# test_43_amplitude_calibration_solutions_field_0	= test_44_amplitude_calibration_solutions_field_0
# test_44_amplitude_calibration_solutions_field_1	= test_45_amplitude_calibration_solutions_field_1
# test_45_amplitude_calibration_solutions_field_3	= test_46_amplitude_calibration_solutions_field_3
# test_46_flux_calibration_solutions	= test_47_flux_calibration_solutions
# test_47_apply_calibration_tables_field_0	= test_48_apply_calibration_tables_field_0
# test_48_apply_calibration_tables_field_1	= test_49_apply_calibration_tables_field_1
# test_49_apply_calibration_tables_field_2	= test_50_apply_calibration_tables_field_2
# test_50_apply_calibration_tables_field_3	= test_51_apply_calibration_tables_field_3
# test_51_splitting_calibrated_data_3c147	= test_52_splitting_calibrated_data_3c147
# test_52_splitting_calibrated_data_j0603_174	= test_53_splitting_calibrated_data_j0603_174
# test_53_splitting_calibrated_data_g192	= test_54_splitting_calibrated_data_g192
# test_54_splitting_calibrated_data_3c84	= test_55_splitting_calibrated_data_3c84
# test_55_single_spectral_window_cleaning	= test_56_single_spectral_window_cleaning
# test_56_lower_frequency_baseband_cleaning	= test_57_lower_frequency_baseband_cleaning
# test_57_upper_frequency_baseband_cleaning	= test_58_upper_frequency_baseband_cleaning
# test_58_basebands_mfs_taylor_cleaning	= test_59_basebands_mfs_taylor_cleaning
# test_59_spectral_index_image_filtering	= test_60_spectral_index_image_filtering
# test_60_spectral_index_probable_errors_filtering	= test_61_spectral_index_probable_errors_filtering
# test_61_intensity_weighted_mean_spectral_analysis	= test_62_intensity_weighted_mean_spectral_analysis