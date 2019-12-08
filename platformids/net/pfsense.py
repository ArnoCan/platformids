# -*- coding: utf-8 -*-
"""pfSense releases.
"""
from __future__ import absolute_import

import re

from pythonids import PYV35Plus
from platformids import rte2num, num2rte, num2pretty, custom_dist, \
    decode_version_str_to_segments, RTE_BSD, PlatformIDsFileCheck

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.2'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_PFSENSE      = RTE_BSD   + custom_dist.add_enum()   #: Registration of the *dist* value
RTE_PFSENSE244   = RTE_PFSENSE            + 0x00006181  #: pfSense-2.4.4 
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'pfsense':   RTE_PFSENSE,
        RTE_PFSENSE: RTE_PFSENSE,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_PFSENSE: 'pfsense',
   }
)


#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_PFSENSE: 'pfsense',
   }
)


dist = ['', '', '', 'pfSense', '', '']

try:
    # same as defaults:
    with open("/etc/platform", 'r') as f:
        for l in f:  # one entry only
            dist[2] = dist[3] = l
            dist[5] = l.lower()
    
    if dist[5] == 'pfsense':
        with open("/etc/version", 'r') as f:
            for l in f:  # one entry only
                dist[1] = re.sub(r'^\([0-9.]+).*', r'\1', l)
                dist[2] += 'pfSense-' + dist[1]
                dist[4] = decode_version_str_to_segments(dist[1])
                dist[0] = 'pfsense%d%d%d' % (dist[4][0], dist[4][1], dist[4][2], ) 

except PlatformIDsFileCheck:
    # not on pfSense platform, so scan will fail
    pass    

if dist[5] != 'pfsense':
    # does not actually match pfSense
    dist = ['pfsense', '0.0.0', 'pfSense-0.0.0', 'pfSense', (0, 0, 0,), 'pfsense']

