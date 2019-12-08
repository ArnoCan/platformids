# -*- coding: utf-8 -*-
"""Cygwin releases.
"""
from __future__ import absolute_import

import os
import sys
import re

from pythonids import PYV35Plus
# from platformids import RTE_CYGWINNT, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
#     PlatformIDsFileCheck

import platformids 

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_CYGWIN        = platformids.RTE_CYGWINNT + 0x00010000     #: Cygwin running within PWEMU on WindowsNT
RTE_CYGWIN1       = platformids.RTE_CYGWINNT + 0x00020000     #: Cygwin-2.* - contains the major version number
RTE_CYGWIN2       = platformids.RTE_CYGWINNT + 0x00040000     #: Cygwin-2.* - contains the major version number
RTE_CYGWIN3       = platformids.RTE_CYGWINNT + 0x00080000     #: Cygwin-3.* - contains the major version number

RTE_CYGWIN290     = RTE_CYGWIN2  + 0x00000520  #: Cygwin-2.9.0


 
#: mapping of the rte string and numeric representation to the numeric value
platformids.rte2num.update(
    {
        'cygwin': RTE_CYGWIN,
        'cygwin1': RTE_CYGWIN1,
        'cygwin2': RTE_CYGWIN2,
        'cygwin290': RTE_CYGWIN290,
        'cygwin3': RTE_CYGWIN3,
        'cygwinnt': platformids.RTE_CYGWINNT,
        RTE_CYGWIN1: RTE_CYGWIN1,
        RTE_CYGWIN290: RTE_CYGWIN290,
        RTE_CYGWIN2: RTE_CYGWIN2,
        RTE_CYGWIN3: RTE_CYGWIN3,
        RTE_CYGWIN: RTE_CYGWIN,
        platformids.RTE_CYGWINNT: platformids.RTE_CYGWINNT,
    }
)


#: mapping of the rte numeric representation to the string value
platformids.num2rte.update(
    {
        RTE_CYGWIN: 'cygwin',
        RTE_CYGWIN1: 'cygwin1',
        RTE_CYGWIN2: 'cygwin2',
        RTE_CYGWIN290: 'cygwin290',
        RTE_CYGWIN3: 'cygwin3',
        platformids.RTE_CYGWINNT: 'cygwinnt',
    }
)

#: mapping of the rte numeric representation to the pretty string value
platformids.num2pretty.update(
    {
        RTE_CYGWIN: 'Cygwin',
        RTE_CYGWIN1: 'Cygwin-1',
        RTE_CYGWIN2: 'Cygwin-2',
        RTE_CYGWIN290: 'Cygwin-2.9.0',
        RTE_CYGWIN3: 'Cygwin-3',
        platformids.RTE_CYGWINNT: 'CygwinNT',
    }
)


dist = ['', '', '', 'Cygwin', '', 'cygwin']

try:
    

    if (
            sys.platform.startswith('cygwin')
            or
            os.path.exists('/cygdrive')  # rely on standard path only for now
        ):

        with open("/proc/version", 'r') as f:
            for l in f:
                dist[1] = re.sub(r'.* version ([0-9.]*).*', '\1', l)  # for all implementations including Jython
    
        dist[4] = platformids.decode_version_str_to_segments(dist[1])
        dist[0] = 'cygwin%d%d%d' % (dist[4][0], dist[4][1], dist[4][2])
        dist[2] = 'Cygwin-' + dist[1]


except platformids.PlatformIDsFileCheck:
    # not on Cygwin platform, so scan will fail
    pass    


if dist[5] != 'cygwin':
    # does not actually match Cygwin
    dist = ['cygwin', '0.0.0', 'Cygwin-0.0.0', 'Cygwin', (0, 0, 0,), 'cygwin']



