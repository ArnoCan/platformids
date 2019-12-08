# -*- coding: utf-8 -*-
"""AIX releases - current for internal study only based on an outdated system on the x86 platform.

Uses standard numbering scheme, thus requires new enum definitions only. 
"""
from __future__ import absolute_import

from platformids import rte2num, num2rte, num2pretty, custom_dist, \
    RTE_UNIX

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_AIX       =  RTE_UNIX      + custom_dist.add_enum()   #: UNIX/Solaris, as Posix system [POSIX]_.

RTE_AIX13PS2  =  RTE_AIX       + 0x00000460  #: AIX-1.3 / PS/2 
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'aix': RTE_AIX,
        'aix13': RTE_AIX13PS2,
        RTE_AIX: RTE_AIX,
        RTE_AIX13PS2: RTE_AIX13PS2,
   }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_AIX: 'aix',
        RTE_AIX13PS2: 'aix13',
    }
)

#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_AIX: 'AIX',
        RTE_AIX13PS2: 'AIX-1.3 PS/2',
    }
)

