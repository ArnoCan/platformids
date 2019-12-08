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

    def testCase020(self):

        res = platformids.fetch_dist()

        if res == platformids.RTE_CENTOS:
            import platform
            # ('CYGWIN_NT-10.0', 'w10p', '2.11.2(0.329/5/3)', '2018-11-08 14:34', 'x86_64', '')
            self.assertTrue(platform.dist()[0].startswith('CYGWIN_NT'))
        else:
            self.skipTest("simple validation only")

if __name__ == '__main__':
    unittest.main()
