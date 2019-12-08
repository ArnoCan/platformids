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

from platformids import RTE, RTE_POSIX, rte2num, RTE_LINUX, RTE_DIST

from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        if RTE != RTE_LINUX:
            self.skipTest("not this platform")

        pform = PlatformParameters()
        pform.scan()
        
        resx = {'category': 'posix', 'osrel_id': 'linux', 'ostype': 'linux'}
        res = pform.get_json()
        
        for k,v in resx.items():
            self.assertEqual(v, res[k])


if __name__ == '__main__':
    unittest.main()
