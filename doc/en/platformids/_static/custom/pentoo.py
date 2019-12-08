# -*- coding: utf-8 -*-
"""Example for a dynamic added custom platform.

Here *Pentoo* Linux, which has the same encoding as *Gentoo*.

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


RTE_PENTOO           = RTE_LINUX   + custom_dist.add_enum()     #: PENTOO

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'pentoo':               RTE_PENTOO,
        RTE_PENTOO:             RTE_PENTOO,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_PENTOO:             'pentoo',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_PENTOO:             'Pentoo',
    }
)


#-----------------------------------------------#
#                                               #
# optional constants for convenience            #
#                                               #
#-----------------------------------------------#


RTE_PENTOO20180      = RTE_PENTOO  + 0x00006000                              #: PENTOO-2018.0 - offset 1970.1.1
RTE_PENTOO20190      = RTE_PENTOO  + 0x00006200                              #: PENTOO-2019.0 - offset 1970.1.1

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'pentoo20180':          RTE_PENTOO20180,
        'pentoo20190':          RTE_PENTOO20190,
        RTE_PENTOO20180:        RTE_PENTOO20180,
        RTE_PENTOO20190:        RTE_PENTOO20190,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_PENTOO20180:        'pentoo20180',
        RTE_PENTOO20190:        'pentoo20190',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_PENTOO20180:        'Pentoo-2018.0',
        RTE_PENTOO20190:        'Pentoo-2019.0',
    }
)



def my_distrel2tuple(rte=RTE):
    """
    A custom example only.
    
    Requires the same encoding as Gentoo - so currently some
    work to do in order to detect the version of the versionless...

    Convert the *Pentoo* specific *distrel* version layout
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
        =>  (2018, 0, 0)  # on PENTOO-2018.0
        =>  (2019, 0, 0)  # on PENTOO-2019.0

    """
    if rte & RTE_DIST != RTE_PENTOO:
        raise PlatformIDsUnknownError("Not Gentoo:  rte = " + str(rte))
        
    try:
        # handle string input
        _rte = rte2num[rte]
    except KeyError:
        # non-registered release
        
        if type(rte) is int:
            # can split basically any number, let's see...
            _rte = rte

        else:
            raise PlatformIDsUnknownError("Unknown Gentoo release rte = " + str(rte))

    # represents the ArchLinux layout for rolling distro
    return (
        ((_rte & 0xfe00) >> 9) + 1970, 
        ((_rte & 0x01e0) >> 5), 
        _rte & 0x001f, 
        )

#: registered callbacks for special handling of custom layout
custom_rte_distrel2tuple.update(
    {
        # e.g. RTE_PENTOO: PENTOO.platformids.my_distrel2tuple,
        
        RTE_PENTOO: my_distrel2tuple,  #: the callback to be registered
    }
)
