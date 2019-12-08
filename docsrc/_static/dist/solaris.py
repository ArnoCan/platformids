# -*- coding: utf-8 -*-
"""Solaris releases.
"""
from __future__ import absolute_import

import os
import sys
import re
import platform


from pythonids import PYV35Plus
from platformids import RTE_SOLARIS, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsError, PlatformIDsFileCheck

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_SUNOS510  = RTE_SOLARIS    + 0x00002800  #: Solaris-10 == SunOS5.10
RTE_SOLARIS10 = RTE_SOLARIS    + 0x00002800  #: Solaris-10

RTE_SUNOS511  = RTE_SOLARIS    + 0x00002c00  #: Solaris-11 == SunOS5.11
RTE_SOLARIS11 = RTE_SOLARIS    + 0x00002c00  #: Solaris-11
RTE_SOLARIS110 = RTE_SOLARIS   + 0x00002c00  #: Solaris-11.0
RTE_SOLARIS111 = RTE_SOLARIS   + 0x00002c20  #: Solaris-11.1
RTE_SOLARIS112 = RTE_SOLARIS   + 0x00002c40  #: Solaris-11.2
RTE_SOLARIS113 = RTE_SOLARIS   + 0x00002c60  #: Solaris-11.3
RTE_SOLARIS114 = RTE_SOLARIS   + 0x00002c80  #: Solaris-11.4
RTE_SOLARIS115 = RTE_SOLARIS   + 0x00002ca0  #: Solaris-11.5
RTE_SOLARIS116 = RTE_SOLARIS   + 0x00002cc0  #: Solaris-11.6
RTE_SOLARIS117 = RTE_SOLARIS   + 0x00002ce0  #: Solaris-11.7
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'solaris10': RTE_SOLARIS10,
        'solaris11': RTE_SOLARIS11,
        'solaris11': RTE_SOLARIS110,
        'solaris111': RTE_SOLARIS111,
        'solaris112': RTE_SOLARIS112,
        'solaris113': RTE_SOLARIS113,
        'solaris114': RTE_SOLARIS114,
        'solaris115': RTE_SOLARIS115,
        'sunos5': RTE_SOLARIS,
        'sunos5.10': RTE_SOLARIS10,
        'sunos5.11': RTE_SOLARIS11,
        RTE_SOLARIS10: RTE_SOLARIS10,
        RTE_SOLARIS110: RTE_SOLARIS110,
        RTE_SOLARIS111: RTE_SOLARIS111,
        RTE_SOLARIS112: RTE_SOLARIS112,
        RTE_SOLARIS113: RTE_SOLARIS113,
        RTE_SOLARIS114: RTE_SOLARIS114,
        RTE_SOLARIS115: RTE_SOLARIS115,
        RTE_SOLARIS11: RTE_SOLARIS11,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_SOLARIS10: 'solaris10',
        RTE_SUNOS510: 'solaris10',
        RTE_SOLARIS11: 'solaris11',
        RTE_SOLARIS110: 'solaris110',
        RTE_SOLARIS111: 'solaris111',
        RTE_SOLARIS112: 'solaris112',
        RTE_SOLARIS113: 'solaris113',
        RTE_SOLARIS114: 'solaris114',
        RTE_SOLARIS115: 'solaris115',
        RTE_SUNOS511: 'solaris11',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_SOLARIS: 'Solaris',
        RTE_SOLARIS10: 'Solaris10',
        RTE_SOLARIS11: 'Solaris11',
    }
)


dist = ['', '', '', 'Solaris', '', '']

try:

    if sys.platform.startswith('sunos5'):
        # Solaris10 + Solaris11
        # CPython, PyPy, IPython
        dist[1] = platform.release()
        
        if dist[1] == '5.10':
            dist[0] = 'solaris10'
            dist[1] = '10'
            dist[2] = 'Solaris10'
            dist[4] = (10, 0, 0)
            
        elif dist[1] == '5.11':
            dist[1] = platform.version()
            dist[4] = decode_version_str_to_segments(dist[1])
            dist[0] = 'solaris' + re.sub(r'[.]', '', dist[1])
            dist[2] = 'Solaris11'
        
        else:
            raise PlatformIDsError("release not suppported: " + str(dist[1]))
    
    elif os.path.exists('/etc/release'):
        # Solaris10 + Solaris11
        # Jython
        x = open('/etc/release')
        _r = x.readline()  # Oracle Solaris 11.3 X86
        x.close()
        _r = re.sub(r'[^S]*(Solaris) *([0-9.]*).*$', r'\1:\2', _r).split(':')
        
        if _r[0] == 'Solaris':
            _r = _r[1].split('.')
            dist[0] = 'solaris' + _r[0]
            dist[1] = _r[1]
            dist[2] = 'Solaris' + _r[1]
            dist[4] = decode_version_str_to_segments(_r[1])
    
        else:
            raise PlatformIDsError("release not suppported: " + str(dist[1]))
    

except PlatformIDsFileCheck:
    # not on Solaris platform, so scan will fail
    pass    


if dist[5] != 'solaris':
    # does not actually match Solaris
    dist = ['solaris', '0.0.0', 'Solaris-0.0.0', 'Solaris', (0, 0, 0,), 'solaris']






