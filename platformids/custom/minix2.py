# -*- coding: utf-8 -*-
"""Example for a dynamic added custom platform.

Here Minix2 as a new distribution is added.

"""
from __future__ import absolute_import

from platformids import RTE, rte2num, num2rte, num2pretty, custom_rte_distrel2tuple, custom_dist, \
    PlatformIDsUnknownError, \
    RTE_OSTYPE, RTE_DIST

from platformids.custom.minix import RTE_MINIX


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

RTE_MINIX2        = RTE_MINIX   + custom_dist.add_enum()   #: Minix2 as distrel

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'minix2':        RTE_MINIX2,   # dist
        RTE_MINIX2:      RTE_MINIX2,   # dist
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_MINIX2:    'minix2',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_MINIX2:    'Minix2',
    }
)


#-----------------------------------------------#
#                                               #
# optional constants for convenience            #
#                                               #
#-----------------------------------------------#


RTE_MINIX200      = RTE_MINIX2  + 0x00000400                            #: Minix-2.0.0

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'minix200':      RTE_MINIX200, # distrel
        RTE_MINIX200:    RTE_MINIX200, # distrel
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_MINIX200:  'minix200',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_MINIX200:  'Minix-2.0.0',
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
        =>  (2, 0, 0)     # on Minix-2.0.0

    """
    if rte & RTE_OSTYPE != RTE_MINIX:
        raise PlatformIDsUnknownError("Not Minix:  rte = " + str(rte))
        
    if rte & RTE_DIST != RTE_MINIX2:
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
        
        RTE_MINIX2: my_distrel2tuple,  #: the callback to be registered
    }
)
