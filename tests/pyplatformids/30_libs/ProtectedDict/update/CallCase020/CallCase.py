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
from platformids import ProtectedDict, PlatformIDsPresentError

class CallUnits(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
#        super(CallUnits, cls).setUpClass()(self)

        cls.dn = ProtectedDict(
            (
                (1000, True),
                (1001, True),
                (1002, True),
                (1003, True),
                (1004, True),
                (1005, True),
            ),
            strict_check=True,
        )

        cls.maxDiff = None

    def testCase010(self):
        self.dn.update({1006: True, 1007: True, 1008: True, })

        resx = dict(
            (
                (1000, True),
                (1001, True),
                (1002, True),
                (1003, True),
                (1004, True),
                (1005, True),
                (1006, True),
                (1007, True),
                (1008, True),
            )
        )
        self.assertEqual(self.dn, resx)

    def testCase020(self):
        self.dn.update({1009: True, 1010: True,})

        resx = dict(
            (
                (1000, True),
                (1001, True),
                (1002, True),
                (1003, True),
                (1004, True),
                (1005, True),
                (1006, True),
                (1007, True),
                (1008, True),
                (1009, True),
                (1010, True),
            )
        )
        self.assertEqual(self.dn, resx)
        
 
    def testCase030(self):
        self.assertRaises(PlatformIDsPresentError, self.dn.update, {1009: True, 1010: True})

if __name__ == '__main__':
    unittest.main()
