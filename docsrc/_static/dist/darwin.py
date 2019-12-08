# -*- coding: utf-8 -*-
"""Darwin / OS-X / macOS - "happy marketing" naming releases - map u' all.
"""
from __future__ import absolute_import

import os
import sys
import re
import platform


from pythonids import PYV35Plus
from platformids import RTE_OSX10, RTE_OSX, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    PlatformIDsFileCheck


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


#
# The values for Darwin OS-X are represented by sub-bitmasks, which map
# a specific release to it's sub releases:
#
#    aaaaaabbb : ...aaaaaaaa:   main releases: 8...
#                bbb:           sub releases:  0-7
#

# *********************************
#
# rebased to RTE_OSX10, because any modern OS-X fom 2001 on is of version 10, 
# or to say - is OS-X - see documentation
#
# *********************************

# # context: RTE_POSIX.RTE_DARWIN
# RTE_OSX      = RTE_DARWIN   + 0x00020000    #: Mac OS-X RTE_OSX is basically the short form of RTE_OSX10
# RTE_OSX10    = RTE_DARWIN   + 0x00040000    #: Mac OS-X v10.x, as Posix system [POSIX]_, no macpath-legacy.
                                             

# Leopard - 2007
RTE_OSX105 = RTE_OSX10      +   0x000028a0  #: Leopard      - OSX-10.5.0 - DARWIN-9.0
RTE_OSX1050 = RTE_OSX105    +   0x000028a0  #: Leopard      - OSX-10.5.0 - DARWIN-9.0
RTE_OSX1058 = RTE_OSX105    +   0x000028a8  #: Leopard      - OSX-10.5.8 - DARWIN-9.8

# SnowLeopard - 2009
RTE_OSX106 = RTE_OSX10      +   0x000028c0  #: SnowLeopard  - OSX-10.6.0 - DARWIN-10.0
RTE_OSX1060 = RTE_OSX106    +   0x000028c6  #: SnowLeopard  - OSX-10.6.0 - DARWIN-10.0
RTE_OSX1068 = RTE_OSX106    +   0x000028c8  #: SnowLeopard  - OSX-10.6.8 - DARWIN-10.8

# Lion - 2011
RTE_OSX107 = RTE_OSX10      +   0x000028e0  #: Lion         - OSX-10.7.0 - DARWIN-11.0.0
RTE_OSX1070 = RTE_OSX107    +   0x000028e0  #: Lion         - OSX-10.7.0 - DARWIN-11.0.0
RTE_OSX1075 = RTE_OSX107    +   0x000028e2  #: Lion         - OSX-10.7.5 - DARWIN-11.4.2

# MountainLion - 2012
RTE_OSX108 = RTE_OSX10      +   0x00002900  #: MountainLion - OSX-10.8.0 - DARWIN-12.0.0
RTE_OSX1080 = RTE_OSX108    +   0x00002900  #: MountainLion - OSX-10.8.0 - DARWIN-12.0.0
RTE_OSX1085 = RTE_OSX108    +   0x00002905  #: MountainLion - OSX-10.8.5 - DARWIN-12.6.0

# Mavericks - 2013
RTE_OSX109 = RTE_OSX10      +   0x00002920  #: Mavericks    - OSX-10.9.0 - DARWIN-13.0.0
RTE_OSX1090 = RTE_OSX109    +   0x00002920  #: Mavericks    - OSX-10.9.0 - DARWIN-13.0.0
RTE_OSX1095 = RTE_OSX109    +   0x00002925  #: Mavericks    - OSX-10.9.5 - DARWIN-13.4.0

# Yosemite - 2014
RTE_OSX1010 = RTE_OSX10     +   0x00002940  #: Yosemite     - OSX-10.10.0 - DARWIN-14.0.0
RTE_OSX10100 = RTE_OSX1010  +   0x00002940  #: Yosemite     - OSX-10.10.0 - DARWIN-14.0.0
RTE_OSX10105 = RTE_OSX1010  +   0x00002945  #: Yosemite     - OSX-10.10.5 - DARWIN-14.5.0

# ElCapitan - 2015
RTE_OSX1011 = RTE_OSX10     +   0x00002960  #: ElCapitan    - OSX-10.11.0 - DARWIN-15.0.0
RTE_OSX10110 = RTE_OSX1011  +   0x00002960  #: ElCapitan    - OSX-10.11.0 - DARWIN-15.0.0
RTE_OSX10116 = RTE_OSX1011  +   0x00002966  #: ElCapitan    - OSX-10.11.6 - DARWIN-15.6.0

# Sierra - 2016
RTE_OSX1012 = RTE_OSX10     +   0x00002980  #: Sierra       - OSX-10.12.0 - DARWIN-16.0.0
RTE_OSX10124 = RTE_OSX1012  +   0x00002984  #: Sierra       - OSX-10.12.4 - DARWIN-16.5.0
RTE_OSX10126 = RTE_OSX1012  +   0x00002986  #: Sierra       - OSX-10.12.6 - DARWIN-16.6.0

# HighSierra - 2017
RTE_OSX1013 = RTE_OSX10     +   0x000029a0  #: HighSierra   - OSX-10.13.0 - DARWIN-17.0.0
RTE_OSX10130 = RTE_OSX1013  +   0x000029a0  #: HighSierra   - OSX-10.13.0 - DARWIN-17.5.0
RTE_OSX10131 = RTE_OSX1013  +   0x000029a1  #: HighSierra   - OSX-10.13.1 - DARWIN-17.5.0
RTE_OSX10132 = RTE_OSX1013  +   0x000029a2  #: HighSierra   - OSX-10.13.2 - DARWIN-17.5.0
RTE_OSX10133 = RTE_OSX1013  +   0x000029a3  #: HighSierra   - OSX-10.13.3 - DARWIN-17.5.0
RTE_OSX10134 = RTE_OSX1013  +   0x000029a4  #: HighSierra   - OSX-10.13.4 - DARWIN-17.5.0
RTE_OSX10135 = RTE_OSX1013  +   0x000029a5  #: HighSierra   - OSX-10.13.5 - DARWIN-17.6.0
RTE_OSX10136 = RTE_OSX1013  +   0x000029a6  #: HighSierra   - OSX-10.13.6 - DARWIN-17.6.0

# Mojave - 2018
RTE_OSX1014 = RTE_OSX10     +   0x000029c0  #: Mojave       - OSX-10.14.0 - DARWIN-18.0.0
RTE_OSX10140 = RTE_OSX1014  +   0x000029c0  #: Mojave       - OSX-10.14.0 - DARWIN-18.0.0
RTE_OSX10141 = RTE_OSX1014  +   0x000029c1  #: Mojave       - OSX-10.14.1 - DARWIN-18.0.0


#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'osx':           RTE_OSX,
        'osx105':        RTE_OSX105,
        'osx106':        RTE_OSX106,
        'osx1060':       RTE_OSX1060,
        'osx10105':      RTE_OSX10105,
        'osx1068':       RTE_OSX1068,
        'osx107':        RTE_OSX107,
        'osx108':        RTE_OSX108,
        'osx1080':       RTE_OSX1080,
        'osx1085':       RTE_OSX1085,
        'osx109':        RTE_OSX109,
        'osx1010':       RTE_OSX1010,
        'osx1011':       RTE_OSX1011,
        'osx1012':       RTE_OSX1012,
        'osx1013':       RTE_OSX1013,
        'osx1014':       RTE_OSX1014,
        'ElCapitan':     RTE_OSX1011,
        'HighSierra':    RTE_OSX1013,
        'Leopard':       RTE_OSX105,
        'Lion':          RTE_OSX107,
        'Mavericks':     RTE_OSX109,
        'Mojave':        RTE_OSX1014,
        'MountainLion':  RTE_OSX108,
        'Sierra':        RTE_OSX1012,
        'SnowLeopard':   RTE_OSX106,
        'Yosemite':      RTE_OSX1010,



        RTE_OSX: RTE_OSX,
        RTE_OSX105: RTE_OSX105,
        RTE_OSX106: RTE_OSX106,
        RTE_OSX1060: RTE_OSX1060,
        RTE_OSX10105: RTE_OSX10105,
        RTE_OSX1068: RTE_OSX1068,
        RTE_OSX107: RTE_OSX107,
        RTE_OSX108: RTE_OSX108,
        RTE_OSX1080: RTE_OSX1080,
        RTE_OSX1085: RTE_OSX1085,
        RTE_OSX109: RTE_OSX109,
        RTE_OSX1010: RTE_OSX1010,
        RTE_OSX1011: RTE_OSX1011,
        RTE_OSX1012: RTE_OSX1012,
        RTE_OSX1013: RTE_OSX1013,
        RTE_OSX1014: RTE_OSX1014,
        RTE_OSX1011: RTE_OSX1011,
        RTE_OSX1013: RTE_OSX1013,
        RTE_OSX105: RTE_OSX105,
        RTE_OSX107: RTE_OSX107,
        RTE_OSX109: RTE_OSX109,
        RTE_OSX1014: RTE_OSX1014,
        RTE_OSX108: RTE_OSX108,
        RTE_OSX1012: RTE_OSX1012,
        RTE_OSX106: RTE_OSX106,
        RTE_OSX1010: RTE_OSX1010,
        
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_OSX:      'osx',
        RTE_OSX1050:  'osx1050',            #: Leopard      - OSX-10.5.0  - DARWIN-9.0
        RTE_OSX1058:  'osx1058',            #: Leopard      - OSX-10.5.8  - DARWIN-9.8
        RTE_OSX106:   'osx106',             #: SnowLeopard  - OSX-10.6    - DARWIN-10
        RTE_OSX1060:  'osx1060',            #: SnowLeopard  - OSX-10.6.0  - DARWIN-10.0
        RTE_OSX1068:  'osx1068',            #: SnowLeopard  - OSX-10.6.8  - DARWIN-10.8
        RTE_OSX1070:  'osx1070',            #: Lion         - OSX-10.7.0  - DARWIN-11.0.0
        RTE_OSX1075:  'osx1075',            #: Lion         - OSX-10.7.5  - DARWIN-11.4.2
        RTE_OSX108:   'osx108',             #: MountainLion - OSX-10.8    - DARWIN-12
        RTE_OSX1080:  'osx1080',            #: MountainLion - OSX-10.8.0  - DARWIN-12.0.0
        RTE_OSX1085:  'osx1085',            #: MountainLion - OSX-10.8.5  - DARWIN-12.6.0
        RTE_OSX1090:  'osx1090',            #: Mavericks    - OSX-10.9.0  - DARWIN-13.0.0
        RTE_OSX1095:  'osx1095',            #: Mavericks    - OSX-10.9.5  - DARWIN-13.4.0
        RTE_OSX10100: 'osx10100',           #: Yosemite     - OSX-10.10.0 - DARWIN-14.0.0
        RTE_OSX10105: 'osx10105',           #: Yosemite     - OSX-10.10.5 - DARWIN-14.5.0
        RTE_OSX10110: 'osx10110',           #: ElCapitan    - OSX-10.11.0 - DARWIN-15.0.0
        RTE_OSX10116: 'osx10116',           #: ElCapitan    - OSX-10.11.6 - DARWIN-15.6.0
        RTE_OSX10124: 'osx10124',           #: Sierra       - OSX-10.12.4 - DARWIN-16.5.0
        RTE_OSX10126: 'osx10126',           #: Sierra       - OSX-10.12.6 - DARWIN-16.6.0
        RTE_OSX10130: 'osx10130',           #: HighSierra   - OSX-10.13.0 - DARWIN-17.0.0
        RTE_OSX10134: 'osx10134',           #: HighSierra   - OSX-10.13.4 - DARWIN-17.5.0
        RTE_OSX10135: 'osx10135',           #: HighSierra   - OSX-10.13.5 - DARWIN-17.6.0
        RTE_OSX10136: 'osx10136',           #: HighSierra   - OSX-10.13.6 - DARWIN-17.6.0
        RTE_OSX10140: 'osx10140',           #: Mojave       - OSX-10.14.0 - DARWIN-18.0.0
        RTE_OSX10140: 'osx10141',           #: Mojave       - OSX-10.14.1 - DARWIN-18.0.0
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_OSX:      'OS-X',
        RTE_OSX105:   'Leopard',
        RTE_OSX1058:  'Leopard',
        RTE_OSX106:   'SnowLeopard',
        RTE_OSX1060:  'SnowLeopard',
        RTE_OSX1068:  'SnowLeopard',
        RTE_OSX107:   'Lion',
        RTE_OSX1070:  'Lion',
        RTE_OSX1075:  'Lion',
        RTE_OSX108:   'MountainLion',
        RTE_OSX1080:  'MountainLion',
        RTE_OSX1085:  'MountainLion',
        RTE_OSX109:   'Mavericks',
        RTE_OSX1090:  'Mavericks',
        RTE_OSX1095:  'Mavericks',
        RTE_OSX1010:  'Yosemite',
        RTE_OSX10100: 'Yosemite',
        RTE_OSX10105: 'Yosemite',
        RTE_OSX1011:  'ElCapitan',
        RTE_OSX10110: 'ElCapitan',
        RTE_OSX10116: 'ElCapitan',
        RTE_OSX1012:  'Sierra',
        RTE_OSX10124: 'Sierra',
        RTE_OSX10126: 'Sierra',
        RTE_OSX1013:  'HighSierra',
        RTE_OSX10130: 'HighSierra',
        RTE_OSX10134: 'HighSierra',
        RTE_OSX10136: 'HighSierra',
        RTE_OSX1014:  'Mojave',
        RTE_OSX10140: 'Mojave',
    }
)

#: official version strings
versions = {
    RTE_OSX1050:  '10.5.0',            #: Leopard      - OSX-10.5.0  - DARWIN-9.0
    RTE_OSX1058:  '10.5.8',            #: Leopard      - OSX-10.5.8  - DARWIN-9.8
    RTE_OSX1060:  '10.6.0',            #: SnowLeopard  - OSX-10.6.0  - DARWIN-10.0
    RTE_OSX1068:  '10.6.8',            #: SnowLeopard  - OSX-10.6.8  - DARWIN-10.8
    RTE_OSX1070:  '10.7.0',            #: Lion         - OSX-10.7.0  - DARWIN-11.0.0
    RTE_OSX1075:  '10.7.5',            #: Lion         - OSX-10.7.5  - DARWIN-11.4.2
    RTE_OSX1080:  '10.8.0',            #: MountainLion - OSX-10.8.0  - DARWIN-12.0.0
    RTE_OSX1085:  '10.8.5',            #: MountainLion - OSX-10.8.5  - DARWIN-12.6.0
    RTE_OSX1090:  '10.9.0',            #: Mavericks    - OSX-10.9.0  - DARWIN-13.0.0
    RTE_OSX1095:  '10.9.5',            #: Mavericks    - OSX-10.9.5  - DARWIN-13.4.0
    RTE_OSX10100: '10.10.0',           #: Yosemite     - OSX-10.10.0 - DARWIN-14.0.0
    RTE_OSX10105: '10.10.5',           #: Yosemite     - OSX-10.10.5 - DARWIN-14.5.0
    RTE_OSX10110: '10.11.0',           #: ElCapitan    - OSX-10.11.0 - DARWIN-15.0.0
    RTE_OSX10116: '10.11.6',           #: ElCapitan    - OSX-10.11.6 - DARWIN-15.6.0
    RTE_OSX10124: '10.12.4',           #: Sierra       - OSX-10.12.4 - DARWIN-16.5.0
    RTE_OSX10126: '10.12.6',           #: Sierra       - OSX-10.12.6 - DARWIN-16.6.0
    RTE_OSX10130: '10.13.0',           #: HighSierra   - OSX-10.13.0 - DARWIN-17.0.0
    RTE_OSX10134: '10.13.4',           #: HighSierra   - OSX-10.13.4 - DARWIN-17.5.0
    RTE_OSX10135: '10.13.5',           #: HighSierra   - OSX-10.13.5 - DARWIN-17.6.0
    RTE_OSX10136: '10.13.6',           #: HighSierra   - OSX-10.13.6 - DARWIN-17.6.0
    RTE_OSX10140: '10.14.0',           #: Mojave       - OSX-10.14.0 - DARWIN-18.0.0
    RTE_OSX10140: '10.14.1',           #: Mojave       - OSX-10.14.1 - DARWIN-18.0.0
}



dist = ['', '', 'OS-X-', 'OS-X', '', '']

try:
    
    if sys.platform.startswith('darwin'):
        # OS-X - CPython, PyPy, IPython
        dist[1] = platform.release()
        dist[5] = 'osx'
    
    elif os.path.exists('/System/Library/Components/AppleScript.component'):
        # OS-X - match on Jython
        x = os.popen("sysctl kern.ostype kern.osrelease", mode='r')
        if x.readline().endswith("Darwin\n")       :
            dist[1] = re.sub(r'[^=]*=([0-9.]*).*$', r'\1', x.readline())
            dist[5] = 'osx'
        x.close()
    
    if dist[5] == 'osx':
        dist[4] = decode_version_str_to_segments(dist[1])
        dist[0] = 'osx%d%d%d' % (dist[4][0], dist[4][1], dist[4][2])
        dist[2] += str(dist[1])


except PlatformIDsFileCheck:
    # not on OS-X platform, so scan will fail
    pass    


if dist[5] != 'osx':
    # does not actually match OS-X 
    dist = ['osx', '0.0.0', 'OS-X-0.0.0', 'OS-X', (0, 0, 0,), 'osx']

