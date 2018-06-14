# -*- coding: utf-8 -*-
"""Distribute 'platformids', a generic unit test wrapper for commandline interfaces.

   Installs 'platformids', adds/modifies the following helper features to standard
   'setuptools' options.

   Args:
      build_doc: Creates Sphinx based documentation with embeded javadoc-style
          API documentation, html only.

      build_sphinx: Creates documentation for runtime system by Sphinx, html only.
         Calls 'callDocSphinx.sh'.

      build_epydoc: Creates standalone documentation for runtime system by Epydoc,
         html only.

      install_project_doc: Install a local copy into the doc directory of the project.

      instal_doc: Install a local copy of the previously build documents in
          accordance to PEP-370.

      test: Runs PyUnit tests by discovery.

      usecases: Runs PyUnit UseCases by discovery, a lightweight
          set of unit tests.

      --sdk:
          Requires sphinx, epydoc, and dot-graphics.

      --no-install-required: Suppresses installation dependency checks,
          requires appropriate PYTHONPATH.
      --offline: Sets online dependencies to offline, or ignores online
          dependencies.

      --exit: Exit 'setup.py'.

      --help-platformids: Displays this help.

   Returns:
      Results for success in installed 'platformids'.

   Raises:
      ffs.

"""
from __future__ import absolute_import
from __future__ import print_function

# priority is offline here - needs manual 'bootstrap', thus dropped ez_setup for now
# import ez_setup
# ez_setup.use_setuptools()

#
#*** common source header
#
__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2017 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "7add5ded-c39b-4b6e-8c87-1b3a1c150ee9"

from platformids import V3K, RTE, RTE_WIN32

import os,sys

from setuptools import setup #, find_packages
import fnmatch
import re, shutil, tempfile


_NAME = 'platformids'

# some debug
# Intentional HACK: offline only, mainly foreseen for developement
__verbose = False
if '--verbose' in sys.argv:
    __verbose = True
    sys.argv.remove('--verbose')

__debug = False
if '--debug' in sys.argv:
    __debug = True
    sys.argv.remove('--debug')

if __debug__:
    __DEVELTEST__ = True
__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    _sdk = True
    sys.argv.remove('--sdk')

# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0,os.path.abspath(_mypath))


#--------------------------------------
#
# Package parameters for setuptools
#
#--------------------------------------
_name='platformids'
"""package name"""

__pkgname__ = "platformids"
"""package name"""

__vers__ = [0, 1, 28,]
"""version parts for easy processing"""

__version__ = "%02d.%02d.%03d"%(__vers__[0],__vers__[1],__vers__[2],)
"""assembled version string"""

__author__ = "acue"
"""author of the package"""

_packages = [
    "platformids",
]
"""Python packages to be installed."""

_scripts = [
    ]
"""Scripts to be installed."""

_package_data = {
    'platformids': ['README.md','ArtisticLicense20.html', 'licenses-amendments.txt',
            ],
}
"""Provided data of the package."""

_platformids = ['Linux','Windows','darwin',]
"""provided platformids"""

_url='https://sourceforge.net/projects/pyplatformids/'
"""URL of this package"""

#_download_url="https://github.com/ArnoCan/platformids/"
_download_url="https://sourceforge.net/projects/pyplatformids/files/"

_install_requires = []
"""prerequired non-standard packages"""

_keywords  = ' platforms Python OS identifier '

_description=(
    "The 'pyplatformids' package provides a set of canonical platform enums."
)

_README = os.path.join(os.path.dirname(__file__), 'README.md')
_long_description = open(_README).read() + 'nn'
"""detailed description of this package"""

_classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: Free To Use But Restricted",
    "License :: OSI Approved :: Artistic License",
    "Natural Language :: English",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: OS Independent",
    "Operating System :: POSIX :: BSD :: OpenBSD",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: SunOS/Solaris",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Unix Shell",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]
"""the classification of this package"""

_epydoc_api_patchlist = [
    'shortcuts.html',
    'config.html',
]
"""Patch list of Sphinx documents for the insertion of links to API documentation."""

_profiling_components = _mypath+os.sep+'bin'+os.sep+'*.py '+_mypath+os.sep+__pkgname__+os.sep+'*.py'
"""Components to be used for the creation of profiling information for Epydoc."""

_doc_subpath='en'+os.path.sep+'html'+os.path.sep+'man7'
"""Relative path under the documents directory."""

_sharepath = os.path.expanduser(os.path.sep+'share'+os.path.sep+'projdata'+os.path.sep+'twint'+os.path.sep+'devops'+os.path.sep+__pkgname__)
"""Project specific common network directory on the AdNovum share."""


_install_requires=[
#    'pysourceinfo >=0.1.20',
]

# if RTE & RTE_WIN32:
#     # pylint: disable-msg=F0401
#     if V3K:
# #        _install_requires.append('winreg')
# #        _install_requires.append('pypiwin32')
# 
#     else:
# #        _install_requires.append('_winreg')
# #        _install_requires.append('win32api')
# #        _install_requires.append('win32security')
# #        _install_requires.append('pypiwin32')


if __sdk: # pragma: no cover
    _install_requires.extend(
        [
            'sphinx >= 1.4',
            'epydoc >= 3.0',
        ]
    )

_test_suite="tests.CallCase"


#
#*** ===>>> setup.py helper
#
def find_files(srcdir, *wildcards, **kw):
    """Assembles a list of package files for package_files.

        Args:
            srcdir: Source root.
            *wildcards: list of globs.
            **kw: Additional control of resolution:
                single_level: Flat only.
                subpath: Cut topmost path elemenr from listelements,
                    special for dictionaries.
                nopostfix: Drop filename postfix.
                packages: List packages only, else files.
                yield_folders:
        Returns:
            Results in an list.

        Raises:
            ffs.

    """
    def all_files(root, *patterns, **kw):
        ret=[]
        single_level = kw.get('single_level', False)
        subpath = kw.get('subpath', False)
        nopostfix = kw.get('nopostfix', True)
        packages = kw.get('packages', True)
        yield_folders = kw.get('yield_folders', True)

        for path, subdirs, files in os.walk(root):
            if yield_folders:
                files.extend(subdirs)
            files.sort( )

            if subpath:
                path=re.sub(r'^[^'+os.sep+']*'+os.sep, '',path)

            for name in files:
                if name in ('.gitignore', '.git', '.svn'):
                    continue

                for pattern in patterns:
                    if fnmatch.fnmatch(name, pattern):
                        if packages:
                            if not name == '__init__.py':
                                continue
                            ret.append(path)
                            continue
                        if nopostfix:
                            name=os.path.splitext(name)[0]

                        ret.append(os.path.join(path, name))

            if single_level:
                break
        return ret

    file_list = all_files(srcdir, *wildcards,**kw)
    return file_list

def usage():
    if __name__ == '__main__':
        import pydoc
        #FIXME: literally displayed '__main__'
        print(pydoc.help(__name__))
    else:
        help(str(os.path.basename(sys.argv[0]).split('.')[0]))

#
#* shortcuts
#

exit_code = 0

# controls the display of pathnames for created documents
# list of urls pointing do created documents
__doc_urls = []

# custom doc creation by sphinx-apidoc
if 'build_sphinx' in sys.argv or 'build_doc' in sys.argv:
    try:
        os.makedirs(_mypath+os.sep+'build'+os.sep+'apidoc'+os.sep+'sphinx')
    except:
        pass

    print("#---------------------------------------------------------")
    exit_code = os.system(_mypath+os.sep+'callDocSphinx.sh') # create apidoc
    print("#---------------------------------------------------------")
    print("Called/Finished callDocSphinx.sh => exit="+str(exit_code))
    if 'build_sphinx' in sys.argv:
        sys.argv.remove('build_sphinx')
    __doc_urls.append(_mypath+os.sep+'build'+os.sep+'apidoc'+os.sep+'sphinx'+os.sep+'_build'+os.sep+'html'+os.sep+'index.html')

# custom doc creation by epydoc
if 'build_epydoc' in sys.argv:
    try:
        os.makedirs('build'+os.sep+'epydoc')
    except:
        pass

    _epycall = 'epydoc --config docsrc/epydoc-standalone.conf'
    if __verbose:
        _epycall += ' --verbose '
    if __debug:
        _epycall += ' --debug '

    print("Call: " + str(_epycall))
    print("#---------------------------------------------------------")
    exit_code = os.system(_epycall) # create apidoc
    print("#---------------------------------------------------------")
    print("Finished: " + str(_epycall) + " => exit="+str(exit_code))
    sys.argv.remove('build_epydoc')
    __doc_urls.append(_mypath+os.sep+'build'+os.sep+'epydoc'+os.sep+'index.html')

# common locations
src0 = os.path.normpath("build/apidoc/sphinx/_build/html")
dst0 = os.path.normpath("build/apidoc/"+str(_NAME))

# custom doc creation by sphinx-apidoc with embeded epydoc
if 'build_doc' in sys.argv:

    def _sed(filename, pattern, repl, flags=0):
        pattern_compiled = re.compile(pattern,flags)
        fname = os.path.normpath(filename)
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            with open(fname) as src_file:
                for line in src_file:
                    ftmp.write(pattern_compiled.sub(repl, line))

        shutil.copystat(fname, ftmp.name)
        shutil.move(ftmp.name, fname)


    # copy sphinx to mixed doc
    if not os.path.exists(src0):
        raise Exception("Missing generated sphinx document source:"+str(src0))
    if os.path.exists(dst0):
        shutil.rmtree(dst0)
    shutil.copytree(src0, dst0)

    __doc_urls.append(_mypath+os.sep+'build'+os.sep+'apidoc'+os.sep+_NAME+os.sep+'index.html')

    pt = r'<li><a class="reference internal" href="#table-of-contents">Table of Contents</a></li>'
    rp  = r'<li><a class="reference internal" href="shortcuts.html">Shortcuts</a></li>'
    rp += r'<li><a class="reference internal" href="install.html">Install</a></li>'
    rp += pt
    fn = dst0+'/index.html'
    _sed(fn, pt, rp, re.MULTILINE)  # @UndefinedVariable

    sys.argv.remove('build_doc')

# install local project doc
if 'install_project_doc' in sys.argv:
    print("# project_doc.sh...")

    dstroot = os.path.normpath("doc/en/html/man3/")+os.sep

    try:
        os.makedirs(dstroot)
    except:
        pass

    if os.path.exists(dst0):
        if os.path.exists(dstroot+str(_NAME)):
            shutil.rmtree(dstroot+str(_NAME))
        shutil.copytree(dst0, dstroot+str(_NAME))


    src0 = os.path.normpath("build/apidoc/sphinx/_build/html")
    if os.path.exists(src0):
        if os.path.exists(dstroot+str(_NAME)+".sphinx"):
            shutil.rmtree(dstroot+str(_NAME)+".sphinx")
        shutil.copytree(src0, dstroot+str(_NAME)+".sphinx")

    src0 = os.path.normpath("build/apidoc/epydoc")
    if os.path.exists(src0):
        if os.path.exists(dstroot+str(_NAME)+".epydoc"):
            shutil.rmtree(dstroot+str(_NAME)+".epydoc")
        shutil.copytree(src0, dstroot+str(_NAME)+".epydoc")

    print("#")
    idx = 0
    for i in sys.argv:
        if i == 'install_doc': break
        idx += 1

    print("#")
    print("Called/Finished PyUnit tests => exit="+str(exit_code))
    print("exit setup.py now: exit="+str(exit_code))
    sys.argv.remove('project_doc')

# call of complete test suite by 'discover'
if 'install_doc' in sys.argv:
    print("#")
    idx = 0
    for i in sys.argv:
        if i == 'install_doc': break
        idx += 1
    print("# install_doc.sh...")
    # src
    src = os.path.normpath("build/apidoc/"+str(_NAME))
    _dst = "doc/en/html/man3/"+str(_NAME)

    # set platform
    if sys.platform in ('win32'):
        dst = os.path.expandvars("%APPDATA%/Python/doc/")
    else:
        dst = os.path.expanduser("~/.local/")
    dst = os.path.normpath(dst+_dst)+os.sep


    print("#")

    # copy sphinx
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print("# "+str(_NAME))
    print("#   from        : "+str(src))
    print("#   to          : "+str(dst))
    print("#   display with: firefox -P preview.simple "+dst+"/index.html")

    # copy epydoc
    src += '.epydoc'
    dst += '.epydoc'
    if os.path.exists(src):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print("#")
        print("# "+str(_NAME)+".epydoc")
        print("#   from        : "+str(src))
        print("#   to          : "+str(dst))
        print("#   display with: firefox -P preview.simple "+dst+"/index.html")

    print("#")
    print("Called/Finished PyUnit tests => exit="+str(exit_code))
    print("exit setup.py now: exit="+str(exit_code))
    sys.argv.remove('install_doc')

#
# list URIs of created and installed documents for easy use by cut-and-paste
#
if __doc_urls:
    print()
    print("#*** The following documents are created:")
    for d in __doc_urls:
        print("  "+str(d))

    print()
    print("#*** Display with:")
    for d in __doc_urls:
        print("  firefox file://"+str(d))

    print

# call of complete test suite by 'discover'
if 'tests' in sys.argv or 'test' in sys.argv:
    if os.path.dirname(__file__)+os.pathsep not in os.environ['PATH']:
        p0 = os.path.dirname(__file__)
        os.putenv('PATH', p0+os.pathsep+os.getenv('PATH',''))
        print("# putenv:PATH[0]="+str(p0))

    print("#")
    print("# Check 'inspect' paths - call in: tests.30_libs.040_platformids")
    exit_code += os.system('python -m unittest discover -s tests.30_libs.040_platformids -p CallCase.py') # traverse tree
    print("# Check 'inspect' paths - call in: tests.30_libs")
    exit_code += os.system('python -m unittest discover -s tests.30_libs -p CallCase.py') # traverse tree
    print("# Check 'inspect' paths - call in: tests")
    exit_code  = os.system('python -m unittest discover -s tests -p CallCase.py') # traverse tree
    print("#")
    print("Called/Finished PyUnit tests => exit="+str(exit_code))
    print("exit setup.py now: exit="+str(exit_code))
    try:
        sys.argv.remove('test')
    except:
        pass
    try:
        sys.argv.remove('tests')
    except:
        pass

# call of complete UseCases by 'discover'
if 'usecases' in sys.argv or 'UseCases' in sys.argv or 'usecase' in sys.argv:
    if os.path.dirname(__file__)+os.pathsep not in os.environ['PATH']:
        p0 = os.path.dirname(__file__)
        os.putenv('PATH', p0+os.pathsep+os.getenv('PATH',''))
        print("# putenv:PATH[0]="+str(p0))

    print("#")
    print("# Check 'inspect' paths - call in: UseCases")
    exit_code = os.system('python -m unittest discover -s UseCases -p CallCase.py') # traverse tree
    print("# Check 'inspect' paths - call in: UseCases.platformids")
    exit_code += os.system('python -m unittest discover -s UseCases.platformids -p CallCase.py') # traverse tree
    print("# Check 'inspect' paths - call in: UseCases.platformids.branches")
    exit_code += os.system('python -m unittest discover -s UseCases.platformids.branches -p CallCase.py') # traverse tree
    print("# Check 'inspect' paths - call in: UseCases.platformids.functions")
    exit_code += os.system('python -m unittest discover -s UseCases.platformids.functions -p CallCase.py') # traverse tree
    print("#")
    print("Called/Finished PyUnit tests => exit="+str(exit_code))
    print("exit setup.py now: exit="+str(exit_code))
    try:
        sys.argv.remove('usecase')
    except:
        pass
    try:
        sys.argv.remove('usecases')
    except:
        pass

# Intentional HACK: ignore (online) dependencies, mainly foreseen for developement
__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

# Intentional HACK: offline only, mainly foreseen for developement
__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')

# Execution failed - Error.
if exit_code != 0:
    sys.exit(exit_code)

# Help on addons.
if '--help-platformids' in sys.argv:
    usage()
    sys.exit(0)

# Exit here.
if '--exit' in sys.argv:
    sys.exit(0)

# if platformids-specials only
if len(sys.argv)==1:
    sys.exit(exit_code)

#
#*** <<<=== setup.py helper
#



if __debug__:
    if __DEVELTEST__:
        print("#---------------------------------------------------------")
        print("packages="+str(_packages))
        print("#---------------------------------------------------------")
        print("package_data="+str(_package_data))
        print("#---------------------------------------------------------")


#
#*** ===>>> setup.py helper
#

# Intentional HACK: ignore (online) dependencies, mainly foreseen for developement
if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   "+str(ir))
    print("#")
    _install_requires=[]

#
#*** <<<=== setup.py helper
#

#
#*** do it now...
#
setup(
    author=__author__,
    author_email=__author_email__,
    classifiers=_classifiers,
    description=_description,
    download_url=_download_url,
    install_requires=_install_requires,
    keywords=_keywords,
    license=__license__,
    long_description=_long_description,
    name=_name,
    package_data=_package_data,
    packages=_packages,
    platformids=_platformids,
    scripts=_scripts,
    url=_url,
    version=__version__,
    zip_safe=False,
)

if '--help' in sys.argv:
    print()
    print("Help on usage extensions by "+str(_NAME))
    print("   --help-"+str(_NAME))
    print()
