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

        if resOs == platformids.RTE_UNIX:

            # (('Linux', 'lap001', '4.17.14-102.fc27.x86_64', '#1 SMP Wed Aug 15 12:26:40 UTC 2018', 'x86_64', 'x86_64')
            import platform
            self.assertTrue(platform.dist()[0] not in ('Linux', 'BSD', 'SunOS', 'Darwin',))  #: weak...
        else:
            self.skipTest("simple validation only")

if __name__ == '__main__':
    unittest.main()
