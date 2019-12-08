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
    RTE_LINUX, RTE_FEDORA, \
    fetch_platform_distribution, fetch_platform_os, \
    fetch_platform_distribution_num, fetch_platform_os_num

from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase020(self):
        if RTE & RTE_DIST != RTE_FEDORA:
            self.skipTest("not this platform")

        res = PlatformParameters()
        res.scan()

        x0 = fetch_platform_distribution() # ('fedora27', '27', 'Fedora27', 'Fedora', (27, 0, 0), 'fedora')
        
        from platformids import fetch_category, fetch_ostype, fetch_dist, fetch_rte_hexversion

        x00 = fetch_category()
        x01 = fetch_ostype()
        x02 = fetch_dist()
        x03 = 0
        x04 = fetch_rte_hexversion()
        x05 = 0

        x0n = fetch_platform_distribution_num()

        x1 = fetch_platform_os()
#        x1n = fetch_platform_os_num()

        resx = PlatformParameters(
            category=RTE_POSIX,
            ostype=RTE_LINUX,
            dist=RTE_FEDORA,
            distrel_key=RTE_FEDORA,
            )
        
        self.assertTrue(rte2num[res.category] == RTE_POSIX)

if __name__ == '__main__':
    unittest.main()
