# -*- coding: utf-8 -*-
"""Distribution 'platformids' provides the enumeration of operating systems,
and their releases.

The following local options are added.

  --sdk:
      Requires sphinx, epydoc, and dot-graphics.

  --no-install-required: Suppresses installation dependency checks,
      requires appropriate PYTHONPATH.

  --offline: Sets online dependencies to offline, or ignores online
      dependencies.

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

import setuptools

import yapyutils.help


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

__vers__ = [0, 1, 39, ]
__version__ = "%02d.%02d.%03d" % (__vers__[0], __vers__[1], __vers__[2],)
__release__ = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],) + '-rc0'
__status__ = 'beta'


__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    __sdk = True
    sys.argv.remove('--sdk')


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


_name = 'platformids'
__pkgname__ = "platformids"
_version = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],)


_packages = [
    'platformids',
    'platformids.custom',
    'platformids.dist',
    'platformids.embed',
    'platformids.net',
]

_scripts = [
    "scripts/rtplatformids.py",
]

_install_requires = [
    'pythonids >= 0.1.30',
    'yapyutils >= 0.1.20',
    'sourceinfo >= 0.1.30',
]


if __sdk:  # pragma: no cover
    try:
        import sphinx_rtd_theme  # @UnusedImport
    except:
        sys.stderr.write(
            "WARNING: Cannot import package 'sphinx_rtd_theme', cannot create local 'ReadTheDocs' style.")

    _install_requires.extend(
        [
            'sphinx >= 1.6',
            'epydoc >= 3.0',
        ]
    )

_test_suite = "tests.CallCase"

__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')

# Help on addons.
if '--help-platformids' in sys.argv:
    yapyutils.help.usage('setup')
    sys.exit(0)

if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   " + str(ir))
    print("#")
    _install_requires = []


setuptools.setup(
    author=__author__,
    author_email=__author_email__,
    description="Enumeration of operating systems and their releases.",
    download_url="https://sourceforge.net/projects/platformids/files/",
    entry_points={
        'enumerateit.commands': [
            'rtplatformids = platformids.build_apidoc:BuildApidocX',
        ]
    },    
    install_requires=_install_requires,
    license=__license__,
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    name=_name,
    packages=_packages,
    scripts=_scripts,
    url='https://sourceforge.net/projects/platformids/',
    version=_version,
    zip_safe=False,
)

if '--help' in sys.argv:
    print()
    print("Help on provided package extensions by " + str(_name))
    print("   --help-" + str(_name))
    print()

sys.exit(0)


