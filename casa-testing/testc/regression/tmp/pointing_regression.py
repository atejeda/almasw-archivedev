import os
import time
import regression_utility as regutl

REGNAME    = "pointing";
#MS         = "pointingSquintPointing.ms"
MS         = "pointingtest.ms";
MODELIMAGE = "pointingmodel50m.im";
EPJTABLE   = "epjones2.tab";
EPJCACHE   = "pointing.cf";
PASTEP     = 360.0;  # No. PA based conv. func. computation (takes longer)
INTEG      = '30.0s';# Test VB integration as well in the solver loop
THISHOME   = "./pointing_regression_data/"; # Local directory for scratch use
#
TOTALTIME  = '*+1:0:0';  # Select only first 1hr worth of data to solve (keep run time small)
EPS        = 1E-4;       # Logical "zero"

TEMPLATEEPJ='template2.epj'; # The template EP-Jones table to check the results against.
#TEMPLATEEPJ='template_twoaxis.epj';

REPOSNAME  = os.environ.get('CASAPATH').split()[0]+"/data/regression/"+REGNAME+'/';
#REPOSNAME  = 'DataRepos/';
REUSELOCALREPOS = False;
#
#--------------------------------------------------------------
#
MYMS      = THISHOME + MS;
MYIMAGE   = THISHOME + MODELIMAGE;
MYTEMPLATEEPJ = THISHOME + TEMPLATEEPJ;
def pointing_reg():
    if (REUSELOCALREPOS):
        os.system("rm -rf " + THISHOME+EPJTABLE);
    else:
        os.system("rm -rf "+THISHOME);
        os.mkdir(THISHOME);
        os.system("cp -r " + REPOSNAME+MS         + " " + MYMS);
        os.system("cp -r " + REPOSNAME+MODELIMAGE + " " + MYIMAGE);
        os.system("cp -r " + REPOSNAME+TEMPLATEEPJ + " " + MYTEMPLATEEPJ);

    cb.open(MYMS);
    
    cb.selectvis(time=TOTALTIME);
    cb.setsolve(type     = "EP",
                t         = INTEG,
                table     = THISHOME+EPJTABLE,
                preavg    = -1,
                phaseonly = false,
                append    = false,
                cfcache   = THISHOME + EPJCACHE,
                painc     = PASTEP);
    cb.setmodel(modelimage=MYIMAGE);
    cb.solve();
#
#--------------------------------------------------------------
#
try:
    startTime = time.time();
    startProc = time.clock();
    regstate = False;
#
#--------------------------------------------------------------
# Run the solver (and generate the subjective truth)
    pointing_reg();
#
#--------------------------------------------------------------
# The objective truth!
#
    tb.open(MYTEMPLATEEPJ);
    tmp_sol=tb.getcol('GAIN');
    tb.close();
    endTime = time.time();
    endProc = time.clock();
    #
    #--------------------------------------------------------------
    # The subjective truth!
    #
    tb.open(THISHOME+EPJTABLE);
    this_sol=tb.getcol('GAIN');
    tb.close();
    #
    #--------------------------------------------------------------
    # Get the statistics
    #
    nt=this_sol.shape[2];
#    dsol=tmp_sol[[0,1],0,0:nt]-this_sol[[0,1],0,0:nt];
    dsol=tmp_sol[[0,2],0,0:nt]-this_sol[[0,2],0,0:nt];
    dMax=dsol.max();
    dMin=dsol.min();
    dVar=dsol.var();
    dMean=dsol.mean();
    #
    import datetime
    datestring=datetime.datetime.isoformat(datetime.datetime.today())
    outfile=REGNAME+'-'+datestring+'.log'
    logfile=open(outfile,'w')

    print >>logfile, "Pointing solution statistics:";
    print >>logfile, "-------------------------------------------------";
    print >>logfile, "Res. Max = ",dMax, "  Res. Var = ",dVar, "  Res. Min = ",dMin, "  Res. Mean = ",dMean;
    print >>logfile, "";

    if ((abs(dMax) < EPS) &
        (abs(dVar) < EPS) &
        (abs(dMin) < EPS)):
        regstate=True;
        print >>logfile,REGNAME+" Regression passed.";
        print ''
        print 'Regression PASSED'
        print ''
    else:
        regstate=False;
        print >>logfile,REGNAME+" Regression failed.";
        print ''
        print 'Regression FAILED'
        print ''

    print >>logfile,''
    print >>logfile,''
    print >>logfile,'********* Benchmarking *****************'
    print >>logfile,'*                                      *'
    print >>logfile,'Total wall clock time was: ', endTime - startTime
    print >>logfile,'Total CPU        time was: ', endProc - startProc
        

    logfile.close();

except Exception, instance:
    print "###Error in pointing regression: ", instance;
