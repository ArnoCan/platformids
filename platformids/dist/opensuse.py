# -*- coding: utf-8 -*-
"""OpenSUSE releases.
"""
from __future__ import absolute_import

from platformids import rte2num, num2rte, num2pretty, decode_version_str_to_segments, RTE_LINUX, \
    DSKORG_ID, DSKORG_VERSION, PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_OPENSUSE     = RTE_LINUX        + 0x000a0000     #: SuSE
RTE_SLES         = RTE_LINUX        + 0x000b0000     #: SLES


RTE_OPENSUSE10   = RTE_OPENSUSE     + 0x00002800  #: OpenSUSE-10
RTE_OPENSUSE11   = RTE_OPENSUSE     + 0x00002c00  #: OpenSUSE-11
RTE_OPENSUSE12   = RTE_OPENSUSE     + 0x00003000  #: OpenSUSE-12
RTE_OPENSUSE13   = RTE_OPENSUSE     + 0x00003400  #: OpenSUSE-13
RTE_OPENSUSE14   = RTE_OPENSUSE     + 0x00003800  #: OpenSUSE-14
RTE_OPENSUSE15   = RTE_OPENSUSE     + 0x00003c00  #: OpenSUSE-15
RTE_OPENSUSE151  = RTE_OPENSUSE     + 0x00003c20  #: OpenSUSE-15.1
RTE_OPENSUSE16   = RTE_OPENSUSE     + 0x00003000  #: OpenSUSE-16
RTE_OPENSUSE17   = RTE_OPENSUSE     + 0x00003400  #: OpenSUSE-17
    
RTE_OPENSUSE423  = RTE_OPENSUSE     + 0x0000a860  #: OpenSUSE-42.3
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'opensuse': RTE_OPENSUSE,
        'opensuse10': RTE_OPENSUSE10,
        'opensuse11': RTE_OPENSUSE11,
        'opensuse12': RTE_OPENSUSE12,
        'opensuse13': RTE_OPENSUSE13,
        'opensuse14': RTE_OPENSUSE14,
        'opensuse15': RTE_OPENSUSE15,
        'opensuse151': RTE_OPENSUSE151,
        'opensuse16': RTE_OPENSUSE16,
        'opensuse17': RTE_OPENSUSE17,
        'opensuse423': RTE_OPENSUSE423,
        RTE_OPENSUSE10: RTE_OPENSUSE10,
        RTE_OPENSUSE11: RTE_OPENSUSE11,
        RTE_OPENSUSE12: RTE_OPENSUSE12,
        RTE_OPENSUSE13: RTE_OPENSUSE13,
        RTE_OPENSUSE14: RTE_OPENSUSE14,
        RTE_OPENSUSE151: RTE_OPENSUSE151,
        RTE_OPENSUSE15: RTE_OPENSUSE15,
        RTE_OPENSUSE16: RTE_OPENSUSE16,
        RTE_OPENSUSE17: RTE_OPENSUSE17,
        RTE_OPENSUSE423: RTE_OPENSUSE423,
        RTE_OPENSUSE: RTE_OPENSUSE,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_OPENSUSE: 'opensuse',
        RTE_OPENSUSE10: 'opensuse10',
        RTE_OPENSUSE11: 'opensuse11',
        RTE_OPENSUSE12: 'opensuse12',
        RTE_OPENSUSE13: 'opensuse13',
        RTE_OPENSUSE14: 'opensuse14',
        RTE_OPENSUSE15: 'opensuse15',
        RTE_OPENSUSE151: 'opensuse151',
        RTE_OPENSUSE16: 'opensuse16',
        RTE_OPENSUSE17: 'opensuse17',
        RTE_OPENSUSE423: 'opensuse423',
    }
)


num2pretty.update(
    {
    }
)


dist = ['', '', '', 'openSUSE', '', '']

try:

    with open("/etc/os-release", 'r') as f:
        for l in f:
            if l.startswith('ID='):
                dist[5] = DSKORG_ID.sub(r'\1', l)

            elif l.startswith('VERSION='):  # priority though more widespread
                dist[1] = DSKORG_VERSION.sub(r'\1', l) 
            
            elif l.startswith('NAME='):
                dist[3] = DSKORG_ID.sub(r'\1', l)

    if dist[5] == 'opensuse':
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = '%s%d%d' % (dist[5], dist[4][0], dist[4][1],)   
        dist[2] = '%s-%d.%d.%d' % (dist[3], dist[4][0], dist[4][1], dist[4][2],)   

        
except PlatformIDsFileCheck:
    # not on OpenSUSE platform, so scan will fail
    pass    


if dist[5] != 'opensuse':
    # does not actually match OpenSUSE
    dist = ['opensuse', '0.0.0', 'openSUSE-0.0.0', 'openSUSE', (0, 0, 0,), 'opensuse']

