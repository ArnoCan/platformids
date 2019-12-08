# -*- coding: utf-8 -*-
"""Kali Linux releases.
"""
from __future__ import absolute_import

import re

from pythonids import PYV35Plus
from platformids import RTE_KALI, rte2num, num2rte, num2pretty, decode_version_str_to_segments, \
    DSKORG_ID, DSKORG_VERSION, PlatformIDsFileCheck



__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"


#
# Releases:
#
#   Rolling Releases - weekly build with week of the year:
#
#     Kali 2019-W11 – 11th March, 2019 – The First weekly release
# 
#   Rolling Releases with arbitrary increments:
#
#     Kali 2019.1 – 18th February, 2019 – The First 2019 Kali Rolling release. Kernel 4.19.13, GNOME 3.30.2
# 
#     Kali 2018.4 – 29th October, 2018 – The Fourth 2018 Kali Rolling release. Kernel 4.18.0, GNOME 3.30.1
#     Kali 2018.3 – 27th August, 2018 – The Third 2018 Kali Rolling release. Kernel 4.17.0, GNOME 3.28.2
#     Kali 2018.2 – 30th April, 2018 – The Second 2018 Kali Rolling release. Kernel 4.15.0, GNOME 3.28.0
#     Kali 2018.1 – 6th February, 2018 – The first 2018 Kali Rolling release. Kernel 4.14.12, GNOME 3.26.2
#     Kali 2017.3 – 21st November, 2017 – The third 2017 Kali Rolling release. Kernel 4.13, GNOME 3.26
#     Kali 2017.2 – 20th September, 2017 – The second 2017 Kali Rolling release. Kernel 4.12, GNOME 3.25.
#     Kali 2017.1 – 25th April, 2017 – The first 2017 Kali Rolling release. Kernel 4.9, GNOME 3.22.
#     Kali 2016.2 – 31st August, 2016 – The second Kali Rolling release. Kernel 4.6, GNOME 3.20.2.
#     Kali 2016.1 – 21st January, 2016 – The first Kali Rolling release. Kernel 4.3, GNOME 3.18.
#
#   Two-number version releases:
#
#     Kali 2.0 – 11th August, 2015 – Major release, “safi”, now a rolling distribution, major UI changes.
#
#   Three-number version releases:
#
#     Kali 1.1.0a – 13th March, 2015 – No fanfare release fixing kernel ABI inconsistencies in the installers.
#     Kali 1.1.0 – 9th Febuary, 2015 – First dot release in 2 years. New kernel, new tools and updates.
#     Kali 1.0.9a – 6th October, 2014 – Security BugFix release covering shellshock and Debian apt vulnerabilities.
#     Kali 1.0.9 – 25th August, 2014 – BugFix release including installer and a set of tool updates and package fixes.
#     Kali 1.0.8 – 22nd July, 2014 – EFI Support for our “full” ISOs and a set of tool updates and package fixes.
#     Kali 1.0.7 – 27th May, 2014 – Kernel 3.14, tool updates, package fixes, Kali Live Encrypted USB Persistence.
#     Kali 1.0.6 – 9th January, 2014 – Kernel 3.12, cryptsetup nuke option, Amazon AMI, ARM build scripts.
#     Kali 1.0.5 – 5th September, 2013 – BugFix rollup. LVM Encrypted installs, Software Defined Radio (SDR) tools.
#     Kali 1.0.4 – 25th July, 2013 – BugFix rollup. Penetration testing tool additions and updates.
#     Kali 1.0.3 – 26th April, 2013 – BugFix rollup. New accessibility features. Added live Desktop installer.
#     Kali 1.0.2 – 27th March, 2013 – Minor BugFix release and update roll-up.
#     Kali 1.0.1 – 14th March, 2013 – Minor BugFix release (USB Keyboard).
#     Kali 1.0.0 – 13th March, 2013 – Initial release, “moto”.
#



RTE_KALI201911   = RTE_KALI     + 0x00006181  #: KaliLinux-2019-W11 => KaliLinux-2019.03.11 

    
#: mapping of the rte string and numeric representation to the numeric value
rte2num.update(
    {
        'kali201911':    RTE_KALI201911,
    }
)


#: mapping of the rte numeric representation to the string value
num2rte.update(
    {
        RTE_KALI201911: 'kali201911',
    }
)

#: mapping of the rte numeric representation to the string value
num2pretty.update(
    {
        RTE_KALI201911: 'KaliLinux-2019.03.11',
    }
)


dist = ['', '', 'KaliLinux-', 'KaliLinux', '', '']  # defaults

try:
    with open("/etc/os-release", 'r') as f:
        for l in f:
            if l.startswith('ID='):
                dist[0] = dist[5] = DSKORG_ID.sub(r'\1', l)
    
            elif l.startswith('VERSION='):  # priority though more widespread
                dist[1] = DSKORG_VERSION.sub(r'\1', l)
                dist[3] += dist[1]
                dist[0] += re.sub(r'[^0-9]', '', dist[1])
            
    dist[4] = decode_version_str_to_segments(dist[1])


except PlatformIDsFileCheck:
    # not on KaliLinux platform, so scan will fail
    pass    

if dist[5] != 'kali':
    # does not catually match KaliLinux
    dist = ['kali', '0.0.0', 'KaliLinux-0.0.0', 'KaliLinux', (0, 0, 0,), 'kali']


