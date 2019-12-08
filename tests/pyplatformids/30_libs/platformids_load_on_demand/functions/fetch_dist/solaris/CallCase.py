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

import platformids
import platformids.dist.solaris


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase020(self):

        res = platformids.fetch_dist()

        if res == platformids.dist.solaris.RTE_SOLARIS:
            import platform

            # ('SunOS', 'solaris10', '5.10', 'Generic_147148-26', 'i86pc', 'i386')
            # ('SunOS', 'solaris11', '5.11', '11.3', 'i86pc', 'i386')
            self.assertEqual(platform.uname()[0], 'SunOS')
            self.assertTrue(platform.uname()[2].startswith('5'))
        else:
            self.skipTest("simple validation only")

if __name__ == '__main__':
    unittest.main()
