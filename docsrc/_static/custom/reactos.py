# -*- coding: utf-8 -*-
"""ReactOS releases, currently experimental for *platformids.RTE* tests.

Uses standard encoding, thus require enum value registration only.
"""
from __future__ import absolute_import

from platformids import rte2num, num2rte, num2pretty, \
    custom_ostype, custom_dist, \
    RTE_WINDOWS


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_REACTOS       = RTE_WINDOWS     + custom_ostype.add_enum()   #: ReactOS as ostype
RTE_REACTOS5_2    = RTE_REACTOS     + custom_dist.add_enum()     #: ReactOS5_2 as dist compatible to NT5_2

#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'reactos': RTE_REACTOS,
        'reactos5_2': RTE_REACTOS5_2,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_REACTOS: 'reactos',
        RTE_REACTOS5_2: 'reactos5_2',
    }
)


#: pretty print for UI display
num2pretty.update(
    {
        RTE_REACTOS: 'ReactOS',
        RTE_REACTOS5_2: 'ReactOS-5.2',
    }
)

#--------------------------------------------------#
#                                                  #
# optional constants for convenience               #
#                                                  #
#--------------------------------------------------#

RTE_REACTOS049    = RTE_REACTOS5_2  +  0x00000089                             #: ReactOS-0.4.9
RTE_REACTOS0410   = RTE_REACTOS5_2  +  0x0000008a                             #: ReactOS-0.4.10
RTE_REACTOS0411   = RTE_REACTOS5_2  +  0x0000008b                             #: ReactOS-0.4.11
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'reactos049': RTE_REACTOS049,
        'reactos0410': RTE_REACTOS0410,
        'reactos0411': RTE_REACTOS0411,
        'reactos5_2': RTE_REACTOS5_2,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_REACTOS049: 'reactos049',
        RTE_REACTOS0410: 'reactos0410',
        RTE_REACTOS0411: 'reactos0411',
        RTE_REACTOS5_2: 'reactos5_2',
    }
)


#: mapping of the pretty print representation
num2pretty.update(
    {
        RTE_REACTOS5_2: 'ReactOS-5.2',
        RTE_REACTOS049: 'ReactOS-0.4.9',
        RTE_REACTOS0410: 'ReactOS-0.4.10',
        RTE_REACTOS0411: 'ReactOS-0.4.11',
    }
)

