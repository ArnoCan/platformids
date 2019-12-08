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

from platformids import RTE, RTE_POSIX
from platformids.platforms import PlatformParameters

class CallUnits(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        if RTE & RTE_POSIX != RTE_POSIX:
            self.skipTest("not this platform")

        p = PlatformParameters()
        p.scan()

        resx = {
            'category': 'posix',
        }        
        o = PlatformParameters(**resx)

        p = p | o
        
        self.assertTrue(p == RTE)


if __name__ == '__main__':
    unittest.main()
