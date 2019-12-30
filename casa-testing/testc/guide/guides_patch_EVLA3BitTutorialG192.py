"""
This is NOT a generated module
all modified changes will be kept.
"""

import sys

# assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"
# assert globals().has_key("IPython"), "IPython environment is needed for this module (%s)" % __file__
# assert globals().has_key("casa"), "CASA environment is needed for this module (%s)" % __file__

import os

from testc.regression.helper import injectEnv

__test__ = False

@injectEnv
def test_17_spectral_information():
	""" "spectral information" patched to standard=manual
	"""
	casalog.origin("test_17_spectral_information")
	casalog.post("starting")

	setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
	      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
	      reffreq='32.4488GHz', \
	      standard="manual")

@injectEnv
def test_35_3c84_spectral_information_column():
	""" "3C84 spectral information column" patched to standard=manual
	"""
	casalog.origin("test_35_3c84_spectral_information_column")
	casalog.post("starting")

	setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
	      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
	      reffreq='32.4488GHz', \
	      standard="manual")

@injectEnv
def test_55_single_spectral_window_cleaning():
	""" "single spectral window cleaning" patched to iteractive=False
	"""
	casalog.origin("test_55_single_spectral_window_cleaning")
	casalog.post("starting")

	# Removing any previous cleaning information
	# This assumes you want to start this clean from scratch
	# If you want to continue this from a previous clean run,
	# the rm -rf system command should be be skipped
	os.system ('rm -rf imgG192_6s_spw48*')
	clean(vis='G192_split_6s.ms', spw='48:5~122', \
	      imagename='imgG192_6s_spw48', \
	      mode='mfs', nterms=1, niter=10000, \
	      imsize=[1280], cell=['0.015arcsec'], \
	      imagermode='csclean', cyclefactor=1.5, \
	      weighting='briggs', robust=0.5, \
	      interactive=False)

@injectEnv
def test_56_lower_frequency_baseband_cleaning():
	""" "lower frequency baseband cleaning" patched to iteractive=False
	"""
	casalog.origin("test_56_lower_frequency_baseband_cleaning")
	casalog.post("starting")

	# Removing any previous cleaning information
	# This assumes you want to start this clean from scratch
	# If you want to continue this from a previous clean run,
	# the rm -rf system command should be be skipped
	os.system ('rm -rf imgG192_6s_spw32-63*')
	clean(vis='G192_split_6s.ms', spw='32~63:5~122', \
	      imagename='imgG192_6s_spw32-63', \
	      mode='mfs', nterms=1, niter=10000, \
	      imsize=[1280], cell=['0.015arcsec'], \
	      imagermode='csclean', cyclefactor=1.5, \
	      weighting='briggs', robust=0.5, \
	      interactive=False)
	#
	viewer('imgG192_6s_spw32-63.image')
	print r'''Command: viewer('imgG192_6s_spw32-63.image')'''
	user_check=raw_input('When you are done with the window, close it and press enter to continue:')
	mystat = imstat('imgG192_6s_spw32-63.residual')
	print 'Residual standard deviation = '+str(mystat['sigma'][0]) + ' Jy'

@injectEnv
def test_57_upper_frequency_baseband_cleaning():
	""" "upper frequency baseband cleaning" patched to iteractive=False
	"""
	casalog.origin("test_57_upper_frequency_baseband_cleaning")
	casalog.post("starting")

	# Removing any previous cleaning information
	# This assumes you want to start this clean from scratch
	# If you want to continue this from a previous clean run,
	# the rm -rf system command should be be skipped
	os.system ('rm -rf imgG192_6s_spw0-31*')
	clean(vis='G192_split_6s.ms', spw='0~31:5~122', \
	      imagename='imgG192_6s_spw0-31', \
	      mode='mfs', nterms=1, niter=10000, \
	      imsize=[1280], cell=['0.015arcsec'], \
	      imagermode='csclean', cyclefactor=1.5, \
	      weighting='briggs', robust=0.5, \
	      interactive=False)
	#
	viewer('imgG192_6s_spw0-31.image')
	print r'''Command: viewer('imgG192_6s_spw0-31.image')'''
	user_check=raw_input('When you are done with the window, close it and press enter to continue:')
	mystat = imstat('imgG192_6s_spw0-31.residual')
	print 'Residual standard deviation = '+str(mystat['sigma'][0]) + ' Jy'
	myfit = imfit('imgG192_6s_spw0-31.image', region='G192.crtf')
	print 'Source flux = '+str(myfit['results']['component0']['flux']['value'][0])+'+/-'+str(myfit['results']['component0']['flux']['error'][0]) + ' Jy'

@injectEnv
def test_58_basebands_mfs_taylor_cleaning():
	""" "basebands mfs taylor cleaning" patched to iteractive=False
	"""
	casalog.origin("test_58_basebands_mfs_taylor_cleaning")
	casalog.post("starting")

	# Removing any previous cleaning information
	# This assumes you want to start this clean from scratch
	# If you want to continue this from a previous clean run,
	# the rm -rf system command should be be skipped
	os.system ('rm -rf imgG192_6s_spw0-63_mfs2*')
	clean(vis='G192_split_6s.ms', spw='0~63:5~122', \
	      imagename='imgG192_6s_spw0-63_mfs2', \
	      mode='mfs', nterms=2, niter=10000, gain=0.1, \
	      threshold='0.0mJy', psfmode='clark', imsize=[1280], \
	      cell=['0.015arcsec'], \
	      weighting='briggs', robust=0.5, interactive=False)
	#
	mystat = imstat('imgG192_6s_spw0-63_mfs2.residual.tt0') + ' Jy'
	print 'Residual standard deviation = '+str(mystat['sigma'][0])
	myfit = imfit('imgG192_6s_spw0-63_mfs2.image.tt0', region='G192.crtf') + ' Jy'
	print 'Source flux = '+str(myfit['results']['component0']['flux']['value'][0])+'+/-'+str(myfit['results']['component0']['flux']['error'][0])