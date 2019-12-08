# -*- coding: utf-8 -*-
"""The package 'platformids' provides canonical enumerations of bit encoded numeric platform IDs
for the Python implementations CPython, IPython, IronPython, Jython, and PyPy.
"""
# See manuals for the detailed API.

from __future__ import absolute_import

#import os
import sys
#import re
#import platform


from rdbg.start import start_remote_debug    # load a slim bootstrap module
start_remote_debug()                         # check whether '--rdbg' option is present, if so accomplish bootstrap

# from pythonids import PYV35Plus5p, ISSTR, PYVxyz, PYV33, PYV2
# from pythonids.pythondist import ISINT, PYDIST, PYE_DIST, PYE_JYTHON

import platformids
import platformids.platforms

for a in sys.argv:
    if a in ('--debug', '-d'):
        platformids._debug += 1
    if a in ('--verbose', '-v'):
        platformids._verbose += 1


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.31'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


pparams = platformids.platforms.PlatformParameters()
pparams.scan()

print(pparams)

