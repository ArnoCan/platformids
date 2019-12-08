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

from platformids import RTE, RTE_POSIX, RTE_CATEGORY, RTE_OSTYPE, rte2num, \
    RTE_LINUX, RTE_FEDORA

from platformids import fetch_dist, fetch_dist_tuple, fetch_rte_hexversion
from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):

        res = PlatformParameters()
        res.scan()

        dist = fetch_dist()
        
        disttuple = fetch_dist_tuple()
        distrel = fetch_rte_hexversion()
        
        resx = PlatformParameters(
            category=RTE & RTE_CATEGORY,
            ostype=RTE & RTE_OSTYPE,
            dist=dist,
            distrel=distrel,
            )
        
        self.assertTrue(rte2num[res.category] == RTE_POSIX)
        self.assertTrue(rte2num[res.ostype] == RTE_LINUX)
        self.assertTrue(rte2num[res.dist] == RTE_FEDORA)

        self.assertEqual(resx, res)

if __name__ == '__main__':
    unittest.main()
