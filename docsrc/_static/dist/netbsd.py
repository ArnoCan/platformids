# -*- coding: utf-8 -*-
"""NetBSD releases.
"""
from __future__ import absolute_import

import sys
import os
import re
import platform

from pythonids import PYV35Plus
from platformids import RTE_BSD, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_NETBSD = RTE_BSD        + 0x00060000  #: NetBSD
RTE_NETBSD60 = RTE_NETBSD   + 0x00001800  #: NETBSD-6.0
RTE_NETBSD70 = RTE_NETBSD   + 0x00001c00  #: NETBSD-7.0
RTE_NETBSD71 = RTE_NETBSD   + 0x00001c20  #: NETBSD-7.1
RTE_NETBSD80 = RTE_NETBSD   + 0x00002000  #: NETBSD-8.0
RTE_NETBSD90 = RTE_NETBSD   + 0x00002400  #: NETBSD-9.0
RTE_NETBSD100 = RTE_NETBSD  + 0x00002800  #: NETBSD-10.0
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'netbsd': RTE_NETBSD,
        'netbsd60': RTE_NETBSD60,
        'netbsd71': RTE_NETBSD71,
        'netbsd70': RTE_NETBSD70,
        'netbsd80': RTE_NETBSD80,
        'netbsd90': RTE_NETBSD90,
        RTE_NETBSD: RTE_NETBSD,
        RTE_NETBSD60: RTE_NETBSD60,
        RTE_NETBSD70: RTE_NETBSD70,
        RTE_NETBSD71: RTE_NETBSD71,
        RTE_NETBSD80: RTE_NETBSD80,
        RTE_NETBSD90: RTE_NETBSD90,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_NETBSD: 'netbsd',
        RTE_NETBSD60: 'netbsd60',
        RTE_NETBSD70: 'netbsd70',
        RTE_NETBSD71: 'netbsd71',
        RTE_NETBSD80: 'netbsd80',
        RTE_NETBSD90: 'netbsd90',
    }
)


#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_NETBSD: 'NetBSD',
    }
)


dist = ['', '', 'NetBSD', 'NetBSD', '', '']

try:
    if sys.platform.lower().startswith('netbsd'):
        # FreeBSD - CPython, PyPy, IPython
        dist[1] = platform.release()
        dist[5] = 'netbsd' 
    
    elif os.path.exists('/etc/netbsd-update.conf'):
        # FreeBSD - match on Jython
        x = os.popen("sysctl kern.ostype kern.osrelease", mode='r')
        if x.readline().endswith("NetBSD\n"):
            dist[1] = re.sub(r'[^=]*=([0-9.]*).*$', r'\1', x.readline())
            dist[5] = 'netbsd' 
        x.close()
            
    
    if dist[5] == 'netbsd':
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = 'netbsd%d' % (dist[4][0], dist[4][1], ) 
        dist[2] = 'NetBSD-%d.%d.%d' %(dist[4][0], dist[4][1], dist[4][2], )


except PlatformIDsFileCheck:
    # not on NetBSD platform, so scan will fail
    pass    


if dist[5] != 'netbsd':
    # does not actually match NetBSD
    dist = ['netbsd', '0.0.0', 'NetBSD-0.0.0', 'NetBSD', (0, 0, 0,), 'netbsd']


