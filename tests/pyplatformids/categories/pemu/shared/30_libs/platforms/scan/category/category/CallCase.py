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

from platformids import RTE, RTE_POSIX, RTE_DIST, RTE_PWEMU, RTE_CATEGORY, rte2num

from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        if RTE & RTE_CATEGORY != RTE_POSIX:
            self.skipTest("not this platform")

        res = PlatformParameters()
        res.scan()
        
        if RTE & RTE_CATEGORY == RTE_PWEMU:
            # POSIX and Windows emulator - Cygwin
            resx = {
                "category": RTE_PWEMU,
            }
        else:
            # native posix
            resx = {
                "category": RTE_POSIX,
            }

        self.assertEqual(res, resx)
    
    def testCase020(self):
        if RTE & RTE_CATEGORY != RTE_POSIX:
            self.skipTest("not this platform")

        res = PlatformParameters()
        res.scan()
        self.assertTrue(rte2num[res.category] & RTE_CATEGORY == RTE_POSIX)

if __name__ == '__main__':
    unittest.main()
