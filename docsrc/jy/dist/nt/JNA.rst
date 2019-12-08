
.. _JYTHON_JNA:

JNA - Java Native Access
========================

The provided packages are transparent to the user, though the *Jython* specific module simply 
converts the data to the canonical format of the *platformids*.
Thus the following implementation details are of relevance for trouble shooting 
and development only. 


Provided Packages
-----------------

jy.dist.nt.Advapi32GetCurrentVersion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Registry access.

For implementation details see :ref:`jy.dist.nt.Advapi32GetCurrentVersion(.java) <JNA_ADVAPI32GETCURRENTVERSION>`.  


jy.dist.nt.Kernel32GetProductInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some product information by the official API, to be basically 'estimated' else.

The applied APIs are:

#. *GetProductInfo*
      The *GetVersionEx* interface is supported beginning with *NT-6.0*. 
  
      .. note::

         see [GetProductInfo]_

         **Parameters**
         
            **dwOSMajorVersion**
         
               The major version number of the operating system. The minimum value is 6.
               
               The combination of the dwOSMajorVersion, dwOSMinorVersion, dwSpMajorVersion, and 
               dwSpMinorVersion parameters describes the maximum target operating system version 
               for the application. For example, Windows Vista and Windows Server 2008 are 
               version 6.0.0.0 and Windows 7 and Windows Server 2008 R2 are version 6.1.0.0. 
               All Windows 10 based releases will be listed as version 6.3.



#. *GetVersionEx*
      The *GetVersionEx* interface has changed with *Windows-8.1* into *GetVersionExA*, where
      some different values are introduced. 
  
      .. note::

         see [GetVersionExA]_

         [GetVersionEx may be altered or unavailable for releases after Windows 8.1. Instead, use the Version Helper 
         functions]
   
         With the release of Windows 8.1, the behavior of the GetVersionEx API has changed in the value it will return
         for the operating system version. The value returned by the GetVersionEx function now depends on how the 
         application is manifested.

      For implementation details see :ref:`jy.dist.nt.Kernel32GetProductInfo(.java) <JNA_ADVAPI32GETPRODUCTINFO>`.  

      The *platformids* relies on the interface
      *com.sun.jna.platform.win32.Kernel32.WinNT.GetVersionEx* and the data
      *com.sun.jna.platform.win32.Kernel32.WinNT.OSVERSIONINFOEX*.
      It expects the changes of *OSVERSIONINFOEXA* were taken into account.

Another issue is the new numbering scheme introduced by *NT-10.0*.
The product version and the build number are now distinguished, while the build number for major version-steps
are subnumbered by the *UBR* instead of the *SP*.
This is handeled by *platformids* by the applied registry interface via :ref:`jy.dist.nt.Advapi32GetCurrentVersion(.java) <JNA_ADVAPI32GETCURRENTVERSION>`..

.. _IMPLEMENTATIONDETAILS_JNASETUP:

Implementation Details
----------------------
* Core Packages of generic support - status at Release 5.0.0  Oct 7, 2018:
   
   .. raw:: html
   
      <div class="shortcuttab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">
   
   +---------------------------------------------------------------------------------------------------------+--------------------------------+
   | implementation                                                                                          | description                    |
   +=========================================================================================================+================================+
   | `jna.jar <https://github.com/java-native-access/jna/blob/master/dist/jna.jar>`_                         | core components                |
   +---------------------------------------------------------------------------------------------------------+--------------------------------+
   | `jna-platform.jar <https://github.com/java-native-access/jna/blob/master/dist/jna-platform.jar>`_       | platform components            |
   +---------------------------------------------------------------------------------------------------------+--------------------------------+
   | `jna-min.jar <https://github.com/java-native-access/jna/blob/master/dist/jna-min.jar>`_                 | minimum set \(?)               |
   +---------------------------------------------------------------------------------------------------------+--------------------------------+
   | `Releases <https://github.com/java-native-access/jna/releases/>`_                                       | downloads                      |
   +---------------------------------------------------------------------------------------------------------+--------------------------------+
   | `jna.jar - Release 5.2.0  Dec 23, 2018 <https://github.com/java-native-access/jna/releases/tag/5.2.0>`_ | Initial tests of *platformids* |
   +---------------------------------------------------------------------------------------------------------+--------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>

   
   
* Native Platform Packages of supported platforms by *JNA* and *platfromids* - status at Release 5.0.0  Oct 7, 2018:
            
   .. raw:: html
   
      <div class="shortcuttab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">
   
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | requiered by | category | ostype | os            | arch | packages                                                                                              |                                                                                                 |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | platfromids  |          |        |               |      |                                                                                                       |                                                                                                 |                                                                                                 | |
   +==============+==========+========+===============+======+=======================================================================================================+=================================================================================================+=================================================================================================+=+
   | --           | POSIX    | BSD    | FreeBSD       | x86  | `freebsd-x86-64.jar <https://github.com/java-native-access/jna/blob/master/dist/freebsd-x86-64.jar>`_ | `freebsd-x86.jar <https://github.com/java-native-access/jna/blob/master/dist/freebsd-x86.jar>`_ |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | --           |          |        | OpenBSD       | x86  | `openbsd-x86-64.jar <https://github.com/java-native-access/jna/blob/master/dist/openbsd-x86-64.jar>`_ | `openbsd-x86.jar <https://github.com/java-native-access/jna/blob/master/dist/openbsd-x86.jar>`_ |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | --           |          | Darwin | OS-X          | x86  | `darwin.jar <https://github.com/java-native-access/jna/blob/master/dist/darwin.jar>`_                 |                                                                                                 |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | --           |          | Linux  | \(any\?)      | ARM  | `linux-aarch64.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-aarch64.jar>`_   | `linux-arm.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-arm.jar>`_     | `linux-armel.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-armel.jar>`_ | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | --           |          |        |               | x86  | `linux-x86-64.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-x86-64.jar>`_     | `linux-x86.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-x86.jar>`_     |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | --           |          | UNIX   | SunOS/Solaris | x86  | `sunos-x86-64.jar <https://github.com/java-native-access/jna/blob/master/dist/sunos-x86-64.jar>`_     | `sunos-x86.jar <https://github.com/java-native-access/jna/blob/master/dist/sunos-x86.jar>`_     |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | **X**        | Windows  | NT     | >=XP \(\?)    | x86  | `win32-x86-64.jar <https://github.com/java-native-access/jna/blob/master/dist/win32-x86-64.jar>`_     | `win32-x86.jar <https://github.com/java-native-access/jna/blob/master/dist/win32-x86.jar>`_     |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   | **X**        |          |        | XP < \(\?)    | x86  | \(?)                                                                                                  |                                                                                                 |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   |              |          |        | IoT           | x86  | -- \(?)                                                                                               |                                                                                                 |                                                                                                 | |
   +--------------+----------+--------+---------------+------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-+
   
   .. raw:: html
   
      </div>
      </div>
      </div>

* Platforms not actively supported by *platformids* - still may work.

   .. raw:: html
   
      <div class="shortcuttab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">
   
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | category | ostype  | os            |                                                                                                         |                                                                                                       |                                                                                                       |
   +==========+=========+===============+=========================================================================================================+=======================================================================================================+=======================================================================================================+
   | POSIX    | UNIX    | AIX           | `aix-ppc.jar <https://github.com/java-native-access/jna/blob/master/dist/aix-ppc.jar>`_                 | `aix-ppc64.jar <https://github.com/java-native-access/jna/blob/master/dist/aix-ppc64.jar>`_           |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          | UNIX    | SunOS/Solaris | `sunos-sparc.jar <https://github.com/java-native-access/jna/blob/master/dist/sunos-sparc.jar>`_         | `sunos-sparcv9.jar <https://github.com/java-native-access/jna/blob/master/dist/sunos-sparcv9.jar>`_   |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          | Linux   |               | `linux-ia64.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-ia64.jar>`_           |                                                                                                       |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          |         |               | `linux-mips64el.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-mips64el.jar>`_   |                                                                                                       |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          |         |               | `linux-ppc.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-ppc.jar>`_             | `linux-ppc64.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-ppc64.jar>`_       | `linux-ppc64le.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-ppc64le.jar>`_   |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          |         |               | `linux-s390x.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-s390x.jar>`_         |                                                                                                       |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          |         |               | `linux-sparcv9.jar <https://github.com/java-native-access/jna/blob/master/dist/linux-sparcv9.jar>`_     |                                                                                                       |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          | Android |               | `android-aarch64.jar <https://github.com/java-native-access/jna/blob/master/dist/android-aarch64.jar>`_ | `android-arm.jar <https://github.com/java-native-access/jna/blob/master/dist/android-arm.jar>`_       | `android-armv7.jar <https://github.com/java-native-access/jna/blob/master/dist/android-armv7.jar>`_   |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          |         |               | `android-mips.jar <https://github.com/java-native-access/jna/blob/master/dist/android-mips.jar>`_       | `android-mips64.jar <https://github.com/java-native-access/jna/blob/master/dist/android-mips64.jar>`_ | `android-x86-64.jar <https://github.com/java-native-access/jna/blob/master/dist/android-x86-64.jar>`_ |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   |          |         |               | `android-x86.jar <https://github.com/java-native-access/jna/blob/master/dist/android-x86.jar>`_         |                                                                                                       |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | Windows  | NT      | WinCE         | `w32ce-arm.jar <https://github.com/java-native-access/jna/blob/master/dist/w32ce-arm.jar>`_             |                                                                                                       |                                                                                                       |
   +----------+---------+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   
   .. raw:: html
   
      </div>
      </div>
      </div>

* Documentation and Sources:

   * Documents: `doc.zip <https://github.com/java-native-access/jna/blob/master/dist/doc.zip>`_
   * Sources: `src-full.zip <https://github.com/java-native-access/jna/blob/master/dist/src-full.zip>`_ / `src.zip <https://github.com/java-native-access/jna/blob/master/dist/src.zip>`_

Installation
------------
The installation of the *Windows-NT* platform requires the packages within the *CLASSPATH*:

#. `jna.jar <https://github.com/java-native-access/jna/blob/master/dist/jna.jar>`_
#. `jna-platform.jar <https://github.com/java-native-access/jna/blob/master/dist/jna-platform.jar>`_
#. `win32-x86-64.jar <https://github.com/java-native-access/jna/blob/master/dist/win32-x86-64.jar>`_  
   and/or `win32-x86.jar <https://github.com/java-native-access/jna/blob/master/dist/win32-x86.jar>`_ - depends on the architectecture of the used *JVM*
