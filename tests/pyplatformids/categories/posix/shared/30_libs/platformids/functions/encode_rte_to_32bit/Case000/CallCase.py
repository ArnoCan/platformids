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
from platformids import RTE_POSIX, encode_rte_segments_to_32bit


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

        # seal present values
        platformids.num2rte.strict_check = True
        platformids.rte2num.strict_check = True

    def testCase011(self):
        self.assertEqual(platformids.encode_rte_to_32bit(category="posix"), RTE_POSIX)

    def testCase012(self):
        self.assertEqual(platformids.encode_rte_to_32bit(category=RTE_POSIX), RTE_POSIX)


if __name__ == '__main__':
    unittest.main()
