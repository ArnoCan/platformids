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

import platformids.dist.windows

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(platformids.dist.windows.RTE_WINNT35, platformids.dist.windows.RTE_NT35 + 807)

    def testCase020(self):
        self.assertEqual(platformids.dist.windows.RTE_WINNT40, platformids.dist.windows.RTE_NT40 + 1381)

    def testCase030(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2000, platformids.dist.windows.RTE_NT50 + 2195)

    def testCase040(self):
        self.assertEqual(platformids.dist.windows.RTE_WINXP64, platformids.dist.windows.RTE_NT52 + 3790)

    def testCase050(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2003, platformids.dist.windows.RTE_NT52 + 3790)

    def testCase060(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2003R2, platformids.dist.windows.RTE_NT52 + 3790)

    def testCase070(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2008, platformids.dist.windows.RTE_NT60 + 6001)

    def testCase080(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2008SP2, platformids.dist.windows.RTE_NT60 + 6002)

    def testCase090(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN7, platformids.dist.windows.RTE_NT61 + 7600)

    def testCase100(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2008R2, platformids.dist.windows.RTE_NT61 + 7600)

    def testCase110(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN7SP1, platformids.dist.windows.RTE_NT61 + 7601)

    def testCase120(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2008R2SP1, platformids.dist.windows.RTE_NT61 + 7601)

    def testCase130(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN8, platformids.dist.windows.RTE_NT62 + 9200)

    def testCase140(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2012, platformids.dist.windows.RTE_NT62 + 9200)

    def testCase150(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN81, platformids.dist.windows.RTE_NT63 + 9600)

    def testCase160(self):
        self.assertEqual(platformids.dist.windows.RTE_WIN2012R2, platformids.dist.windows.RTE_NT63 + 9600)


if __name__ == '__main__':
    unittest.main()
