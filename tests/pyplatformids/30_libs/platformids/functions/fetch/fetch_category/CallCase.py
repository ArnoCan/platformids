"""Initial raw tests by SubprocessUnit with hard-coded defaults.

Due to the basic character of the test these are done a little more than less.
 
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"

import unittest
import os

from platformids import RTE, RTE_POSIX, RTE_DIST, RTE_CATEGORY, rte2num, \
    RTE_WINDOWS, RTE_WIN, RTE_WIN32, \
    RTE_LINUX, RTE_FEDORA, \
    fetch_platform_distribution, fetch_platform_os, \
    fetch_platform_distribution_num, fetch_platform_os_num, \
    fetch_category, fetch_ostype, fetch_dist, fetch_rte_hexversion, \
    PlatformIDsError

from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase020(self):

        res = fetch_category()

        if os.name == 'java':
            osname = os._name
        else:
            osname = os.name
        
        if osname == 'posix':
            self.assertTrue(res == RTE_POSIX)
        elif osname == 'win32':
            self.assertTrue(res == RTE_WINDOWS)
            self.assertTrue(res == RTE_WIN)
            self.assertTrue(res == RTE_WIN32)
        else:
            self.skipTest("unknown category = " + str(res))

if __name__ == '__main__':
    unittest.main()
