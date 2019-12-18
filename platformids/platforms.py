# -*- coding: utf-8 -*-
"""The module 'platforms' provides the class for the representation of platform parameters.
This includes the scan of the current platform and the calculation of arbitrary hexadecimal
labels for the fast processing of repetitive comparisons.

The supported implementations are: CPython, IPython, IronPython, Jython, and PyPy.

"""
#############################################
#
# See manuals for the detailed API.
#
#############################################

from __future__ import absolute_import
from __future__ import print_function

import sys
import platform
import re


from pythonids.pythondist import ISINT
# from platformids import _debug, _verbose
import platformids
from platformids import RTE, ISSTR, RTE_DIST, RTE_GENERIC


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.35'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__docformat__ = "restructuredtext en"


# : The corresponding *bash* environment names for print out.
bash_map = {
    'category': "CATEGORY",
    'dist': "DIST",
    'distrel': "DISTREL",
    'distrel_hexversion': "distrel_hexversion",
    'distrel_key': "DISTRIBUTION_KEY",
    'distrel_name': "DISTRIBUTION_NAME",
    'distrel_version': "DISTRIBUTION_VERSION",
    'ostype': "OSTYPE",
    'ostype_id': "OS_ID",
    'ostype_version': "OS_VERSION",

    'cpu': "CPU",
    'cpudata': "CPUDATA",
}

# : The mapping of attributes to values for pretty print.
attribute_map = {
    'category': "category",
    'dist': "dist",
    'distrel': "distrel",
    'distrel_hexversion': "distrel_hexversion",
    'distrel_key': "distribution_key",
    'distrel_name': "distribution_name",
    'distrel_version': "distribution_version",
    'ostype': "ostype",
    'ostype_id': "ostype_id",
    'ostype_version': "ostype_version",

    'cpu': "cpu",
    'cpudata': "cpudata",
}

if platformids.osname in ('nt', 'cygwin'):
    #
    # specials for ostype NT for bash print outs and pretty print
    #
    bash_map.update({
        'wServicePack': "WSERVICEPACK",
        'wProductType': "WPRODUCTTYPE",
        'wSuiteMask': "WSUITEMASK",
    })

    attribute_map.update({
        'wServicePack': "wServicePack",
        'wProductType': "wProductType",
        'wSuiteMask': "wSuiteMask",
    })


class PlatformParametersError(platformids.PlatformIDsError):
    pass


class PlatformParameters(object):
    
    def __init__(self, *args, **kargs):
        """Creates an empty object.
        No automatic call of *PlatformParameters.scan()*.
        The instance could be either initialized by the provided
        parameters, or remains empty - which is zero *0*.
        
        Each call of *PlatformParameters.scan()* replaces the previous
        values.
        
        Args:
            args:
                Optional positional parameters in the following order.
                  The corresponding keyword-arguments dominate. ::
           
                    args[0] := category
                    args[1] := ostype
                    args[2] := dist
                    args[3] := distrel
        
            kargs:
                category:
                    The *category* for initialization.
                     
                    default := 0
                
                ostype:
                    The *ostype* for initialization.
                     
                    default := 0
                 
                dist:
                    The *dist* for initialization.
                     
                    default := 0
                 
                distrel:
                    The *distrel* for initialization.
                     
                    default := 0

           Returns:
                Initial instance, optionally initialized by the provided
                parameters. 
        
           Raises:
                pass-through

        """
        self.category = self.ostype = self.distrel_hexversion = self.wProductType = self.wSuiteMask = 0
        self.dist = self.distrel = 0
        self.distrel_name = self.distrel_key = ''
        self.ostype_id = self.ostype_id = ''
        self.distrel_version = self.ostype_version = []

        #
        # first check positional arguments
        #
        self.osrel_sp = []
        _myargs = list(args)
        if _myargs:
            self.category = _myargs[0]  #: category
            _myargs.pop(0)
        if _myargs:
            self.ostype = _myargs[0]  #: ostype - cumulated sub-vector
            _myargs.pop(0)
        if _myargs:
            self.dist = _myargs[0] #: dist - cumulated sub-vector
            _myargs.pop(0)
        if _myargs:
            self.distrel_hexversion = self.distrel = _myargs[0] #: distrel - cumulated sub-vector
            # _myargs.pop(0)

        #
        # second check keyword arguments, when present superpose current values
        #
        self.category = kargs.get('category', self.category)
        self.ostype = kargs.get('ostype', self.ostype)
        self.dist = kargs.get('dist', self.dist)
        self.distrel_hexversion = self.distrel = kargs.get('distrel', self.distrel)

    def __and__(self, other):
        """The *&* operator for the resulting *hexversion*: ::
     
            self-bitmask & other-bitmask
        
        Args:
            other:
                The bitmask for operations. ::
        
                    other := (
                        <int-32bit-mask>                   # compare with hexversion 
                      | <dictionary>)                      # compare keys only
                      | <tuple>)                           # compare key-index only
                      | <instance-of-PlatformParameters>   # compare both hexversions
                    )
           
        Returns:
            The resulting bitmask as numeric value.
        
        Raises:   
            pass-through

        """
        if not self.distrel_hexversion:
            self.distrel_hexversion = self.get_hexversion()

        if isinstance(other, int):
            return self.distrel_hexversion & other

        elif isinstance(other, PlatformParameters):
            return self.distrel_hexversion & other.get_hexversion()

        elif isinstance(other, dict):
            # use other as init parameters - simply trust or pass exception
            return self.distrel_hexversion & PlatformParameters(**other).get_hexversion()

        elif isinstance(other, tuple):
            return self.distrel_hexversion & PlatformParameters(*other).get_hexversion()

        raise platformids.PlatformIDsError("type not supported: other = " + str(other))
    
    def __eq__(self, other):
        """Supports standard comparison with the types
        *PlatformParameters*, and *dict*. In case of
        a dict the attributes are used as keys literally.
             
        Args:
            other:
                The instannce to be compared. The comparison is provided as:
                
                * literal contents of objects: 
                
                  literally for objects *PlatformParameters*, or partially
                  for *dict*.
                
                * partial hierarchical matches           
                
                  The partial comparison is based on the keys provided by
                  the dictionary argument. Only attributes with a corresponding
                  key are compared.
                
                  The following items are handled specially:
                
                    distrel_version, ostype_version:
                        The present values are compared only, e.g. 
                        the following is considered as *True* ::
                
                           self.distrel_version = [1, 2, 3]
                           other.distrel_version = [1, 2,]
                
                           TRUE: self.distrel_version == other.distrel_version
                
                        While still: :: 
                
                           self.distrel_version = [1, 2, 3]
                           other.distrel_version = [1, 2, 7]
                
                           FALSE: self.distrel_version == other.distrel_version
                
                      distrel:
                        Valuesa are compared by *startswith()* e.g. 
                        the following is considered as *True* ::
                
                           self.distrel  = 'fedora-27.0.0'
                           other.distrel = 'fedora-27.0'
                
                           TRUE: self.distrel == other.distrel
                
                        While still: :: 
                
                           self.distrel  = 'fedora-27.0.0'
                           other.distrel = 'fedora-27.0.1'
                
                           FALSE: self.distrel == other.distrel
                
                * integer bit masks
                
                  Special treatment of integers is provided:
                  
                  * *category*:
                    
                    When a valid *category*, *self.category* is compared only.
                  
                  * *ostype*:
                    
                    When a valid *ostype*, *self.ostype* is compared only.
                  
                  * *dist* and/or *distrel*:
                
                    The value is compared to the same maximal extend.                  
        
        Returns:
            True:  relevant parts are equal - see args.
            False: else
        
        Raises:
            KeyError
            AttributeError

        """
        res = False
        
        if type(other) in ISINT:
            # some special type comparison
            # hex id of dist and/or distrel
            if self.distrel_hexversion == other:
                return True
            elif (
                self.distrel_hexversion & RTE_DIST == other
                and  other & RTE_DIST == other  # it is actually a dist only
                ):
                return True
            
            return False

        elif isinstance(other, PlatformParameters):
            return self.distrel_hexversion == other.get_hexversion()

        elif isinstance(other, dict):
            # compare selected keys only
            res = True
            for k, v in other.items():
                try:
                    if k in ("osrel_sp", "wProductType", "wSuiteMask"):
                        if self.ostype in ('nt', 'cygwin'):
                            res &= self.__dict__[k] == v
                        else:
                            res = False 
                    elif k in ("distrel_version", "ostype_version",):
                        res &= self.__dict__['distrel_version'][:len(v)] == v
                    elif k == "distrel":
                        res &= self.__dict__['distrel'] == v
                    else:
                        res &= self.__dict__[k] == v 
                except KeyError:
                    res = False

        elif isinstance(other, tuple):
            # compare selected keys only

            res = True
            self.osrel_sp = []
            _myargs = list(other)
            if _myargs:
                res &= self.category == _myargs[0]
                _myargs.pop(0)
            if _myargs:
                res &= self.ostype == _myargs[0]
                _myargs.pop(0)
            if _myargs:
                res &= self.dist == _myargs[0]
                _myargs.pop(0)
            if _myargs:
                res &= self.distrel == _myargs[0]
                _myargs.pop(0)
            
        return res

    def __getitem__(self, key):
        """Gets the value of an attribute.
        """
        return self.__dict__[key] 

    def __iter__(self):
        """Iterates the non-private attribute names.
        """
        for k in self.__dict__.keys():
            if k[0] != '_':
                yield k 
                
    def items(self):
        """Yields the non-private attributes as key-value-pairs.
        """
        for k in self.__dict__.keys():
            if k[0] != '_':
                yield (k, self.__dict__[k],)
        
    def keys(self):
        """Yields the non-private attribute names.
        """
        for k in self.__dict__.keys():
            if k[0] != '_':
                yield k

    def __len__(self):
        """Counts and returns the number of non-private attributes - not starting with underscore.
        """
        l = 0
        for k in self.__dict__.keys():
            if k[0] != '_':
                l += 1
        return l

    def values(self):
        """Yields the values of non-private attributes.
        """
        for k in self.__dict__.keys():
            if k[0] != '_':
                yield self.__dict__[k]

    def __setitem__(self, key, val):
        """Standard set.
        """
        self.__dict__[key] = val 

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        res = (
            '{"category": "%s", "ostype": "%s", "dist": "%s", "distrel": "%s", '
            '"distrel_name": "%s", "distrel_key": "%s", '
            '"distrel_version": %s, "ostype_version": %s, "distrel_hexversion": %s, "ostype_id": %s, "ostype_id": %s}') % (
                str(self.category),
                str(self.ostype),
                str(self.dist),
                str(self.distrel),
                str(self.distrel_name),
                str(self.distrel_key),
                str(self.distrel_version),
                str(self.ostype_version),
                str(self.distrel_hexversion),
                str(self.ostype_id),
                str(self.ostype_id)
            )

        if self.ostype in ('nt', 'cygwin'):
            res += '"wServicePack": %s, ' % str(self.osrel_sp)
            res += '"wProductType": %s, ' % str(self.wProductType)
            res += '"wSuiteMask": %s' % str(self.wSuiteMask)
        res += "}"

        return res

    def __str__(self):
        return self.pretty_format(type='str')
 
    def pretty_format(self, raw=False, **kargs):
        """   Formats and returns a string of attributes.
   
        Args:
            raw:
                Controls the use of the value types::

                    raw := (
                          True   # prints the internal types
                        | False  # prints the symbolic names where applicable
                    )
                    
                    default := False

            kargs:
                quiet:
                    Supress standard display contents.
        
                    default := False
        
                terse:
                    Format for postprocessing.
        
                    default := False
        
                type:
                    Defines the type for the output::
               
                        type := (
                             bashvars
                           | json
                           | raw
                           | repr
                           | str
                        )
        
                    default := str
        
        Returns:
            Formatted string of attributes.
        
        Raises:
            TypeError
        
            pass-through

        """
        _type = kargs.get('type', 'str')
        _terse = kargs.get('terse', False)
        _quiet = kargs.get('quiet', False)
        _select = kargs.get(
            'select',
            attribute_map.keys()
        )

        res = ""
        
        def _get_value_str(v):
            if raw:
                return str(self.__getattribute__(k))
            else:
                return str(self.__getattribute__(attribute_map.get(k)))
                
        print("4TEST:a")
        if _type in ('str',):
            try:
                for k in sorted(_select):
                    if _terse and _quiet:
                        res += "\n%s" % (_get_value_str(k))
        
                    elif _terse:
                        res += "\n%s=%s" % (str(k), _get_value_str(k))
        
                    else:
                        res += "\n%-25s = %s" % (str(k), _get_value_str(k))

            except TypeError as e:
                exinfo = sys.exc_info()
                exinfo[1].args += (
                    "%s attribute error for str-map key: %s" %(str(self.__class__.__name__), str(k), ), )            
                raise
            
        elif _type in ('raw',):
            try:
                for k in _select:
                    if _terse and _quiet:
                        res += "\n%s" % (_get_value_str(k))
        
                    else:
                        res += "\n%s=%s" % (str(k), _get_value_str(k))

            except TypeError as e:
                exinfo = sys.exc_info()
                exinfo[1].args += (
                    "%s attribute error for raw-map key: %s" %(str(self.__class__.__name__), str(k), ), )            
                raise

        elif _type in ('repr',):
            if _terse and _quiet:
                res = '['
            else:
                res = '{'
            for k in _select:
                if type(k) in ISSTR:
                    _k = '"%s"' % k
                else:
                    _k = '%s' % str(k)
                
                try:
                    v = _get_value_str(k)
                except TypeError as e:
                    exinfo = sys.exc_info()
                    exinfo[1].args += (
                        "%s attribute error for repr-map key: %s" %(str(self.__class__.__name__), str(k), ), )            
                    raise

                if type(v) in ISSTR:
                    _v = '"%s"' % v
                else:
                    _v = '%s' % str(v)

                if _terse and _quiet:
                    res += '%s, ' % (_v)
                else:
                    res += '%s: %s, ' % (_k, _v)

            if _terse and _quiet:
                res += ']'
            else:
                res += '}'

        elif _type in ('json',):
            try:

# REMINDER: For now dropped due to layering architecture.
#                 if _terse:
#                     sys.stdout.write(repr(JSONData(self.get_json(select=_select))))
#                 else:
#                     sys.stdout.write(str(JSONData(self.get_json(select=_select))))

                if _terse:
                    sys.stdout.write(repr(self.get_json(select=_select)))
                else:
                    sys.stdout.write(str(self.get_json(select=_select)))
                sys.stdout.write('\n')
            except TypeError as e:
                raise TypeError(
                    str(e) 
                    +"\n\nTypeError: Check the contents of the environment variables for JSON conformity,"
                    +"\n           and/or Choose another output format.\n"
                    )

        elif _type in ('bashvars',):
            for k in _select:
                v = _get_value_str(k)
                if type(v) in ISSTR:
                    res += "\n%s='%s'" % (
                        str(bash_map.get(k)),
                        _get_value_str(k)
                    )
                elif type(v) in (list, tuple):
                    res += "\ntypeset -a %s" % (str(bash_map.get(k)))
                    res += "\n%s=%s" % (
                        str(bash_map.get(k)),
                        str(tuple(_get_value_str(k)))
                    )
                elif type(v) is dict:
                    res += "\ntypeset -A %s" % (str(bash_map.get(k)))
                    res += "\n%s=(" % (str(bash_map.get(k)))
                    for k0 in v.keys():
                        res += '"\n  %s[%s]="%a' % (
                            str(bash_map.get(k)),
                            str(bash_map.get(k0)),
                            str(tuple(_get_value_str(k)))
                        )
                    res += "\n)"
                else:
                    res += "\n%s=%s" % (
                        str(bash_map.get(k)),
                        _get_value_str(k)
                    )

        print("4TEST:b:<" + str(res) + ">")
        print("4TEST:c:")

        return res

    def __iand__(self, other):
        """The in-place *&* operator for the resulting *hexversion*: ::
     
           self-bitmask &= other-bitmask
        
        Args:
            other:
                The bitmask for operations. ::
               
                    other := (<int-32bit-mask> | <instance-of-PlatformParameters>)
           
        Returns:
            The resulting bitmask as numeric value.
        
        Raises:
            pass-through

        """
        if not self.distrel_hexversion:
            self.distrel_hexversion = self.get_hexversion()

        if isinstance(other, int):
            self.distrel_hexversion &= other
            return self

        elif isinstance(other, PlatformParameters):
            self.distrel_hexversion &= other.get_hexversion()
            return self

        elif isinstance(other, dict):
            self.distrel_hexversion &= PlatformParameters(**other).get_hexversion()
            return self

        elif isinstance(other, tuple):
            self.distrel_hexversion &= PlatformParameters(*other).get_hexversion()
            return self

        raise platformids.PlatformIDsError("type not supported: other = " + str(other))
    
    def __int__(self):
        """   The cast operator into the botmask: ::
     
            int(self) == self-bitmask
        
        Args:
            none
        
        Returns:
            The resulting bitmask of self as numeric value.
        
        Raises:
            pass-through

        """
        if not self.distrel_hexversion:
            self.distrel_hexversion = self.get_hexversion()
        return self.distrel_hexversion

    def __ior__(self, other):
        """The in-place *|* operator for the resulting *hexversion*::
     
            self-bitmask |= other-bitmask
        
        Args:
            other:
                The bitmask for operations. ::
               
                    other := (<int-32bit-mask> | <instance-of-PlatformParameters>)
           
        Returns:
            The resulting bitmask as numeric value.
        
        Raises:
            pass-through

        """
        if not self.distrel_hexversion:
            self.distrel_hexversion = self.get_hexversion()

        if isinstance(other, int):
            self.distrel_hexversion |= other
            return self

        elif isinstance(other, PlatformParameters):
            self.distrel_hexversion |= other.get_hexversion()
            return self

        elif isinstance(other, dict):
            self.distrel_hexversion |= PlatformParameters(**other).get_hexversion()
            return self

        elif isinstance(other, tuple):
            self.distrel_hexversion |= PlatformParameters(*other).get_hexversion()
            return self

        raise platformids.PlatformIDsError("type not supported: other = " + str(other))

    def __or__(self, other):
        """The *|* operator for the resulting *hexversion*: ::

           self-bitmask | other-bitmask
        
        Args:
            other:
                The bitmask for operations. ::
               
                    other := (<int-32bit-mask> | <instance-of-PlatformParameters>)
           
        Returns:
            The resulting bitmask as numeric value.
        
        Raises:
            pass-through

        """
        if not self.distrel_hexversion:
            self.distrel_hexversion = self.get_hexversion()

        if isinstance(other, int):
            return self.distrel_hexversion | other

        elif isinstance(other, PlatformParameters):
            return self.distrel_hexversion | other.get_hexversion()

        elif isinstance(other, dict):
            # use other as init parameters - simply trust or pass exception
            return self.distrel_hexversion | PlatformParameters(**other).get_hexversion()

        elif isinstance(other, tuple):
            return self.distrel_hexversion | PlatformParameters(*other).get_hexversion()

        raise platformids.PlatformIDsError("type not supported: other = " + str(other))
    
    def __rand__(self, other):
        """   The r-side *&* operator for the resulting *hexversion*: ::
     
           other-bitmask & self-bitmask
        
        Args:
            other:
                The bitmask for operations. ::
               
                    other := (<int-32bit-mask> | <instance-of-PlatformParameters>)
           
        Returns:
            The resulting bitmask as numeric value.
        
        Raises:
            pass-through

        """
        return self.__and__(other)

    def __ror__(self, other):
        """   The right-side *|* operator for the resulting *hexversion*: ::
     
           other-bitmask | self-bitmask
        
        Args:
            other:
                The bitmask for operations. ::
               
                    other := (<int-32bit-mask> | <instance-of-PlatformParameters>)
           
        Returns:
            The resulting bitmask as numeric value.
        
        Raises:
            pass-through

        """
        return self.__or__(other)

    def get_json(self, **kargs):
        """Returns a dictionary of attributes prepared to be processed
        as JSON data.
        
        Args:
            kargs:
                select:
                    List of attributes to be returned.
        
                default: all non-private
        
        Returns:
            Dictionary of key-value-pairs.
        
        Raises:
            pass-through

        """
        _select = kargs.get(
            'select',
            attribute_map.keys()
        )
        res = {}
        for k in _select:
            res[k] = self.__getattribute__(attribute_map.get(k))
        return res
   
    def scan(self):
        """Scans local platform for attributes specifying the underlying
        OS platform including the distribution. The provided data is
        consistent across all supported *Python* implementations
        including *Jython*. 
        Internally calls *platformids.platformids.fetch_platform_distribution()*.
        
        * dist
        * distrel
        * distrel_hexversion
        * distrel_id
        * distrel_version
        * ostype
        * ostype_id
        * ostype_version

        """
         
        #   
        # Common standard data
        #
        
        # numeric bitmasks   
        self.category = platformids.fetch_category()
        self.ostype = platformids.fetch_ostype()
        self.dist = platformids.fetch_dist()
        self.distrel = self.distrel_hexversion = RTE

        #
        # native platform string representation
        #
        # platform info - OS release
        self.ostype_key, self.ostype_version, self.ostype_version_num, self.ostype_id, = platformids.fetch_platform_os()
  
        # platform info - distribution release
        self.distribution = platformids.fetch_platform_distribution()
        (
            self.distribution_key, self.distribution_version, self.distribution_name, 
            self.distribution_name, self.distribution_version_num, self.distribution
        )  = platformids.fetch_platform_distribution()

        #   
        # Common basic HW data
        #   

        # CPU architecture
        self.cpu = platform.machine()
        try:
            self.cpudata = re.sub(r'bit', r'', platform.architecture()[0])
        except:
            try:
                self.cpudata = int(self.cpu[-2:]) 
            except:
                self.cpudata = 0  # for now...
            

        #   
        # Jython with optional special data about Java and JVM
        #   
        
        if platformids.isJython:
            # some optional data about Java
            
            _jv = platform.java_ver()
            self.java_version = tuple(int(x) for x in re.split(r'[._]',_jv[0]))
            
            try:
                self.javadata = int(re.sub(r'.*([0-9]+)-[Bb]it.*', r'\1', _jv[2][0]))  # could be different from platform, e.g. 32 on 64
            except:
                self.javadata = self.cpudata  # for now...

            if re.sub(r'.*(HotSpot).*', r'\1', _jv[2][0]) == 'HotSpot':
                self.jvm = 'JHS'  # Java-HotSpot
            else:
                self.jvm = None  # for now...



        #   
        # Cygwin or Windows with optional special data about Windows Product and SP/build
        #   

        if self.ostype in ('cygwinnt', 'nt'):

            from platformids.dist.nt.windows_kernel32dll import get_win32_OSVersionInfoExa, \
                get_win32_OSProductInfo

 
            osver = get_win32_OSVersionInfoExa()  # @UndefinedVariable
            self.osrel_sp = [osver.wServicePackMajor, osver.wServicePackMinor]
            self.wProductType = osver.wProductType  # ostype, server, workstation, domain-controller
            self.wSuiteMask = osver.wSuiteMask

            # the sub type - e.g. Ultimate, Enterprise, etc.
            pinfo = get_win32_OSProductInfo()  # @UndefinedVariable
            self.wProductVariant = pinfo.pdwReturnedProductType


            if osver.wProductType == 1:  # VER_NT_WORKSTATION
                self.dist = 'winws'
            elif osver.wProductType == 4:  # VER_NT_IOT
                self.dist = 'iot'
            else:
                self.dist = 'wins'

            # base - well-known - marketing name
            # self.distrel_name = "Windows%s" % (_uname[2])

            # specialization extension - well-known too
            # self.distrel_name += str(prod_type_categories[prod_ext[self.wProductVariant]]) 

        

    def get_hexversion(self):
        """Returns the hexversion of calculated platform from current 
        parameters. The conversion is based on the table 
        *platformids.platformids.rte2num*.
        """
        res = None
        # 1. try version steps
        for rx in range(len(self.distrel_version), 0, -1):
            _kx = self.dist + ''.join(str(x) for x in self.distrel_version[:rx])
            try:
                res = platformids.rte2num[_kx]
                break
            except KeyError:
                pass

        if res:
            return res

        res = RTE_GENERIC  # generic fallback
        try:
            # complete distribution release key in canonical platformids format
            res = platformids.rte2num[self.distrel]

        except KeyError:
            try:
                # complete distribution release key in accordance to the project
                res = platformids.rte2num[self.distrel_key]

            except KeyError:
                try:
                    # distribution without release information
                    res = platformids.rte2num[self.dist]

                except KeyError:
                    try:
                        # os type, very basic, almost generic
                        res = platformids.rte2num[self.ostype]

                    except KeyError:
                        try:
                            # category - lets say more generic than specific, 
                            # even though POSIX or Windows defines a lot of 
                            # standrad interfaces 
                            res = platformids.rte2num[self.category]

                        except KeyError:
                            # keep the generic fallback
                            pass

        return res

    def get_oshexversion(self):
        """Returns the oshexversion calculated from current parameters.
        """
        raise NotImplementedError("avaiable soon")
        return 0

