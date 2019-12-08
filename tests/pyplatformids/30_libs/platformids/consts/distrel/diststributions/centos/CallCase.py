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

import platformids.dist.centos

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(platformids.dist.centos.RTE_CENTOS7, platformids.RTE_CENTOS + 0x00001c00)

    def testCase020(self):
        self.assertEqual(platformids.dist.centos.RTE_CENTOS79, platformids.dist.centos.RTE_CENTOS7 + 0x00000120)


if __name__ == '__main__':
    unittest.main()
