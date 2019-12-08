# -*- coding: utf-8 -*-
"""Oracle Enterprise Linux releases.
"""
from __future__ import absolute_import

import re

from pythonids import PYV35Plus
from platformids import RTE_LINUX, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_OEL       = RTE_LINUX   + 0x00080000     #: Oracle Enterprise Linux

RTE_OEL6      = RTE_OEL     + 0x00001800  #: Oracle Enterprise Linux 6
RTE_OEL6U9    = RTE_OEL     + 0x00001920  #: Oracle Enterprise Linux 6 Update-9

RTE_OEL7      = RTE_OEL     + 0x00001c00  #: Oracle Enterprise Linux 7
RTE_OEL7U6    = RTE_OEL     + 0x00001cc0  #: Oracle Enterprise Linux 7 Update-6
    
RTE_OEL8      = RTE_OEL     + 0x00002000  #: Oracle Enterprise Linux 8
RTE_OEL8U0    = RTE_OEL     + 0x00002000  #: Oracle Enterprise Linux 8 Update-0
RTE_OEL8U1    = RTE_OEL     + 0x00002020  #: Oracle Enterprise Linux 8 Update-1
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'oel': RTE_OEL,
        'oel6': RTE_OEL6,
        'oel6u9': RTE_OEL6U9,
        'oel7': RTE_OEL7,
        'oel7u6': RTE_OEL7U6,
        RTE_OEL: RTE_OEL,
        RTE_OEL6: RTE_OEL6,
        RTE_OEL6U9: RTE_OEL6U9,
        RTE_OEL7: RTE_OEL7,
        RTE_OEL7U6: RTE_OEL7U6,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_OEL: 'oel',
        RTE_OEL6: 'oel6',
        RTE_OEL6U9: 'oel6u9',
        RTE_OEL7: 'oel7',
        RTE_OEL7U6: 'oel7u6',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_OEL: 'Oracle Linux',
        RTE_OEL6: 'Oracle Enterprise Linux 6',
        RTE_OEL6U9: 'Oracle Enterprise Linux 6 Update 9',
        RTE_OEL7: 'Oracle Enterprise Linux 7',
        RTE_OEL7U6: 'Oracle Enterprise Linux 7 Update 6',
    }
)


dist = ['', '', '', 'OracleLinux', '', '']

try:

    with open("/etc/redhat-release", 'r') as f:
        for l in f:
            _d = re.split(r'(?s)^([^0-9]*) release *([0-9.]*[^ ]*) [^(]*[(]([^)]*)[)][\n\t ]*$', l)
    
    if _d[1].startswith('Oracle'):
        dist[1] = _d[2]
        dist[4] = decode_version_str_to_segments(_d[2])
        dist[0] = 'oel%d%d' % (dist[4][0], dist[4][1])
        dist[2] = "OracleLinux-" + _d[2]
        dist[5] = 'oel'


except PlatformIDsFileCheck:
    # not on OracleLinux platform, so scan will fail
    pass    


if dist[5] != 'oel':
    # does not actually match OracleLinux
    dist = ['oel', '0.0.0', 'OracleLinux-0.0.0', 'OracleLinux', (0, 0, 0,), 'oel']



