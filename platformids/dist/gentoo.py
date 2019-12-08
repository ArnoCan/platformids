# -*- coding: utf-8 -*-
"""Gentoo releases.
"""
from __future__ import absolute_import

import os
import time


# from platformids import _debug, _verbose
from pythonids import PYV35Plus
from platformids import RTE, rte2num, num2rte, num2pretty, custom_rte_distrel2tuple, \
    RTE_LINUX, RTE_DISTEXT, \
    RTE_DIST , PlatformIDsUnknownError, PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"



RTE_GENTOO          = RTE_LINUX + RTE_DISTEXT + 0x00030000    #: Gentoo    - rolling dist since 2008
RTE_GENTOO121 =       RTE_GENTOO              + 0x00000001    #: Gentoo-12.1 - April 1, 2012[64] (With an April Fool's joke named "Install Wizard") 
RTE_GENTOO20181202  = RTE_GENTOO              + 0x00000082    #: autobuild Gentoo-2018.12.02 
RTE_GENTOO20181204  = RTE_GENTOO              + 0x00000084    #: autobuild Gentoo-2018.12.04 


    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {

        'gentoo': RTE_GENTOO,
        'gentoo121': RTE_GENTOO121,
        'gentoo20181202': RTE_GENTOO20181202,
        'gentoo20181204': RTE_GENTOO20181204,
        RTE_GENTOO121: RTE_GENTOO121,
        RTE_GENTOO20181202: RTE_GENTOO20181202,
        RTE_GENTOO20181204: RTE_GENTOO20181204,
        RTE_GENTOO: RTE_GENTOO,
    }
)

#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_GENTOO: 'gentoo',
        RTE_GENTOO121: 'gentoo121',
        RTE_GENTOO20181202: 'gentoo20181202',
        RTE_GENTOO20181204: 'gentoo20181204',
    }
)


#: mapping of the rte numeric representation to the pretty string value
num2pretty.update(
    {
        RTE_GENTOO: 'Gentoo',
    }
)




dist = ['', '', '', 'GentooLinux', '', 'gentoo']

try:

    if os.path.exists("/etc/gentoo-release"):
        __s = os.stat('/va/cache/edb/mtimedb')
        __t = time.gmtime(__s.st_mtime)
        dist[4] = (__t.tm_year, __t.tm_mon, __t.tm_mday)
        dist[1] = '%d%02d%02d' % (__t.tm_year, __t.tm_mon, __t.tm_mday)
        dist[0] =  'gentoo%d%d%d' % (__t.tm_year, __t.tm_mon, __t.tm_mday)
        dist[2] = 'GentooLinux-' + str(dist[1])  


except PlatformIDsFileCheck:
    # not on OpenWRT platform, so scan will fail
    pass    


if dist[5] != 'gentoo':
    # does not actually match pfSense
    dist = ['gentoo', '0.0.0', 'GentooLinux-0.0.0', 'GentooLinux', (0, 0, 0,), 'gentoo']


def my_distrel2tuple(rte=RTE):
    """Callback for special version layout of Armbian, see manuals. 
    
    A callback to be used by the function:
    
       platformids.decode_rte_distrel_to_segments(rte=RTE)
    
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
         =>  (2018, 0, 0)  # on GENTOO-2018.0
         =>  (2019, 0, 0)  # on GENTOO-2019.0

    """
    if rte & RTE_DIST != RTE_GENTOO:
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
        (_rte & 0xfe00) >> 9 + 1970, 
        (_rte & 0x01e0) >> 5, 
        _rte & 0x001f, 
        )


#: registered callbacks for special handling of custom layout
custom_rte_distrel2tuple.update(
    {
        RTE_GENTOO: my_distrel2tuple,  #: the callback to be registered
    }
)



