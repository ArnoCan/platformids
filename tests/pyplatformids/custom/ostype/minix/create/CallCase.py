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

#
# load and init ostype=minix + dist=minix3
#
from platformids.custom.minix import * 

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(rte2num['minix'], RTE_MINIX)        

    def testCase011(self):
        self.assertEqual(rte2num['minix3'], RTE_MINIX3)        

    def testCase012(self):
        self.assertEqual(rte2num['minix321'], RTE_MINIX321)        

    def testCase013(self):
        self.assertEqual(rte2num['minix330'], RTE_MINIX330)        

    def testCase020(self):
        self.assertEqual(num2rte[RTE_MINIX], 'minix')        

    def testCase021(self):
        self.assertEqual(num2rte[RTE_MINIX3], 'minix3')        

    def testCase022(self):
        self.assertEqual(num2rte[RTE_MINIX321], 'minix321')        

    def testCase023(self):
        self.assertEqual(num2rte[RTE_MINIX330], 'minix330')        

    def testCase030(self):
        self.assertEqual(num2pretty[RTE_MINIX], 'Minix')        

    def testCase031(self):
        self.assertEqual(num2pretty[RTE_MINIX3], 'Minix3')        

    def testCase032(self):
        self.assertEqual(num2pretty[RTE_MINIX321], 'Minix-3.2.1')        

    def testCase033(self):
        self.assertEqual(num2pretty[RTE_MINIX330], 'Minix-3.3.0')        

    def testCase040(self):
        self.assertEqual(custom_rte_distrel2tuple[RTE_MINIX3], my_distrel2tuple)        

    def testCase050(self): 
        self.assertEqual(RTE_MINIX, rte2num[RTE_MINIX])        

    def testCase051(self): 
        self.assertEqual(RTE_MINIX3, rte2num[RTE_MINIX3])        

    def testCase052(self): 
        self.assertEqual(RTE_MINIX321, rte2num[RTE_MINIX321])        

    def testCase053(self): 
        self.assertEqual(RTE_MINIX330, rte2num[RTE_MINIX330])        


if __name__ == '__main__':
    unittest.main()
