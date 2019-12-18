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

from platformids.platforms import PlatformParameters


class CallUnits(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)
        
        self.maxDiff = None

    def testCase010(self):
        pform = PlatformParameters()
        pform.scan()

        resx = """
category                  = %s
cpu                       = %s
cpudata                   = %s
dist                      = %s
distrel                   = %s
distrel_hexversion        = %s
distrel_key               = %s
distrel_name              = %s
distrel_version           = %s
ostype                    = %s
ostype_id                 = %s
ostype_version            = %s""" % (
            str(pform.category),
            str(pform.cpu),
            str(pform.cpudata),
            str(pform.dist),
            str(pform.distrel),
            str(pform.distrel_hexversion),
            str(pform.distribution_key),
            str(pform.distribution_name),
            str(pform.distribution_version),
            str(pform.ostype),
            str(pform.ostype_id),
            str(pform.ostype_version),
        )
        
        res = pform.pretty_format()
        # print("4TEST:<" + str(res) + ">")
        
        self.assertEqual(res, resx)
        pass
        

if __name__ == '__main__':
    unittest.main()
