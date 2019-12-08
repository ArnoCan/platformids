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

import platformids
from platformids import ProtectedDictEnum, PlatformIDsEnumerationError

class CallUnits(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
#        super(CallUnits, cls).setUpClass()(self)

        cls.dn = ProtectedDictEnum(
            custom_min=1000,
            custom_max=1005,
        )

        cls.maxDiff = None

    def testCase011(self):
        res = self.dn.add_enum()
        resx = 1004 
        self.assertEqual(res, resx)

    def testCase012(self):
        res = self.dn.add_enum()
        resx = 1003 
        self.assertEqual(res, resx)

    def testCase013(self):
        res = self.dn.add_enum()
        resx = 1002 
        self.assertEqual(res, resx)

    def testCase014(self):
        res = self.dn.add_enum()
        resx = 1001 
        self.assertEqual(res, resx)

    def testCase015(self):
        res = self.dn.add_enum()
        resx = 1000 
        self.assertEqual(res, resx)

    def testCase020(self):
        self.assertRaises(PlatformIDsEnumerationError, self.dn.add_enum)

    def testCase030(self):
        self.assertTrue(self.dn.delete_enum(1003))

    def testCase031(self):
        self.assertTrue(self.dn.delete_enum(1001))

    def testCase032(self):
        self.assertTrue(self.dn.delete_enum(1004))

    def testCase033(self):
        self.assertTrue(self.dn.delete_enum(1000))  # min is purged automatic by delete_enum

    def testCase034(self):
        self.assertTrue(self.dn.delete_enum(1002))

    def testCase036(self):
        self.assertTrue(self.dn.purge() == 4)

    def testCase037(self):
        self.assertTrue(self.dn.purge() == 0)

    def testCase041(self):
        res = self.dn.add_enum()
        resx = 1004 
        self.assertEqual(res, resx)

    def testCase042(self):
        res = self.dn.add_enum()
        resx = 1003 
        self.assertEqual(res, resx)

    def testCase043(self):
        res = self.dn.add_enum()
        resx = 1002 
        self.assertEqual(res, resx)

    def testCase044(self):
        res = self.dn.add_enum()
        resx = 1001 
        self.assertEqual(res, resx)

    def testCase045(self):
        res = self.dn.add_enum()
        resx = 1000 
        self.assertEqual(res, resx)

    def testCase050(self):
        self.assertRaises(PlatformIDsEnumerationError, self.dn.add_enum)

if __name__ == '__main__':
    unittest.main()
