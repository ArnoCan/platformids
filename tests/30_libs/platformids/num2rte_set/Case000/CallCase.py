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

    def testCase010(self):
        res = None
        try:
            platformids.num2rte[platformids.RTE_DEBIAN8] = platformids.RTE_FEDORA
        except platformids.PlatformIDsError as e:
            res = str(e)

        resx = """READONLY: Key is already present:
  key:     131400(RTE_DEBIAN8)
  old-val: debian8(131400(RTE_DEBIAN8))
  new-val: 131168(RTE_OPENBSD)"""
   
#         print("4TEST:<" + str(res) + ">")
#         print("4TEST:<" + str(resx) + ">")
        
        self.assertEqual(res, resx)
        
        pass
    
    def testCase020(self):
        res = None
        try:
            platformids.num2rte[platformids.RTE_DEBIAN8] = 123
        except platformids.PlatformIDsError as e:
            res = str(e)

        resx = """READONLY: Key is already present:
  key:     131400(RTE_DEBIAN8)
  old-val: debian8(131400(RTE_DEBIAN8))
  new-val: 123"""
   
#         print("4TEST:<" + str(res) + ">")
#         print("4TEST:<" + str(resx) + ">")
        
        self.assertEqual(res, resx)
        
        pass

    def testCase030(self):
        res = None
        try:
            platformids.num2rte[125] = 457
        except platformids.PlatformIDsError as e:
            res = str(e)

        resx = None
   
#         print("4TEST:<" + str(res) + ">")
#         print("4TEST:<" + str(resx) + ">")
        
        self.assertEqual(res, resx)

        self.assertEqual(platformids.num2rte[125], 457)

        pass

if __name__ == '__main__':
    unittest.main()
