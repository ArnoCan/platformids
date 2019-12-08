"""Initial raw tests by SubprocessUnit with hard-coded defaults.

Due to the basic character of the test these are done a little more than less.
 
"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


# try:
#     from rdbg.start import start_remote_debug    # load a slim bootstrap module
#     start_remote_debug()                         # check whether '--rdbg' option is present, if so accomplish bootstrap
# except:
#     pass


import unittest
import uuid

import platformids.dist.windows
from platformids import RTE, RTE_WINDOWS, RTE_DIST


class CallUnits(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.maxDiff = None
        platformids.num2rte.strict_check = True
        platformids.rte2num.strict_check = True
        self.u = str(uuid.uuid4())

    def testCase010(self):
        if (RTE & RTE_DIST) == RTE_WINDOWS:
            res = platformids.dist.windows.get_win32_IsWindowsXPSP1OrGreater()
            if res:
                self.assertGreaterEqual(RTE, platformids.dist.windows.RTE_NT51)
        else:
            self.skipTest("not applicable")
            
            
if __name__ == '__main__':
    unittest.main()
