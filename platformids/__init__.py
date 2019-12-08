# -*- coding: utf-8 -*-
"""The package 'platformids' provides canonical enumerations of bit encoded numeric platform IDs
for the Python implementations CPython, IPython, IronPython, Jython, and PyPy.
"""
#############################################
#
# See manuals for the detailed API.
#
#############################################

from __future__ import absolute_import

import os
import sys
import re
import platform

#
# load Python syntax and implementation basics - requires support by 'pythonids.pythondist'
#
from pythonids import PYV35Plus,ISSTR, PYVxyz, PYV33, PYV2
from pythonids.pythondist import isJython, ISINT, PYDIST, PYE_DIST, PYE_JYTHON
from yapyutils.modules.loader import get_modulelocation, load_module


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.31'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"

# central debug and verbose control of curretn package
_debug = 0
_verbose = 0

#
# static pre-compiled scanner
#

# version conversion and normalization
DSKORG_ID = re.compile(r'^(?s)ID=["\']*([^"\'\n\r]*).*')
DSKORG_ID_LIKE = re.compile(r'^(?s)ID_LIKE=["\']*([^"\'\n\r]*).*')
DSKORG_NAME_RELEASE = re.compile(r'(?s)^NAME=["\']*([^ ]*) *([^"\']*).*')
DSKORG_RELEASE = re.compile(r'(?s)^VERSION=["\']*([^"\']*)["\']*[^(]*[(]*([^)]*)[)]*.*')
DSKORG_VERSION = re.compile(r'(?s)^VERSION=["\']*([^"\']*)["\']*.*')
PRENONNUM = re.compile(r'([^0-9]+[^ \t0-9]).*')
VERSION_ID = re.compile(r'(?s)^VERSION_ID=["\']*([^"\']*)["\']*.*')
VERSNUM = re.compile(r'([0-9]+)[.]*([0-9]*)[.]*([0-9]*)')


#
# shared exceptions
#
class PlatformIDsError(Exception):
    """Subsystem *PlatformIDs*."""
    pass


class PlatformIDsEnumerationError(PlatformIDsError):
    """Enumeration of dynamic assigned values."""
    pass


class PlatformIDsUnknownError(PlatformIDsError):
    """Unknown value."""
    pass


class PlatformIDsPresentError(PlatformIDsError):
    """Item already present, prohibited in strict mode."""
    pass


class PlatformIDsCustomError(PlatformIDsError):
    """No more custom keys are available."""
    pass


class PlatformIDsKeyError(PlatformIDsError):
    """Key invalid."""
    pass


#
# prepare  Jython vs. others - the most significant impact on available libraries
#
if not isJython:
    try:
        osname = os.name
    except AttributeError:
        # e.g. CirctuiPython, MicroPython
        raise NotImplementedError('requires special module')

    if PYV35Plus:
        PlatformIDsFileCheck = (FileNotFoundError,)  # @UndefinedVariable
    
    else:
        PlatformIDsFileCheck = (Exception,)

else:
    osname = os._name  # @UndefinedVariable  # set to the platform name
    PlatformIDsFileCheck = (IOError,)  # @UndefinedVariable


RTE = 0  #: the numeric bitmask record

#
# current platform as bit-array with following bitmasks
#
RTE_CATEGORY_B = 0xf0000000  # : bit: 31-28
RTE_OSTYPE_B = 0x0f800000  # : bit: 27-23
RTE_DIST_B = 0x007f0000  # : bit: 22-16
RTE_DISTREL_B = 0x0000ffff  # : bit: 15-0

RTE_CATEGORY_OFFSET = 0x0fffffff  # : bit: 28
RTE_OSTYPE_OFFSET = 0x007fffff  # : bit: 23
RTE_DIST_OFFSET = 0x0000ffff  # : bit: 16
RTE_DISTREL_OFFSET = 0x00000000  # : bit: 0

RTE_CATEGORY_SHIFT = 28  # : bit: 28
RTE_OSTYPE_SHIFT = 23  # : bit: 23
RTE_DIST_SHIFT = 16  # : bit: 16
RTE_DISTREL_SHIFT = 0  # : bit: 0

RTE_CATEGORY = 0xf0000000  # : bit: 31-28
RTE_OSTYPE = 0xff800000  # : bit: 31-23
RTE_DIST = 0xffff0000  # : bit: 31-16
RTE_DISTREL = 0xffffffff  # : bit: 31-0

#
# Distribution with optional non-standard version scheme and optional callback
# the value is used as common offset for the *dist* defines
#
RTE_DISTEXT = 0x00400000  # : bit: 22 flag for distribution schemes with optional callback

#
# category
#
RTE_POSIX = 0x10000000  # : Posix systems using *fcntl* [POSIX]_.
RTE_WIN32 = 0x20000000  # : all Windows systems
RTE_WIN = 0x20000000  # : all Windows systems
RTE_WINDOWS = 0x20000000  # : all Windows systems
RTE_EMU = 0x40000000  # : Logical Emulation Layer - Meta-Category providing a bit
RTE_PWEMU = 0x70000000  # : Cygwin [CYGWIN]_ - special virtual environment
RTE_WPEMU = 0x50000000  # : Windows emulation on Posix
RTE_EMBEDDED = 0x80000000  # : Embedded OS/dist


#
# ostype
#

# context: RTE_WIN32
RTE_NT = RTE_WIN32 + 0x00800000  # : all Windows workstation systems

RTE_CYGWINNT = RTE_PWEMU + 0x00800000  # : all Windows workstation systems - the 'os.uname' is 'posix'

# context: RTE_POSIX
RTE_LINUX = RTE_POSIX + 0x00800000  # : all LINUX systems
RTE_BSD = RTE_POSIX + 0x01000000  # : all BSD systems
RTE_DARWIN = RTE_POSIX + 0x02000000  # : Darwin, as Posix OS/Core system
RTE_UNIX = RTE_POSIX + 0x04000000  # : all UNIX systems

#
# dist
#

# context: RTE_POSIX.RTE_LINUX - standard distributions
RTE_FEDORA = RTE_LINUX + 0x00010000  # : Fedora
RTE_CENTOS = RTE_LINUX + 0x00020000  # : CentOS
RTE_DEBIAN = RTE_LINUX + 0x00030000  # : Debian
RTE_RHEL = RTE_LINUX + 0x00040000  # : RedHat Enterprise Linux
RTE_SLES = RTE_LINUX + 0x00050000  # : Suse Enterprise Linux
RTE_UBUNTU = RTE_LINUX + 0x00060000  # : Ubuntu

RTE_OPENWRT = RTE_LINUX + 0x00070000  # : OpenWRT
RTE_RASPBIAN = RTE_LINUX + 0x00080000  # : Raspbian

#
# *** rolling distributions ***
#
RTE_KALI = RTE_LINUX + RTE_DISTEXT + 0x00010000  # : Kali Linux - rolling dist
RTE_ARCHLINUX = RTE_LINUX + RTE_DISTEXT + 0x00020000 #: ArchLinux - rolling dist

# context: RTE_POSIX.RTE_UNIX
RTE_SUNOS5 = RTE_UNIX + 0x00020000  # : UNIX/SunOS5 is Solaris
RTE_SOLARIS = RTE_SUNOS5  # : UNIX/SunOS5 is Solaris

# context: RTE_POSIX.RTE_DARWIN
RTE_OSX = RTE_DARWIN + 0x00020000  # : Mac OS-X RTE_OSX is basically the short form of RTE_OSX10
RTE_OSX10 = RTE_OSX  # : Mac OS-X v10.x, as Posix system [POSIX]_, no macpath-legacy.

# context: RTE_POSIX.RTE_BSD
RTE_OPENBSD = RTE_BSD + 0x00020000  # : OpenBSD

#
# category - perform basic platform identification
#
if 'posix' == osname:  # unix, linux, bsd, osx
    if platform.system().startswith('CYGW'):
        # Cygwin
        category = RTE_PWEMU
    else:
        category = RTE_POSIX

    # TODO" RTE_WPEMU

elif 'nt' == osname:  # modern windows
    category = RTE_WIN32


class ProtectedDict(dict):
    """Implements a 'dict' with protection against modification of items. This is
    in order to protect a repository from erroneous modifications of it's 
    entries by malicious code. The deletion is still supported, which is
    considered as intentional, thus done beeing aware of the consequences.  
    
    The main intention for the *platformids* is to avoid inconsistencies of
    hard-coded values of assigned enumerations by runtime redefinitions. 
    Unintentional redefinitions also may proof as hard to debug.
    
    The member attribute *self.strict_check* controls how new items are added:
          
    0. single new item:
          add silently
    
    1. single item which is already present:
          * strict_check == True: raises exception
          * strict_check == False: ignores silently
    
    2. set of items, where none of the new set is present:
          add silently
    
    3. set of items, where at least one is present:
          * strict_check == True: raises exception
          * strict_check == False: add silently new, ignore present silently
    
     
    The common variables such as central dictionaries are thus read-only protected
    during the runtime of the process. The response style for the attempt to alter
    a value could be modified - raised to a stronger level - by the attribute
    'strict_check', which raises an exception once set. 
    """
    def __init__(self, *args, **kargs):
        """   
        Args:
            args:
            pass-through to dict
            
            kargs:
                non-defined are passed-through to dict
                
                int_keys_only:
                    Controls type of valid keys. ::
                    
                        int_keys_only := (
                            True    # permits interger keys only
                           | False  # permits any valid *dict* key
                        )
                
                strict_check:
                    Defines the handling of values for present keys. ::
                
                        True:   when True raises exception for present
                                items, 
                        
                        False:  silently ignores new values for present
                                items
            
        Returns:
            Initialized object, or raises exception.
        
        Raises:
            pass-through
    
        """
        self.strict_check = kargs.get('strict_check', False)
        try:
            kargs.pop('strict_check')
        except:
            pass

        self.int_keys_only = kargs.get('int_keys_only', False)
        try:
            kargs.pop('int_keys_only')
        except:
            pass

        super(ProtectedDict, self).__init__(*args, **kargs)

    def __delattr__(self, name):
        ""
        if name in ('strict_check_reset', 'strict_check',):
            raise PlatformIDsCustomError("deletion not permitted for attribute: " + str(name))
        return dict.__delattr__(self, name)

    def __setattr__(self, name, value):
        """Filters and controls attribute values to be set.
   
        Args:
            name:
                Sets the attribute named by *name*. Establishes special
                handling for the in-band control attributes.
              
                    **strict_check**:
                        The value can only be raised to *True* in order to
                        strengthen the strictness.
                    
                    **strict_check_reset**:
                        If the value is set to *True*, than the member attribute
                        '*strict_check*' is set to *False*.
        
                Else calls '*dict.__setattr__*'. 
        
            value:
                The value is passed through to *dict*, see also for special
                values of *name*.
        
        Returns:
            Either filters defined control attributes - see *name*, or
            calls *dict.__setattr__*.
        
        Raises:
            pass-through
        
        """
        if name == 'strict_check_reset' and value == True:
            return dict.__setattr__(self, 'strict_check', False)

        elif name == 'strict_check':
            if self.__dict__.get('strict_check'):
                if value != True:
                    return
            # initial value, this could later only be modified to the 'stronger' True
            return dict.__setattr__(self, name, value)

        return dict.__setattr__(self, name, value)

    def __setitem__(self, key, value):
        """Filter for already present mappings controlled by the
        member *strict_check*. 
        
        Args:
            name:
                Sets the item named by *name*. Controlled by
                the attribute *strict_check*. ::         
                  
                    self.strict_check := (
                         True   # permits only creation of non-present
                       | False  # normal behaviour
                    )
            
                Dependent on the presence raises an exception when
                strict is enabled.
            
            value:
                The value is passed through to *dict*, see also for special
                values of *name*.
        
        Returns:
            dict.__setitem__
        
        Raises:
            PlatformIDsPresentError
                Conditional based on *strict_check*, if *True* raises
                for present attributes *PlatformIDsPresentError*.
              
            PlatformIDsKeyError
                For non-int keys when *int_keys_only* is set.
        
            pass-through

        """
        try:
            if dict.__getitem__(self, key):
                if self.strict_check:
                    raise PlatformIDsPresentError("key-present: " + str(key))
                return
        except KeyError:
            if self.int_keys_only and type(key) not in ISINT:
                raise PlatformIDsKeyError("Integer keys only: " + str(key))

            return dict.__setitem__(self, key, value)

    def update(self, dict2, *args, **kargs):
        """Adds a set of items, filters each for presence.

        * none of the new set is present: 
            adds all silently
                 
        * at least one is present:
            * strict_check == True: raises exception
            * strict_check == False: add silently
        
        Args:
        
            dict2:
                Adds items controlled by the attribute *strict_check*. ::         
                 
                    self.strict_check := (
                         True   # permits only creation of non-present
                       | False  # normal behaviour
                    )
        
                Dependent on the presence of at least one raises an 
                exception when strict is enabled.
        
            args:
                Passed to *dict.update*.
              
            kargs:
                Passed to *dict.update*.
        
        Returns:
            dict.update or None
        
        Raises:
            PlatformIDsPresentError
                Conditional based on *strict_check*, if *True* raises
                for present attributes *PlatformIDsPresentError*.
        
            PlatformIDsKeyError
                For non-int keys when *int_keys_only* is set.
        
            pass-through

        """

        # should not be called frequently, thus ok.
        if self.int_keys_only:
            for k in dict2.keys():
                if type(k) not in ISINT:
                    if isJython:
                        try:
                            if type(k) is not long:  # @UndefinedVariable
                                raise PlatformIDsKeyError("Numeric keys only: " + str(k))
                        except:
                            pass
                    else:
                        raise PlatformIDsKeyError("Numeric keys only: " + str(k))

        if set(self.keys()) & set(dict2.keys()):
            # has keys already present

            if self.strict_check:
                # strict is enabled
                _str = []

                # get list of present keys
                for x in set(self.keys()) & set(dict2.keys()):
                    if type(x) in ISSTR:
                        _str.append(x)
                    else:
                        _str.append(str(x))

                # notify with complete list
                raise PlatformIDsPresentError(
                    "keys-present:\n  %s\n" % (
                        str(sorted(_str))))

            else:
                # not in strict mode, thus normal procedure

                common = set(self.keys()) & set(dict2.keys())
                for k, v in dict2.items():
                    if type(k) in common:
                        continue
                    self[k] = v

        else:
            # normal procedure
            return super(ProtectedDict, self).update(dict2, *args, **kargs)


class ProtectedDictEnum(ProtectedDict):
    """Implements the dynamic creation and management of numeric enumeration
    values. These are used as dynamic assigned constants with the life time
    of the process itself. The enums are optimized to be used in conjunction
    with numeric bitmask vectors.
    The values are created on-demand, e.g. for dynamic loaded packages, and
    could be removed when no longer required. Thus are released than for the 
    reuse.
    
    The management of the unused numeric values for assignment is performed
    by two levels. 
    
    0. The value is managed by a protected counter within the defined range.
    1. Once the values are exhausted, the dictionary is used as release map.
       This is required due to the possible storage of the values by the
       application, thus assigned values cannot be reassigned and though
       the ranges could become used sparse. 
          
       This level is much slower, though it is based on the lookup and remove
       form the unused-map.
       And of course, previous releases has to be present |smilecool|.
    
    Anyhow, e.g. in case of *platformids* for the *ostype*
    and *dist* the ranges for the additional dynamic assigments in are 
    about 100 for the distribution *dist*, about 25 for the OS 
    type *ostype*, and about 12 for the category *category*. This should be 
    in practical realworld use-cases more than sufficient.
    
    
    REMARK: Implemented as *dict* for coming extensions. 

    """
    def __init__(self, **kargs):
        """Initializes key reservation.
        The custom range values has to comply to the bitmask segments.
        These define the minimal and maximal values in accordance to the common ranges 
        by the mathematical notation:
        
        .. parsed-literal::
        
           values := [custom_min, custom_max)   # excluding custom_max
        
        The values could be processed by the application of the helper constants,
        see :ref:`Helper Constants <BITMASK_HELPERCONSTS>`.   
        E.g. in case of *dist* for the *ostype* context of *RTE_LINUX* :
        
        .. parsed-literal::
        
           custom_min == ((RTE_LINUX + RTE_DISTEXT + RTE_DIST_OFFSET +   0) & RTE_DIST_B) 
           custom_max == ((RTE_LINUX + RTE_DISTEXT + RTE_DIST_OFFSET + 126) & RTE_DIST_B) 
        
        or
        
        .. parsed-literal::
        
           (custom_min >> 16) == 0 
           (custom_max >> 16) == 126 
        
        
        
        The caller is responsible for the appropriate values.
        
        Args:
            kargs:
                default pass-through to dict
                
                custom_max:
                    Defines the maximum of custom range.
                    When missing no custom range os available.
                    
                    .. parsed-literal::
                    
                       custom_max > custom_min
                    
                    default := None
                
                custom_min:
                    Defines the minimum of custom range.
                    When missing no custom range os available.
                    
                    default := None
                
                custom_offset:
                    Defines the offset for the increment and decrement.
                    This is required e.g. in case of bitmask fields
                    with segments starts at bits greater than 0.
                    
                    default := 0
        
        Returns:
            Initialized object, or raises exception.
        
        Raises:
            PlatformIDsEnumerationError
                Erroneous custom range is provided.
               
            pass-through

        """
        ProtectedDict.__setattr__(self, 'custom_offset', kargs.get('custom_offset', 0))
        try:
            # drop for parent __init__
            kargs.pop('custom_offset')
        except:
            pass

        # : the last permitted reservation
        _cm = kargs.get('custom_max', 0)
        ProtectedDict.__setattr__(self, 'custom_max', _cm)

        try:
            # drop for parent __init__
            kargs.pop('custom_max')

            # the current
            ProtectedDict.__setattr__(self, 'reserved', _cm)
        except:
            # the current
            ProtectedDict.__setattr__(self, 'reserved', _cm)

        ProtectedDict.__setattr__(self, 'custom_min', kargs.get('custom_min', 0))
        try:
            # drop for parent __init__
            kargs.pop('custom_min')
        except:
            pass

        if self.custom_min > self.custom_max or (self.custom_min == self.custom_max and self.custom_min != 0):
            raise PlatformIDsEnumerationError(
                "Invalid custom range min = %s - max = %s" % (str(self.custom_min), str(self.custom_max))
                )

        kargs['int_keys_only'] = True
        super(ProtectedDictEnum, self).__init__(**kargs)
        
        # deleted non-continous entries
        self.free = {}

    def __delitem__(self, enum):
        """Prohibits unmanaged access to the enum pool, use method *delete_enum* instead for
        managed release.
        
        Args:
            enum:
                Enum key.
        
        Returns:
            Raises exception.
        
        Raises:
            PlatformIDsCustomError

        """
        raise PlatformIDsCustomError("prohibits unmanaged access, use method delete_enum")

    def __delattr__(self, name):
        """Protects the enumeration management attributes from deletion.

        Args:
            name:
                Excludes reserved attributes from deletion. ::
        
                    name :=(
                         'reserved'
                       | 'custom_min'
                       | 'custom_max'
                    )
        
        Returns:
            None
        
        Raises:
            PlatformIDsEnumerationError
           
            pass-through

        """
        if name in ('reserved', 'custom_min', 'custom_max',):
            raise PlatformIDsEnumerationError("attribute cannot be deleted: " + str(name))
        return ProtectedDict.__delattr__(self, name)

    def __setattr__(self, name, value):
        """Protects the enumeration management attributes from non-managed 
        direct access.
        
        Args:
            name:
                Excludes reserved attributes from direct access. ::
        
                    name :=(
                         'reserved'
                       | 'custom_min'
                       | 'custom_max'
                    )
        
            value:
                Value to be set.
        
        Returns:
            None
        
        Raises:
            PlatformIDsEnumerationError
           
            pass-through

        """
        if name in ('reserved', 'custom_min', 'custom_max',):
            raise PlatformIDsEnumerationError("attribute cannot be set direct: " + str(name))
        return ProtectedDict.__setattr__(self, name, value)

    def __setitem__(self, enum, value):
        """Prohibits unmanaged access to the enum pool, use method *add_enum* instead for
        managed release.
        
        Args:
            enum:
                Enum key.
        Returns:
            Raises exception.
        
        Raises:
            PlatformIDsCustomError

        """
        raise PlatformIDsCustomError("prohibits unmanaged access, use method add_enum")

    def add_enum(self, value=True):
        """Reserves and assigns the next free unique key to the
        value. The assigned key value is returned for use. 
        Custom ranges are available when the values *custom_max*
        and *custom_min* are initialized appropriately.
        
        Args:
            None.
        
        Returns:
            Either returns the reserved key, or raises exception when range is exhausted.
        
        Raises:
            PlatformIDsCustomError:
                No custom ranges are configured.
            
            PlatformIDsEnumerationError
                The configured range is exhausted.
            
            pass-through

        """
        if self.free:
            # reuse released first
            
            _x = self.free.popitem()
            ProtectedDict.__setitem__(self, _x[0], value)
            return _x[0]

        else:
            if not self.reserved:  # 0 is non active
                raise PlatformIDsCustomError(
                    "No custom ranges are available"
                    )
    
            if self.reserved <= self.custom_min:
                raise PlatformIDsEnumerationError(
                    "custom range exhausted"
                    )

            # get next key
            ProtectedDict.__setattr__(self, 'reserved', self.reserved - self.custom_offset - 1)
    
            # add value
            ProtectedDict.__setitem__(self, self.reserved, value)
        
            # return key for use
            return self.reserved

    def check_next_free_enum(self):
        """Checks and returns the next free value.
   
        **Does not reserve, just displays next.**
        
        Args:
           None
           
        Returns:
           Value to be used by next call of *add_enum*.
        
        Raises:
           PlatformIDsCustomError:
              No custom ranges are configured.
        
           PlatformIDsEnumerationError
              Range exhausted, no free values are available.

        """
        if not self.reserved:  # 0 is non active
            raise PlatformIDsCustomError(
                "No custom ranges are available"
                )

        if self.reserved > self.custom_min:
            return self.reserved  # - self.custom_offset - 1

        raise PlatformIDsEnumerationError(
            "Reserved range exhausted."
            )

    def purge(self, **kargs):
        """Clears the list of deleted non-continous enums.
        Deletes all entries in the release map, which could be added
        incremental and continous to the reserved-list of vallues
        beginning at from *custom_min*. 
        This re-initializes for the purged items the pure numeric first level 
        assignement by ranges - spares for these the lookup in the non-continous
        list.
        
        Args:
            kargs:
                maxrel:
                    Maximum to be released.
        
                minrel:
                    Minimum to be released.
        
        Returns:
            Returns the number of actual releases.
        
        Raises:
            PlatformIDsEnumerationError:
                Could not fulfil *minrel*.
        
            pass-through   

        """
        minrel = kargs.get('minrel', 0)
        maxrel = kargs.get('maxrel', len(self.free))
        
        relcnt = 0
        
        _n = len(self.free)
        
        for enum in sorted(self.free.keys()):
            if enum == self.reserved:
                # continous optimization at low-cost
                ProtectedDict.__setattr__(self, 'reserved', enum + self.custom_offset + 1)
                self.free.pop(enum)
                relcnt += 1
                maxrel -= 1
                if not maxrel:
                    break
            
            else:
                # needs continous ranges beginning at self.custom_min / self.reserved
                break
        
        if minrel:
            if relcnt < minrel:
                raise PlatformIDsEnumerationError(
                    "Could not release requested range: req = %d / done = %d / free = %d" % (
                        minrel,
                        relcnt,
                        (self.reserved - self.custom_min),
                        )
                    )

        return relcnt

    def delete_enum(self, enum):
        """Releases a given enum, either continous values by changing the reserved values,
        or by adding a non-continous values to the dict of released items.
        The non-continous released items could be cleared by the method *purge*.
        
        Args:
            enum:
                Enum key.
              
        Returns:
            None.
        
        Raises:
            pass-through

        """
        if enum == self.reserved:
            # continous optimization at low-cost
            ProtectedDict.__setattr__(self, 'reserved', enum + self.custom_offset + 1)
            self.pop(enum)
            return True

        self.free[enum] = self.pop(enum)
        return True 

    def update(self, dict2, *args, **kargs):
        """Prohibits updates.
        This is required in order to avoid arbitrary updates which simply
        would complicate the management and assignment of further values.
        Thus only individual values could be added and removed. 
        
        Args:
            None.
        
        Returns:
            Raises Exception.
        
        Raises:
            PlatformIDsEnumerationError

        """
        raise PlatformIDsCustomError("operation not permitted: update")


# : mapping of the rte string and numeric representation to the numeric value
rte2num = ProtectedDict(
    {
        'bsd': RTE_BSD,
        'darwin': RTE_DARWIN,
        'emu': RTE_EMU,
        'linux': RTE_LINUX,
        'linux2': RTE_LINUX,
        'nt': RTE_NT,
        'wpemu': RTE_WPEMU,
        'posix': RTE_POSIX,
        'pwemu': RTE_PWEMU,
        'unix': RTE_UNIX,
        'win': RTE_WIN32,
        'win32': RTE_WIN32,
        'windows': RTE_WINDOWS,
        RTE_BSD: RTE_BSD,
        RTE_DARWIN: RTE_DARWIN,
        RTE_EMU: RTE_EMU,
        RTE_LINUX: RTE_LINUX,
        RTE_NT: RTE_NT,
        RTE_WPEMU: RTE_WPEMU,
        RTE_POSIX: RTE_POSIX,
        RTE_PWEMU: RTE_PWEMU,
        RTE_WIN32: RTE_WIN32,
        RTE_WINDOWS: RTE_WINDOWS,

        #
        # frequent used current subsets
        #
        'SunOS5': RTE_SOLARIS,
        'arch': RTE_ARCHLINUX,
        'archlinux': RTE_ARCHLINUX,
        'centos': RTE_CENTOS,
        'debian': RTE_DEBIAN,
        'fedora': RTE_FEDORA,
        'openbsd': RTE_OPENBSD,
        'openwrt': RTE_OPENWRT,
        'osx': RTE_OSX,
        'osx10': RTE_OSX10,
        'raspbian': RTE_RASPBIAN,
        'rhel': RTE_RHEL,
        'solaris': RTE_SOLARIS,
        RTE_ARCHLINUX: RTE_ARCHLINUX,
        RTE_CENTOS: RTE_CENTOS,
        RTE_DEBIAN: RTE_DEBIAN,
        RTE_FEDORA: RTE_FEDORA,
        RTE_OPENBSD: RTE_OPENBSD,
        RTE_OPENWRT: RTE_OPENWRT,
        RTE_OSX10: RTE_OSX10,
        RTE_OSX: RTE_OSX,
        RTE_RASPBIAN: RTE_RASPBIAN,
        RTE_RHEL: RTE_RHEL,
        RTE_SOLARIS: RTE_SOLARIS,
    }
)

# : mapping of the rte numeric representation to the string value
# num2rte = {
num2rte = ProtectedDict(
    {
        RTE_ARCHLINUX: 'archlinux',
        RTE_BSD: 'bsd',
        RTE_CENTOS: 'centos',
        RTE_DARWIN: 'darwin',
        RTE_DEBIAN: 'debian',
        RTE_EMU: 'emu',
        RTE_FEDORA: 'fedora',
        RTE_LINUX: 'linux',
        RTE_NT: 'nt',
        RTE_OPENBSD: 'openbsd',
        RTE_OPENBSD: 'openbsd',
        RTE_OPENWRT: 'openwrt',
        RTE_OSX10: 'osx10',
        RTE_WPEMU: 'wpemu',
        RTE_POSIX: 'posix',
        RTE_PWEMU: 'pwemu',
        RTE_RASPBIAN: 'raspbian',
        RTE_RHEL: 'rhel',
        RTE_SOLARIS: 'solaris',
        RTE_UNIX: 'unix',
        RTE_WIN32: 'win32',
        RTE_WINDOWS: 'windows',
    }
)

# : For UI of command line tools, load on demand by update()
# : see platformids.map_enum_labels
num2enumstr = ProtectedDict(
    {
        # RTE_POSIX: "RTE_POSIX",
        # RTE_WINDOWS: "RTE_WINDOWS",
    }
)

# : mapping of the rte numeric representation to the pretty string value
# num2pretty = {
num2pretty = ProtectedDict(
    {
        RTE_ARCHLINUX: 'Arch Linux',
        RTE_BSD: "Berkeley Software Distribution",
        RTE_CENTOS: "CentOS",
        RTE_DARWIN: "Darwin",
        RTE_DEBIAN: "Debian",
        RTE_FEDORA: "Fedora",
        RTE_LINUX: "Linux",
        RTE_NT: "NT",
        RTE_OPENBSD: "OpenBSD",
        RTE_WPEMU: "Windows-Emulation",
        RTE_POSIX: "POSIX",
        RTE_PWEMU: "POSIX-Windows-Emulation",
        RTE_RASPBIAN: "Raspbian",
        RTE_RHEL: "RHEL",
        RTE_UNIX: "Unix",
        RTE_WIN32: "Windows",
        RTE_WIN: "Windows",
        RTE_WINDOWS: "Windows",
    }
)

# : registered callbacks for special handling of custom layout
custom_rte_distrel2tuple = ProtectedDict(
    {
        # e.g. RTE_MINIX3: minix.platformids.my_distrel2tuple,
    }
)

# : dynamic registry for custom *category*
custom_category = ProtectedDictEnum(
    custom_min=0x90000000,
    custom_max=0xf0000000,
    custom_offset=0x0fffffff,
)

# : dynamic registry for custom *ostype*
custom_ostype = ProtectedDictEnum(
    custom_min=0x08000000,
    custom_max=0x0f800000,
    custom_offset=0x007fffff,
)

# : dynamic registry for custom *dist*
custom_dist = ProtectedDictEnum(
    custom_min=0x00410000,
    custom_max=0x007f0000,
    custom_offset=0x0000ffff,
)


def get_modlocation(mname, mbase=None, mpaths=None, **kargs):
    """   Calls the *pythonids.get_modulelocation* function with specific default parameters
    for the *platformids*. 
     
    Args:
        mbase:
            Base for module search paths by default within the subdirectory of *platformids*.
            The filepath name with a trailing separator. ::
    
                default := os.path.dirname(__file__) + os.sep
    
            The base path is used within the post-processing of the eventually matched
            path, thus has to be appropriate for each item of *mpaths*. 
    
        mname:
            The relative path of the module in dotted *Python* notation. ::
    
                mname := (
                     <dotted-module-name-str>
                   | <dotted-module-name-path-name-str>
                )
    
        mpaths:
            List of module specific search paths for *platformids*, these
            are relative to *mbase*, ::
    
                default := [
                   'dist',
                   'custom',
                   'net',
                   'embed',
                   '',
                ]

            resulting in::
    
                default := [
                   mbase + 'dist' + os.sep,
                   mbase + 'custom' + os.sep,
                   mbase + 'net' + os.sep,
                   mbase + 'embed' + os.sep,
                   mbase,
                ]
    
        kargs:
            permitrel: 
                Permit the return of relative module names within *mpath*.
                If *False* absolute only, which is relative to an existing
                *sys.path* entry. ::
                   
                    permitrel := (
                       True,       # returns a relative module name if within subtree
                       False       # returns in any case a module name relative to sys.path
                    )            
    
                Sets relative base within *platformids* as the default: ::
    
                    rbase = os.path.normpath(os.path.dirname(__file__)) + os.sep
    
    Returns:
        Returns in case of a match the resulting entry within *sys.modules*::
    
            match -> (<relative-module-name>, <module-file-path-name>,)
       
        The default when no match occured is to rely on the more versatile
        search mechanism of the import implementation of the concrete 
        *Python* implementation for another final trial by the caller::
    
            default -> (<mname>, None,)
    
    Raises:
        PlatformIDsError
            'mbase' does not match 'mpaths'
       
        PlatformIDsPresentError
            missing 'mbase'
       
        pass-through

    """
    # not using sourceinfo package in order to avoid circular dependencies,
    # so keep platformids on lowest possible software-stack level
    _permitrel = kargs.get('permitrel', False)
    if _permitrel:
        rbase = kargs.get('rbase')
        if rbase == None:
            rbase = os.path.normpath(os.path.dirname(__file__) + os.sep) + os.sep
        kargs['rbase'] = rbase 

    if mbase == None:
        mbase = os.path.dirname(__file__) + os.sep
    mbase = os.path.normpath(mbase) + os.sep

    if mpaths == None:
        # default
        mpaths = [
            mbase + 'dist' + os.sep,
            mbase + 'custom' + os.sep,
            mbase + 'net' + os.sep,
            mbase + 'embed' + os.sep,
            mbase ,
        ]
    elif mpaths and mpaths[0]:
        # permit relative to mbase only
        for mi in range(len(mpaths)):
            mpaths[mi] = os.path.normpath(mbase + mpaths[mi]) + os.sep

    elif not mpaths:
        raise PlatformIDsPresentError("missing 'mpaths'")

    if mpaths and not mpaths[0].startswith(mbase):
        raise PlatformIDsError(
            "'mbase' does not match 'mpaths'\nmbase = %s\nmpaths[0] = %s" %(
                mbase, mpaths[0]
                )
            )
    
    return get_modulelocation(mname, mbase, mpaths, **kargs)
    

def decode_version_str_to_segments(v):
    """Split a version string separated by '.' into an integer 
    array. ::
       
        decode_version_str_to_segments('1.22.17')     =>  (1, 22, 17)
        decode_version_str_to_segments('2012.02.17')  =>  (2012, 2, 17)
        decode_version_str_to_segments('10.0.1809')   =>  (10, 0, 1809)
    
    A tiny utility - frequently required.
    
    Args:
        v: Version string with maximal 3 digits::
           
            ('1.2.3')  =>  (1, 2, 3)
            ('1.2')    =>  (1, 2, 0)
            ('1')      =>  (1, 0, 0)
    
    Returns:
        Tuple of *int*. ::
          
            ('1.2.3')  =>  (1, 2, 3)
            ('1.2')    =>  (1, 2, 0)
            ('1')      =>  (1, 0, 0)
    
        In case an error occured::
    
            (0, 0, 0)

    Raises:
        None.

    """

    # see manual
    def tonum(x):
        try:
            return int(x)
        except ValueError:
            if x == '':
                return 0
            raise

    return tuple([tonum(x) for x in VERSNUM.split(v)[1:4]])


def encode_rte_to_32bit(**kargs):
    """Encodes the provided 32bit bitmask of each field into
    the combined integer value of the bitmask vector.
    
    Args:
       kargs:
            category:
                The numeric 32bit bitmask of the category: ::
             
                    category := (
                         <int-enum>
                       | <category-key>
                    )
                    int-enum:     the integer enum, preferbly a predefined value-by-var
                    category-key: the key value as string to be evaluated by one
    
                 of::
                 
                    *rte2num*:      the common mapping dictionary
                    *get_rte2num*:  the function interface for *rte2num*
             
                default is 0
    
            ostype:
                The numeric 32bit bitmask of the ostype::
             
                    ostype := (
                         <int-enum>
                       | <ostype-key>
                    )
                    int-enum:     the integer enum, preferbly a predefined value-by-var
                    ostype-key:   the key value as string to be evaluated by one
    
                of::
             
                    *rte2num*:      the common mapping dictionary
                    *get_rte2num*:  the function interface for *rte2num*
             
                default is 0.
          
            dist:
                The numeric 32bit bitmask of the dist::
          
                    ostype := (
                         <int-enum>
                       | <dist-key>
                    )
                    int-enum:     the integer enum, preferbly a predefined value-by-var
                    dist-key:     the key value as string to be evaluated by one
    
                of::
          
                    *rte2num*:      the common mapping dictionary
                    *get_rte2num*:  the function interface for *rte2num*
          
                default is 0.
          
            distrel:
                The numeric 32bit encoded integer for the distrel, default is 0.
    
    Returns:
        The 32bit compressed bitmask of the RTE.
    
    Raises:
        pass-through
    
    """
    return (
        get_rte2num(kargs.get('category', 0)) | get_rte2num(kargs.get('ostype', 0)) | get_rte2num(kargs.get('dist', 0)) | get_rte2num(kargs.get('distrel', 0))
    )


def encode_rte_segments_to_32bit(**kargs):
    """Converts the numeric base values of the fields into a 32bit bitmask and
    encodes them into the combined integer value of the bitmask vector.
    
    Args:
        kargs:
            category:
                The non-shifted base value of the category::
    
                    category := (
                         <int-val>
                    )
                    int-val:     the relative integer value of the category bits
    
                default is 0
    
            ostype:
                The non-shifted base value of the ostype::
    
                    ostype := (
                         <int-val>
                    )
                    int-val:     the relative integer value of the ostype bits
    
                default is 0.
    
            dist:
                The non-shifted base value of the dist::
    
                    dist := (
                         <int-val>
                    )
                    int-val:     the relative integer value of the dist bits
    
                default is 0.
    
            distrel:
                The non-shifted encoded base value of the distrel, default is 0.
    
    Returns:
        The 32bit compressed bitmask of the RTE.
    
    Raises:
        pass-through

    """
    return (
        kargs.get('category', 0) << 28 | kargs.get('ostype', 0) << 23 | kargs.get('dist', 0) << 16 | kargs.get('distrel', 0)
    )


def fetch_platform_distribution():
    """Scans the platform and returns the complete distribution data prepared for
    common post-processing.
     
    Args:
        none
    
    Returns:
        Returns the information about the current distribution. ::
    
            result := (
               <lowercase-dist-id>,                 # 0: lower case str including release number
               <dist-release-number-str>,           # 1: the release number as string
               <original-literal-release-name>,     # 2: case sensitive release name
               <original-literal-dist-name>,        # 3: case sensitive distribution name
               <dist-release-number-list>,          # 4: release version as list of int
               <lowercase-dist->,                   # 5: lower case str of dist name only
            )
    
    Raises:
        PlatformIDsError
    
    """
    #
    # provides a resulting canonical record, see manual
    # the most reliable and common code is to rely on the configuration files

    # 0: <lowercase-dist-id>,                 # lower case str
    # 1: <dist-release-number-str>,           # string
    # 2: <original-literal-release-name>,     # case sensitive str
    # 3: <original-literal-dist-name>,        # case sensitive str
    # 4: <dist-release-number-list>,          # list of int
    # 5: <lowercase-dist->,                   # lower case str of dist name only
    #

    if category & RTE_POSIX == RTE_POSIX:
        dist = ['', '', '', '', []]

        #
        # a lot has to be evaluated by various extras - including some /etc/*
        # this is in particular the case for derived dist
        #

        if os.path.exists("/etc/redhat-release"):
            # rhel, centos, fedora, sc, oel, ...

            with open("/etc/redhat-release", 'r') as f:
                for l in f:  # hopefully one only
                    if l:
                        dist = re.split(r'(?s)^([^0-9]*) release *([0-9.]*[^ ]*) [^(]*[(]([^)]*)[)][\n\t ]*$', l)

                        if dist[1].startswith('CentOS'):
                            import platformids.dist.centos
                            return tuple(platformids.dist.centos.dist)
                            
                        elif dist[1].startswith('Red H'):
                            import platformids.dist.rhel
                            return tuple(platformids.dist.rhel.dist)
                        
                        elif dist[1].startswith('Fedora'):
                            import platformids.dist.fedora
                            return tuple(platformids.dist.fedora.dist)

                        elif dist[1].startswith('Oracle'):
                            import platformids.dist.oraclelinux
                            return tuple(platformids.dist.oraclelinux.dist)

                        else:
                            dist.pop(0)

            dist[0] = dist[0].lower() + re.sub(r'[.-_]', '', dist[1])
            dist.append(dist[3].lower())
            return tuple(dist)

        elif os.path.exists("/etc/armbian-release"):
            import platformids.embed.armbian
            return tuple(platformids.embed.armbian.dist)

        elif os.path.exists("/etc/arch-release"):
            # loads ArchLinux defines, a later stage loads an eventually derived distribution
            import platformids.dist.archlinux
            return tuple(platformids.dist.archlinux.dist)

        elif os.path.exists("/etc/alpine-release"):
            # loads ArchLinux defines, a later stage loads an eventually derived distribution
            import platformids.dist.alpinelinux
            return tuple(platformids.dist.alpinelinux.dist)

        elif os.path.exists("/etc/gentoo-release"):
            # loads ArchLinux defines, a later stage loads an eventually derived distribution
            import platformids.dist.gentoo
            return tuple(platformids.dist.gentoo.dist)

        elif os.path.exists("/etc/os-release"):
            # debian, raspbian, etc.
            # openSUSE
            # sles???

            if os.path.exists("/etc/debian_version"):
                dist = ['debian', '', '', 'Debian', '']
                with open("/etc/debian_version", 'r') as f:
                    for l in f:
                        dist[1] = re.split(r'(?s)^([0-9.]*).*$', l)[1]
                        dist[4] = decode_version_str_to_segments(dist[1])

            else:
                dist = ['', '', '', '', '']

            _ver = ''
            _name = ''

            with open("/etc/os-release", 'r') as f:
                for l in f:
                    if l.startswith('ID='):
                        dist[0] = DSKORG_ID.sub(r'\1', l)
                    elif l.startswith('VERSION='):  # priority though more widespread
                        _ver = l
                    elif l.startswith('VERSION_ID=') and not _ver:  # Ubuntu, redundant in Slackware
                        _ver = l
                    elif l.startswith('NAME='):
                        _nam = l

            if dist[0].startswith('raspbian'):
                import platformids.embed.raspbian
                return tuple(platformids.embed.raspbian.dist)

            elif dist[0].startswith('kali'):
                import platformids.net.kali
                return tuple(platformids.net.kali.dist)

            elif os.path.exists("/etc/openwrt_release"):
                import platformids.net.openwrt
                return tuple(platformids.net.openwrt.dist)

            elif dist[0].startswith('debian'):
                import platformids.dist.debian
                return tuple(platformids.dist.debian.dist)

            elif dist[0].startswith('ubuntu'):
                import platformids.dist.ubuntu
                return tuple(platformids.dist.ubuntu.dist)

            elif dist[0].startswith('opensuse'):
                import platformids.dist.opensuse
                return tuple(platformids.dist.opensuse.dist)

            else:
                # loads module in second stage only by direct import
                
                _l = DSKORG_RELEASE.split(_ver)
                dist.append(dist[0])
                dist[0] += re.sub(r'[.]', '', _l[1])
                dist[1] = _l[1]
                dist[3] = re.sub(r'NAME=(.*)[\n]*', r'\1', _nam)
                dist[2] = dist[3] + '-' + _l[1]
                dist[4] = decode_version_str_to_segments(_l[1])

                return tuple(dist)

        elif (os.path.exists('/etc/pfSense-rc')):
            import platformids.net.pfsense
            return tuple(platformids.net.pfsense.dist)

        elif (
                sys.platform.startswith('openbsd')  # OpenBSD - CPython, PyPy, IPython
                or
                os.path.exists('/bsd.booted')  # OpenBSD - match on Jython
            ):
            import platformids.dist.openbsd
            return tuple(platformids.dist.openbsd.dist)

        elif (
                sys.platform.startswith('cygwin')
                or
                os.path.exists('/cygdrive')  # rely on standard path only for now
            ):
            # Cygwin is a bit special as it mimics POSIX,
            # but runs the OS windows.
            import platformids.dist.cygwin
            return tuple(platformids.dist.cygwin.dist)
            
        elif (
                sys.platform.startswith('freebsd')  # FreeBSD - CPython, PyPy, IPython
                or
                os.path.exists('/etc/freebsd-update.conf')  # FreeBSD - match on Jython
            ):
            import platformids.dist.freebsd
            return tuple(platformids.dist.freebsd.dist)

        elif (
                sys.platform.startswith('netbsd')  # NetBSD - CPython, PyPy, IPython
                or
                os.path.exists('/etc/netbsd-update.conf')  # NetBSD - match on Jython
            ):
            import platformids.dist.netbsd
            return tuple(platformids.dist.netbsd.dist)

        elif (
                sys.platform.startswith('sunos5')  # Solaris10 + Solaris11 - CPython, PyPy, IPython
                or
                os.path.exists('/etc/release')  # Solaris10 + Solaris11 - match on Jython
            ):
            import platformids.dist.solaris
            return tuple(platformids.dist.solaris.dist)

        elif (
                sys.platform.startswith('darwin')  # Solaris10 + Solaris11 - CPython, PyPy, IPython
                or
                os.path.exists('/System/Library/Components/AppleScript.component')  # Solaris10 + Solaris11 - match on Jython
            ):
            import platformids.dist.darwin
            return tuple(platformids.dist.darwin.dist)

        else:
            try:
                # default for unknown POSIX system
                _u = os.uname()  # @UndefinedVariable
                dist = [
                    '',
                    re.sub(r'([0-9.]*).*', '\1', _u[2]),
                    '',
                    re.sub(r'([a-zA-Z-_]*).*', '\1', _u[0]),
                    '',
                ]
                dist[0] = dist[3].lower()
                dist[2] = dist[3] + '-' + dist[1]
                dist[4] = dist[1].split('.')
                dist.append(dist[3].lower())
                return tuple(dist)

            except:
                return ('', '', '', '', '', '',)

    elif category & RTE_WIN32 == RTE_WIN32:
        #
        # windows support of NT-releases including Windows10IoT
        #
        from platformids.dist.windows import WinVersion
        return tuple(WinVersion().readout_versioninfo_ext())

    else:
        raise PlatformIDsError("Platform not supported: " + str(osname))


def fetch_platform_distribution_num():
    """The numeric version of 'fetch_platform_distribution'.

    Args:
        none
    
    Returns:
        Returns the information about the current distribution. ::
    
          result := (
             #dist,                              # 0: distribution identifier
             #distrel,                           # 1: distribution release identifier
             #dist-release-number-list>,         # 2: release version as list of int
          )
    
    Raises:
        PlatformIDsError
    
    """
    #
    # provides a resulting canonical record, see manual
    #
    # 0: <category>,                        # category
    # 1: <ostype>,                          # ostype
    # 2: <dist>,                            # dist
    # 3: <distrel>,                         # distrel
    # 4: <hexversion>,                      # hexversion of platform distribution release
    # 5: <producttype>,                     # producttype
    #
    return (
        fetch_category(),
        fetch_ostype(),
        fetch_dist(),
        0,
        fetch_rte_hexversion(),
        0,
    )


def fetch_platform_os():
    """Scans the platform and returns the information on the OS including 
    the name and the release version.

    The name of the OS is commonly basically the kernel name. The *ostype*
    of *linux* has one common kernel only, while OS in the *bsd* and
    *unix* family commonly have distribution specific customized kernels.
    
    Args:
        none
    
    Returns:
        Returns the information about the current os. ::
    
            res = (
               <lowercase-os-id>,            # osname: lower case str of os name
               <os-release-number-str>,      # osrel: string of os release version
               <os-release-number-list>,     # osrel: list of int of os release version
               <lowercase-os-rel-id>,        # osname+osrel: lower case str rel + id
            )
    
    Raises:
        PlatformIDsError
       
    """
    if isJython:
        # Jython uname targets the JVM - need the actual underlying OS
        on = PRENONNUM.sub(r'\1', platform.System.getProperty('os.name').lower())  # @UndefinedVariable
        ov = decode_version_str_to_segments(platform.System.getProperty('os.version'))  # @UndefinedVariable
        return (
            on,
            '%d.%d.%d' % ov,
            ov,
            on + '-%d.%d.%d' % ov
            )

    k = platform.uname()

    if osname == 'posix':
        if k[0][-3:] == 'BSD':
            # the kernel release is the same as the distrel
            ov = decode_version_str_to_segments(k[2])
            return(
                k[0],
                k[2],
                ov,
                "%s%d%d" % (k[0], ov[0], ov[1])
                )

        elif k[0] == 'SunOS':
            if k[2] == '5.10':
                # assume this release version more or less static for now
                _patch = re.compile(r'Generic_([0-9]*)-([0-9]*)')  # e.g. Generic_147148-26 -> 14714826
                _p = _patch.sub(r"\1\2", k[3])
                return(
                    'sunos',
                    '5.10.0',
                    (5, 10, 0, int(_p)),
                    'sunos5100'
                    )

            elif k[2] == '5.11':
                # for now - until 2021++??? - the future of Solaris remains nebulous and unsafe
                ver = decode_version_str_to_segments(k[3])
                return(
                    'sunos',
                    '5.' + k[3],
                    (5, 11, int(ver[-2])),
                    'sunos511' + str(ver[-2])
                    )

        ov = decode_version_str_to_segments(k[2])
        return (
            k[0].lower(),
            "%d.%d.%d" % (ov[0], ov[1], ov[2],),
            ov,
            "%s%d%d%d" % (k[0].lower(), ov[0], ov[1], ov[2],)
            )

    elif osname == 'nt':

        if k[0] == 'Windows':
            ov = decode_version_str_to_segments(k[2])
            return (
                'nt100',
                k[2],
                ov,
                "%s%d%d%d" % (k[0], ov[0], ov[1], ov[2],)
                )

        ov = decode_version_str_to_segments(k[3])
        return (
            k[0].lower(),
            k[3],
            ov,
            "%s%d%d%d" % (k[0], ov[0], ov[1], ov[2],)
            )

    else:
        raise Exception("Platform not supported: " + str(osname))


def fetch_platform_os_num():
    """The numeric version of '`fetch_platform_os <#fetch-platform-os>`_'.

    Args:
        none
    
    Returns:
        Returns the information about the current os. ::
    
            res = (
               <enum-os-id>,                 # osname: lower case str of os name
               <32bit-os-release-number>,    # osrel: string of os release version
               <os-release-number-list>,     # osrel: list of int of os release version
               <enum-os-rel-id>,             # osname+osrel: lower case str rel + id
            )
    
    Raises:
        PlatformIDsError

    """
    #
    # provides a resulting canonical record, see manual
    #
    # 0: <numeric-dist-id>,                 # lower case str
    # 1: <dist-release-number-str>,         # enum
    # 2: <original-literal-release-name>,   # case sensitive str
    # 3: <numeric-dist>,                    # enum
    # 4: <dist-release-number-list>,        # list of int
    # 5: <numeric-dist->,                   # enum
    #
    _r = fetch_platform_os()
    return (
        get_rte2num(_r[0]),
        0,
        0,
        get_rte2num(_r[3]),
        0,
        get_rte2num(_r[5]),

    # 0: <lowercase-dist-id>,                 # lower case str
    # 1: <dist-release-number-str>,           # string
    # 2: <original-literal-release-name>,     # case sensitive str
    # 3: <original-literal-dist-name>,        # case sensitive str
    # 4: <dist-release-number-list>,          # list of int
    # 5: <lowercase-dist->,                   # lower case str of dist name only

    )


def fetch_category():
    """Scans the platform and returns the numeric id for the current *category*.

    Args:
        none
    
    Returns:
        Returns the *category*. ::
    
            res = <category-bits><ostype-bits-zero><dist-bits-zero><distrel-bits-zero> 
    
    Raises:
        PlatformIDsError
    
    """
    try:
        return rte2num[osname]
    except KeyError:
        raise Exception("Platform category not supported: " + str(osname))


def fetch_ostype():
    """Scans the platform and returns the numeric id for the current *ostype*.

    Args:
        none
    
    Returns:
        Returns the *ostype* as integer enum. The bitmask includes 
        the *category*. ::
    
            res = <category-bits><ostype-bits><dist-bits-zero><distrel-bits-zero> 
    
    Raises:
        PlatformIDsError

    """
    if osname == 'posix':
        if isJython:
            # _os = sys.getNativePlatform() # Available for 2.7.1+
            # _os = platform.System.getProperty('os.name').lower()  # @UndefinedVariable  # seems 2.0+
            try:
                return rte2num[platform.System.getProperty('os.name').lower()] & RTE_OSTYPE  # @UndefinedVariable
            except KeyError:
                k = platform.dist() 
                raise Exception("OS type not supported: %s.%s (platform.dist=%s)" % (str(osname), str(k[0]), str(k)))

        else:
            k = platform.uname()
            if k[0] == 'Linux':
                return RTE_POSIX | RTE_LINUX

            elif k[0][-3:] == 'BSD':
                return RTE_POSIX | RTE_BSD

            else:
                try:
                    # results on most supported OS for sys.platform:
                    #
                    #   correct as ostype, with minor fuzz
                    #      cygwin, darwin
                    #      linux, linux2
                    #      sunos5
                    #      win32
                    #
                    #   not exactly correct, these are distributions or almost distribution-releases
                    #      dragonfly5, freebsd11, netbsd8, openbsd6
                    #
                    #      minix3
                    #
                    #   some additional non-ostype
                    #      cli
                    #      java10.0.1, java11.0.2, java1.8.0_131, ... the jre/jdk - the world is encapsulated...

                    #
                    # SOLUTION: matches pre-registered and isolates ostype
                    #
                    return  rte2num[sys.platform] & RTE_OSTYPE

                except KeyError:
                    k = platform.dist()
                    raise Exception("OS type not supported: %s.%s (platform.uname=%s)" % (str(osname), str(k[0]), str(k)))

    elif osname == 'nt':
        return RTE_WIN | RTE_NT

    else:
        # default pure dynamic by registration
        try:
            return rte2num[k[0].lower()] & RTE_OSTYPE  # @UndefinedVariable
        except KeyError:
            raise Exception("Platform not supported: " + str(osname))


def fetch_dist():
    """Scans the platform and returns the numeric id for the current *dist*.

    Args:
        none
    
    Returns:
        Returns the *dist* as integer enum. The bitmask includes 
        the *category* and *ostype*. ::
    
            res = <category-bits><ostype-bits><dist-bits><distrel-bits-zero> 
    
    Raises:
        PlatformIDsError
    
    """
    _d = fetch_platform_distribution()
    try:
        return rte2num[_d[5]]
    except KeyError:
        return get_rte2num(_d[5])


def fetch_dist_tuple():
    """Scans the platform and returns the complete tuple for the current *dist*.

    Args:
        none
    
    Returns:
        Returns the complete tuple of information related to a distribution. ::
    
            res = (<distid-string>, <distrel-string>, <distrel-tuple>, <ditst-rel-key-string>)
    
    Raises:
        PlatformIDsError

    """
    _d = fetch_platform_distribution()
    return (
        _d[5],
        _d[1],
        _d[4],
        _d[0],
        )


#
# first try the pre-scanned module offline created by setup.py
#
_impmodname = None
try:
    with open(os.path.dirname(__file__) + os.sep + "setup_platform", 'r') as f:
        _impmodname = f

#
#         if
#         for l in f:
#
#                     dist = re.split(r'(?s)^([^0-9]*) release *([0-9.]*[^ ]*) [^(]*[(]([^)]*)[)][\n\t ]*$', l)
#                     dist.pop(0)
#                     dist[-1] = dist[0]
except:
    pass

#
# assign numeric value for current run time environment for dist(or windows)
# the resulting value bootstraps the load of the details of the release distrel
# exceptions:
#   some known are pre-loaded: windows
#   some known are hardcoded: see previous defines, e.g. some major Linux dists
#
# try to resolve the hierarchy as deep as possible
# it is basically the pre-load bootstrap, so the database is not reliable yet for non-standard
#
if osname == 'posix':
    if (
            os.path.exists("/etc/redhat-release") or
            os.path.exists("/etc/os-release")
        ):
        try:
            RTE = rte2num[fetch_platform_distribution()[5]]
        except KeyError:
            for r in rte2num.keys():
                # iterate for something seems to be known
                # ATTENTION: there are ambiguities, e.g. for debian derived
                if type(r) in ISINT:
                    continue
                if sys.platform.startswith(r):
                    RTE = rte2num[r]

            else:
                # for now we only know the category
                RTE = RTE_POSIX

    elif sys.platform.startswith('openbsd'):
        RTE = RTE_OPENBSD

    elif sys.platform.startswith('darwin'):
        RTE = RTE_DARWIN

    elif os.path.exists("/etc/openwrt_release"):
        RTE = RTE_OPENWRT

    elif sys.platform.startswith('sunos5'):
#        RTE = RTE_UNIX
        RTE = RTE_SOLARIS

    elif sys.platform.startswith('cygwin'):
        RTE = RTE_PWEMU

    else:
        RTE = RTE_POSIX

elif osname == 'nt':
    # due to required special handling loads initially the complete windows set
    RTE = RTE_WIN32

elif osname == 'java':
    # it is jython,
    # so have to pierce the encapsulation for getting the native platform parameters - want to do it in Python

    RTE = 0
    try:
        _snp = sys.getNativePlatform()  # @UndefinedVariable
        RTE = rte2num[_snp]

    except (NameError, AttributeError):
        if platform.linux_distribution()[0]:
            RTE = RTE_LINUX

            if os.path.exists("/etc/openwrt_release"):
                RTE = RTE_OPENWRT

            elif (
                    os.path.exists("/etc/redhat-release") or
                    os.path.exists("/etc/os-release")
                ):
                try:
                    RTE = rte2num[fetch_platform_distribution()[5]]
                except KeyError:
                    for r in rte2num.keys():
                        if type(r) in ISINT:
                            continue
                        if platform.linux_distribution()[0].lower().startswith(r):
                            RTE = rte2num[r]
                    else:
                        RTE = RTE_POSIX

#             elif sys.platform.startswith('openbsd'):
#                 RTE = RTE_OPENBSD
#
#             elif sys.platform.startswith('sunos5'):
#                 RTE = RTE_SOLARIS
#
#             elif sys.platform.startswith('darwin'):
#                 RTE = RTE_DARWIN
#
            elif sys.platform.startswith('cygwin'):
                RTE = RTE_PWEMU

            else:
                RTE = RTE_POSIX

        elif platform.mac_ver()[0]:
            RTE = RTE_DARWIN
        elif platform.win32_ver()[0]:
            RTE = RTE_WIN32

    if not RTE:
        raise PlatformIDsError("Unknown platform: " + str(_snp))

else:
    raise Exception("Platform not supported")

#
# check setup dist exists, if not try dynamic evaluation
#
if not _impmodname or not os.path.exists(_impmodname):
    try:
        _impmodname = num2rte[RTE]

    except KeyError:
        if RTE == RTE_WIN32:
            _impmodname = 'windows'
        else:
            raise PlatformIDsError("not supported, requires:" + str(num2rte.values()))

#
# once the bootstrap module is selected load it
# loads the required module only for the current dist(or windows)
#
modnamerel, modfpath = get_modlocation(_impmodname) 
if modfpath == None:

    # system data - prohibit redefinition of present system data
    if RTE & RTE_WIN32 or (RTE & RTE_PWEMU) == RTE_PWEMU:
        mbase_altbase = os.environ['CommonProgramFiles'] + os.sep + 'platformids'
    else:
        mbase_altbase = os.sep + 'etc' + os.sep + 'platformids'

    # alternate data - prohibit redefinition of present data
    if not os.path.exists(mbase_altbase):
        mbase_altbase = os.getenv('PLATFORMIDS_ALTBASE', None)
    
    if mbase_altbase != None:
        modnamerel, modfpath = get_modlocation(_impmodname, mbase=mbase_altbase, )

    # user data
    if RTE & RTE_WIN32 or (RTE & RTE_PWEMU) == RTE_PWEMU:
        mbase_altbase = os.environ['LOCALAPPDATA'] + os.sep + 'platformids'
        if not os.path.exists(mbase_altbase) and RTE & RTE_LINUX:
            mbase_altbase = os.environ['HOME'] + os.sep + '.config' + os.sep + 'platformids'
    if not mbase_altbase or not os.path.exists(mbase_altbase):
        mbase_altbase = os.environ['HOME'] + os.sep + 'platformids'

try:
    # load module by file system path name
    load_module(_impmodname, modfpath)
except KeyError:
    # continue with generic
    pass


def fetch_rte_hexversion():
    """Retrieves the bitmask encoding for current runtime environemnt.
    
    Args:
        None.
    
    Returns:
        The encoded bitmask to be used for caching and *RTE*.
    
    Raises:
        pass-through
    
    """
    ret = 0
    try:
        _pi = fetch_platform_distribution()
        ret = rte2num[_pi[0]]
        # here it is at least one defined as present

    except KeyError:
        # no mapping available,

        # try next 'nearest' version to be expected compatible - for now cutting minor version numbers,
        # if not found step up the hierarchy "category.ostype.dist.distrel"

        #
        # TODO: adapt a better strategy, decrement major version - BUT for all platform version schemes!
        #

        # 1. try version steps
        for rx in range(len(_pi[4]), 0, -1):
            _k = _pi[5] + ''.join((str(x) for x in _pi[4][:rx]))
            try:
                ret = rte2num[_k]

            except KeyError:
                pass

        if not ret:
            try:
                # 2. try dist name
                ret = rte2num[_pi[5]]

            except KeyError:
                try:
                    # 3. try ostype
                    ret = rte2num[fetch_platform_os()[0]]

                except KeyError:
                    try:
                        # 4. try category

                        ret = rte2num[fetch_platform_distribution()]

                    except KeyError:

                        ret = rte2num[fetch_platform_os()]

    return ret


#
# here we have the *dist*, so now set the actual release of the distribution *distrel*, when present
RTE = fetch_rte_hexversion()

#
# set: generic
#

# : Use the current block-offset only,
# : results in the current platformm enum.
RTE_GENERIC = RTE & RTE_POSIX & RTE_WIN32

# : Dyanmic local platform, synonym for generic.
RTE_LOCAL = RTE_GENERIC + 1


def decode_rte_category_to_num(rte=RTE):
    """Decodes the compressed category from the 32bit integer bitmask
    into the corresponding integer enum.
    
    Args:
        rte:
            The comppressed runtime environment identifier bitmask.
            
            default := RTE
             
    Returns:
        Integer value of the category enum.
     
    Raises:
        pass-through
    
    """
    return (get_rte2num(rte) & RTE_CATEGORY)


def decode_rte_ostype_to_num(rte=RTE):
    """Decodes the compressed ostype from the 32bit integer bitmask
    into the corresponding integer enum.
    
    Args:
        rte:
            The comppressed runtime environment identifier bitmask.
            
            default := RTE
    
    Returns:
        Integer value of the ostype enum.
     
    Raises:
        pass-through
    
    """
    return (get_rte2num(rte) & RTE_OSTYPE)


def decode_rte_dist_to_num(rte=RTE):
    """Decodes the compressed dist from the 32bit integer bitmask
    into the corresponding integer enum.
    Recognizes the *ostype* domain e.g. for *RTE_NT*.
    
    Args:
        rte:
            The comppressed runtime environment identifier bitmask.
             
            default := RTE
    
    Returns:
        Integer value of the dist enum.
     
    Raises:
        pass-through

    """
    return (get_rte2num(rte) & RTE_DIST)


def decode_rte_distrel_to_num(rte=RTE):
    """Decodes the compressed distrel from the 32bit integer bitmask
    into the corresponding integer enum.
    Recognizes the *ostype* and *dist* domain, the distrel 
    extension flag.
    
    Args:
        rte:
            The comppressed runtime environment identifier bitmask.
             
            default := RTE
    
    Returns:
        Integer value of the encoded distrel.
     
    Raises:
        pass-through

    """
    return (get_rte2num(rte) & RTE_DISTREL)


def decode_rte_distrel_to_segments(rte=RTE):
    """Decodes the compressed distrel from the 32bit integer bitmask
    into the corresponding tuple of integer segments.
    
    This is probably one of the most important functions, because
    it has the knowledge to split *distrel* including calling
    a custom-callback function when required.
    Recognizes the *ostype* and *dist* domain, the *distrel* 
    extension flag in order to determine the further processing.
    The supported special cases of known and pre-loaded standard
    distributions are hardcoded for better performance here,
    currently these are: ::
    
        ArchLinux, KaliLinux
        Windows-NT
        
        BlackArch, Gentoo, 
        Armbian, ArchLinux, BlackArch, Gentoo, KaliLinux
    
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

    """
    try:
        _rte = rte2num[rte]
        
    except KeyError:
        if type(rte) in ISINT:
            # can split basically any number, let's see...
            _rte = rte

        elif decode_version_str_to_segments(rte):
            # assume is a valid version string
            return decode_version_str_to_segments(rte)

        else:
            raise PlatformIDsUnknownError("Not registered distrel = " + str(rte))

    if _rte & RTE_OSTYPE == RTE_NT:
        # known specials - Windows-NT
        return (
            _rte & 0xffff,
            0,
            0,
            )

    elif _rte & RTE_OSTYPE == RTE_LINUX and _rte & RTE_DISTEXT:
        if (_rte & RTE_DIST) in (RTE_KALI, RTE_ARCHLINUX,):
            # known specials - date based rolling distros
            # fixed offset to 1970 - the UNIX-time
            return (
                ((_rte & 0xfe00) >> 9) + 1970,
                (_rte & 0x01e0) >> 5,
                _rte & 0x001f,
                )

        elif _rte & RTE_DIST in custom_rte_distrel2tuple.keys():
            # registered specials - call custom callback
            return custom_rte_distrel2tuple[_rte & RTE_DIST](rte)

    # default handler - see docu for '3-number-default'
    return (
        (_rte & 0xfc00) >> 10,
        (_rte & 0x03e0) >> 5,
        _rte & 0x001f,
        )


def decode_rte_to_segments(rte=RTE):
    """Decodes the compressed components from the 32bit integer bitmask
    into the corresponding segments of relative integer values.
    
    Args:
        rte:
            The comppressed runtime environment identifier bitmask.
             
            default := RTE
             
    Returns:
        Tuple of integer values of the components. ::
    
           ret := =>  (#category-bits, #ostype-bits, #dist-bits, #distrel-bits)
    
        Where the following os true: ::
            
           rte == #category-bits << 28 | #ostype-bits << 23 | #dist-bits << 16 | #distrel-bits
           rte == encode_rte_segments_to_32bit(#category-bits, #ostype-bits, #dist-bits, #distrel-bits)
           rte == encode_rte_segments_to_32bit( *decode_rte_to_segments( rte ) )
    
    Raises:
        pass-through

    """
    rte = get_rte2num(rte)
    return ((rte & RTE_CATEGORY_B), (rte & RTE_OSTYPE_B), (rte & RTE_DIST_B), (rte & RTE_DISTREL_B))


def decode_rte_to_tuple(rte=RTE):
    """Decodes the compressed components from the 32bit integer bitmask
    into the corresponding tuple of partial integer enums.
    
    Args:
        rte:
            The comppressed runtime environment identifier bitmask.
             
            default := RTE
             
    Returns:
        Tuple of integer values of the components. ::
    
           ret := =>  (#category-num, #ostype-num, #dist-num, #distrel-num)
    
        Where the following os true: ::
            
           ret == #category-num | #ostype-num | #dist-num | #distrel-num
           ret == #category-num + #ostype-num + #dist-num + #distrel-num
    
    Raises:
        pass-through

    """
    rte = get_rte2num(rte)
    return ((rte & RTE_CATEGORY), (rte & RTE_OSTYPE), (rte & RTE_DIST), (rte & RTE_DISTREL))


def decode_rte_to_tuple_str(rte=RTE):
    """Decodes the compressed components from the 32bit integer bitmask
    into the corresponding tuple of string keywords.
    
    Args:
        rte:
            The comppressed runtime environment identifier bitmask.
             
            default := RTE
             
    Returns:
        Tuple of keywords of string values for the components. ::
    
           ret := =>  (<category>, <ostype>, <dist>, <distrel>)
     
    Raises:
        pass-through
    
    """
    try:
        try:
            _rte = rte2num[rte]  # requires registered strings
        except KeyError:
            if type(rte) not in ISINT:
                # currently converting strings only if registered
                raise
            
            # so is an numeric rte - seems at least to be
            _rte = rte
            
        if (_rte & RTE_OSTYPE) == RTE_NT:
            #
            return (
                get_num2rte(_rte & RTE_CATEGORY),
                get_num2rte(_rte & RTE_OSTYPE),
                get_num2rte(_rte & RTE_DIST),
                get_num2rte(_rte & RTE_DIST) + str(_rte & RTE_DISTREL_B)
                )

        elif _rte & RTE_DISTEXT:
            #
            return (
                get_num2rte(_rte & RTE_CATEGORY),
                get_num2rte(_rte & RTE_OSTYPE),
                get_num2rte(_rte & RTE_DIST),
                get_num2rte(_rte & RTE_DISTREL)
                )


        else:
            # default handler - with expected table entries
            return (
                num2rte[(_rte & RTE_CATEGORY)],
                num2rte[(_rte & RTE_OSTYPE)],
                num2rte[(_rte & RTE_DIST)],
                num2rte[(_rte & RTE_DISTREL)]
                )

    except:
        if type(rte) in ISINT:
            pass

def get_num2rte(num):
    """Gets the corresponding string representation
    for the string numeric value.
     
    Alternatively the official dict *num2rte*
    could be used. 
     
    Args:
        num:
            Numeric enum value of the requested platform.
    
    Returns:
        The string value, or *None**.
    
    Raises:
        None

    """
    if type(num) not in ISINT:
        return str(num)
    return num2rte.get(num)


def get_rte2num(rte):
    """Gets corresponding numerical representation
    for the numeric or string value.
     
    Alternatively the official dict *rte2num*
    could be used. 
    
    Args:
        rte:
            Numeric enum value or string representation
            of the requested platform.
    
    Returns:
        The numeric value, or *None**.
    
    Raises:
        None

    """
    if type(rte) in ISINT:
        return rte

    #
    # do not want to mix it up with platforms due to arising circular dependencies than
    #

    try:
        return rte2num.get(rte)
    except TypeError:
        raise PlatformIDsError(
            "TypeError: requires a valid key for 'platformids.rte2num' (int, str)- got:" + str(type(rte)))


def set_num2rte(key, value):
    """Sets the numeric to string map.
    
    Alternatively the official dict *num2rte*
    could be used. 
     
    Args:
        key:
            Numeric key value.
    
        value:
            String value.
    
    Returns:
        None
    
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
        key:
            Numeric or string key value.
    
        value:
            Numeric value.
    
    Returns:
        None
    
    Raises:
        None

    """
    if type(value) != int:
        raise PlatformIDsError("requires an int value, got: " + str(value))
    rte2num[key] = value

# 4debug
pass

