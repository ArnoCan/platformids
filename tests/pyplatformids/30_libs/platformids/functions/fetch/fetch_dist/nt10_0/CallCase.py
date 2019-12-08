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

import unittest


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase020(self):
        import platformids

        resOs = platformids.fetch_ostype()
        resDist = platformids.fetch_dist()

        if resOs == platformids.RTE_NT:
            import platformids.dist.windows

            # (system='Windows', node='w10p', release='10', version='10.0.17763', machine='AMD64', processor='Intel64 Family 6 Model 60 Stepping 3, GenuineIntel')
            if resDist == platformids.dist.windows.RTE_NT100:
                import platform
                self.assertEqual(platform.dist()[0], 'Windows')
                self.assertTrue(platform.dist()[3].startswith('10.0'))
            else:
                self.skipTest("simple validation only")
        else:
            self.skipTest("simple validation only")

if __name__ == '__main__':
    unittest.main()
