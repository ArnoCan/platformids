# -*- coding: utf-8 -*-
"""AlpineLinux releases.
"""
from __future__ import absolute_import

import os


from pythonids import PYV35Plus
from platformids import rte2num, num2rte, num2pretty, decode_version_str_to_segments, RTE_LINUX, \
    DSKORG_ID, DSKORG_VERSION, VERSION_ID, PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_ALPINELIN         = RTE_LINUX              + 0x00090000     #: Alpine Linux
RTE_ALPINELIN381      = RTE_ALPINELIN          + 0x0000d01      #: AlpieLinux-3.8.1
RTE_ALPINELIN39       = RTE_ALPINELIN          + 0x0000d20      #: AlpieLinux-3.9
RTE_ALPINELIN310      = RTE_ALPINELIN          + 0x0000d40      #: AlpieLinux-3.10

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'alpinelinux':             RTE_ALPINELIN,
        'alpinelinux381':          RTE_ALPINELIN381,
        RTE_ALPINELIN381:          RTE_ALPINELIN381,
        RTE_ALPINELIN:             RTE_ALPINELIN,
        'alpinelinux39':          RTE_ALPINELIN39,
        RTE_ALPINELIN39:          RTE_ALPINELIN39,
        'alpinelinux310':          RTE_ALPINELIN310,
        RTE_ALPINELIN310:          RTE_ALPINELIN310,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_ALPINELIN:        'alpinelinux',
        RTE_ALPINELIN381:     'alpinelinux381',
        RTE_ALPINELIN39:      'alpinelinux39',
        RTE_ALPINELIN310:     'alpinelinux310',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_ALPINELIN:        'AlpineLinux',
    }
)

dist = ['', '', '', '', '', '']

try:
    if os.path.exists("/etc/os-release"):
        #
        # slightly different to others, thus do not want shared code
        #
        with open("/etc/os-release", 'r') as f:
            for l in f:
                if l.startswith('ID='):
                    dist[0] = dist[5] = DSKORG_ID.sub(r'\1', l)
    
                #  = re.compile(r'(?s)^VERSION_ID=["\']*([^"\']*)["\']*.*')
                elif l.startswith('VERSION_ID='):
                    # optional custom value, not defined by ArchLinux
                    dist[1] = VERSION_ID.sub(r'\1', l)

                elif l.startswith('VERSION='):
                    # optional custom value, not defined by ArchLinux
                    dist[1] = DSKORG_VERSION.split(l)

    if dist[0] == 'alpine':
        dist[2] += '-' + dist[1]  
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] +=  '%d%d%d' % (dist[4][0], dist[4][1], dist[4][2],)


except PlatformIDsFileCheck:
    # not on AlpineLinux platform, so scan will fail
    pass    


if dist[5] != 'alpine':
    # does not actually match AlpineLinux
    dist = ['alpine', '0.0.0', 'AlpineLinux-0.0.0', 'AlpineLinux', (0, 0, 0,), 'alpine']

