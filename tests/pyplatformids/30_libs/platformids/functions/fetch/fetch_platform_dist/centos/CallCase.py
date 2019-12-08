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

class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase020(self):

        res = platformids.fetch_platform_distribution()

        if res == platformids.RTE_CENTOS:
            import platform
            self.assertEqual(platform.dist()[0], 'centos')
            # ('archlinux27', '27', 'ArchLinux27', 'ArchLinux', (27, 0, 0), 'archlinux')
            pd = platform.dist()
            resx = ('centos' + pd[1], pd[1], 'CentOS' + pd[1], 'CentOS', 
                    platformids.decode_version_str_to_segments(pd[1]), 'centos')
            self.assertEqual(res, resx)
            
        else:
            self.skipTest("simple validation only")

if __name__ == '__main__':
    unittest.main()
