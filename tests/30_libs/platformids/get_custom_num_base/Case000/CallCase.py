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
import sys
import io

import platformids


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase011(self):
        res = platformids.get_custom_num_base()
        resx = 262144  #                               100 0000 0000 0000 0000
        self.assertEqual(res, resx)

    def testCase012(self):
        res = platformids.get_custom_num_base()
        resx = 524288  #                              1000 0000 0000 0000 0001
        self.assertEqual(res, resx)

    def testCase013(self):
        res = platformids.get_custom_num_base()
        resx = 1048576  #                           1 0000 0000 0000 0000 0000
        self.assertEqual(res, resx)

if __name__ == '__main__':
    unittest.main()
