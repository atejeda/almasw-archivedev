#!/usr/bin/env bash

if [ -z $WORKSPACE ]; then
	echo "This isn't a Jenkins workspace";
	exit 1;
fi

# setup libraries
$WORKSPACE/casa-testing/lib/python/site-packages/install
export PYTHONPATH=$WORKSPACE/casa-testing/lib/python/site-packages:$PYTHONPATH
export PYTHONPATH=$WORKSPACE/casa-testing/lib/python/site-packages/airspeed-0.4.2dev_20131111-py2.6.egg:$PYTHONPATH
export PYTHONPATH=$WORKSPACE/casa-testing/lib/python/site-packages/coverage-3.7.1-py2.6-linux-x86_64.egg:$PYTHONPATH
export PYTHONPATH=$WORKSPACE/casa-testing/lib/python/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg:$PYTHONPATH

# setup extraction and parsing
export CASA_TESTING=$WORKSPACE/casa-testing
export PYTHONPATH=$CASA_TESTING:$PYTHONPATH
export PATH=$CASA_TESTING/testc/guide:$PATH
export EXTRACTED=$CASA_TESTING/guides/extracted
export PARSED=$CASA_TESTING/testc/guide
export CONFIG=$CASA_TESTING/guides/guides.conf

# setup casa
export CASAROOT=$WORKSPACE/casapy-42.2.30986-1-64b
export CASAPATH=$CASAROOT
export LD_LIBARY_PATH=$CASAPATH/lib:$LD_LIBARY_PATH
export PATH=$CASAPATH/bin:$PATH

casaGuideExtract -c $CONFIG -o $EXTRACTED
casaGuideMerge -c $CONFIG -e $EXTRACTED -o $PARSED

# setup the testing framework
rm -rf $CASAPATH/lib/python/testc && ln -s $WORKSPACE/casa-testing/testc $CASAPATH/lib/python/

# exec the regression
rm -rf $WORKSPACE/test && mkdir -p $WORKSPACE/test
cp $WORKSPACE/casa-testing/regression.py $WORKSPACE/test/regression.py

cd $WORKSPACE/test

echo "copying G192_6s.ms"
cp -r ../G192_6s.ms .

casapy --nogui -c regression.py