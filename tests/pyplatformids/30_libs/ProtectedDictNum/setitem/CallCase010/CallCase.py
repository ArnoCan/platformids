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
from platformids import ProtectedDictEnum, PlatformIDsCustomError

class CallUnits(unittest.TestCase):

    def setUp(self):
        self.dn = ProtectedDictEnum(
            custom_min=1000,
            custom_max=1010,
        )

        self.maxDiff = None

    def testCase010(self):
        try:
            self.dn[1010] = True
        except PlatformIDsCustomError:
            pass

if __name__ == '__main__':
    unittest.main()
