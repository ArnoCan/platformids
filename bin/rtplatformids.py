#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" command line interface for *platformids*
"""
from __future__ import absolute_import
from __future__ import print_function

import sys
import os
import re
import platform

from rdbg.start import start_remote_debug    # load a slim bootstrap module
start_remote_debug()                         # check whether '--rdbg' option is present, if so accomplish bootstrap

from platformids import PlatformIDsError, \
    rte2num, num2rte, num2enumstr, \
    PYV35Plus, PYVxyz, PYV33, PYV2
from platformids.optionparser_platformids import OptionsParser
from platformids.platforms import PlatformParameters
import platformids.map_enum_labels  # @UnusedImport



__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2018 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.29'
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"
__release__ = 'alpha2'
__docformat__ = "restructuredtext en"


# pre-fetch debugging
if '--debug' in sys.argv:
    platformids._debug += 1
else:
    platformids._debug = 0

# pre-fetch verbose
if '--verbose' in sys.argv:
    platformids._verbose += 1
else:
    platformids._verbose = 0

# fetch options
x = OptionsParser(sys.argv[1:])
opts, unknown, args = x.get_options()

if unknown:
    raise PlatformIDsError("Unknown options:" + str(unknown))

_tasks = x.get_JSON_bin()  #: fetch options for task data

#
# defaults
#

# name of tested application
_appname = _tasks.get('appname', 'rtplatformids')

# verbose output
platformids._verbose = _tasks.get('verbose', 0)

# debug output
platformids._debug = _tasks.get('debug', 0)


#
# load additional modules
#
if _tasks.get('load'):
    for f in  _tasks.get('load'):
        modfpath = f
        _impmodname = re.sub(r'[.][^.]*$', '', os.path.basename(f))
        
        try:
            if PYV35Plus: # PYVxyz >= PYV35: # Python 3.5+
                import importlib.util  # @UnresolvedImport
                spec = importlib.util.spec_from_file_location(_impmodname, modfpath)  # @UndefinedVariable
                if spec:
                    _modx = importlib.util.module_from_spec(spec)  # @UndefinedVariable
                    spec.loader.exec_module(_modx)
        
            elif PYVxyz >= PYV33: # Python 3.3 and 3.4
                from importlib.machinery import SourceFileLoader  # @UnresolvedImport
                _modx = SourceFileLoader(_impmodname, modfpath).load_module()
        
        
            elif PYVxyz & PYV2: # Python 2 - verified and released for 2.7 only, but don't block
                import imp
                _modx = imp.load_source(_impmodname, modfpath)
        
        
            sys.modules[_impmodname] = _modx
            globals()[_impmodname] = _modx
        
        except KeyError:
            # continue with generic
            pass


#
# enumerate stored platform identifier mappings
#
if _tasks.get('enumerate'):

    _type = _tasks['enumerate'].get('type', 'all')
    _num = _tasks['enumerate'].get('num', 'int')
    _scope = _tasks['enumerate'].get('scope', 'strkey')
    _pad = _tasks['enumerate'].get('pad', 'true')
    _reverse = _tasks['enumerate'].get('reverse', 'false')

    print()
    if _reverse in ('on', 'true', '1', ):
        _lst = sorted(num2rte.items())
    else:
        _lst = sorted(rte2num.items())
        
    for k,v in _lst:
        if _pad in ('off', '0', 'false', 'no') and k == v:
            continue
 
        if _scope == 'strkey' and type(k) != str:
            continue
        elif _scope == 'numkey' and type(k) == str:
            continue

        if type(k) is int:
            if _num == 'int':
                _k = str(k)
            elif _num == 'hex':
                _k = "0x%x" % k
            elif _num == 'bit':
                _k = '{:#032b}'.format(k)
            elif _num == 'sym':
                try:
                    _k = num2enumstr[k]
                except KeyError:
                    _k = k
        else:
            _k = k

        if type(v) is int:
            if _num == 'int':
                _v = str(v)
            elif _num == 'hex':
                _v = "0x%x" % v
            elif _num == 'bit':
                _v = '{0:#032b}'.format(v)
            elif _num == 'sym':
                try:
                    _v = num2enumstr[v]
                except KeyError:
                    _v = v
        else:
            _v = v
            
        print("%-32s = %s" % (str(_k), str(_v)))

    sys.exit(0)


#
# display platform parameters from standards libraries:
#   os
#   sys
#   platform
#
if _tasks.get('platform'):

    print()
    print("%-30s = %s" % ('os.name', str(os.name)))
    print("%-30s = %s" % ('sys.platform', str(sys.platform)))
    print("%-30s = %s" % ('platform.architecture', str(platform.architecture())))
    print("%-30s = %s" % ('platform.dist', str(platform.dist())))
    print("%-30s = %s" % ('platform.linux_distribution', str(platform.linux_distribution())))
    print("%-30s = %s" % ('platform.machine', str(platform.machine())))
    print("%-30s = %s" % ('platform.node', str(platform.node())))
    print("%-30s = %s" % ('platform.platform', str(platform.platform())))
    print("%-30s = %s" % ('platform.processor', str(platform.processor())))
    print("%-30s = %s" % ('platform.release', str(platform.release())))
    print("%-30s = %s" % ('platform.system', str(platform.system())))
    print("%-30s = %s" % ('platform.uname', str(platform.uname())))
    print("%-30s = %s" % ('platform.version', str(platform.version())))
    print()
    print("%-30s = %s" % ('platform.mac_ver', str(platform.mac_ver())))
    print("%-30s = %s" % ('platform.win32_ver', str(platform.win32_ver())))
    print()
    print("%-30s = %s" % ('platform.python_branch', str(platform.python_branch())))
    print("%-30s = %s" % ('platform.python_build', str(platform.python_build())))
    print("%-30s = %s" % ('platform.python_compiler', str(platform.python_compiler())))
    print("%-30s = %s" % ('platform.python_implementation', str(platform.python_implementation())))
    print("%-30s = %s" % ('platform.python_revision', str(platform.python_revision())))
    print("%-30s = %s" % ('platform.python_version', str(platform.python_version())))
    print("%-30s = %s" % ('platform.python_version_tuple', str(platform.python_version_tuple())))
    print()
    print("%-30s = %s" % ('sys.api_version', str(sys.api_version)))
    print("%-30s = %s" % ('sys.byteorder', str(sys.byteorder)))
    print("%-30s = %s" % ('sys.hexversion', str(sys.hexversion)))
    print("%-30s = %s" % ('sys.version', str(sys.version)))
    print("%-30s = %s" % ('sys.version_info', str(sys.version_info)))
  
    sys.exit(0)


#
# display scanned platform data by PlatformParameters 
#

# collect all
platformparams = PlatformParameters()
platformparams.scan()

if not _tasks['selected']:
    # display all
    try:
        outform = _tasks['outform']['out_format']
        if outform not in ('str', 'raw', 'repr', 'json', 'bashvars'):
            raise PlatformIDsError("not supported: --out-format " + str(outform))

    except KeyError:
        outform = 'str'

    if outform in ('str', 'raw', 'repr', 'json', 'bashvars'):
        print(platformparams.pretty_format(
            select=_tasks['params'].keys(),
            type=outform,
            terse=_tasks.get('terse', False),
            quiet=_tasks.get('quiet', False),
        ))
    else:
        raise PlatformIDsError("not supported: --out-format " + str(outform))

else:
    # display selected
    try:
        outform = _tasks['outform']['out_format']
        if outform not in ('str', 'raw', 'repr', 'json', 'bashvars'):
            raise PlatformIDsError("not supported: --out-format " + str(outform))
    except KeyError:
        outform = None


    _sel = []
    for k,v in _tasks['params'].items():
        if v:
            _sel.append(k)

    print(platformparams.pretty_format(
        select=_sel,
        type=outform,
        terse=_tasks.get('terse', False),
        quiet=_tasks.get('quiet', False),
        ))

