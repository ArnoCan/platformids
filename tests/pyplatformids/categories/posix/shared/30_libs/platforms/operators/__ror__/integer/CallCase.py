from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


try:
    from rdbg.start import start_remote_debug    # load a slim bootstrap module
    start_remote_debug()                         # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass

import unittest

import platformids
from platformids import RTE, RTE_POSIX
from platformids.platforms import PlatformParameters

class CallUnits(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None

    def testCase010(self):
        if RTE & RTE_POSIX != RTE_POSIX:
            self.skipTest("not this platform")

        p = PlatformParameters()
        p.scan()
        p = RTE_POSIX | p
        
        self.assertTrue(p == RTE)


if __name__ == '__main__':
    unittest.main()
