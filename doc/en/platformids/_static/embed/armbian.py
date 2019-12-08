# -*- coding: utf-8 -*-
"""Armbian releases.

The *Armbian* Linux is implemented as a module 
based on custom numbering scheme due to the specific value ranges, 
which are required for this distribution only.

The *Armbian* distribution represents a *shrinked multi-role PC-Platform* as an
embedded system with integrated low-level HW interfaces for a wide range of *ARM*
based boards. 
"""
from __future__ import absolute_import

# from platformids import _debug, _verbose
from pythonids import PYV35Plus
from platformids import RTE, rte2num, num2rte, num2pretty, custom_rte_distrel2tuple, custom_dist, \
    decode_version_str_to_segments, \
    PlatformIDsUnknownError, \
    RTE_LINUX, RTE_DIST, \
    DSKORG_ID, DSKORG_RELEASE, DSKORG_VERSION, PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


#
# *** special modifications ***
#
RTE_ARMBIAN = RTE_LINUX          + custom_dist.add_enum()    #: Armbian - re-grouped version sub-ranges 

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'armbian':   RTE_ARMBIAN,
        RTE_ARMBIAN: RTE_ARMBIAN,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_ARMBIAN:        'armbian',
    }
)

num2pretty.update(
    {
        RTE_ARMBIAN:         'Armbian',
    }
)


#-----------------------------------------------#
#                                               #
# optional constants for convenience            #
#                                               #
#-----------------------------------------------#


RTE_ARMBIAN5 = RTE_ARMBIAN          + 0x00002800 #: ARMBIAN - stretch
RTE_ARMBIAN550 = RTE_ARMBIAN5       + 0x00000190 #: ARMBIAN - stretch

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'armbian5':          RTE_ARMBIAN5,
        'armbian550':        RTE_ARMBIAN550,
        'Armbian-stretch':   RTE_ARMBIAN550,
        RTE_ARMBIAN5:        RTE_ARMBIAN5,
        RTE_ARMBIAN550:      RTE_ARMBIAN550,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_ARMBIAN5:        'armbian5',
        RTE_ARMBIAN550:      'armbian550',
    }
)


num2pretty.update(
    {
        RTE_ARMBIAN5:        'Armbian-stretch',
    }
)



# armbian
dist = ['', '', 'Armbian-', 'Armbian', '', '']

try:

    with open("/etc/os-release", 'r') as f:
        for l in f:
            if l.startswith('ID='):
                # id
                dist[0] = dist[5] = DSKORG_ID.sub(r'\1', l)

            elif l.startswith('VERSION='):
                # actual pretty name
                _pretty = DSKORG_RELEASE.split(l)[2]  # for now a reminder only 

    #
    # scan dist + distrel
    #
    with open("/etc/armbian-release", 'r') as f:
        # has it's own numbering
        for l in f:
            if l.startswith('VERSION='):
                dist[1] = DSKORG_VERSION.sub(r'\1', l)
                dist[4] = decode_version_str_to_segments(dist[1])
                dist[0] += '%d%d' % (dist[4][0], dist[4][1],)
                dist[2] += dist[1]
    

except PlatformIDsFileCheck:
    # not on armbian platform, so scan will fail
    pass


if dist[0] != 'armbian':
    # not actually armbian
    dist = ['armbian', '0.0.0', 'Armbian-0.0.0', 'Armbian', (0, 0, 0,), 'armbian']


def my_distrel2tuple(rte=RTE):
    """Callback for special version layout of Armbian, see manuals. 
    
    A callback to be used by the function:
    
       platformids.decode_rte_distrel_to_segments(rte=RTE)
    
    Decodes the compressed *distrel* from the 32bit integer
    bitmask *rte* into the corresponding tuple of integer
    segments.

   Args:
       **rte**:
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
        =>  (5, 50, 0)    # on Armbian-5.50

    """
    if rte & RTE_DIST != RTE_ARMBIAN:
        raise PlatformIDsUnknownError("Not Armbian:  rte = " + str(rte))
        
    try:
        # handle string input
        _rte = rte2num[rte]
        
    except KeyError:
        # non-registered release
        
        if type(rte) is int:
            # can split basically any number, let's see...
            _rte = rte

        else:
            raise PlatformIDsUnknownError("Unknown Armbian release rte = " + str(rte))

    # represents the Armbian layout
    return (
        (_rte & 0xf800) >> 11, 
        (_rte & 0x07f8) >> 3, 
        _rte & 0x0003, 
        )


#: registered callbacks for special handling of custom layout
custom_rte_distrel2tuple.update(
    {
        RTE_ARMBIAN: my_distrel2tuple,  #: the callback to be registered
    }
)

