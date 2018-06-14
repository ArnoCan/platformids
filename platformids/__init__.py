# -*- coding: utf-8 -*-
"""The package 'platformids' provides canonical enumerations of bit encoded numeric platform IDs.

"""
from __future__ import absolute_import
from sys import version_info, platform

import os
import sys
import re

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.28'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


msg_loponly = "Logic operators only."


class PlatformIDsError(Exception):
    """Subsystem *PlatformIDs*.
    """
    pass


# pylint: disable-msg=W0105


def getPYVxyz(x=0, y=0, z=0):
    """Calculates the 16bit integer bi-mask for the provided 
    Python release values. For example from *sys.version_info*: ::

       x = sys.version_info[0]  # uses 3bits:  x: 0-7
       y = sys.version_info[1]  # uses 5bits:  y: 0-31
       z = sys.version_info[2]  # uses 8bits:  z: 0-255
    
    resulting in: ::

       Vxyz = 0bxxxyyyyyzzzzzzzz

    For example: ::

       x, y, z = (3, 6, 5)
       
       self.bits = (3, 5, 8)

       # => result = 0b 011 00110 00000101 
       # => result = 0b0110011000000101 =  26,117

    Args:
        **x**:
            The major version number. ::

               0 <= y

               0 <= y0 < 4  # internal low-level 16-bit optimization threshold 

        **y**:
            The minor version number. ::
               0 <= y < 63

        **z**:
            The numeric relase-build tag. ::

               0 <= y < 257

    Returns:
        The bit-mask.

    Raises:
        pass-through
    """
    return (
       (x & 255) << 13   # bit 15 - 13 - see version_info[0] - PythonX
       | (y & 31) << 8  # bit 12 -  8 - see version_info[1] - Pythonx.Y
       | (z & 7)        # bit  7 -  0 - see version_info[2] - Pythonx.y - x.y.Y
       )

#
# Some pre-calculated and cached common Python release values of bit masks 
# for the use of conditional code segments.
#
PYV2 = 16384  # getPYVxyz(2,)
PYV26 = 17920  # getPYVxyz(2, 6)
PYV27 = 18176  # getPYVxyz(2, 7)
PYV3 = 24576  # getPYVxyz(3,)
PYV32 = 25088  # getPYVxyz(3, 2)
PYV34 = 25600  # getPYVxyz(3, 4)
PYV35 = 25856  # getPYVxyz(3, 5)
PYV36 = 26112  # getPYVxyz(3, 6)
PYV362 = 26114  # getPYVxyz(3, 6, 2)
PYV365 = 26117  # getPYVxyz(3, 6, 5)

#: The Python release of current process
PYVxyz = getPYVxyz(*sys.version_info[:3])

#:
#: Adjust to current major Python version to Python3 vs. Python2.
#:
V3K = False  #: Python3.5+
if PYVxyz >= PYV35:
    V3K = True
    ISSTR = (str, bytes)  #: string and unicode

    #: Superpose for generic Python3 compatibility.
    unicode = str  # @ReservedAssignment

elif PYVxyz >= PYV27:
    ISSTR = (str, unicode)  #: string and unicode

else:
    raise PlatformIDsError(
        "Requires Python 2.7+, or 3.5+, current: " 
        + str(version_info[:2]))


# pylint: enable-msg=W0105


#
# current platform as bit-array
#

#
# categories - bit-blocks
#
RTE_WIN32 = 65536 #: all Windows systems [MS-DTYP]_
RTE_POSIX = 131072 #: Posix systems using *fcntl* [POSIX]_.

#:
#: special for cross-over conversions 0 the native is reset to the native-enum
#:
RTE_CNP = RTE_POSIX + 1 #: cross native Posix systems using *fcntl* [POSIX]_.
RTE_CNW = RTE_WIN32 + 1 #: cross native all Windows systems [MS-DTYP]_, slightly different from RTE_WIN32

#
# standard platform sets
#
RTE_CYGWIN = RTE_POSIX + 2  #: Cygwin [CYGWIN]_


# set: posix
RTE_DARWIN = RTE_POSIX + 4  #: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
RTE_OSX = RTE_POSIX + 8  #: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
RTE_SOLARIS = RTE_POSIX + 16  #: UNIX/Solaris, as Posix system [POSIX]_.
RTE_BSD = RTE_POSIX + 32  #: BSD, - OpenBSD, FreeBSD, NetBSD - as Posix system [POSIX]_.
RTE_LINUX = RTE_POSIX + 64  #: Linux with specific add-ons - OS, DIST, GNU - as Posix system [POSIX]_.

# members" Linux
RTE_CENTOS  = RTE_LINUX + 1  #: CentOS
RTE_CENTOS4 = RTE_CENTOS + 4  #: CentOS-4
RTE_CENTOS5 = RTE_CENTOS + 5  #: CentOS-5
RTE_CENTOS6 = RTE_CENTOS + 6  #: CentOS-6
RTE_CENTOS7 = RTE_CENTOS + 7  #: CentOS-7

RTE_FEDORA = RTE_LINUX + 32  #: Fedora
RTE_FEDORA19 = RTE_FEDORA + 19  #: Fedora-19
RTE_FEDORA27 = RTE_FEDORA + 27  #: Fedora-27

RTE_DEBIAN = RTE_LINUX + 256  #: Debian
RTE_DEBIAN6 = RTE_DEBIAN + 6  #: Debian - squeeze
RTE_DEBIAN7 = RTE_DEBIAN + 7  #: Debian - wheezy
RTE_DEBIAN8 = RTE_DEBIAN + 8  #: Debian - jessy
RTE_DEBIAN9 = RTE_DEBIAN + 9  #: Debian - stretch

RTE_SUSE = RTE_LINUX + 96  #: OpenSUSE

RTE_UBUNTU = RTE_LINUX + 128  #: OpenSUSE

# set: bsd
RTE_DRAGONFLYBSD = RTE_BSD + 4
RTE_NETBSD = RTE_BSD + 16
RTE_OPENBSD = RTE_BSD + 64
RTE_FREEBSD = RTE_BSD + 256

# set: win32
# currently no sub-categories, some are contained in 
# the 'set: generic': drives, shares
#
RTE_DOS = RTE_WIN32 + 1  #: MS-DOS - frozen

RTE_WINNT4 = RTE_WIN32 + 9  #: Windows-NT4 - frozen
RTE_WINNT4WS = RTE_WIN32 + 10  #: Windows-NT4-Workstation - frozen
RTE_WINNT4S = RTE_WIN32 + 11  #: Windows-NT4-Server - frozen
RTE_WIN2000 = RTE_WIN32 + 16  #: Windows-2000 - frozen
RTE_WINS2000WS = RTE_WIN32 + 17  #: Windows-2000-Workstation - frozen
RTE_WINS2000S = RTE_WIN32 + 18  #: Windows-2000-Server - frozen
RTE_WINS2008 = RTE_WIN32 + 19  #: Windows-2008-Server - frozen

RTE_POWERSHELL1 = RTE_WIN32 + 64  #: PowerShell-1-Windows
RTE_POWERSHELL2 = RTE_WIN32 + 65  #: PowerShell-2-Windows
RTE_POWERSHELL2LINUX = RTE_WIN32 + 66  #: PowerShell-2-Linux

RTE_WIN7 = RTE_WIN32 + 128  #: Windows7
RTE_WIN8 = RTE_WIN32 + 129  #: Windows7
RTE_WIN81 = RTE_WIN32 + 130  #: Windows7
RTE_WIN10 = RTE_WIN32 + 131  #: Windows10
RTE_WINS2012 = RTE_WIN32 + 144  #: Windows-2012-Server


if platform in ('linux', 'linux2'):
    RTE = RTE_LINUX
    RTE_CNP = RTE_POSIX

elif platform == 'bsd':
    RTE = RTE_BSD
    RTE_CNP = RTE_POSIX

elif platform == 'darwin':
    RTE = RTE_DARWIN
    RTE_CNP = RTE_POSIX

elif platform == 'cygwin':
    RTE = RTE_POSIX | RTE_WIN32 | RTE_CYGWIN
    RTE_CNP = RTE_POSIX

elif platform == 'win32':
    RTE = RTE_WIN32
    RTE_CNW = RTE_WIN32

else:
    raise PlatformIDsError("Platform not supported:" + str(platform))

#
# set: generic
#

#: Use the current block-offset only,
#: results in the current platformm enum.
RTE_GENERIC = RTE & RTE_POSIX & RTE_WIN32
                    
#: Dyanmic local platform, synonym for generic.
RTE_LOCAL = RTE_GENERIC + 1


class ProtectedDict(dict):
    def __setitem__(self, key, value):
        """
        """
        try:
            if dict.__getitem__(self, key):
                #
                # key exists - error
                #
                from platformids.map_enum_labels import num2enumstr 

                if type(key) == int:
                    _k0 = num2enumstr.get(key)
                else:
                    _k0 = get_rte2num(key)
                if _k0:
                    # known
                    _k = "%s(%s)" % (str(key), str(_k0))
                else:
                    # unknown
                    _k = str(key)

    
                #
                # new value
                #
                if type(value) == int:
                    _v0 = num2enumstr.get(value)
                else:
                    _v0 = get_rte2num(value)

                if _v0:
                    _v = "%s(%s)" % (str(value),str( _v0))
                else:
                    _v = str(value)

    
                #
                # old value
                #
                oval = dict.__getitem__(self, key)
                if type(oval) == int:
                    _ov = num2enumstr.get(oval)
                else:
                    _ov = get_rte2num(oval)
                    _ovl = num2enumstr.get(_ov)
                    if _ovl:
                        _ov = "%s(%s)" % (str(_ov), str(_ovl))
                if _ov:
                    
                    _ov = "%s(%s)" % (str(oval), str(_ov))
                else:
                    _ov = str(oval)


                raise PlatformIDsError(
                    "READONLY: Key is already present:\n  key:     %s\n  old-val: %s\n  new-val: %s" %(
                        _k,
                       _ov,
                        _v
                        )
                    ) 
        except KeyError:
            return dict.__setitem__(self, key, value)
    
    
#: mapping of the rte string and numeric representation to the numeric value
rte2num = ProtectedDict(
    {
        'bsd': RTE_BSD,
        'centos': RTE_CENTOS,
        'centos4': RTE_CENTOS4,
        'centos5': RTE_CENTOS5,
        'centos6': RTE_CENTOS6,
        'centos7': RTE_CENTOS7,
        'cygwin': RTE_CYGWIN,
        'debian': RTE_DEBIAN,
        'debian6': RTE_DEBIAN6,
        'debian7': RTE_DEBIAN7,
        'debian8': RTE_DEBIAN8,
        'debian9': RTE_DEBIAN9,
        'dos': RTE_DOS,
        'dragonfly': RTE_DRAGONFLYBSD,
        'fedora': RTE_FEDORA,
        'fedora19': RTE_FEDORA19,
        'fedora27': RTE_FEDORA27,
        'freebsd': RTE_FREEBSD,
        'linux': RTE_LINUX,
        'netbsd': RTE_NETBSD,
        'openbsd': RTE_OPENBSD,
        'posix': RTE_POSIX,
        'solaris': RTE_SOLARIS,
        'suse': RTE_SUSE,
        'ubuntu': RTE_UBUNTU,
        'win': RTE_WIN32,
        'win10': RTE_WIN10,
        'win2000': RTE_WIN2000,
        'win32': RTE_WIN32,
        'win7': RTE_WIN7,
        'winnt2000s': RTE_WINS2000S,
        'winnt2000ws': RTE_WINS2000WS,
        'winnt2008': RTE_WINS2008,
        'winnt2012': RTE_WINS2012,
        'winnt4': RTE_WINNT4,
        'winnt4s': RTE_WINNT4S,
        'winnt4ws': RTE_WINNT4WS,
        RTE_BSD: RTE_BSD,
        RTE_CENTOS4: RTE_CENTOS4,
        RTE_CENTOS5: RTE_CENTOS5,
        RTE_CENTOS6: RTE_CENTOS6,
        RTE_CENTOS7: RTE_CENTOS7,
        RTE_CENTOS: RTE_CENTOS,
        RTE_CYGWIN: RTE_CYGWIN,
        RTE_DARWIN: RTE_DARWIN,
        RTE_DEBIAN6: RTE_DEBIAN6,
        RTE_DEBIAN7: RTE_DEBIAN7,
        RTE_DEBIAN8: RTE_DEBIAN8,
        RTE_DEBIAN9: RTE_DEBIAN9,
        RTE_DEBIAN: RTE_DEBIAN,
        RTE_DOS: RTE_DOS,
        RTE_DRAGONFLYBSD: RTE_DRAGONFLYBSD,
        RTE_FEDORA19: RTE_FEDORA19,
        RTE_FEDORA27: RTE_FEDORA27,
        RTE_FEDORA: RTE_FEDORA,
        RTE_FREEBSD: RTE_FREEBSD,
        RTE_LINUX: RTE_LINUX,
        RTE_NETBSD: RTE_NETBSD,
        RTE_OPENBSD: RTE_OPENBSD,
        RTE_OSX: RTE_OSX,
        RTE_POSIX: RTE_POSIX,
        RTE_SOLARIS: RTE_SOLARIS,
        RTE_SUSE: RTE_SUSE,
        RTE_UBUNTU: RTE_UBUNTU,
        RTE_WIN10: RTE_WIN10,
        RTE_WIN2000: RTE_WIN2000,
        RTE_WIN32: RTE_WIN32,
        RTE_WIN32: RTE_WIN32,
        RTE_WIN7: RTE_WIN7,
        RTE_WINNT4: RTE_WINNT4,
        RTE_WINNT4S: RTE_WINNT4S,
        RTE_WINNT4WS: RTE_WINNT4WS,
        RTE_WINS2000S: RTE_WINS2000S,
        RTE_WINS2000WS: RTE_WINS2000WS,
        RTE_WINS2008: RTE_WINS2008,
        RTE_WINS2012: RTE_WINS2012,
    }
)


#: mapping of the rte numeric representation to the string value
#num2rte = {
num2rte = ProtectedDict(
    {
        RTE_BSD: 'bsd',
        RTE_CENTOS: 'centos',
        RTE_CENTOS4: 'centos4',
        RTE_CENTOS5: 'centos5',
        RTE_CENTOS6: 'centos6',
        RTE_CENTOS7: 'centos7',
        RTE_CYGWIN: 'cygwin',
        RTE_DEBIAN: 'debian',
        RTE_DEBIAN6: 'debian6',
        RTE_DEBIAN7: 'debian7',
        RTE_DEBIAN8: 'debian8',
        RTE_DEBIAN9: 'debian9',
        RTE_DOS: 'dos',
        RTE_DRAGONFLYBSD: 'dragonfly',
        RTE_FEDORA: 'fedora',
        RTE_FEDORA19: 'fedora19',
        RTE_FEDORA27: 'fedora27',
        RTE_FREEBSD: 'freebsd',
        RTE_LINUX: 'linux',
        RTE_NETBSD: 'netbsd',
        RTE_OPENBSD: 'openbsd',
        RTE_POSIX: 'posix',
        RTE_SOLARIS: 'solaris',
        RTE_SUSE: 'suse',
        RTE_UBUNTU: 'ubuntu',
        RTE_WIN32: 'win',
        RTE_WIN10: 'win10',
        RTE_WIN2000: 'win2000',
        RTE_WIN32: 'win32',
        RTE_WIN7: 'win7',
        RTE_WINS2000S: 'winnt2000s',
        RTE_WINS2000WS: 'winnt2000ws',
        RTE_WINS2008: 'winnt2008',
        RTE_WINS2012: 'winnt2012',
        RTE_WINNT4: 'winnt4',
        RTE_WINNT4S: 'winnt4s',
        RTE_WINNT4WS: 'winnt4ws',
    }
)


#:
#: Initial custom offset and the free number range for custom member add-ons.
#: The first 16 bits are reserved for custom bit-blocks.
#:
__CUSTOM_BASE_NUM_DEFAULT = 262144  #: initial offset
__CUSTOM_BASE_MIN_MEMBER_REL = + 0  #: range start for members
__CUSTOM_BASE_MAX_MEMBER_REL = 65535  #: inclusive range end for members


#:
#: Current value of the next-free custom bit-block
#:
__CUSTOM_BASE_NUM = __CUSTOM_BASE_NUM_DEFAULT

def get_custom_num_base():
    """Reserves and returns the current available base value for 
    the next bit-block. Each reserved bit-block for custom usage
    is 16-bit wide, and could be used by the application arbitrarily.

    Each call increments the integer address of the next free block
    by one bit. 
    
    .. note::

       In current release the reservation of the value ranges
       for bit-blocks is not released until the process termination. 

    Args:
        None

    Returns:
        The base index for the new reservation.

    Raises:
        pass-through

    """
    global __CUSTOM_BASE_NUM
    _ret = __CUSTOM_BASE_NUM
    __CUSTOM_BASE_NUM = __CUSTOM_BASE_NUM << 1 
    return  _ret


def get_custom_num_range():
    """Returns the available range of values for 
    elements within bit blocks.

    Args:
        None.

    Returns:
        The inclusive range as tuple: ::

           (min, max)

    Raises:
        None
    """
    return (
        __CUSTOM_BASE_NUM + __CUSTOM_BASE_MIN_MEMBER_REL, 
        __CUSTOM_BASE_NUM + __CUSTOM_BASE_MAX_MEMBER_REL
        )


def get_num2rte(num):
    """Gets the corresponding string representation
    for the string numeric value.
    
    Alternatively the official dict *num2rte*
    could be used. 
    
    Args:
        **num**:
            Numeric enum value of the requested platform.

    Returns:
        The string value, or *None**.

    Raises:
        None

    """
    if type(num) != int:
        return str(num)
    return num2rte.get(num)


def get_rte2num(rte):
    """Gets corresponding numerical representation
    for the numeric or string value.
    
    Alternatively the official dict *rte2num*
    could be used. 

    Args:
        **rte**:
            Numeric enum value or string representation
            of the requested platform.

    Returns:
        The numeric value, or *None**.

    Raises:
        None

    """
    if type(rte) == int:
        return rte
    return rte2num.get(rte)


def set_num2rte(key, value):
    """Sets the numeric to string map.
    
    Alternatively the official dict *num2rte*
    could be used. 
    
    Args:
        **key**:
            Numeric key value.

        **value**:
            String value.

    Returns:
        *None*

    Raises:
        PlatformIDsError

    """
    if type(key) != int:
        raise PlatformIDsError("requires a int key, got: " + str(key))
    if type(value) not in ISSTR:
        raise PlatformIDsError("requires a string value, got: " + str(value))
    
    num2rte[key] = value


def set_rte2num(key, value):
    """Sets the rte to numeric mapping

    Alternatively the official dict *rte2num*
    could be used. 

    Args:
        **key**:
            Numeric or string key value.

        **value**:
            Numeric value.

    Returns:
        *None*

    Raises:
        None

    """
    if type(value) != int:
        raise PlatformIDsError("requires an int value, got: " + str(value))
    
    rte2num[key] = value

