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
import platformids.dist.solaris

from platformids import RTE, RTE_POSIX, RTE_DIST, RTE_CATEGORY, rte2num, \
    RTE_LINUX, RTE_FEDORA, \
    fetch_platform_distribution, fetch_platform_os, \
    fetch_platform_distribution_num, fetch_platform_os_num, decode_rte_distrel_to_num

from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase020(self):
        res = decode_rte_distrel_to_num(platformids.dist.solaris.RTE_SOLARIS112)
        resx = platformids.dist.solaris.RTE_SOLARIS112 & platformids.RTE_DISTREL
        self.assertEqual(res, resx)

    def testCase030(self):
        res = decode_rte_distrel_to_num(platformids.dist.solaris.RTE_SOLARIS112)
        resx = platformids.dist.solaris.RTE_SOLARIS + 0x00002c40
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
