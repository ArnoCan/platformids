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
from platformids import RTE_LINUX, RTE_POSIX, decode_rte_ostype_to_num
from platformids import RTE_CENTOS, RTE_FEDORA, RTE_RHEL, RTE_DEBIAN


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

        # seal present values
        platformids.num2rte.strict_check = True
        platformids.rte2num.strict_check = True

    def testCase011(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num("linux"), RTE_LINUX)

    def testCase012(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num(RTE_LINUX), RTE_LINUX)

    def testCase021(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num("centos"), RTE_LINUX)

    def testCase022(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num(RTE_CENTOS), RTE_LINUX)

    def testCase031(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num("fedora"), RTE_LINUX)

    def testCase032(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num(RTE_FEDORA), RTE_LINUX)

    def testCase041(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num("rhel"), RTE_LINUX)

    def testCase042(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num(RTE_RHEL), RTE_LINUX)

    def testCase051(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num("debian"), RTE_LINUX)

    def testCase052(self):
        self.assertEqual(platformids.decode_rte_ostype_to_num(RTE_DEBIAN), RTE_LINUX)


if __name__ == '__main__':
    unittest.main()
