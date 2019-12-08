# -*- coding: utf-8 -*-
"""CentOS releases.
"""
from __future__ import absolute_import

import re

from pythonids import PYV35Plus
from platformids import RTE_CENTOS, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsFileCheck

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


#
# for bit mapping scheme see manuals "2-number version"
#

RTE_CENTOS5    = RTE_CENTOS     + 0x00001400  #: CentOS-5 - EOL-2007

RTE_CENTOS6    = RTE_CENTOS     + 0x00001800  #: CentOS-6.0
RTE_CENTOS60   = RTE_CENTOS6    + 0x00000000  #: CentOS-6.0
RTE_CENTOS61   = RTE_CENTOS6    + 0x00000020  #: CentOS-6.1
RTE_CENTOS62   = RTE_CENTOS6    + 0x00000040  #: CentOS-6.2
RTE_CENTOS63   = RTE_CENTOS6    + 0x00000060  #: CentOS-6.3
RTE_CENTOS64   = RTE_CENTOS6    + 0x00000080  #: CentOS-6.4
RTE_CENTOS65   = RTE_CENTOS6    + 0x000000a0  #: CentOS-6.5
RTE_CENTOS66   = RTE_CENTOS6    + 0x000000c0  #: CentOS-6.6  
RTE_CENTOS67   = RTE_CENTOS6    + 0x000000e0  #: CentOS-6.7
RTE_CENTOS68   = RTE_CENTOS6    + 0x00000100  #: CentOS-6.8
RTE_CENTOS69   = RTE_CENTOS6    + 0x00000120  #: CentOS-6.9
RTE_CENTOS610  = RTE_CENTOS6    + 0x00000140  #: CentOS-6.10
RTE_CENTOS611  = RTE_CENTOS6    + 0x00000160  #: CentOS-6.11
RTE_CENTOS612  = RTE_CENTOS6    + 0x0000018c  #: CentOS-6.12

RTE_CENTOS7    = RTE_CENTOS     + 0x00001c00  #: CentOS-7.0
RTE_CENTOS70   = RTE_CENTOS7    + 0x00000000  #: CentOS-7.0
RTE_CENTOS71   = RTE_CENTOS7    + 0x00000020  #: CentOS-7.1
RTE_CENTOS72   = RTE_CENTOS7    + 0x00000040  #: CentOS-7.2
RTE_CENTOS73   = RTE_CENTOS7    + 0x00000060  #: CentOS-7.3
RTE_CENTOS74   = RTE_CENTOS7    + 0x00000080  #: CentOS-7.4
RTE_CENTOS75   = RTE_CENTOS7    + 0x000000a0  #: CentOS-7.5
RTE_CENTOS76   = RTE_CENTOS7    + 0x000000c0  #: CentOS-7.6
RTE_CENTOS77   = RTE_CENTOS7    + 0x000000d0  #: CentOS-7.7
RTE_CENTOS78   = RTE_CENTOS7    + 0x00000100  #: CentOS-7.8
RTE_CENTOS79   = RTE_CENTOS7    + 0x00000120  #: CentOS-7.9
RTE_CENTOS710  = RTE_CENTOS7    + 0x00000140  #: CentOS-7.10
RTE_CENTOS711  = RTE_CENTOS7    + 0x00000160  #: CentOS-7.11

RTE_CENTOS8    = RTE_CENTOS     + 0x00002000  #: CentOS-8.0

RTE_CENTOS9    = RTE_CENTOS     + 0x00002400  #: CentOS-9.0
RTE_CENTOS10   = RTE_CENTOS     + 0x00002800  #: CentOS-10.0
RTE_CENTOS11   = RTE_CENTOS     + 0x00002c00  #: CentOS-11.0
RTE_CENTOS12   = RTE_CENTOS     + 0x00003000  #: CentOS-12.0

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'centos10':     RTE_CENTOS10,
        'centos5':      RTE_CENTOS5,
        'centos6':      RTE_CENTOS6,
        'centos60':     RTE_CENTOS60,
        'centos61':     RTE_CENTOS61,
        'centos62':     RTE_CENTOS62,
        'centos63':     RTE_CENTOS63,
        'centos64':     RTE_CENTOS64,
        'centos65':     RTE_CENTOS65,
        'centos66':     RTE_CENTOS66,
        'centos67':     RTE_CENTOS67,
        'centos68':     RTE_CENTOS68,
        'centos69':     RTE_CENTOS69,
        'centos610':    RTE_CENTOS610,
        'centos7':      RTE_CENTOS7,
        'centos70':      RTE_CENTOS7,
        'centos71':      RTE_CENTOS71,
        'centos72':      RTE_CENTOS72,
        'centos73':      RTE_CENTOS73,
        'centos74':      RTE_CENTOS74,
        'centos75':     RTE_CENTOS75,
        'centos76':     RTE_CENTOS76,
        'centos8':      RTE_CENTOS8,
        'centos9':      RTE_CENTOS9,
        RTE_CENTOS10:   RTE_CENTOS10,
        RTE_CENTOS5:    RTE_CENTOS5,
        RTE_CENTOS610:  RTE_CENTOS610,
        RTE_CENTOS6:    RTE_CENTOS6,
        RTE_CENTOS75:   RTE_CENTOS75,
        RTE_CENTOS7:    RTE_CENTOS7,
        RTE_CENTOS8:    RTE_CENTOS8,
        RTE_CENTOS9:    RTE_CENTOS9,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_CENTOS5: 'centos5',
        RTE_CENTOS6: 'centos60',
        RTE_CENTOS60: 'centos60',
        RTE_CENTOS61: 'centos61',
        RTE_CENTOS62: 'centos62',
        RTE_CENTOS63: 'centos63',
        RTE_CENTOS64: 'centos64',
        RTE_CENTOS65: 'centos65',
        RTE_CENTOS66: 'centos66',
        RTE_CENTOS67: 'centos67',
        RTE_CENTOS68: 'centos68',
        RTE_CENTOS69: 'centos69',
        RTE_CENTOS610: 'centos610',
        RTE_CENTOS7: 'centos7',
        RTE_CENTOS70: 'centos70',
        RTE_CENTOS71: 'centos71',
        RTE_CENTOS72: 'centos72',
        RTE_CENTOS73: 'centos73',
        RTE_CENTOS74: 'centos74',
        RTE_CENTOS75: 'centos75',
        RTE_CENTOS76: 'centos76',
        RTE_CENTOS77: 'centos77',
        RTE_CENTOS78: 'centos78',
        RTE_CENTOS79: 'centos79',
        RTE_CENTOS710: 'centos710',
        RTE_CENTOS8: 'centos8',
        RTE_CENTOS9: 'centos9',
        RTE_CENTOS10: 'centos10',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_CENTOS60: 'CentOS-6.0',
        RTE_CENTOS610: 'CentOS-6.10',
        RTE_CENTOS61: 'CentOS-6.1',
        RTE_CENTOS62: 'CentOS-6.2',
        RTE_CENTOS63: 'CentOS-6.3',
        RTE_CENTOS64: 'CentOS-6.4',
        RTE_CENTOS65: 'CentOS-6.5',
        RTE_CENTOS66: 'CentOS-6.6',
        RTE_CENTOS67: 'CentOS-6.7',
        RTE_CENTOS68: 'CentOS-6.8',
        RTE_CENTOS69: 'CentOS-6.9',
        RTE_CENTOS6:  'CentOS-6.0',
        RTE_CENTOS70: 'CentOS-7.0-1406',
        RTE_CENTOS71: 'CentOS-7.1-1503',
        RTE_CENTOS72: 'CentOS-7.2-1511',
        RTE_CENTOS73: 'CentOS-7.3-1611',
        RTE_CENTOS74: 'CentOS-7.4-1708',
        RTE_CENTOS75: 'CentOS-7.5-1804',
        RTE_CENTOS76: 'CentOS-7.6-1810',
        RTE_CENTOS7:  'CentOS-7.0-1406',
        RTE_CENTOS8:  'CentOS-8',
        RTE_CENTOS9:  'CentOS-9',
        RTE_CENTOS:   'CentOS',
    }
)


dist = ['', '', '', 'CentOS', '', '']

try:
    with open("/etc/redhat-release", 'r') as f:
        for l in f:
            _d = re.split(r'(?s)^([^0-9]*) release *([0-9.]*[^ ]*) [^(]*[(]([^)]*)[)][\n\t ]*$', l)
    
    if _d[1].startswith('CentOS'):
        dist[1] = _d[2]
        dist[4] = decode_version_str_to_segments(_d[2])
        dist[0] = 'centos%d%d' % (dist[4][0], dist[4][1])
        dist[2] = "CentOS-" + _d[2]
        dist[5] = 'centos'


except PlatformIDsFileCheck:
    # not on CentOS platform, so scan will fail
    pass    


if dist[5] != 'centos':
    # does not actually match CentOS
    dist = ['centos', '0.0.0', 'CentOS-0.0.0', 'CentOS', (0, 0, 0,), 'centos']

