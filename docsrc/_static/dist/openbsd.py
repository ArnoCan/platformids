# -*- coding: utf-8 -*-
"""OpenBSD releases.
"""
from __future__ import absolute_import

import os
import sys
import re
import platform

from pythonids import PYV35Plus
from platformids import RTE_OPENBSD, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_OPENBSD4   = RTE_OPENBSD    +  0x00001000  #: OPENBSD-4
RTE_OPENBSD5   = RTE_OPENBSD    +  0x00001400  #: OPENBSD-5

RTE_OPENBSD6   = RTE_OPENBSD    +  0x00001800  #: OPENBSD-6
RTE_OPENBSD61  = RTE_OPENBSD6   +  0x00000020  #: OPENBSD-6.1
RTE_OPENBSD62  = RTE_OPENBSD6   +  0x00000040  #: OPENBSD-6.2
RTE_OPENBSD63  = RTE_OPENBSD6   +  0x00000060  #: OPENBSD-6.3
RTE_OPENBSD64  = RTE_OPENBSD6   +  0x00000080  #: OPENBSD-6.4
RTE_OPENBSD65  = RTE_OPENBSD6   +  0x000000b0  #: OPENBSD-6.5
RTE_OPENBSD66  = RTE_OPENBSD6   +  0x000000d0  #: OPENBSD-6.6
RTE_OPENBSD67  = RTE_OPENBSD6   +  0x000000e0  #: OPENBSD-6.7
RTE_OPENBSD68  = RTE_OPENBSD6   +  0x00000100  #: OPENBSD-6.8

RTE_OPENBSD7   = RTE_OPENBSD    +  0x00001c00  #: OPENBSD-7
RTE_OPENBSD8   = RTE_OPENBSD    +  0x00002000  #: OPENBSD-8
RTE_OPENBSD9   = RTE_OPENBSD    +  0x00002400  #: OPENBSD-9
RTE_OPENBSD10  = RTE_OPENBSD    +  0x00002800  #: OPENBSD-10


#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'openbsd': RTE_OPENBSD,
#         'openbsd4': RTE_OPENBSD4,
        'openbsd5': RTE_OPENBSD5,
        'openbsd6': RTE_OPENBSD6,
        'openbsd61': RTE_OPENBSD61,
        'openbsd62': RTE_OPENBSD62,
        'openbsd63': RTE_OPENBSD63,
        'openbsd64': RTE_OPENBSD64,
        'openbsd65': RTE_OPENBSD65,
        'openbsd66': RTE_OPENBSD66,
        'openbsd67': RTE_OPENBSD67,
        'openbsd68': RTE_OPENBSD68,
        'openbsd7': RTE_OPENBSD7,
        'openbsd8': RTE_OPENBSD8,
        'openbsd9': RTE_OPENBSD9,
        'openbsd10': RTE_OPENBSD10,
        RTE_OPENBSD: RTE_OPENBSD,
#         RTE_OPENBSD4: RTE_OPENBSD4,
        RTE_OPENBSD5: RTE_OPENBSD5,
        RTE_OPENBSD6: RTE_OPENBSD6,
        RTE_OPENBSD61: RTE_OPENBSD61,
        RTE_OPENBSD62: RTE_OPENBSD62,
        RTE_OPENBSD63: RTE_OPENBSD63,
        RTE_OPENBSD64: RTE_OPENBSD64,
        RTE_OPENBSD65: RTE_OPENBSD65,
        RTE_OPENBSD66: RTE_OPENBSD66,
        RTE_OPENBSD67: RTE_OPENBSD67,
        RTE_OPENBSD68: RTE_OPENBSD68,
        RTE_OPENBSD7: RTE_OPENBSD7,
        RTE_OPENBSD8: RTE_OPENBSD8,
        RTE_OPENBSD9: RTE_OPENBSD9,
        RTE_OPENBSD10: RTE_OPENBSD10,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_OPENBSD: 'openbsd',
#         RTE_OPENBSD4: 'openbsd4',
        RTE_OPENBSD5: 'openbsd5',
        RTE_OPENBSD6: 'openbsd6',
        RTE_OPENBSD61: 'openbsd61',
        RTE_OPENBSD62: 'openbsd62',
        RTE_OPENBSD63: 'openbsd63',
        RTE_OPENBSD64: 'openbsd64',
        RTE_OPENBSD65: 'openbsd65',
        RTE_OPENBSD66: 'openbsd66',
        RTE_OPENBSD67: 'openbsd67',
        RTE_OPENBSD7: 'openbsd7',
        RTE_OPENBSD8: 'openbsd8',
        RTE_OPENBSD9: 'openbsd9',
        RTE_OPENBSD10: 'openbsd10',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_OPENBSD: 'OpenBSD',
    }
)



dist = ['', '', '', 'OpenBSD', '', '']

try:

    if sys.platform.startswith('openbsd'):
        # OpenBSD - CPython, PyPy, IPython
        dist[1] = platform.release()
        dist[5] = 'openbsd'
    
    elif os.path.exists('/bsd.booted'):
        # OpenBSD - match on Jython
        x = os.popen("sysctl kern.ostype kern.osrelease", mode='r')
        if x.readline().endswith("OpenBSD\n"):
            # 'kern.ostype=OpenBSD\n'
            _r = x.readline()
            # 'kern.osrelease=6.3\n'
        x.close()
        dist[1] = _r = re.sub(r'[^=]*=([0-9.]*).*$', r'\1', _r)
        dist[5] = 'openbsd'


    if dist[5] == 'openbsd':
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = 'openbsd%d' % (dist[4][0], dist[4][1], ) 
        dist[2] = 'OpenBSD-%d.%d.%d' %(dist[4][0], dist[4][1], dist[4][2], )
        
        
except PlatformIDsFileCheck:
    # not on OpenBSD platform, so scan will fail
    pass    


if dist[5] != 'openbsd':
    # does not actually match OpenBSD
    dist = ['openbsd', '0.0.0', 'OpenBSD-0.0.0', 'OpenBSD', (0, 0, 0,), 'openbsd']

