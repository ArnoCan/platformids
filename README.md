platformids
===========

**REMARK**: This is a nighlty build with some minor issues, the final is following within a these days.

The ‘platformids‘ package provides the categorization and enumeration of OS platforms and
distributions.

This enables the development of portable generic code for arbitrary platforms in IT and
IoT landscapes consisting of heterogeneous physical and virtual runtime environments.

The introduced hierarchical bitmask vectors enable for fast and efficient platform specific
code and data selection for OS and distributions with routines for specific platform releases. 

The supported version numbering comprise various release schemes such as classical
version numbers with variable segments and optional release names,

	AlpineLinux-3.8.1
	CentOS-6.10
	Debian-9.6
	Fedora31
	OS-X-10.6.8
	Ubuntu-18.04
	armbian-5.76
	cygwin-2.9.0
	opensuse-15.1
	opensuse-42.3
	raspbian-9.4
	slackware-14.2
	solaris-11.3

variations of numbering schemes,

	CentOS-7.5-1804
	CentOS-7.6-1810
	NT-6.3.9600
	NT-6.1.7601
	NT-5.1.2600

as well as various numbering schemes for continuous
deployment including the numbering schemes of Windows releases.

	archlinux-2018.12.01
	kali-linux-2019-W11
	kali-linux-2019.1
	NT-10.0.1809
	NT-10.0.1806

The current supported platforms are:

* Linux, BSD, Unix, Minix, Cygwin, OS-X, and Windows

* Servers, Workstations, Embedded Systems

* Datacenters, public and private Clouds, IoT 

* x86, amd64, arm32/armhf, arm64/aarch64

**Online documentation**:

* https://platformids.sourceforge.io/


**Runtime-Repository**:

* PyPI: https://pypi.org/project/platformids/

  Install: *pip install platformids*, see also section 'Install' of the online documentation.


**Downloads**:

* sourceforge.net: https://sourceforge.net/projects/platformids/files/

* bitbucket.org: https://bitbucket.org/acue/platformids

* github.com: https://github.com/ArnoCan/platformids/

* pypi.org: https://pypi.org/project/platformids/


Project Data
------------

* PROJECT: 'platformids'

* MISSION: Identify and enumerate platform IDs for the OS and it's distribution.

* VERSION: 00.01

* RELEASE: 00.01.039

* STATUS: beta

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints

Concepts and enumeration values are migrated from the 

* *UnifiedSessionsManager* (C) 2008 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez.  

Runtime Environment
-------------------
For a comprehensive list refer to the documentation.

**Python Syntax Support**

*  Python2.7, and Python3

**Python Implementation Support**

*  CPython, IPython, IronPython, Jython, and PyPy

Jython requires on Windows platforms the optional Java package *platformids.jy.dist.nt* -  see documentation:

* JDK/JRE >= Java8

* JNA

* For the source-installation of the contained Java modules refer to
  *setuplib* with the *setup.py* commands *build_java* and *build_jy*.


**OS on Server, Workstation, Laptops, Virtual Machines, and Containers**

* Linux: AlpineLinux, ArchLinux, CentOS, Debian, Fedora, Gentoo, OpenSUSE, Raspbian, RHEL, Slackware, SLES, Ubuntu, ...  

* BSD: DragonFlyBSD, FreeBSD, NetBSD, OpenBSD, GhostBSD, TrueOS, NomadBSD

* OS-X: Snow Leopard

* Windows: Win10, Win8.1, Win7, WinXP, Win2019, Win2016, Win2012, Win2008, Win2000

* WSL-1.0: Alpine, Debian, KaliLinux, openSUSE, SLES, Ubuntu

* Cygwin

* UNIX: Solaris10, Solaris11

* Minix: Minix3

* ReactOS

**Network and Security**

* Network Devices: OpenWRT

* Security: KaliLinux, pfSense, BlackArch, ParrotOS, Pentoo

**OS on Embedded Devices**

* RaspberryPI: ArchLinux, CentOS, OpenBSD, OpenWRT, Raspbian

* ASUS-TinkerBoard: Armbian

* e.g. Adafruit Trinket M0: CircuitPython, MicroPython

Current Release
---------------

Major Changes:

* Initial version.

* Concepts and enumeration values migrated from the *UnifiedSessionsManager* (C) 2008 Arno-Can Uestuensoez,
  starting at 2007/2008
  
  See docs@ctys.sourceforge.io - https://ctys.sourceforge.io/.

ToDo:

* AIX

* MicroPython, CircuitPython

* test OpenBSD on rpi3

* test Windows10IoT-Core

* NomadBSD: has some issues with running in VirtualBox, so shifted for now
