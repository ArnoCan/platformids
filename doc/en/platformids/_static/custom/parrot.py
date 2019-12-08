# -*- coding: utf-8 -*-
"""Example for a dynamic added custom platform.

Here *Parrot* Linux, which actually has a default 
release version layout, and though could be handled 
by the default handler.

"""
from __future__ import absolute_import

from platformids import RTE, rte2num, num2rte, num2pretty, custom_rte_distrel2tuple, custom_dist, \
    PlatformIDsUnknownError, \
    RTE_LINUX, RTE_OSTYPE, RTE_DIST


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

RTE_PARROT        = RTE_LINUX   + custom_dist.add_enum()     #: Parrot

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'parrot':        RTE_PARROT,
        RTE_PARROT:      RTE_PARROT,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_PARROT:          'parrot',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_PARROT:          'Parrot',
    }
)


#-----------------------------------------------#
#                                               #
# optional constants for convenience            #
#                                               #
#-----------------------------------------------#


RTE_PARROT451     = RTE_PARROT  + 0x000010a1                              #: Parrot-4.5.1

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'parrot451':     RTE_PARROT451,
        RTE_PARROT451:   RTE_PARROT451,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_PARROT451:       'parrot451',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_PARROT451:       'Parrot-4.5.1',
    }
)

def my_distrel2tuple(rte=RTE):
    """
    A custom example only - standard encoding is default layout.

    Convert the *Parrot* specific *distrel* version layout
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
        =>  (4, 1, 0)     # on Parrot-4.1
        =>  (4, 5, 1)     # on Parrot-4.5.1

    """
    if rte & RTE_OSTYPE != RTE_LINUX:
        raise PlatformIDsUnknownError("Not Linux:  rte = " + str(rte))
        
    if rte & RTE_DIST != RTE_PARROT:
        raise PlatformIDsUnknownError("Not Parrot: rte = " + str(rte))
    
    try:
        _rte = rte2num[rte]
    except KeyError:
        # non-registered release
        
        if type(_rte) is int:
            # can split basically any number, let's see...
            _rte = rte

        else:
            raise PlatformIDsUnknownError("Unknown Parrot release rte = " + str(rte))

    # here same as the default handler
    return (
        (_rte & 0xfc00) >> 10, 
        (_rte & 0x03e0) >> 5, 
        _rte & 0x001f, 
        )


#: registered callbacks for special handling of custom layout
custom_rte_distrel2tuple.update(
    {
        # e.g. RTE_PARROT: parrot.platformids.my_distrel2tuple,
        
        RTE_PARROT: my_distrel2tuple,  #: the callback to be registered
    }
)
