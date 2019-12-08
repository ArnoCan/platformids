# -*- coding: utf-8 -*-
"""SLES releases.
"""
from __future__ import absolute_import

from platformids import RTE_SLES, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    DSKORG_ID, DSKORG_VERSION, PlatformIDsFileCheck

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_SLES15  = RTE_SLES       + 0x00003400  #: RHEL-5
RTE_SLES150 = RTE_SLES       + 0x00003c00  #: RHEL-15.0
RTE_SLES151 = RTE_SLES       + 0x00003c20  #: RHEL-15.1


#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'sles15': RTE_SLES15,
        RTE_SLES15: RTE_SLES15,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_SLES15: 'sles15',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_SLES15: 'SLES15',
    }
)


dist = ['', '', '', 'SLES', '', '']

try:

    with open("/etc/os-release", 'r') as f:
        for l in f:
            if l.startswith('ID='):
                dist[5] = DSKORG_ID.sub(r'\1', l)

            elif l.startswith('VERSION='):  # priority though more widespread
                dist[1] = DSKORG_VERSION.sub(r'\1', l) 
            
            elif l.startswith('NAME='):
                dist[3] = DSKORG_ID.sub(r'\1', l)

    if dist[5] == 'sles':
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = '%s%d%d' % (dist[5], dist[4][0], dist[4][1],)   
        dist[2] = '%s-%d.%d.%d' % (dist[3], dist[4][0], dist[4][1], dist[4][2],)   


except PlatformIDsFileCheck:
    # not on SLES platform, so scan will fail
    pass    


if dist[5] != 'sles':
    # does not actually match SLES
    dist = ['sles', '0.0.0', 'SLES-0.0.0', 'SLES', (0, 0, 0,), 'sles']


