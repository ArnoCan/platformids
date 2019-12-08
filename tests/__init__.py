"""PyUnit tests

These tests could either be called from the command line,
or within Eclipse by the plugin PyDev / PyUnit.

* CLI: '*python setup.py test*' 

* Eclipse: Install PyDev, open the view PyUnit and proceed.


**REMARK**: For additional unit tests refer to subdirectory 'UseCases' 


30_libs
-------
Provided library modules of 'epyunit'.

"""
from __future__ import print_function


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.0'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__package__ = 'filesysobjects_pyunit'


import platform
print()
print()
print("#*******************************#")
print("#  Python implementation data   #")
print("#*******************************#")
print()
print()
print("python_implementation  = " + str(platform.python_implementation()))
print("python_version         = " + str(platform.python_version()))

try:
    print("python_build           = " + str(platform.python_build()))
except:
    pass

try:
    print("linux_distribution     = " + str(platform.linux_distribution()))
except:
    pass

try:
    print("python_compiler        = " + str(platform.python_compiler()))
except:
    pass

try:
    print("libc_ver               = " + str(platform.libc_ver()))
except:
    pass


