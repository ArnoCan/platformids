# -*- coding: utf-8 -*-
"""RHEL releases.
"""
from __future__ import absolute_import

import re


from pythonids import PYV35Plus
from platformids import RTE_RHEL, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsFileCheck

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_RHEL5   = RTE_RHEL      + 0x00001400  #: RHEL-5
# RTE_RHEL50  = RTE_RHEL      + 0x00001400  #: RHEL-5.0
# RTE_RHEL51  = RTE_RHEL      + 0x00001420  #: RHEL-5.1
# RTE_RHEL52  = RTE_RHEL      + 0x00001440  #: RHEL-5.2
# RTE_RHEL53  = RTE_RHEL      + 0x00001460  #: RHEL-5.3
# RTE_RHEL54  = RTE_RHEL      + 0x00001480  #: RHEL-5.4
# RTE_RHEL55  = RTE_RHEL      + 0x000014a0  #: RHEL-5.5
# RTE_RHEL56  = RTE_RHEL      + 0x000014c0  #: RHEL-5.6
# RTE_RHEL57  = RTE_RHEL      + 0x000014e0  #: RHEL-5.7
# RTE_RHEL58  = RTE_RHEL      + 0x00001500  #: RHEL-5.8
# RTE_RHEL59  = RTE_RHEL      + 0x00001520  #: RHEL-5.9
# RTE_RHEL510 = RTE_RHEL      + 0x00001540  #: RHEL-5.10
# RTE_RHEL511 = RTE_RHEL      + 0x00001560  #: RHEL-5.11

RTE_RHEL6   = RTE_RHEL      + 0x00001800  #: RHEL-6
RTE_RHEL60  = RTE_RHEL      + 0x00001800  #: RHEL-6.0
RTE_RHEL61  = RTE_RHEL      + 0x00001820  #: RHEL-6.1
RTE_RHEL62  = RTE_RHEL      + 0x00001840  #: RHEL-6.2
RTE_RHEL63  = RTE_RHEL      + 0x00001860  #: RHEL-6.3
RTE_RHEL64  = RTE_RHEL      + 0x00001880  #: RHEL-6.4
RTE_RHEL65  = RTE_RHEL      + 0x000018a0  #: RHEL-6.5
RTE_RHEL66  = RTE_RHEL      + 0x000018c0  #: RHEL-6.6
RTE_RHEL67  = RTE_RHEL      + 0x000018e0  #: RHEL-6.7
RTE_RHEL68  = RTE_RHEL      + 0x00001900  #: RHEL-6.8
RTE_RHEL69  = RTE_RHEL      + 0x00001920  #: RHEL-6.9
RTE_RHEL610 = RTE_RHEL      + 0x00001940  #: RHEL-6.10

RTE_RHEL7 = RTE_RHEL        + 0x00001c00  #: RHEL-7
RTE_RHEL70 = RTE_RHEL       + 0x00001c00  #: RHEL-7.0
RTE_RHEL71 = RTE_RHEL       + 0x00001c20  #: RHEL-7.1
RTE_RHEL72 = RTE_RHEL       + 0x00001c40  #: RHEL-7.2
RTE_RHEL73 = RTE_RHEL       + 0x00001c60  #: RHEL-7.3
RTE_RHEL74 = RTE_RHEL       + 0x00001c80  #: RHEL-7.4
RTE_RHEL75 = RTE_RHEL       + 0x00001ca0  #: RHEL-7.5
RTE_RHEL76 = RTE_RHEL       + 0x00001cc0  #: RHEL-7.6
RTE_RHEL77 = RTE_RHEL       + 0x00001ce0  #: RHEL-7.7
RTE_RHEL78 = RTE_RHEL       + 0x00001d00  #: RHEL-7.8
RTE_RHEL79 = RTE_RHEL       + 0x00001d20  #: RHEL-7.9
RTE_RHEL710 = RTE_RHEL      + 0x00001d40  #: RHEL-7.10

RTE_RHEL8 = RTE_RHEL        + 0x00002000  #: RHEL-8
RTE_RHEL80 = RTE_RHEL       + 0x00002000  #: RHEL-8.0
RTE_RHEL81 = RTE_RHEL       + 0x00002020  #: RHEL-8.1
RTE_RHEL82 = RTE_RHEL       + 0x00002040  #: RHEL-8.2
RTE_RHEL83 = RTE_RHEL       + 0x00002060  #: RHEL-8.3
RTE_RHEL84 = RTE_RHEL       + 0x00002080  #: RHEL-8.4
RTE_RHEL85 = RTE_RHEL       + 0x000020a0  #: RHEL-8.5

RTE_RHEL9 = RTE_RHEL       + 0x000002200  #: RHEL-9
RTE_RHEL90 = RTE_RHEL      + 0x000002200  #: RHEL-9.0


#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'Maipo': RTE_RHEL7,
        'Ootpa': RTE_RHEL8,
        'RHEL9': RTE_RHEL9,
        'Santiago': RTE_RHEL6,
        'Tikanga': RTE_RHEL5,
        'rhel5': RTE_RHEL5,
        'rhel6': RTE_RHEL6,
        'rhel7': RTE_RHEL7,
        'rhel8': RTE_RHEL8,
        'rhel9': RTE_RHEL9,
        RTE_RHEL5: RTE_RHEL5,
        RTE_RHEL6: RTE_RHEL6,
        RTE_RHEL7: RTE_RHEL7,
        RTE_RHEL8: RTE_RHEL8,
        RTE_RHEL9: RTE_RHEL9,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_RHEL5: 'rhel5',
        RTE_RHEL6: 'rhel6',
        RTE_RHEL7: 'rhel7',
        RTE_RHEL8: 'rhel8',
        RTE_RHEL9: 'rhel9',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_RHEL5: 'Tikanga',
        RTE_RHEL6: 'Santiago',
        RTE_RHEL7: 'Maipo',
        RTE_RHEL8: 'Ootpa',
        RTE_RHEL9: 'RHEL9',
    }
)


dist = ['', '', '', 'RHEL', '', '']

try:

    with open("/etc/redhat-release", 'r') as f:
        for l in f:
            _d = re.split(r'(?s)^([^0-9]*) release *([0-9.]*[^ ]*) [^(]*[(]([^)]*)[)][\n\t ]*$', l)
    

    if _d[1].startswith('Red Hat'):
        dist[1] = _d[2]
        dist[4] = decode_version_str_to_segments(_d[2])
        dist[0] = 'rhel%d%d' % (dist[4][0], dist[4][1])
        dist[2] = "RHEL-" + _d[2]
        dist[5] = 'rhel'


except PlatformIDsFileCheck:
    # not on RHEL platform, so scan will fail
    pass    


if dist[5] != 'rhel':
    # does not actually match RHEL
    dist = ['rhel', '0.0.0', 'RHEL-0.0.0', 'RHEL', (0, 0, 0,), 'rhel']


