# -*- coding: utf-8 -*-
"""Fedora releases.

See Fedora - Release Name process ended [FEDORARELNAMES]_.

"""
from __future__ import absolute_import

import re


from pythonids import PYV35Plus
from platformids import RTE_FEDORA, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_FEDORA19 = RTE_FEDORA       + 0x00004c00  #: Fedora-19
RTE_FEDORA20 = RTE_FEDORA       + 0x00005000  #: Fedora-20
RTE_FEDORA21 = RTE_FEDORA       + 0x00005400  #: Fedora-21
RTE_FEDORA25 = RTE_FEDORA       + 0x00064000  #: Fedora-25
                                        
RTE_FEDORA27 = RTE_FEDORA       + 0x00006c00  #: Fedora-27 - Everything
RTE_FEDORA28 = RTE_FEDORA       + 0x00007000  #: Fedora-28 - Everything
RTE_FEDORA29 = RTE_FEDORA       + 0x00007400  #: Fedora-29 - Everything
RTE_FEDORA30 = RTE_FEDORA       + 0x00007800  #: Fedora-30 - Everything
RTE_FEDORA31 = RTE_FEDORA       + 0x00007e00  #: Fedora-31 - Everything
RTE_FEDORA32 = RTE_FEDORA       + 0x00008000  #: Fedora-32 - Everything
RTE_FEDORA33 = RTE_FEDORA       + 0x00008400  #: Fedora-33 - Everything


#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        "Schroedinger's Cat": RTE_FEDORA19,  # avoid UTF as mandatory: "Schrödinger's Cat"
        'Heisenbug':       RTE_FEDORA20,
        'fedora27':       RTE_FEDORA27,
        'fedora28':       RTE_FEDORA28,
        'fedora29':       RTE_FEDORA29,
        'fedora30':       RTE_FEDORA30,
        'fedora31':       RTE_FEDORA31,
        'fedora32':       RTE_FEDORA32,
        'fedora33':       RTE_FEDORA33,
        RTE_FEDORA19:     RTE_FEDORA19,
        RTE_FEDORA20:     RTE_FEDORA20,
        RTE_FEDORA21:     RTE_FEDORA21,
        RTE_FEDORA25:     RTE_FEDORA25,
        RTE_FEDORA27:     RTE_FEDORA27,
        RTE_FEDORA28:     RTE_FEDORA28,
        RTE_FEDORA29:     RTE_FEDORA29,
        RTE_FEDORA30:     RTE_FEDORA30,
        RTE_FEDORA31:     RTE_FEDORA31,
        RTE_FEDORA32:     RTE_FEDORA32,
        RTE_FEDORA33:     RTE_FEDORA33,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update({
        RTE_FEDORA19:     'fedora19',
        RTE_FEDORA20:     'fedora20',
        RTE_FEDORA27:     'fedora27',
        RTE_FEDORA28:     'fedora28',
        RTE_FEDORA29:     'fedora29',
        RTE_FEDORA30:     'fedora30',
        RTE_FEDORA31:     'fedora31',
        RTE_FEDORA32:     'fedora32',
        RTE_FEDORA33:     'fedora33',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update({
        RTE_FEDORA:       'Fedora Linux',
        RTE_FEDORA19:     "Schroedinger's Cat",  # avoid UTF as mandatory: "Schrödinger's Cat"
        RTE_FEDORA20:     'Heisenbug',
        RTE_FEDORA27:     'Fedora27',
        RTE_FEDORA28:     'Fedora28',
        RTE_FEDORA29:     'Fedora29',
        RTE_FEDORA30:     'Fedora30',
        RTE_FEDORA31:     'Fedora31',
        RTE_FEDORA32:     'Fedora32',
        RTE_FEDORA33:     'Fedora33',
    }
)



dist = ['', '', 'Fedora-', 'Fedora', '', '']

try:
    with open("/etc/redhat-release", 'r') as f:
        for l in f:
            _d = re.split(r'(?s)^([^0-9]*) release *([0-9.]*[^ ]*) [^(]*[(]([^)]*)[)][\n\t ]*$', l)

    if _d[1] == 'Fedora':
        dist[0] = 'fedora' + _d[2]
        dist[4] = decode_version_str_to_segments(_d[2])
        dist[1] = _d[2]
        dist[3] = 'Fedora'
        dist[5] = 'fedora'

        if dist[4][0] > 21:
            dist[2] = "Fedora-%d" % (dist[4][0])
        else:
            dist[2] = _d[1]    


except PlatformIDsFileCheck:
    # not on Fedora platform, so scan will fail
    pass    


if dist[5] != 'fedora':
    # does not actually match Fedora
    dist = ['fedora', '0.0.0', 'Fedora-0.0.0', 'Fedora00', (0, 0, 0,), 'fedora']

