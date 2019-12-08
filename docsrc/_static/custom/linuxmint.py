# -*- coding: utf-8 -*-
"""*LinuxMint*, which actually has a default 
release version layout, and though could be handled 
by the default handler.

"""
from __future__ import absolute_import

from platformids import rte2num, num2rte, num2pretty, custom_dist, \
    RTE_LINUX


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

RTE_LINUXMINT       = RTE_LINUX   + custom_dist.add_enum()     #: LinuxMint
RTE_LINUXMINT191    = RTE_LINUXMINT    + 0x00001480            #: LinuxMint-19.1

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'linuxmint':        RTE_LINUXMINT,
        RTE_LINUXMINT:      RTE_LINUXMINT,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_LINUXMINT:          'linuxmint',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_LINUXMINT:          'LinuxMint',
    }
)
