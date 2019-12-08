# -*- coding: utf-8 -*-
"""OpenWRT releases.
"""
from __future__ import absolute_import

import re

from pythonids import PYV35Plus
from platformids import rte2num, num2rte, num2pretty, decode_version_str_to_segments, RTE_OPENWRT, \
    DSKORG_ID, DSKORG_VERSION, PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_OPENWRT17 = RTE_OPENWRT        + 0x00004400  #: OpenWRT-17.*.*
RTE_OPENWRT1701 = RTE_OPENWRT      + 0x00004420  #: OpenWRT-17.01.*
RTE_OPENWRT17016 = RTE_OPENWRT     + 0x00004426  #: OpenWRT-17.01.6

RTE_OPENWRT18 = RTE_OPENWRT        + 0x00004800  #: OpenWRT-18.*.*
RTE_OPENWRT1806 = RTE_OPENWRT      + 0x000048c0  #: OpenWRT-18.06.*
RTE_OPENWRT18061 = RTE_OPENWRT     + 0x000048c1  #: OpenWRT-18.06.1
    
RTE_OPENWRT19 = RTE_OPENWRT        + 0x00004c00  #: OpenWRT-19.*.*
RTE_OPENWRT1901 = RTE_OPENWRT      + 0x00004c20  #: OpenWRT-19.01.*
RTE_OPENWRT19011 = RTE_OPENWRT     + 0x00004c21  #: OpenWRT-19.01.1


#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'openwrt': RTE_OPENWRT,
        'openwrt17016': RTE_OPENWRT17016,
        'openwrt18061': RTE_OPENWRT18061,
        RTE_OPENWRT17016: RTE_OPENWRT17016,
        RTE_OPENWRT18061: RTE_OPENWRT18061,
        RTE_OPENWRT: RTE_OPENWRT,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_OPENWRT: 'openwrt',
        RTE_OPENWRT17016: 'openwrt17016',
        RTE_OPENWRT18061: 'openwrt18061',
    }
)


#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_OPENWRT: 'OpenWRT',
        RTE_OPENWRT17016: 'OpenWRT-17.01.6',
        RTE_OPENWRT18061: 'OpenWRT-18.06.1',
    }
)


dist = ['', '', '', 'OpenWRT', '', '']

try:
    
    with open("/etc/os-release", 'r') as f:
        for l in f:
            if l.startswith('ID='):
                dist[0] = dist[5] = DSKORG_ID.sub(r'\1', l)

            elif l.startswith('VERSION='):  # priority though more widespread
                dist[1] = DSKORG_VERSION.sub(r'\1', l)
            
            elif l.startswith('NAME='):
                dist[2] = dist[3] = re.sub(r'.*NAME=["\']*([^\n"\']*)["\']*[\n]*.*$', '\\1', l)
    
    if dist[0] == 'openwrt':
        dist[2] = 'OpenWRT-' + dist[1]  
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = 'openwrt%d%d%d' % (dist[4][0], dist[4][1], dist[4][2], ) 
    

except PlatformIDsFileCheck:
    # not on OpenWRT platform, so scan will fail
    pass    


if dist[5] != 'openwrt':
    # does not actually match OpenWRT
    dist = ['openwrt', '0.0.0', 'OpenWRT-0.0.0', 'OpenWRT', (0, 0, 0,), 'openwrt']
