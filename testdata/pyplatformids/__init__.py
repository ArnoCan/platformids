"""
Common test data
================
Common data for 'UseCases' and 'tests'. Refer to the package by PYTHONPATH.
The global variable 'testdata.platformids.mypath' provides the pathname into 'testdata'.
"""

import os
mypath = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))

mysyspath = os.path.normpath(os.path.abspath(os.path.dirname(__file__) + os.sep + '..' + os.sep + '..'))

curcygdrive = 'cygdrive'