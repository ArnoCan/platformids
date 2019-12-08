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

        res = platformids.fetch_dist()


        if res == platformids.RTE_FEDORA:
            import platform
            try:
                # removed 3.x
                self.assertEqual(platform.dist()[0], 'fedora')
            except:
                try:
                    # removed 3.5
                    self.assertEqual(platform.linux_distribution()[0], 'fedora')
                except:
                    # for now...
                    import re
                    _X = re.search(r'[.]fc[0-9]+[.]', platform.uname()[2])
                    self.assertFalse(not _X)

        else:
            self.skipTest("simple validation only")


if __name__ == '__main__':
    unittest.main()
