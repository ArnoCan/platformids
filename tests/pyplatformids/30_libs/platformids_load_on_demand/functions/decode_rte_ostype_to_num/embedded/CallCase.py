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


try:
    from rdbg.start import start_remote_debug    # load a slim bootstrap module @UnresolvedImport
    start_remote_debug()                         # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass


import unittest

import platformids
import platformids.dist.openbsd


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        res = platformids.decode_rte_ostype_to_num(
            platformids.RTE_EMBEDDED | platformids.RTE_MICROPYTHON
            )
        resx = platformids.RTE_EMBEDDED
        self.assertEqual(res, resx)

    def testCase020(self):
        res = platformids.decode_rte_ostype_to_num(platformids.RTE_MICROPYTHON)
        resx = platformids.RTE_EMBEDDED
        self.assertEqual(res, resx)

    def testCase030(self):
        res = platformids.decode_rte_ostype_to_num(platformids.RTE_CIRCUITPYTHON)
        resx = platformids.RTE_EMBEDDED
        self.assertEqual(res, resx)


if __name__ == '__main__':
    unittest.main()
