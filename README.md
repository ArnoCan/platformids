platformids
===========

The ‘platformids‘ package provides the enumeration of runtime platforms. This extends the standard Python facilities by

* more specific canonical platform enumerations
* provides additional hierarchical bitmasks for platform values for faster processing
* provides mapping of string and numeric representation for human display
* provides a boolean flag *V3K* for Python3
* provides Python release numbers as integer by compressed bit masks, current *PYVxyz* and predefined values e.g. *PYV27*, *PYV3*, or *PYV365*
* provides an interface *getPYVxyz()* for the encoding of arbitrary Python release numbers into compressed bit masks

The supported platforms are:

* Linux, BSD, Unix, OS-X, Cygwin, and Windows

* Python2.7+, Python3.5+


**Runtime-Repository**:

* PyPI: https://pypi.org/project/platformids/

  Install: *pip install platformids*, see also 'Install'.


**Downloads**:

* Sourceforge.net: https://sourceforge.net/projects/pyplatformids/files/

* bitbucket.org: https://bitbucket.org/acue/pyplatformids

* github: https://github.com/ArnoCan/pyplatformids/

* PyPI: https://pypi.org/project/platformids/

**Online documentation**:

* https://pyplatformids.sourceforge.io/

setup.py
--------

The installer adds a few options to the standard setuptools options.

* *build_sphinx*: Creates documentation for runtime system by Sphinx, html only. Calls 'callDocSphinx.sh'.

* *build_epydoc*: Creates documentation for runtime system by Epydoc, html only. Calls 'callDocEpydoc.sh'.

* *instal_doc*: Install a local copy of the previously build documents in accordance to PEP-370.

* *test*: Runs PyUnit tests by discovery.

* *--help-platformids*: Displays this help.

* *--no-install-required*: Suppresses installation dependency checks, requires appropriate PYTHONPATH.

* *--offline*: Sets online dependencies to offline, or ignores online dependencies.

* *--exit*: Exit 'setup.py'.
 

Project Data
------------

* PROJECT: 'platformids'

* MISSION: Extend the standard PyUnit package for arbitrary ExecUnits.

* VERSION: 00.01

* RELEASE: 00.01.028

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2008-2018 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints


  Refer to enclosed documents ArtisticLicense20.html and licenses-amendments.txt:
  
  * bitbucket: https://bitbucket.org/acue/pyplatformids/src
  * github.com: https://github.com/ArnoCan/pyplatformids/ArtisticLicense20.html
  * sourceforge.net: https://pyplatformids.sourceforge.io/_static/ArtisticLicense20.html

  * pythonhosted.org: https://bitbucket.org/acue/pyplatformids/src
  * github.com: https://github.com/ArnoCan/pyplatformids/licenses-amendments.txt
  * sourceforge.net: https://pyplatformids.sourceforge.io/_static/licenses-amendments.txt

VERSIONS and RELEASES
---------------------

**Planned Releases:**

* RELEASE: 00.00.00x - Pre-Alpha: Extraction of the features from hard-coded application into a reusable package.

* RELEASE: 00.01.00x - Alpha: Completion of basic features. 

* RELEASE: 00.02.00x - Alpha: Completion of features, stable interface. 

* RELEASE: 00.03.00x - Beta: Accomplish test cases for medium to high complexity.

* RELEASE: 00.04.00x - Production: First production release.

* RELEASE: 00.05.00x - Production: Various performance enhancements.

* RELEASE: 00.06.00x - Production: Security review.

**Current Release: 00.01.028 - Alpha:**

Python support:

*  Python2.7, and Python3.5+

OS-Support:

* Linux: Fedora, CentOS, RHEL, Debian, and SuSE 

* BSD - OpenBSD, FreeBSD

* Mac-OS: Snow Leopard - others should work too

* Windows: Win7, Win10 - others see Cygwin

* Cygwin: 2.874/64 bit


Major Changes:

* Initial version.

* Concepts and enumeration values migrated from the *UnifiedSessionsManager* 
  starting at 2007/2008  

  