# -*- coding: utf-8 -*-
"""FreeBSD releases.
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
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_FREEBSD       = RTE_BSD      + 0x00040000    #: FreeBSD
# RTE_FREEBSD4     = RTE_FREEBSD   + 0x00001000  #: FREEBSD-4
# RTE_FREEBSD5     = RTE_FREEBSD   + 0x00001400  #: FREEBSD-5
# RTE_FREEBSD6     = RTE_FREEBSD   + 0x00001800  #: FREEBSD-6
# RTE_FREEBSD7     = RTE_FREEBSD   + 0x00001c00  #: FREEBSD-7
# RTE_FREEBSD8     = RTE_FREEBSD   + 0x00002000  #: FREEBSD-8
# RTE_FREEBSD9     = RTE_FREEBSD   + 0x00002400  #: FREEBSD-9
RTE_FREEBSD10    = RTE_FREEBSD   + 0x00002800  #: FREEBSD-10
RTE_FREEBSD11    = RTE_FREEBSD   + 0x00002c00  #: FREEBSD-11
RTE_FREEBSD111   = RTE_FREEBSD   + 0x00002c20  #: FREEBSD-11.1
RTE_FREEBSD112   = RTE_FREEBSD   + 0x00002c40  #: FREEBSD-11.2
RTE_FREEBSD12    = RTE_FREEBSD   + 0x00003000  #: FREEBSD-12
RTE_FREEBSD121   = RTE_FREEBSD   + 0x00003020  #: FREEBSD-12.1
RTE_FREEBSD122   = RTE_FREEBSD   + 0x00003040  #: FREEBSD-12.2
RTE_FREEBSD13    = RTE_FREEBSD   + 0x00003400  #: FREEBSD-13
RTE_FREEBSD14    = RTE_FREEBSD   + 0x00003800  #: FREEBSD-14
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
         RTE_FREEBSD: RTE_FREEBSD,
        'freebsd': RTE_FREEBSD,
        'freebsd10': RTE_FREEBSD10,
        'freebsd11': RTE_FREEBSD11,
        'freebsd111': RTE_FREEBSD111,
        'freebsd112': RTE_FREEBSD112,
        'freebsd12': RTE_FREEBSD12,
        'freebsd121': RTE_FREEBSD121,
        'freebsd122': RTE_FREEBSD122,
        'freebsd13': RTE_FREEBSD13,
#         'freebsd4': RTE_FREEBSD4,
#         'freebsd5': RTE_FREEBSD5,
#         'freebsd6': RTE_FREEBSD6,
#         'freebsd7': RTE_FREEBSD7,
#         'freebsd8': RTE_FREEBSD8,
#         'freebsd9': RTE_FREEBSD9,
        RTE_FREEBSD10: RTE_FREEBSD10,
        RTE_FREEBSD111: RTE_FREEBSD111,
        RTE_FREEBSD112: RTE_FREEBSD112,
        RTE_FREEBSD11: RTE_FREEBSD11,
        RTE_FREEBSD12: RTE_FREEBSD12,
        RTE_FREEBSD121: RTE_FREEBSD121,
        RTE_FREEBSD122: RTE_FREEBSD122,
        RTE_FREEBSD13: RTE_FREEBSD13,
#         RTE_FREEBSD4: RTE_FREEBSD4,
#         RTE_FREEBSD5: RTE_FREEBSD5,
#         RTE_FREEBSD6: RTE_FREEBSD6,
#         RTE_FREEBSD7: RTE_FREEBSD7,
#         RTE_FREEBSD8: RTE_FREEBSD8,
#         RTE_FREEBSD9: RTE_FREEBSD9,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_FREEBSD: 'freebsd',
#         RTE_FREEBSD4: 'freebsd4',
#         RTE_FREEBSD5: 'freebsd5',
#         RTE_FREEBSD6: 'freebsd6',
#         RTE_FREEBSD7: 'freebsd7',
#         RTE_FREEBSD8: 'freebsd8',
#         RTE_FREEBSD9: 'freebsd9',
        RTE_FREEBSD10: 'freebsd10',
        RTE_FREEBSD11: 'freebsd11',
        RTE_FREEBSD111: 'freebsd111',
        RTE_FREEBSD112: 'freebsd112',
        RTE_FREEBSD12: 'freebsd12',
        RTE_FREEBSD121: 'freebsd121',
        RTE_FREEBSD122: 'freebsd122',
        RTE_FREEBSD13: 'freebsd13',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_FREEBSD: 'FreeBSD',
        RTE_FREEBSD11: 'FreeBSD-11',
        RTE_FREEBSD12: 'FreeBSD-12',
        RTE_FREEBSD13: 'FreeBSD-13',
    }
)


dist = ['', '', '', 'FreeBSD', '', '']

try:
    if sys.platform.lower().startswith('freebsd'):
        # FreeBSD - CPython, PyPy, IPython
        dist[1] = platform.release()
        dist[5] = 'freebsd' 
    
    elif os.path.exists('/etc/freebsd-update.conf'):
        # FreeBSD - match on Jython
        x = os.popen("sysctl kern.ostype kern.osrelease", mode='r')
        if x.readline().endswith("FreeBSD\n"):
            dist[1] = re.sub(r'[^=]*=([0-9.]*).*$', r'\1', x.readline())
            dist[5] = 'freebsd' 
        x.close()
            
    
    if dist[5] == 'freebsd':
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = 'freebsd%d' % (dist[4][0], dist[4][1], ) 
        dist[2] = 'FreeBSD-%d.%d.%d' %(dist[4][0], dist[4][1], dist[4][2], )


except PlatformIDsFileCheck:
    # not on FreeBSD platform, so scan will fail
    pass    


if dist[5] != 'freebsd':
    # does not actually match FreeBSD
    dist = ['freebsd', '0.0.0', 'FreeBSD-0.0.0', 'FreeBSD', (0, 0, 0,), 'freebsd']


