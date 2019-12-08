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

from platformids import RTE, RTE_POSIX, rte2num
from platformids import RTE, RTE_POSIX, rte2num, RTE_DEBIAN

from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        if RTE & RTE_DEBIAN != RTE_DEBIAN:
            self.skipTest("not this platform")

        import platformids.dist.debian 
        if RTE & platformids.dist.debian.RTE_DEBIAN9 != platformids.dist.debian.RTE_DEBIAN9:
            self.skipTest("not this platform")

        pform = PlatformParameters()
        pform.scan()
        
        resx = {'category': 'posix', 'dist': 'debian', 'distrel': 'debian-9.4.0', 
                'distrel_hexversion': 17039877, 'distrel_key': 'debian9', 
                'distrel_name': 'stretch', 'distrel_version': (9, 4, 0), 
                'osrel_id': 'linux', 'osrel_version': [4, 16, 15], 'ostype': 'linux'}
        res = pform.get_json()
        
        assert sorted(res) == sorted(resx)
        

if __name__ == '__main__':
    unittest.main()
