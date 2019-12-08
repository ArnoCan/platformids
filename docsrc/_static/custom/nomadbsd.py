# -*- coding: utf-8 -*-
"""NomadBSD releases.

Use standard encoding, thus require enum value registration only.
"""
from __future__ import absolute_import

from platformids import rte2num, num2rte, num2pretty, custom_dist, \
    RTE_BSD

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_NOMADBSD      = RTE_BSD   + custom_dist.add_enum()   #: Registration of the *dist* value
RTE_NOMADBSD12    = RTE_NOMADBSD        + 0x00001480     #: NomadBSD-1.2
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'nomadbsd': RTE_NOMADBSD,
        RTE_NOMADBSD: RTE_NOMADBSD,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_NOMADBSD: 'nomadbsd',
   }
)


#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_NOMADBSD: 'NomadBSD',
   }
)

