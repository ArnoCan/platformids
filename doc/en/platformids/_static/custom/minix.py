# -*- coding: utf-8 -*-
"""Example for a dynamic added custom platform.

Here Minix as a new OS type, which actually has a default 
release version layout, and though could be handled by the 
default handler.

"""
from __future__ import absolute_import

from platformids import RTE, rte2num, num2rte, num2pretty, \
    RTE_POSIX, RTE_OSTYPE, RTE_DIST, \
    custom_ostype, custom_dist, custom_rte_distrel2tuple, \
    PlatformIDsUnknownError


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_MINIX         = RTE_POSIX   + custom_ostype.add_enum()     #: Minix as ostype
RTE_MINIX3        = RTE_MINIX   + custom_dist.add_enum()       #: Minix3 as dist

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'minix':         RTE_MINIX,    # ostype
        'minix3':        RTE_MINIX3,   # dist
        RTE_MINIX:       RTE_MINIX,    # ostype
        RTE_MINIX3:      RTE_MINIX3,   # dist
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_MINIX:     'minix',
        RTE_MINIX3:    'minix3',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_MINIX:     'Minix',
        RTE_MINIX3:    'Minix3',
    }
)

#-----------------------------------------------#
#                                               #
# optional constants for convenience            #
#                                               #
#-----------------------------------------------#

RTE_MINIX321      = RTE_MINIX  + 0x00000641                                #: Minix-3.2.1
RTE_MINIX330      = RTE_MINIX  + 0x00000660                                #: Minix-3.3.0

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'minix321':      RTE_MINIX321, # distrel
        'minix330':      RTE_MINIX330, # distrel
        RTE_MINIX321:    RTE_MINIX321, # distrel
        RTE_MINIX330:    RTE_MINIX330, # distrel
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_MINIX321:  'minix321',
        RTE_MINIX330:  'minix330',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_MINIX321:  'Minix-3.2.1',
        RTE_MINIX330:  'Minix-3.3.0',
    }
)

def my_distrel2tuple(rte=RTE):
    """
    A custom example only - standard encoding is default layout.

    Convert the *Minix* specific *distrel* version layout
    to a tuple.
    
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
        =>  (3, 2, 1)     # on Minix-3.2.1
        =>  (3, 3, 0)     # on Minix-3.3.0

    """
    if rte & RTE_OSTYPE != RTE_MINIX:
        raise PlatformIDsUnknownError("Not Minix:  rte = " + str(rte))
        
    if rte & RTE_DIST != RTE_MINIX3:
        raise PlatformIDsUnknownError("Not Minix3: rte = " + str(rte))
    
    try:
        _rte = rte2num[rte]
    except KeyError:
        # non-registered release
        
        if type(_rte) is int:
            # can split basically any number, let's see...
            _rte = rte

        else:
            raise PlatformIDsUnknownError("Unknown Minix3 release rte = " + str(rte))

    # here same as the default handler
    return (
        _rte & 0xfc00, 
        _rte & 0x03e0, 
        _rte & 0x001f, 
        )


#: registered callbacks for special handling of custom layout
custom_rte_distrel2tuple.update(
    {
        # e.g. RTE_MINIX3: parrot.platformids.my_distrel2tuple,
        
        RTE_MINIX3: my_distrel2tuple,  #: the callback to be registered
    }
)
