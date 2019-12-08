# -*- coding: utf-8 -*-
"""BlackArch Linux releases.

Here *BlackArch* Linux, which has the same encoding as *ArchLinux*.

"""
from __future__ import absolute_import

from platformids import RTE, rte2num, num2rte, num2pretty, custom_rte_distrel2tuple, custom_dist, \
    PlatformIDsUnknownError, \
    RTE_LINUX, RTE_DISTEXT, RTE_OSTYPE, RTE_DIST


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_BLACKARCH        = RTE_LINUX      + custom_dist.add_enum()   #: BlackArch Linux
RTE_BLACKARCH20180   = RTE_BLACKARCH  + 0x00006000                            #: BlackArch-2018.0 - offset 1970.1.1

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'blackarch':               RTE_BLACKARCH,
        'blackarch20180':          RTE_BLACKARCH20180,
        RTE_BLACKARCH:             RTE_BLACKARCH,
        RTE_BLACKARCH20180:        RTE_BLACKARCH20180,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_BLACKARCH:             'blackarch',
        RTE_BLACKARCH20180:        'blackarch20180',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_BLACKARCH:             'BlackArch',
        RTE_BLACKARCH20180:        'BlackArch-2018.0',
    }
)

def my_distrel2tuple(rte=RTE):
    """Callback for special version layout of BlackArch Linux, the
    same as ArchLinux by Rolling-Versioning, see manuals. 
    
    A callback to be used by the function:
    
       platformids.decode_rte_distrel_to_segments(rte=RTE)
    
    Decodes the compressed *distrel* from the 32bit integer
    bitmask *rte* into the corresponding tuple of integer
    segments.

   Args:
       rte:
           The comppressed runtime environment identifier bitmask.
            
           default := RTE

   Returns:
       Tuple of Integer values of the encoded segments, either
       as defined by the default layout, or any known as defined
       by additional extended and/or custom criteria.
    
   Raises:
       pass-through

   Examples:
     ::

        decode_rte_distrel_to_segments()     
        =>  (2019, 4, 1)     # on BlackArch-2019.4.1

    """
    if rte & RTE_DIST != RTE_BLACKARCH:
        raise PlatformIDsUnknownError("Not BlackArch:  rte = " + str(rte))
        
    try:
        # handle string input
        _rte = rte2num[rte]
    except KeyError:
        # non-registered release
        
        if type(rte) is int:
            # can split basically any number, let's see...
            _rte = rte

        else:
            raise PlatformIDsUnknownError("Unknown BlackArch release rte = " + str(rte))

    # represents the ArchLinux layout for rolling distro
    return (
        (_rte & 0xfe00) >> 9 + 1970, 
        (_rte & 0x01e0) >> 5, 
        _rte & 0x001f, 
        )


#: registered callbacks for special handling of custom layout
custom_rte_distrel2tuple.update(
    {
        # e.g. RTE_PENTOO: PENTOO.platformids.my_distrel2tuple,
        
        RTE_BLACKARCH: my_distrel2tuple,  #: the callback to be registered
    }
)
