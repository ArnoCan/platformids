# -*- coding: utf-8 -*-
"""Slackware releases.

Use standard encoding, thus require enum value registration only.
Here a custom call is presented for demo purposes. 
"""
from __future__ import absolute_import

from platformids import rte2num, num2rte, custom_dist, \
    RTE_LINUX, RTE_OSTYPE, RTE_DIST, \
    RTE, PlatformIDsUnknownError, \
    custom_rte_distrel2tuple
    
__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


RTE_SLACK        = RTE_LINUX   + custom_dist.add_enum()   #: Scientific Linux

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'slackware': RTE_SLACK,
        RTE_SLACK: RTE_SLACK,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_SLACK: 'slackware',
    }
)


#-----------------------------------------------#
#                                               #
# optional constants for convenience            #
#                                               #
#-----------------------------------------------#


RTE_SLACK14  = RTE_SLACK     + 0x00003800  #: Slackware-14
RTE_SLACK140 = RTE_SLACK     + 0x00003800  #: Slackware-14.0
RTE_SLACK141 = RTE_SLACK     + 0x00003820  #: Slackware-14.1
RTE_SLACK142 = RTE_SLACK     + 0x00003840  #: Slackware-14.2
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'slackware14': RTE_SLACK14,
        'slackware140': RTE_SLACK140,
        'slackware141': RTE_SLACK141,
        'slackware142': RTE_SLACK142,
        RTE_SLACK14: RTE_SLACK14,
        RTE_SLACK140: RTE_SLACK140,
        RTE_SLACK141: RTE_SLACK141,
        RTE_SLACK142: RTE_SLACK142,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_SLACK14: 'slackware14',
        RTE_SLACK140: 'slackware140',
        RTE_SLACK141: 'slackware141',
        RTE_SLACK142: 'slackware142',
    }
)

def my_distrel2tuple(rte=RTE):
    """
    A custom example only - standard encoding is default layout.

    Convert the *Slackware* specific *distrel* version layout
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
        =>  (14, 1, 0)  # on Slackware-14.1

    """
    if rte & RTE_OSTYPE != RTE_LINUX:
        raise PlatformIDsUnknownError("Not Linux:  rte = " + str(rte))
        
    if rte & RTE_DIST != RTE_SLACK:
        raise PlatformIDsUnknownError("Not Slackware: rte = " + str(rte))
    
    try:
        _rte = rte2num[rte]
    except KeyError:
        # non-registered release
        
        if type(_rte) is int:
            # can split basically any number, let's see...
            _rte = rte

        else:
            raise PlatformIDsUnknownError("Unknown Slackware release rte = " + str(rte))

    # here same as the default handler
    return (
        (_rte & 0xfc00) >> 10, 
        (_rte & 0x03e0) >> 5, 
        _rte & 0x001f, 
        )


#: registered callbacks for special handling of custom layout
custom_rte_distrel2tuple.update(
    {
        RTE_SLACK: my_distrel2tuple,  #: the callback to be registered
    }
)

