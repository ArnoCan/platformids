# -*- coding: utf-8 -*-
"""ArchLinux releases.
"""
from __future__ import absolute_import

import os
import time


# from platformids import _debug, _verbose
from pythonids import PYV35Plus
from platformids import RTE, rte2num, num2rte, num2pretty, custom_rte_distrel2tuple, \
    RTE_LINUX, RTE_DISTEXT, RTE_ARCHLINUX, \
    RTE_DIST , PlatformIDsUnknownError, \
    DSKORG_ID, DSKORG_ID_LIKE, DSKORG_NAME_RELEASE, DSKORG_VERSION, PlatformIDsFileCheck



__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_ARCHLINUX20180601 = RTE_ARCHLINUX           + 0x000060c1 #: archlinux - 2018.06.01
RTE_ARCHLINUX20181001 = RTE_ARCHLINUX           + 0x00006141 #: archlinux - 2018.10.01
RTE_ARCHLINUX20181101 = RTE_ARCHLINUX           + 0x00006161 #: archlinux - 2018.11.01
RTE_ARCHLINUX20181201 = RTE_ARCHLINUX           + 0x00006181 #: archlinux - 2018.12.01
RTE_ARCHLINUX20190401 = RTE_ARCHLINUX           + 0x00006281 #: archlinux - 2019.04.01

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'archlinux20180601':          RTE_ARCHLINUX20180601,
        'archlinux20181001':          RTE_ARCHLINUX20181001,
        'archlinux20181101':          RTE_ARCHLINUX20181101,
        'archlinux20181201':          RTE_ARCHLINUX20181201,
        'archlinux20190401':          RTE_ARCHLINUX20190401,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_ARCHLINUX20180601:        'archlinux20180601',
        RTE_ARCHLINUX20181001:        'archlinux20181001',
        RTE_ARCHLINUX20181101:        'archlinux20181101',
        RTE_ARCHLINUX20181201:        'archlinux20181201',
        RTE_ARCHLINUX20190401:        'archlinux20190401',
    }
)

#: mapping of the rte numeric representation to the string value
# num2pretty.update(
#     {
#     }
# )


dist = ['', '', '', 'ArchLinux', '', '']

try:

    if os.path.exists("/etc/os-release"):

        #
        # slightly different to others, thus do not want shared code
        #
        with open("/etc/os-release", 'r') as f:
            for l in f:
                if l.startswith('ID='):
                    dist[0] = dist[5] = DSKORG_ID.sub(r'\1', l)
    
                elif l.startswith('VERSION='):
                    # optional custom value, not defined by ArchLinux
                    dist[1] = _ver = DSKORG_VERSION.split(l)
    
                elif l.startswith('ID_LIKE='):
                    dist[2] = DSKORG_ID_LIKE.sub(r'\1', l)
    
                elif l.startswith('NAME='):
                    dist[3] = _nam = DSKORG_NAME_RELEASE.split(l)[-1]
    
        if dist[5] == 'arch':
            _s = os.stat('/va/cache/pacman/pkg')
            _t = time.gmtime(_s.st_mtime)
            dist[4] = (_t.tm_year, _t.tm_mon, _t.tm_mday)
            dist[1] = '%d.%02d.%02d' % (_t.tm_year, _t.tm_mon, _t.tm_mday)
            dist[0] = 'arch%d%d%d' % (_t.tm_year, _t.tm_mon, _t.tm_mday)
            dist[2] = 'ArchLinux-' + dist[1]  


except PlatformIDsFileCheck:
    # not on ArchLinux platform, so scan will fail
    pass    


if dist[5] != 'arch':
    # does not actually match ArchLinux
    dist = ['arch', '0.0.0', 'ArchLinux-0.0.0', 'ArchLinux', (0, 0, 0,), 'arch']



