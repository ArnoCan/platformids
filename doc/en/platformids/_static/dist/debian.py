# -*- coding: utf-8 -*-
"""Debian releases.
"""
from __future__ import absolute_import

import os
import re

from pythonids import PYV35Plus
from platformids import RTE_DEBIAN, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    DSKORG_ID, PlatformIDsFileCheck




__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_DEBIAN7 = RTE_DEBIAN      + 0x00001c00  #: Debian - wheezy

RTE_DEBIAN8 = RTE_DEBIAN      + 0x00002000  #: Debian - jessy
RTE_DEBIAN80 = RTE_DEBIAN8    + 0x00002000  #: Debian - jessy
RTE_DEBIAN81 = RTE_DEBIAN8    + 0x00002020  #: Debian - jessy
RTE_DEBIAN82 = RTE_DEBIAN8    + 0x00002040  #: Debian - jessy
RTE_DEBIAN83 = RTE_DEBIAN8    + 0x00002060  #: Debian - jessy
RTE_DEBIAN84 = RTE_DEBIAN8    + 0x00002080  #: Debian - jessy
RTE_DEBIAN85 = RTE_DEBIAN8    + 0x000020a0  #: Debian - jessy
RTE_DEBIAN86 = RTE_DEBIAN8    + 0x000020c0  #: Debian - jessy
RTE_DEBIAN87 = RTE_DEBIAN8    + 0x000020e0  #: Debian - jessy
RTE_DEBIAN88 = RTE_DEBIAN8    + 0x00002100  #: Debian - jessy
RTE_DEBIAN89 = RTE_DEBIAN8    + 0x00002120  #: Debian - jessy
RTE_DEBIAN810 = RTE_DEBIAN8   + 0x00002140  #: Debian - jessy

RTE_DEBIAN9 = RTE_DEBIAN      + 0x00002400  #: Debian - stretch
RTE_DEBIAN90 = RTE_DEBIAN9    + 0x00002400  #: Debian - stretch
RTE_DEBIAN91 = RTE_DEBIAN9    + 0x00002420  #: Debian - stretch
RTE_DEBIAN92 = RTE_DEBIAN9    + 0x00002440  #: Debian - stretch
RTE_DEBIAN93 = RTE_DEBIAN9    + 0x00002460  #: Debian - stretch
RTE_DEBIAN94 = RTE_DEBIAN9    + 0x00002480  #: Debian - stretch
RTE_DEBIAN95 = RTE_DEBIAN9    + 0x000024a0  #: Debian - stretch
RTE_DEBIAN96 = RTE_DEBIAN9    + 0x000024c0  #: Debian - stretch
RTE_DEBIAN97 = RTE_DEBIAN9    + 0x000024e0  #: Debian - stretch
RTE_DEBIAN98 = RTE_DEBIAN9    + 0x00002500  #: Debian - stretch
RTE_DEBIAN99 = RTE_DEBIAN9    + 0x00002520  #: Debian - stretch

RTE_DEBIAN10 = RTE_DEBIAN     + 0x00002800  #: Debian - buster 
RTE_DEBIAN100 = RTE_DEBIAN    + 0x00002800  #: Debian - buster 
RTE_DEBIAN101 = RTE_DEBIAN    + 0x00002820  #: Debian - buster 
RTE_DEBIAN102 = RTE_DEBIAN    + 0x00002840  #: Debian - buster 

RTE_DEBIAN11 = RTE_DEBIAN     + 0x00002c80  #: Debian - bullseye
RTE_DEBIAN12 = RTE_DEBIAN     + 0x00003000  #: Debian - bookworm
RTE_DEBIAN13 = RTE_DEBIAN     + 0x00003400  #: Debian - ...

   
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'wheezy': RTE_DEBIAN7,
        'jessy': RTE_DEBIAN8,
        'stretch': RTE_DEBIAN9,
        'buster': RTE_DEBIAN10,
        'bullseye': RTE_DEBIAN11,
        'bookworm': RTE_DEBIAN12,
        'debian7': RTE_DEBIAN7,
        'debian8': RTE_DEBIAN8,
        'debian9': RTE_DEBIAN9,
        'debian10': RTE_DEBIAN10,
        'debian11': RTE_DEBIAN11,
        'debian12': RTE_DEBIAN12,
        RTE_DEBIAN7: RTE_DEBIAN7,
        RTE_DEBIAN8: RTE_DEBIAN8,
        RTE_DEBIAN9: RTE_DEBIAN9,
        RTE_DEBIAN10: RTE_DEBIAN10,
        RTE_DEBIAN11: RTE_DEBIAN11,
        RTE_DEBIAN12: RTE_DEBIAN12,

        #
#         'debian96': RTE_DEBIAN96,
#         RTE_DEBIAN96: RTE_DEBIAN96,

    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_DEBIAN7: 'debian7',
        RTE_DEBIAN8: 'debian8',
        RTE_DEBIAN9: 'debian9',
        RTE_DEBIAN10: 'debian10',
        RTE_DEBIAN11: 'debian11',
        RTE_DEBIAN12: 'debian12',

        #
#         RTE_DEBIAN96: 'debian96',

    }
)

num2pretty.update(
    {
        RTE_DEBIAN7: 'wheezy',
        RTE_DEBIAN8: 'jessy',
        RTE_DEBIAN9: 'stretch',
        RTE_DEBIAN10: 'buster',
        RTE_DEBIAN11: 'bullseye',
        RTE_DEBIAN12: 'bookworm',
    }
)


dist = ['', '', 'Debian-', 'Debian', '', '']

try:
    if os.path.exists("/etc/debian_version"):
        dist = ['debian', '', '', 'Debian', '']
        with open("/etc/debian_version", 'r') as f:
            for l in f:
                dist[1] = re.split(r'(?s)^([0-9.]*).*$', l)[1]
                dist[4] = decode_version_str_to_segments(dist[1])
    
    
    _ver = ''
    _name = ''
    
    with open("/etc/os-release", 'r') as f:
        for l in f:
            if l.startswith('ID='):
                dist[0] = dist[5] = DSKORG_ID.sub(r'\1', l)

    if dist[5] == 'debian':
        # debian
        dist[0] += str(dist[4][0]) + str(dist[4][1])
        dist[2] += dist[1]


except PlatformIDsFileCheck:
    # not on Debian platform, so scan will fail
    pass    


if dist[5] != 'debian':
    # does not actually match Debian
    dist = ['debian', '0.0.0', 'Debian-0.0.0', 'Debian', (0, 0, 0,), 'debian']

