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

from platformids import RTE, RTE_POSIX, RTE_DIST, RTE_CATEGORY, rte2num, \
    RTE_LINUX,  \
    fetch_platform_distribution, fetch_platform_os

from platformids.platforms import PlatformParameters
from platformids.embed.armbian import RTE_ARMBIAN 

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase020(self):
        if RTE & RTE_DIST != RTE_ARMBIAN:
            self.skipTest("not this platform")

        res = PlatformParameters()
        res.scan()

        x0 = fetch_platform_distribution()
        x1 = fetch_platform_os()

        resx = PlatformParameters(
            category=RTE_POSIX,
            ostype=RTE_LINUX,
            dist=RTE_ARMBIAN,
            distrel_key=RTE_ARMBIAN,
            )
        
        self.assertTrue(rte2num[res.category] == RTE_POSIX)

if __name__ == '__main__':
    unittest.main()
