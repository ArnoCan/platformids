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
from platformids import RTE_CATEGORY_B, RTE_CATEGORY


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None
        platformids.num2rte.strict_check = True
        platformids.rte2num.strict_check = True

    def testCase010(self):
        self.assertEqual(platformids.RTE_POSIX, 0x10000000)

    def testCase020(self):
        self.assertEqual(platformids.RTE_WIN32, 0x20000000)

    def testCase030(self):
        self.assertEqual(platformids.RTE_WIN, 0x20000000)

    def testCase040(self):
        self.assertEqual(platformids.RTE_WINDOWS, 0x20000000)

    def testCase050(self):
        self.assertEqual(platformids.RTE_EMBEDDED, 0x80000000)


if __name__ == '__main__':
    unittest.main()
