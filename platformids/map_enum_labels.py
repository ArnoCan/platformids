# -*- coding: utf-8 -*-
"""Mapping of numeric and symbolic enum strings, optional loaded on demand for human display of debug info only.
"""
from __future__ import absolute_import
from sys import version_info, platform

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.28'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


from platformids import *  # @UnusedWildImport

    
#: mapping of the numeric value to it's symbolic representation
num2enumstr = {
        RTE_BSD: "RTE_BSD",
        RTE_CENTOS4: "RTE_CENTOS4",
        RTE_CENTOS5: "RTE_CENTOS5",
        RTE_CENTOS6: "RTE_CENTOS6",
        RTE_CENTOS7: "RTE_CENTOS7",
        RTE_CENTOS: "RTE_CENTOS",
        RTE_CYGWIN: "RTE_CYGWIN",
        RTE_DARWIN: "RTE_DARWIN",
        RTE_DEBIAN6: "RTE_DEBIAN6",
        RTE_DEBIAN7: "RTE_DEBIAN7",
        RTE_DEBIAN8: "RTE_DEBIAN8",
        RTE_DEBIAN9: "RTE_DEBIAN9",
        RTE_DEBIAN: "RTE_DEBIAN",
        RTE_DOS: "RTE_DOS",
        RTE_DRAGONFLYBSD: "RTE_DRAGONFLYBSD",
        RTE_FEDORA19: "RTE_FEDORA19",
        RTE_FEDORA27: "RTE_FEDORA27",
        RTE_FEDORA: "RTE_FEDORA",
        RTE_FREEBSD: "RTE_FREEBSD",
        RTE_LINUX: "RTE_LINUX",
        RTE_NETBSD: "RTE_NETBSD",
        RTE_OPENBSD: "RTE_OPENBSD",
        RTE_OSX: "RTE_OSX",
        RTE_POSIX: "RTE_POSIX",
        RTE_SOLARIS: "RTE_SOLARIS",
        RTE_SUSE: "RTE_SUSE",
        RTE_UBUNTU: "RTE_UBUNTU",
        RTE_WIN10: "RTE_WIN10",
        RTE_WIN2000: "RTE_WIN2000",
        RTE_WIN32: "RTE_WIN32",
        RTE_WIN32: "RTE_WIN32",
        RTE_WIN7: "RTE_WIN7",
        RTE_WINNT4: "RTE_WINNT4",
        RTE_WINNT4S: "RTE_WINNT4S",
        RTE_WINNT4WS: "RTE_WINNT4WS",
        RTE_WINS2000S: "RTE_WINS2000S",
        RTE_WINS2000WS: "RTE_WINS2000WS",
        RTE_WINS2008: "RTE_WINS2008",
        RTE_WINS2012: "RTE_WINS2012",
    }

