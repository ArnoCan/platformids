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


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None
        platformids.num2rte.strict_check = True
        platformids.rte2num.strict_check = True

    def testCase030(self):
        self.assertEqual(platformids.RTE_LINUX, platformids.RTE_POSIX   + 0x00800000)

    def testCase040(self):
        self.assertEqual(platformids.RTE_BSD, platformids.RTE_POSIX   + 0x01000000)

    def testCase050(self):
        self.assertEqual(platformids.RTE_DARWIN, platformids.RTE_POSIX   + 0x02000000)

    def testCase060(self):
        self.assertEqual(platformids.RTE_UNIX, platformids.RTE_POSIX   + 0x04000000)
        

if __name__ == '__main__':
    unittest.main()
