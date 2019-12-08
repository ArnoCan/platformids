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

from platformids import get_modlocation


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase020(self):
        for m in ('armbian', 'circuitpython', 'micropython', 'raspbian',
                  ):
            res = get_modlocation(m, permitrel=True)
            self.assertEqual(res[0], 'embed.' + m)

    def testCase030(self):
        for m in ('armbian', 'circuitpython', 'micropython', 'raspbian',
                  ):
            res = get_modlocation(m, permitrel=False)
            self.assertEqual(res[0], 'platformids.embed.' + m)

if __name__ == '__main__':
    unittest.main()



