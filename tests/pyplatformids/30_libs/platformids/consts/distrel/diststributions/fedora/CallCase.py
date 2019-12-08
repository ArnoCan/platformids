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

import platformids.dist.fedora

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        self.assertEqual(platformids.dist.fedora.RTE_FEDORA27, platformids.RTE_FEDORA + 0x00006c00)

    def testCase020(self):
        self.assertEqual(platformids.dist.fedora.RTE_FEDORA28, platformids.RTE_FEDORA + 0x00007000)

    def testCase030(self):
        self.assertEqual(platformids.dist.fedora.RTE_FEDORA29, platformids.RTE_FEDORA + 0x00007400)


if __name__ == '__main__':
    unittest.main()
