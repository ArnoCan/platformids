# -*- coding: utf-8 -*-
"""Raspbian releases.

The *Raspbian* distribution represents a *shrinked multi-role PC-Platform* as an
embedded system with integrated low-level HW interfaces.

*Raspbian* is specialized for the *Raspberry Pi* boards.
"""
from __future__ import absolute_import

import re

from pythonids import PYV35Plus
from platformids import rte2num, num2rte, num2pretty, decode_version_str_to_segments, RTE_RASPBIAN, \
    DSKORG_ID, PlatformIDsFileCheck

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



#-----------------------------------------------#
#                                               #
# optional constants for convenience            #
#                                               #
#-----------------------------------------------#


RTE_RASPBIAN7 = RTE_RASPBIAN        +  0x00001c00  #: RASPBIAN - wheezy
RTE_RASPBIAN8 = RTE_RASPBIAN        +  0x00002000  #: RASPBIAN - jessy
                                  
RTE_RASPBIAN9 = RTE_RASPBIAN        +  0x00002400  #: RASPBIAN - stretch
RTE_RASPBIAN90 = RTE_RASPBIAN       +  0x00002400  #: RASPBIAN - stretch - 9.0
RTE_RASPBIAN91 = RTE_RASPBIAN       +  0x00002420  #: RASPBIAN - stretch - 9.1
RTE_RASPBIAN92 = RTE_RASPBIAN       +  0x00002440  #: RASPBIAN - stretch - 9.2
RTE_RASPBIAN93 = RTE_RASPBIAN       +  0x00002460  #: RASPBIAN - stretch - 9.3
RTE_RASPBIAN94 = RTE_RASPBIAN       +  0x00002480  #: RASPBIAN - stretch - 9.4
RTE_RASPBIAN95 = RTE_RASPBIAN       +  0x000024b0  #: RASPBIAN - stretch - 9.5
RTE_RASPBIAN96 = RTE_RASPBIAN       +  0x000024c0  #: RASPBIAN - stretch - 9.6
RTE_RASPBIAN97 = RTE_RASPBIAN       +  0x000024e0  #: RASPBIAN - stretch - 9.7

RTE_RASPBIAN10 = RTE_RASPBIAN       +  0x00002800  #: RASPBIAN - buster 
RTE_RASPBIAN100 = RTE_RASPBIAN      +  0x00002800  #: RASPBIAN - buster 
RTE_RASPBIAN101 = RTE_RASPBIAN      +  0x00002820  #: RASPBIAN - buster 
RTE_RASPBIAN102 = RTE_RASPBIAN      +  0x00002840  #: RASPBIAN - buster 

RTE_RASPBIAN11 = RTE_RASPBIAN       +  0x00002c00  #: RASPBIAN - bullseye
RTE_RASPBIAN12 = RTE_RASPBIAN       +  0x00003000  #: RASPBIAN - bookworm
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'Raspbian-wheezy': RTE_RASPBIAN7,
        'Raspbian-jessy': RTE_RASPBIAN8,
        'Raspbian-stretch': RTE_RASPBIAN9,
        'Raspbian-buster': RTE_RASPBIAN10,
        'Raspbian-bullseye': RTE_RASPBIAN11,
        'Raspbian-bookworm': RTE_RASPBIAN12,
        'raspbian7': RTE_RASPBIAN7,
        'raspbian8': RTE_RASPBIAN8,
        'raspbian9': RTE_RASPBIAN9,
        'raspbian10': RTE_RASPBIAN10,
        'raspbian11': RTE_RASPBIAN11,
        'raspbian12': RTE_RASPBIAN12,
        RTE_RASPBIAN7: RTE_RASPBIAN7,
        RTE_RASPBIAN8: RTE_RASPBIAN8,
        RTE_RASPBIAN9: RTE_RASPBIAN9,
        RTE_RASPBIAN10: RTE_RASPBIAN10,
        RTE_RASPBIAN11: RTE_RASPBIAN11,
        RTE_RASPBIAN12: RTE_RASPBIAN12,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_RASPBIAN7: 'raspbian7',
        RTE_RASPBIAN8: 'raspbian8',
        RTE_RASPBIAN9: 'raspbian9',
        RTE_RASPBIAN10: 'raspbian10',
        RTE_RASPBIAN11: 'raspbian11',
        RTE_RASPBIAN12: 'raspbian12',
    }
)


#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_RASPBIAN8: 'Raspbian-jessy',
        RTE_RASPBIAN9: 'Raspbian-stretch',
        RTE_RASPBIAN10: 'Raspbian-buster',
        RTE_RASPBIAN11: 'Raspbian-bullseye',
        RTE_RASPBIAN12: 'Raspbian-bookworm',
        RTE_RASPBIAN7: 'Raspbian-wheezy',
    }
)


dist = ['', '', 'Raspbian-', 'Raspbian', '', '']

try:
    with open("/etc/os-release", 'r') as f:
        for l in f:
            if l.startswith('ID='):
                dist[0] = dist[5] = DSKORG_ID.sub(r'\1', l)

    if dist[0] == 'raspbian':
        with open("/etc/debian_version", 'r') as f:
            for l in f:
                dist[1] = re.split(r'(?s)^([0-9.]*).*$', l)[1]  # just for safety
                dist[4] = decode_version_str_to_segments(dist[1])
                dist[0] += '%d%d' % (dist[4][0], dist[4][1],)
                dist[2] += dist[1]

except PlatformIDsFileCheck:
    # not on raspbian platform, so scan will fail
    pass    


if dist[0] == 'raspbian':
    dist = ['raspbian', '0.0.0', 'Raspbian-0.0.0', 'Raspbian', (0, 0, 0,), 'raspbian']

