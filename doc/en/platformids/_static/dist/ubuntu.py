# -*- coding: utf-8 -*-
"""Ubuntu releases.
"""
from __future__ import absolute_import

from pythonids import PYV35Plus
from platformids import rte2num, num2rte, num2pretty, decode_version_str_to_segments, RTE_UBUNTU, \
    DSKORG_ID, VERSION_ID, PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.30'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_UBUNTU1004 = RTE_UBUNTU   + 0x00002880  #: Ubuntu 10.04 LTS (Lucid Lynx)
RTE_UBUNTU1204 = RTE_UBUNTU   + 0x00003080  #: Ubuntu 12.04 LTS (Precise Pangolin)
RTE_UBUNTU1404 = RTE_UBUNTU   + 0x00003880  #: Ubuntu 14.04 LTS (Trusty Tahr)
RTE_UBUNTU1504 = RTE_UBUNTU   + 0x00003c80  #: Ubuntu 15.04 (Vivid Vervet)
RTE_UBUNTU1510 = RTE_UBUNTU   + 0x00003d40  #: Ubuntu 15.10 (Wily Werewolf)
RTE_UBUNTU1604 = RTE_UBUNTU   + 0x00004040  #: Ubuntu 16.04 LTS (Xenial Xerus) 
RTE_UBUNTU1610 = RTE_UBUNTU   + 0x00004140  #: Ubuntu 16.10 (Yakkety Yak) 
RTE_UBUNTU1704 = RTE_UBUNTU   + 0x00004480  #: Ubuntu 17.04 (Zesty Zapus) 
RTE_UBUNTU1710 = RTE_UBUNTU   + 0x00004540  #: Ubuntu 17.10 (Artful Aardvark) 
RTE_UBUNTU1804 = RTE_UBUNTU   + 0x00004880  #: Ubuntu 18.04 LTS (Bionic Beaver) 
RTE_UBUNTU1810 = RTE_UBUNTU   + 0x00004940  #: Ubuntu 18.10 (Cosmic Cuttlefish) 
RTE_UBUNTU1904 = RTE_UBUNTU   + 0x00004c80  #: Ubuntu 19.04 (Disco Dingo) 
RTE_UBUNTU1910 = RTE_UBUNTU   + 0x00004c80  #: Ubuntu 19.10 (Eoan EANIMAL) 

#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'ArtfulAardvark': RTE_UBUNTU1710,
        'BionicBeaver': RTE_UBUNTU1804,
        'CosmicCuttlefish': RTE_UBUNTU1810,
        'DiscoDingo': RTE_UBUNTU1904,
        'LucidLynx': RTE_UBUNTU1004,
        'PrecisePangolin': RTE_UBUNTU1204,
        'TrustyTahr': RTE_UBUNTU1404,
        'VividVervet': RTE_UBUNTU1504,
        'WilyWerewolf': RTE_UBUNTU1510,
        'XenialXerus': RTE_UBUNTU1604,
        'YakketyYak': RTE_UBUNTU1610,
        'ZestyZapus': RTE_UBUNTU1704,
        'EoanEANIMAL': RTE_UBUNTU1910,
        'ubuntu': RTE_UBUNTU,
        'ubuntu1004': RTE_UBUNTU1004,
        'ubuntu1204': RTE_UBUNTU1204,
        'ubuntu1404': RTE_UBUNTU1404,
        'ubuntu1504': RTE_UBUNTU1504,
        'ubuntu1510': RTE_UBUNTU1510,
        'ubuntu1604': RTE_UBUNTU1604,
        'ubuntu1610': RTE_UBUNTU1610,
        'ubuntu1704': RTE_UBUNTU1704,
        'ubuntu1710': RTE_UBUNTU1710,
        'ubuntu1804': RTE_UBUNTU1804,
        'ubuntu1810': RTE_UBUNTU1810,
        'ubuntu1904': RTE_UBUNTU1904,
        'ubuntu1910': RTE_UBUNTU1910,
        RTE_UBUNTU1004: RTE_UBUNTU1004,
        RTE_UBUNTU1204: RTE_UBUNTU1204,
        RTE_UBUNTU1404: RTE_UBUNTU1404,
        RTE_UBUNTU1504: RTE_UBUNTU1504,
        RTE_UBUNTU1510: RTE_UBUNTU1510,
        RTE_UBUNTU1604: RTE_UBUNTU1604,
        RTE_UBUNTU1610: RTE_UBUNTU1610,
        RTE_UBUNTU1704: RTE_UBUNTU1704,
        RTE_UBUNTU1710: RTE_UBUNTU1710,
        RTE_UBUNTU1804: RTE_UBUNTU1804,
        RTE_UBUNTU1810: RTE_UBUNTU1810,
        RTE_UBUNTU1904: RTE_UBUNTU1904,
        RTE_UBUNTU1910: RTE_UBUNTU1910,
        RTE_UBUNTU: RTE_UBUNTU,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_UBUNTU1004: 'ubuntu1004',
        RTE_UBUNTU1204: 'ubuntu1204',
        RTE_UBUNTU1404: 'ubuntu1404',
        RTE_UBUNTU1504: 'ubuntu1504',
        RTE_UBUNTU1510: 'ubuntu1510',
        RTE_UBUNTU1604: 'ubuntu1604',
        RTE_UBUNTU1610: 'ubuntu1610',
        RTE_UBUNTU1704: 'ubuntu1704',
        RTE_UBUNTU1710: 'ubuntu1710',
        RTE_UBUNTU1804: 'ubuntu1804',
        RTE_UBUNTU1810: 'ubuntu1810',
        RTE_UBUNTU1904: 'ubuntu1904',
        RTE_UBUNTU1910: 'ubuntu1910',
        RTE_UBUNTU:     'ubuntu',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_UBUNTU1004: 'LucidLynx',
        RTE_UBUNTU1204: 'PrecisePangolin',
        RTE_UBUNTU1404: 'TrustyTahr',
        RTE_UBUNTU1504: 'VividVervet',
        RTE_UBUNTU1510: 'WilyWerewolf',
        RTE_UBUNTU1604: 'XenialXerus',
        RTE_UBUNTU1610: 'YakketyYak',
        RTE_UBUNTU1704: 'ZestyZapus',
        RTE_UBUNTU1710: 'ArtfulAardvark',
        RTE_UBUNTU1804: 'BionicBeaver',
        RTE_UBUNTU1810: 'CosmicCuttlefish',
        RTE_UBUNTU1904: 'DiscoDingo',
        RTE_UBUNTU1910: 'EoanEANIMAL',
        RTE_UBUNTU:     'Ubuntu',
    }
)


dist = ['', '', '', 'Ubuntu', '', '']

try:
    
    with open("/etc/os-release", 'r') as f:
        for l in f:
            
            if l.startswith('ID='):
                dist[5] = DSKORG_ID.sub(r'\1', l)
            
            elif l.startswith('VERSION_ID='):  # Ubuntu, redundant in Slackware
                dist[1] = VERSION_ID.sub(r'\1', l)  

    if dist[5] == 'ubuntu':    
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = '%s%d%d' % (dist[5], dist[4][0], dist[4][1], ) 
        dist[2] = 'Ubuntu-%d.%d.%d' % (dist[4][0], dist[4][1], dist[4][2], ) 


except PlatformIDsFileCheck:
    # not on Ubuntu platform, so scan will fail
    pass    


if dist[5] != 'ubuntu':
    # does not actually match Ubuntu
    dist = ['ubuntu', '0.0.0', 'Ubuntu-0.0.0', 'Ubuntu', (0, 0, 0,), 'ubuntu']

