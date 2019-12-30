# In CASA: splitting fields for analysis
split('TVER0004.sb14459364.eb14492359.56295.26287841435.ms', outputvis='G192_6s.ms', \
      datacolumn='all', field='3,6,7,10', keepflags=False, spw='2~65')
# In CASA: listobs on the initial data set
listobs('G192_6s.ms', listfile='G192_listobs.txt')
# In CASA
os.system("cat G192_listobs.txt")
# In CASA
flagcmd(vis='G192_6s.ms', inpmode='table', action='list', \
        useapplied=True)
# In CASA
myrows = range(2868)
flagcmd(vis='G192_6s.ms', inpmode='table', action='plot', \
        useapplied=True, tablerows=myrows)
# In CASA: flag table plot
myrows = range(2868)
flagcmd(vis='G192_6s.ms', inpmode='table', action='plot', tablerows=myrows, 
        useapplied=True, plotfile='PlotG192_flagcmd_4.1.png')
# In CASA
plotants('G192_6s.ms')
print r'''Command: plotants('G192_6s.ms')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
clearstat
# In CASA
plotms(vis='G192_6s.ms', field='', spw='*:31~31', \
       antenna='ea02&ea05', xaxis='time', yaxis='amp', \
       correlation='rr', coloraxis='field')
print r'''Command: plotms(vis='G192_6s.ms', field='', spw='*:31~31', \\n       antenna='ea02&ea05', xaxis='time', yaxis='amp', \\n       correlation='rr', coloraxis='field')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_6s.ms', field='3', spw='*:31~31', \
       antenna='', xaxis='baseline',\
       yaxis='amp', coloraxis='antenna1')
print r'''Command: plotms(vis='G192_6s.ms', field='3', spw='*:31~31', \\n       antenna='', xaxis='baseline',\\n       yaxis='amp', coloraxis='antenna1')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_6s.ms', field='3', \
       antenna='ea05;!ea01;!ea10;!ea19', \
       xaxis='frequency', yaxis='amp', 
       coloraxis='corr', iteraxis='antenna')
print r'''Command: plotms(vis='G192_6s.ms', field='3', \\n       antenna='ea05;!ea01;!ea10;!ea19', \\n       xaxis='frequency', yaxis='amp', \n       coloraxis='corr', iteraxis='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_6s.ms', field='3', \
       antenna='ea05;!ea01;!ea10;!ea13;!ea19', \
       xaxis='frequency', yaxis='phase', \
       coloraxis='spw', iteraxis='antenna')
print r'''Command: plotms(vis='G192_6s.ms', field='3', \\n       antenna='ea05;!ea01;!ea10;!ea13;!ea19', \\n       xaxis='frequency', yaxis='phase', \\n       coloraxis='spw', iteraxis='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: bandpass calibrator analysis flagging
flaglist = ['antenna="ea01,ea10,ea19,ea13"',
            'antenna="ea24" spw="40,47~48"',
            'antenna="ea18" spw="16~31"']
flagcmd(vis='G192_6s.ms', inpmode='list', inpfile=flaglist, \
        action='apply', flagbackup=True)
# In CASA
plotms(vis='G192_6s.ms', field='3', antenna='ea05', \
       xaxis='frequency', yaxis='amp')
print r'''Command: plotms(vis='G192_6s.ms', field='3', antenna='ea05', \\n       xaxis='frequency', yaxis='amp')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_6s.ms', field='1', antenna='ea05', coloraxis = 'spw',\
       correlation = 'RR,LL', xaxis='frequency', yaxis='amp', scan='10,20,30,40,50,60')
print r'''Command: plotms(vis='G192_6s.ms', field='1', antenna='ea05', coloraxis = 'spw',\\n       correlation = 'RR,LL', xaxis='frequency', yaxis='amp', scan='10,20,30,40,50,60')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: RFI phase calibrator flagging
flaglist = ['spw="33:124,37:91,38:66~67;75~77,46:126,48:0"', \
            'spw="53:68~69,63:80,10:26,15:127,27:62,27:64"']
flagcmd(vis='G192_6s.ms', inpmode='list', inpfile=flaglist, \
        action='apply', flagbackup=True)
# In CASA: splitting good and bad data
# Remove any existing split data, otherwise split will not happen
os.system('rm -rf G192_flagged_6s.ms')
split(vis='G192_6s.ms', outputvis='G192_flagged_6s.ms', \
      datacolumn='data', keepflags=False)
# In CASA
os.system('du -sh G192_flagged_6s.ms')
# In CASA
plotms(vis='G192_flagged_6s.ms', xaxis='time', yaxis='antenna2', \
       symbolshape = 'circle', plotrange=[-1,-1,0,26], coloraxis='field')
print r'''Command: plotms(vis='G192_flagged_6s.ms', xaxis='time', yaxis='antenna2', \\n       symbolshape = 'circle', plotrange=[-1,-1,0,26], coloraxis='field')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: split and flagged listobs
listobs('G192_flagged_6s.ms', listfile='G192_flagged_listobs.txt')
# In CASA
setjy(vis='G192_flagged_6s.ms', listmodels=True)
# In CASA: model for the flux calibrator
setjy(vis='G192_flagged_6s.ms', field='0', scalebychan=True, \
      model='3C147_A.im')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='0', antenna='ea02&ea05', \
       xaxis='freq', yaxis='amp', ydatacolumn='model')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='0', antenna='ea02&ea05', \\n       xaxis='freq', yaxis='amp', ydatacolumn='model')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: determining antenna position corrections
gencal('G192_flagged_6s.ms', caltable='calG192.antpos', \
       caltype='antpos', antenna='')
# In CASA: generating gaincurve calibration
gencal('G192_flagged_6s.ms', caltable='calG192.gaincurve', \
       caltype='gc')
# In CASA
myTau = plotweather(vis='G192_flagged_6s.ms', doPlot=T)
# In CASA: generate atmospheric opacity calibration
myTau = plotweather(vis='G192_flagged_6s.ms', doPlot=F)
SPWs = []
for window in range(0,64):
    SPWs.append(str(window))
#
spwString = ','.join(SPWs)
gencal(vis='G192_flagged_6s.ms', caltable='calG192.opacity',
       caltype='opac', spw=spwString, parameter=myTau)
# In CASA: generate requantizer gains corrections
gencal('G192_flagged_6s.ms', caltable='calG192.requantizer', \
       caltype='rq')
# In CASA: phase only calibration
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0', \
        field='3', spw='*:60~68', \
        gaintable=['calG192.antpos','calG192.gaincurve', \
                   'calG192.requantizer','calG192.opacity'], \
        gaintype='G', refant='ea05', calmode='p', \
        solint='int', minsnr=3)
# In CASA
plotcal(caltable='calG192.G0', xaxis='time', yaxis='phase', \
        iteration='antenna', plotrange=[-1,-1,-180,180])
print r'''Command: plotcal(caltable='calG192.G0', xaxis='time', yaxis='phase', \\n        iteration='antenna', plotrange=[-1,-1,-180,180])'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotcal(caltable='calG192.G0', xaxis='time', yaxis='phase', \
        antenna='0~10,12~15', subplot=531, iteration='antenna', \
        plotrange=[-1,-1,-180,180], fontsize=8.0, \
        markersize=3.0, figfile='plotG192_plotcal_G0p1.png')
print r'''Command: plotcal(caltable='calG192.G0', xaxis='time', yaxis='phase', \\n        antenna='0~10,12~15', subplot=531, iteration='antenna', \\n        plotrange=[-1,-1,-180,180], fontsize=8.0, \\n        markersize=3.0, figfile='plotG192_plotcal_G0p1.png')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
plotcal(caltable='calG192.G0', xaxis='time', yaxis='phase', \
        antenna='16~26', subplot=531, iteration='antenna', \
        plotrange=[-1,-1,-180,180], fontsize=8.0, \
        markersize=3.0, figfile='plotG192_plotcal_G0p2.png')
print r'''Command: plotcal(caltable='calG192.G0', xaxis='time', yaxis='phase', \\n        antenna='16~26', subplot=531, iteration='antenna', \\n        plotrange=[-1,-1,-180,180], fontsize=8.0, \\n        markersize=3.0, figfile='plotG192_plotcal_G0p2.png')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: residual delays
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.G0'], \
        field='3', spw='*:5~122', gaintype='K', \
        refant='ea05', solint='inf', minsnr=3)
# In CASA
plotcal(caltable='calG192.K0', xaxis='antenna', yaxis='delay')
print r'''Command: plotcal(caltable='calG192.K0', xaxis='antenna', yaxis='delay')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: antenna bandpasses
bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0', \
         gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                    'calG192.opacity', 'calG192.G0', 'calG192.K0'], \
         field='3', refant='ea05', solnorm=False, \
         bandtype='B', solint='inf')
# In CASA
plotcal(caltable='calG192.B0', xaxis='freq', yaxis='amp', \
        spw='0~31', iteration='antenna')
print r'''Command: plotcal(caltable='calG192.B0', xaxis='freq', yaxis='amp', \\n        spw='0~31', iteration='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.B0', xaxis='freq', yaxis='amp', \
        spw='32~63', iteration='antenna')
print r'''Command: plotcal(caltable='calG192.B0', xaxis='freq', yaxis='amp', \\n        spw='32~63', iteration='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.B0', xaxis='freq', yaxis='phase', \
        iteration='antenna', spw='0~31', \
        plotrange=[-1,-1,-180,180])
print r'''Command: plotcal(caltable='calG192.B0', xaxis='freq', yaxis='phase', \\n        iteration='antenna', spw='0~31', \\n        plotrange=[-1,-1,-180,180])'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.B0', xaxis='freq', yaxis='phase', \
        iteration='antenna', spw='32~63', \
        plotrange=[-1,-1,-180,180])
print r'''Command: plotcal(caltable='calG192.B0', xaxis='freq', yaxis='phase', \\n        iteration='antenna', spw='32~63', \\n        plotrange=[-1,-1,-180,180])'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: flux and bandpass calibrators gain
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1', field='0,3', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0', \
                   'calG192.B0'], \
        gaintype='G', refant='ea05', calmode='ap', solint='30s', minsnr=3)
# In CASA
plotcal(caltable='calG192.G1', xaxis='time', yaxis='amp', \
        field='0', iteration='antenna')
print r'''Command: plotcal(caltable='calG192.G1', xaxis='time', yaxis='amp', \\n        field='0', iteration='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.G1', xaxis='time', yaxis='amp', \
        field='3', iteration='antenna')
print r'''Command: plotcal(caltable='calG192.G1', xaxis='time', yaxis='amp', \\n        field='3', iteration='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.G1', xaxis='time', yaxis='phase', \
        iteration='antenna', plotrange=[-1,-1,-180,180], \
        field='0')
print r'''Command: plotcal(caltable='calG192.G1', xaxis='time', yaxis='phase', \\n        iteration='antenna', plotrange=[-1,-1,-180,180], \\n        field='0')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.G1', xaxis='time', yaxis='phase', \
        iteration='antenna', plotrange=[-1,-1,-180,180], \
        field='3')
print r'''Command: plotcal(caltable='calG192.G1', xaxis='time', yaxis='phase', \\n        iteration='antenna', plotrange=[-1,-1,-180,180], \\n        field='3')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: bandpass calibrator gain amplitudes scaling
flux1 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G1', \
                  fluxtable='calG192.F1', reference='0', \
                  transfer='3', listfile='3C84.fluxinfo', fitorder=1)
# In CASA
freq = flux1['freq'] / 1e9
spw_list = range(0,64)
spw_str = []
for i in spw_list:
   thisspw = str(i)
   spw_str.append(thisspw)
 
bootstrapped_fluxes = []
for j in spw_str:
    thisflux = a[j]['fluxd'][0]
    bootstrapped_fluxes.append(thisflux)
 
pl.clf()
pl.plot(freq, bootstrapped_fluxes, 'bo')
pl.xlabel('Frequency (GHz)')
pl.ylabel('Flux Density (Jy)')
pl.title('3C84')
pl.show()
# In CASA: spectral information
setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
      reffreq='32.4488GHz')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='3', antenna='ea05&ea02', \
       xaxis='freq', yaxis='amp', ydatacolumn='model')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='3', antenna='ea05&ea02', \\n       xaxis='freq', yaxis='amp', ydatacolumn='model')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: phase only recalibration
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0.b', \
        field='3', spw='*:60~68', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', \
                   'calG192.requantizer', 'calG192.opacity'], \
        gaintype='G', refant='ea05', calmode='p', \
        solint='int', minsnr=3) 
# In CASA: residual delays recalibration
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0.b', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                  'calG192.opacity', 'calG192.G0.b'], \
        field='3', spw='*:5~122', gaintype='K', \
        refant='ea05', solint='inf', minsnr=3)
# In CASA: antenna bandpasses recalibration
bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0.b', \
         gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                    'calG192.opacity', 'calG192.G0.b', 'calG192.K0.b'], \
         field='3', refant='ea05', solnorm=False, \
         bandtype='B', solint='inf')
# In CASA
plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='amp', \
        spw='0~31', iteration='antenna')
print r'''Command: plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='amp', \\n        spw='0~31', iteration='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='amp', \
        spw='32~63', iteration='antenna')
print r'''Command: plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='amp', \\n        spw='32~63', iteration='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='phase', \
        iteration='antenna', spw='0~31', \
        plotrange=[-1,-1,-180,180])
print r'''Command: plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='phase', \\n        iteration='antenna', spw='0~31', \\n        plotrange=[-1,-1,-180,180])'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='phase', \
        iteration='antenna', spw='32~63', \
        plotrange=[-1,-1,-180,180])
print r'''Command: plotcal(caltable='calG192.B0.b', xaxis='freq', yaxis='phase', \\n        iteration='antenna', spw='32~63', \\n        plotrange=[-1,-1,-180,180])'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: compute gain phases using 3C147
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
        field='0', refant='ea05', solnorm=F, \
        solint='int', gaintype='G', calmode='p')
# In CASA: compute gain phases using J0603+174
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
        field='1', refant='ea05', solnorm=F, \
        solint='12s', gaintype='G', calmode='p', append=True)
# In CASA: compute gain phases using 3C84
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
        field='3', refant='ea05', solnorm=F, \
        solint='int', gaintype='G', calmode='p', append=True)
# In CASA
plotcal(caltable='calG192.G1.int', xaxis='time', yaxis='phase', \
        iteration='antenna', plotrange=[-1,-1,-180,180])
print r'''Command: plotcal(caltable='calG192.G1.int', xaxis='time', yaxis='phase', \\n        iteration='antenna', plotrange=[-1,-1,-180,180])'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: applying phase calibration
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.inf', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
        field='1', refant='ea05', solnorm=F, \
        solint='inf', gaintype='G', calmode='p')
# In CASA
plotcal(caltable='calG192.G1.inf', xaxis='time', yaxis='phase', \
        iteration='antenna', plotrange=[-1,-1,-180,180])
print r'''Command: plotcal(caltable='calG192.G1.inf', xaxis='time', yaxis='phase', \\n        iteration='antenna', plotrange=[-1,-1,-180,180])'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: 3C147 scan solving amplitudes
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
        gainfield=['', '', '', '', '3', '3', '0'], \
        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
        field='0', refant='ea05', solnorm=F, \
        solint='inf', gaintype='G', calmode='a')
 
# In CASA: J0603+174  scan solving amplitudes
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
        gainfield=['', '', '', '', '3', '3', '1'], \
        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
        field='1', refant='ea05', solnorm=F, \
        solint='inf', gaintype='G', calmode='a', append=True)
# In CASA: 3C84 scan solving amplitudes
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
        gainfield=['', '', '', '', '3', '3', '3'], \
        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
        field='3', refant='ea05', solnorm=F, \
        solint='inf', gaintype='G', calmode='a', append=True)
#
# In CASA
plotcal(caltable='calG192.G2', xaxis='time', yaxis='amp', \
        iteration='antenna')
print r'''Command: plotcal(caltable='calG192.G2', xaxis='time', yaxis='amp', \\n        iteration='antenna')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: using fluxscale to transfer the amplitude solutions
flux2 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
                  fluxtable='calG192.F2', reference='0')
# In CASA: 3C147 accumulated calibration
applycal(vis='G192_flagged_6s.ms', field='0', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
                    'calG192.G1.int', 'calG192.G2'], \
         gainfield=['', '', '', '', '', '', '0', '0'],
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)
# In CASA: gain accumulated calibration
applycal(vis='G192_flagged_6s.ms', field='1', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
                    'calG192.G1.int', 'calG192.F2'], \
         gainfield=['', '', '', '', '', '', '1', '1'],
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)
# In CASA: G192 accumulated calibration
applycal(vis='G192_flagged_6s.ms', field='2', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b',\
                    'calG192.G1.inf', 'calG192.F2'], \
         gainfield=['', '', '', '', '', '', '1', '1'],
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'linear'], calwt=False)
# In CASA: 3C84 accumulated calibration
applycal(vis='G192_flagged_6s.ms', field='3', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
                    'calG192.G1.int', 'calG192.F2'], \
         gainfield=['', '', '', '', '', '', '3', '3'],
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)
# In CASA
plotms(vis='G192_flagged_6s.ms', field='0', \
       xaxis='frequency', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='0', \\n       xaxis='frequency', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='0', \
       xaxis='time', yaxis='amp', \
       ydatacolumn='corrected', spw='29:5~122', \
       averagedata=True, avgchannel='16', \
       avgtime='', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='0', \\n       xaxis='time', yaxis='amp', \\n       ydatacolumn='corrected', spw='29:5~122', \\n       averagedata=True, avgchannel='16', \\n       avgtime='', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: flagging isolated RFI
flagdata(vis='G192_flagged_6s.ms', field='0', \
         spw='29', timerange='6:35:00~6:36:40')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='0', \
       xaxis='baseline', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='antenna1')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='0', \\n       xaxis='baseline', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='antenna1')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='1', \
       xaxis='frequency', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='32', \
       avgtime='6000s', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='1', \\n       xaxis='frequency', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='32', \\n       avgtime='6000s', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='1', \
       xaxis='baseline', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='32', \
       avgtime='6000s', coloraxis='antenna1')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='1', \\n       xaxis='baseline', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='32', \\n       avgtime='6000s', coloraxis='antenna1')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='3', \
       xaxis='frequency', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='3', \\n       xaxis='frequency', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: baseline flagging
flagdata(vis='G192_flagged_6s.ms', antenna='ea03&ea07')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='3', \
       xaxis='baseline', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='antenna1')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='3', \\n       xaxis='baseline', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='antenna1')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='3', \
       xaxis='phase', yaxis='amp', \
       xdatacolumn='corrected', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='3', \\n       xaxis='phase', yaxis='amp', \\n       xdatacolumn='corrected', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
# Clear the corrected data and model from header
clearcal('G192_flagged_6s.ms', addmodel=False)
 
# In CASA: 3C147 density model
setjy(vis='G192_flagged_6s.ms', field='0', scalebychan=True, \
      model='3C147_A.im')
 
# In CASA: 3C84 spectral information column
setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
      reffreq='32.4488GHz')
 
# In CASA: initial phase calibration
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0.b.2', field='3', spw='*:60~68',\
        gaintable=['calG192.antpos', 'calG192.gaincurve', \
                  'calG192.requantizer', 'calG192.opacity'], \
        gaintype='G', refant='ea05', calmode='p', solint='int', minsnr=3) 
 
# In CASA: delay calibration
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0.b.2', \
        field='3', spw='*:5~122', gaintype='K', \
        gaintable=['calG192.antpos', 'calG192.gaincurve', \
                  'calG192.requantizer', 'calG192.opacity','calG192.G0.b.2'], \
        refant='ea05', solint='inf', minsnr=3)
 
# In CASA: bandpass calibration
bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0.b.2', \
         field='3', refant='ea05', solnorm=False, \
        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer',\
                   'calG192.opacity','calG192.G0.b.2', 'calG192.K0.b.2'], \
         bandtype='B', solint='inf')
 
# In CASA: phase gain calibration field 0
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
        field='0', refant='ea05', solnorm=F, \
        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
        solint='int', gaintype='G', calmode='p')
 
# In CASA: phase gain calibration field 1
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
        field='1', refant='ea05', solnorm=F, \
        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
        solint='12s', gaintype='G', calmode='p', append=True)
 
# In CASA: phase gain calibration field 3
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
        field='3', refant='ea05', solnorm=F, \
        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
        solint='int', gaintype='G', calmode='p', append=True)
 
# In CASA: phase gain calibration infinite solution interval 
# (Note: we will apply this table to our science target at the applycal stage.)
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.inf.2', \
        field='1', refant='ea05', solnorm=F, \
        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
        solint='inf', gaintype='G', calmode='p')
 
# In CASA: amplitude calibration solutions field 0
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
        field='0', refant='ea05', solnorm=F, \
        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
                   'calG192.opacity', 'calG192.K0.b.2', \
                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
        gainfield=['', '', '', '', '3', '3', '0'], \
        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
        solint='inf', gaintype='G', calmode='a')
 
# In CASA: amplitude calibration solutions field 1
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
        field='1', refant='ea05', solnorm=F, \
        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
                   'calG192.opacity', 'calG192.K0.b.2', \
                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
        gainfield=['', '', '', '', '3', '3', '1'], \
        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
        solint='inf', gaintype='G', calmode='a', append=True)
 
# In CASA: amplitude calibration solutions field 3
gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
        field='3', refant='ea05', solnorm=F, \
        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
                   'calG192.opacity', 'calG192.K0.b.2', \
                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
        gainfield=['', '', '', '', '3', '3', '3'], \
        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
        solint='inf', gaintype='G', calmode='a', append=True)
 
# In CASA: flux calibration solutions
flux3 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
                  fluxtable='calG192.F2.2', reference='0')
 
# In CASA: apply calibration tables field 0
applycal(vis='G192_flagged_6s.ms', field='0', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.G2.2'], \
         gainfield=['', '', '', '', '', '', '0', '0'], \
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)
 
# In CASA: apply calibration tables field 1
applycal(vis='G192_flagged_6s.ms', field='1', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.F2.2'], \
         gainfield=['', '', '', '', '', '', '1', '1'], \
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)
 
# In CASA: apply calibration tables field 2
applycal(vis='G192_flagged_6s.ms', field='2', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.inf.2', 'calG192.F2.2'], \
         gainfield=['', '', '', '', '', '', '1', '1'], \
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'linear'], calwt=False)
 
# In CASA: apply calibration tables field 3
applycal(vis='G192_flagged_6s.ms', field='3', \
         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.F2.2'], \
         gainfield=['', '', '', '', '', '', '3', '3'], \
         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)
# In CASA
plotms(vis='G192_flagged_6s.ms', field='0', \
       xaxis='baseline', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='antenna1')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='0', \\n       xaxis='baseline', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='antenna1')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotms(vis='G192_flagged_6s.ms', field='1', \
       xaxis='baseline', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='32', \
       avgtime='6000s', coloraxis='antenna1')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='1', \\n       xaxis='baseline', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='32', \\n       avgtime='6000s', coloraxis='antenna1')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotms(vis='G192_flagged_6s.ms', field='3', \
       xaxis='baseline', yaxis='amp', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='antenna1')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='3', \\n       xaxis='baseline', yaxis='amp', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='antenna1')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
plotms(vis='G192_flagged_6s.ms', field='0', \
       xaxis='phase', yaxis='amp', \
       xdatacolumn='corrected', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='0', \\n       xaxis='phase', yaxis='amp', \\n       xdatacolumn='corrected', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotms(vis='G192_flagged_6s.ms', field='1', \
       xaxis='phase', yaxis='amp', \
       xdatacolumn='corrected', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='32', \
       avgtime='6000s', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='1', \\n       xaxis='phase', yaxis='amp', \\n       xdatacolumn='corrected', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='32', \\n       avgtime='6000s', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
#
plotms(vis='G192_flagged_6s.ms', field='3', \
       xaxis='phase', yaxis='amp', \
       xdatacolumn='corrected', \
       ydatacolumn='corrected', spw='*:5~122', \
       averagedata=True, avgchannel='8', \
       avgtime='1000s', coloraxis='baseline')
print r'''Command: plotms(vis='G192_flagged_6s.ms', field='3', \\n       xaxis='phase', yaxis='amp', \\n       xdatacolumn='corrected', \\n       ydatacolumn='corrected', spw='*:5~122', \\n       averagedata=True, avgchannel='8', \\n       avgtime='1000s', coloraxis='baseline')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: splitting calibrated data 3C147
os.system('rm -rf 3C147_split_6s.ms')
split(vis='G192_flagged_6s.ms', outputvis='3C147_split_6s.ms', \
      datacolumn='corrected', field='0')
# In CASA: splitting calibrated data J0603+174
os.system('rm -rf J0603_split_6s.ms')
split(vis='G192_flagged_6s.ms', outputvis='J0603_split_6s.ms', \
      datacolumn='corrected', field='1')
# In CASA: splitting calibrated data G192
os.system('rm -rf G192_split_6s.ms')
split(vis='G192_flagged_6s.ms', outputvis='G192_split_6s.ms', \
      datacolumn='corrected', field='2')
# In CASA: splitting calibrated data 3C84
os.system('rm -rf 3C84_split_6s.ms')
split(vis='G192_flagged_6s.ms', outputvis='3C84_split_6s.ms', \
      datacolumn='corrected', field='3')
# In CASA: single spectral window cleaning
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
      interactive=True)
# In CASA
viewer('imgG192_6s_spw48.image')
print r'''Command: viewer('imgG192_6s_spw48.image')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
mystat = imstat('imgG192_6s_spw48.residual')
print 'Residual standard deviation = '+str(mystat['sigma'][0]) + ' Jy'
# In CASA: lower frequency baseband cleaning
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
      interactive=True)
#
viewer('imgG192_6s_spw32-63.image')
print r'''Command: viewer('imgG192_6s_spw32-63.image')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
mystat = imstat('imgG192_6s_spw32-63.residual')
print 'Residual standard deviation = '+str(mystat['sigma'][0]) + ' Jy'
# In CASA
myfit = imfit('imgG192_6s_spw32-63.image', region='G192.crtf')
print 'Source flux = '+str(myfit['results']['component0']['flux']['value'][0])+'+/-'+str(myfit['results']['component0']['flux']['error'][0]) + ' Jy'
# In CASA: upper frequency baseband cleaning
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
      interactive=True)
#
viewer('imgG192_6s_spw0-31.image')
print r'''Command: viewer('imgG192_6s_spw0-31.image')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
mystat = imstat('imgG192_6s_spw0-31.residual')
print 'Residual standard deviation = '+str(mystat['sigma'][0]) + ' Jy'
myfit = imfit('imgG192_6s_spw0-31.image', region='G192.crtf')
print 'Source flux = '+str(myfit['results']['component0']['flux']['value'][0])+'+/-'+str(myfit['results']['component0']['flux']['error'][0]) + ' Jy'
# In CASA: basebands mfs taylor cleaning
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
      weighting='briggs', robust=0.5, interactive=True)
#
mystat = imstat('imgG192_6s_spw0-63_mfs2.residual.tt0') + ' Jy'
print 'Residual standard deviation = '+str(mystat['sigma'][0])
myfit = imfit('imgG192_6s_spw0-63_mfs2.image.tt0', region='G192.crtf') + ' Jy'
print 'Source flux = '+str(myfit['results']['component0']['flux']['value'][0])+'+/-'+str(myfit['results']['component0']['flux']['error'][0])
# In CASA
viewer('imgG192_6s_spw0-63_mfs2.image.tt0')
print r'''Command: viewer('imgG192_6s_spw0-63_mfs2.image.tt0')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA: spectral index image filtering
immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha', 
                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
       mode='evalexpr',
       expr='IM0[IM1>2.0E-4]',
       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.filtered')
# In CASA: spectral index probable errors filtering
immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha.error', 
                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
       mode='evalexpr',
       expr='IM0[IM1>2E-4]',
       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.error.filtered')
# In CASA
viewer('imgG192_6s_spw0-63_mfs2.image.alpha.filtered')
print r'''Command: viewer('imgG192_6s_spw0-63_mfs2.image.alpha.filtered')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
listobs('G192_split_6s.ms', listunfl=True)
# In CASA: intensity weighted mean spectral analysis
# Removing any file output from previous runs, so immath will proceed
os.system('rm -rf imgG192_6s_spw0-63_mfs2.image.tt1.filtered')
immath(imagename=['imgG192_6s_spw0-63_mfs2.image.tt1',
                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
       mode='evalexpr',
       expr='IM0[IM1>2E-4]',
       outfile='imgG192_6s_spw0-63_mfs2.image.tt1.filtered')
#
# Removing any file output from previous runs, so immath will proceed
os.system('rm -rf imgG192_6s_spw0-63_mfs2.image.tt0.filtered')
immath(imagename=['imgG192_6s_spw0-63_mfs2.image.tt0'],
       mode='evalexpr',
       expr='IM0[IM0>2E-4]',
       outfile='imgG192_6s_spw0-63_mfs2.image.tt0.filtered')
# In CASA
mystat = imstat('imgG192_6s_spw0-63_mfs2.image.tt1.filtered',
                region='G192.crtf')
avgtt0alpha = mystat['mean'][0]
#
mystat = imstat('imgG192_6s_spw0-63_mfs2.image.tt0.filtered',
                region='G192.crtf')
avgtt0 = mystat['mean'][0]
avgalpha = avgtt0alpha / avgtt0
print 'G192 intensity-weighted alpha = ' + str(avgalpha)
