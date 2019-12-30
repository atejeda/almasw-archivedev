# CASA testing framework

The main purpose of this approach is provide a standar way and sort of framework to test CASA regression and guides tests by using python xunit framework implementation, nose + plugins and jenkins + plugins.

## Scope

Python, that's it (to be done).

## Architecture, design and implementation

### Architecture

<div align="center">
    <img src="http://s18.postimg.org/kezwcw4l5/architecture.png" />
</div>

### Design

The core of the design relies on the ```RegressionBase``` which is extended from ```unittest.TestCase``` python class, each regression test class inherits helper methods of the ```RegressionBase``` and at the same time provides the capabilities and methods from the ```unittest.TestCase```class for create testing fixtures and tests suites, executable by python testing or nose utilities.

```
a class diagram w/ an example.
```

```RegressionBase``` also use static defined methods from ```RegressionHelper``` to manage data, get environment variables and find data.


```RegressionRunner``` is used to execute the test class by using nose utils, this class locate and create the test suite from the test class methods.


```
action diagram example.
```

### Implementation

The ```testc``` is the main package where all the testing framework lives, 

   * testc
      * guide: extract and merge/generate modules and test classes for casa-guides testing
      * nose
         * plugin: in-house and thirdparty nose plugins
      * regression: regression tests modules, classes and helper classes
      * unit: unit test and unit test classes implementations

## How to use

A static helper method defined in ```RegressionRunner``` is provided to execute the regression test class, which is located at ```testc/regression```:

```
from testc.regression.helper import RegressionRunner
RegressionRunner.execute("regression_3c129_tutorial")
```

The ```RegressionRunner.execute``` method allows to specifiy custom nose arguments. The ```guide``` argument should be specified for a casa-guide regression test.

```
def execute(test, nose_argv = None, guide = False):
	"""Execute the regression test by using nose with the nose arguments
	and with -d -s -v and --with-xunit (xml generation)
	"""
```

For automation, a ```casa_regression.py``` module is provided to enable, disable

### Writing your own classes

Few things are needed:

   * The class, there's a pre-stablished name convention, all regression classes should be prefixed with ```regresion_<id-of-the-test>```
      * import the needed helper classes
      * in your tests class, add ```__all__ = ["<name-of-your-class>"]``` for your class be visible for the testing framework (if you want)
      * define your methods, ```test_<name-of-the-method>``` is a must for python xunit
   * The script to be executed by/within CASA, using the prefix ```casapy_<id-of-the-test-case>```, which contains only the code to be executed within CASA

The inherited method ```execute``` is a helper to execute or import the ```casapy_``` module within CASA, is defined by:

```
def execute(self, casapy_script, test_assert = False, import_module = False)
```

   * casapy_script: the ```casapy_``` module to use.
   * test_assert: a future feature to assert outputs of a regression tests.
   * import_module: if True, it will import the module rather than execute it (```execfile```), useful for dummy non casa tests.

Within the testing context, it is possible to define:

   * Several test classes within a module (```regresion_<id-of-the-test>```)
   * Several method / test cases per tests classes
   * Several ```casapy_<id-of-the-test-case>``` executing per method.

Things sare much simpler by using an already implemented class as an example, see the [regression_3c129_tutorial.py](https://github.com/atejeda/casa-testing/blob/master/testc/regression/regression_3c129_tutorial.py).

A few helper methods are implemented in the ```RegressionHelper``` class to deal with the setup, specially the data:

```
@staticmethod
def data_copy(array_path):
	"""Given an array of paths, it will iterate and copy all to the
	current working directory, which is where casapy is executed
	"""
```	

```
@staticmethod
def data_remove(array_path):
	"""Given an array of paths, it will iterate and delete them
	"""
```

```
@staticmethod
def assert_file(file):
	"""Assert that the file exists
	"""
```

Bear in mind that the working space is the current working directory.

The Python xunit implementation provides several methods to deal with the test setup per class and per method, refer to the ```Python xunit hints``` section.

### Python xunit hints

Ignoring, works in a method nor class level, just append the decorator, e.g.:

```
@unittest.skip("reason")
test_<name-of-the-method>(self): ...
```

Class level helpers, ```setUpClass```  and ```tearDownClass```, are executed just before and after a test class is executed, the ```@classmethod
``` decorator is mandatory.

```
@classmethod
def setUpClass(cls): ...
```

```
@classmethod
def tearDownClass(cls): ....
````

In both methods, the ```cls``` argument is an instance of your testing class object.

The first line of the pydoc added to the ```test_<name-of-the-method>``` will be printed instead of the test name when it is executed.

## Jenkins Integration

## About CASA

See [http://casa.nrao.edu/](casa.nrao.edu) for more info and licenses.