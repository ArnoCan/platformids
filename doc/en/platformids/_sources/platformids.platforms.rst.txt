
.. _PLATFORMSMODULE:

.. raw:: html

   <div class="shortcuttab">


platformids.platforms
=====================

The *platforms* module provides the identifiers for the runtime platform as defined by
the OS and distribution.
The values are either scanned from the current platform by:

   .. code-block:: python
      :linenos:
      
      from platformids.platforms import PlatformParameters 
      
      x = PlatformParameters()  # creates an empty object
      x.scan()                  # scans the platform
      print(str(x))             # prints display-format, see also 'repr'

For predefined and tested platforms on *amd64* and *arm64/32* refer to the :ref:`table of standard OS <OS_SUPPORTED>`.

For example:

* Fedora27:

   .. parsed-literal::
   
      category         = posix - RTE_POSIX
      ostype           = linux - RTE_LINUX
      dist             = fedora - RTE_FEDORA
      distrel          = fedora27 - RTE_FEDORA27
      dist-rel-name    = Twenty Seven
      dist-vers        = [27, 0, 0]
      os-vers          = [4, 16, 15]
      hexversion       = 
      os-hexversion    = 0

* OS-X-10.6.8 - SnowLeopard:

   .. parsed-literal::
   
      category         = posix - RTE_POSIX
      ostype           = darwin - RTE_DARWIN
      dist             = osx - RTE_OSX
      distrel          = osx-10.6.8 - RTE_OSX1068
      dist-rel-name    = todo-distrelname
      dist-vers        = [10, 6, 8]
      os-vers          = [10, 8, 0]
      hexversion       = 
      os-hexversion    = 0

* CentOS7 - aarch64:

   .. parsed-literal::
   
      category         = posix - RTE_POSIX
      ostype           = linux - RTE_LINUX
      dist             = centos - RTE_CENTOS
      distrel          = centos-7.5.1804  - RTE_CENTOS75
      dist-rel-name    = Core
      dist-vers        = [7, 5, 1804]
      os-vers          = [4, 14, 52]
      hexversion       = 
      os-hexversion    = 0
 
* Armbian - armhfx:

   Or in case of *Armbian* derived from *debian* the release names are coupled, while
   the release numbering is independent:
   
      .. parsed-literal::
      
         category         = `posix - RTE_POSIX <platformids.html#bit-mask-definitions>`_
         ostype           = `linux - RTE_LINUX <platformids.html#bit-mask-definitions>`_
         dist             = `armbian - RTE_ARMBIAN <platformids.html#bit-mask-definitions>`_
         distrel          = `armbian-5.50.0 - RTE_ARMBIAN5500 <embed/armbian.html#>`_
         dist-rel-name    = `Armbian-stretch <embed/armbian.html#>`_
         dist-vers        = [5, 50, 0]
         os-vers          = [4, 14, 52]
         hexversion       = 
         os-hexversion    = 0

* Windows7 Ultimate:

   The windows release provides the additional windows specific parameters
   *ServicePack*, *ProductType*, and *SuiteMask*.   
   
      .. parsed-literal::
      
         category         = windows - RTE_WINDOWS
         ostype           = nt - RTE_NT
         dist             = winws
         distrel          = nt-6.1.7601
         dist-rel-name    = Windows7U
         dist-vers        = [6, 1, 7601]
         os-vers          = [7, 0, 0]
         hexversion       = RTE_FEDORA27
         os-hexversion    = 0
         wServicePack     = [1, 0]        # see [GetVersionEx]_
         wProductType     = 1             # see [GetVersionEx]_
         wSuiteMask       = 256           # see [GetVersionEx]_

Module
------
The doc-strings of the document are spared in order to support in any case a slim memory-print
and fast load time.

.. automodule:: platformids.platforms

PlatformParameters
------------------
The class provides the representation of the current and/or a user provided platform.
The automatic scan of the current runtime environment has to be triggered explicitly 
by the method `platformids.PlatformParameters.scan() <#scan>`_.
The call replaces all attribute values of the current instance by the detected values.

.. autoclass:: PlatformParameters

Attributes
^^^^^^^^^^

The following public attributes are provided for the 
:ref:`hierachical platform categorization <OSTYPEANDDISTCATEGORIES>`:

.. index::
   triple: PlatformParameters; attributes; category

.. _attr_category:

* **category**

   The type of operating system. 
   
      .. parsed-literal::
      
        category := <class-of-os>
        
        class-of-os := (
             wpemu            # RTE_WPEMU
           | posix            # RTE_POSIX
           | pwemu            # RTE_PWEMU 
           | windows          # RTE_WIN
        )  

.. index::
   triple: PlatformParameters; attributes; ostype

.. _attr_ostype:

* **ostype**

   The family of operating systems. 
   
      .. parsed-literal::
      
        ostype := <type-of-os>
        
        type-of-os := (
             bsd              # RTE_BSD
           | cygwinnt         # RTE_CYGWINNT
           | darwin           # RTE_DARWIN
           | linux            # RTE_LINUX
           | nt               # RTE_NT
           | unix             # RTE_UNIX
        )

.. index::
   triple: PlatformParameters; attributes; dist

.. _attr_dist:

* **dist**

   The packaged distributions of operating systems.
   
      .. parsed-literal::
      
        dist := <name-of-distribution>
        
        name-of-distribution := (
             centos           # RTE_CENTOS 
           | debian           # RTE_DEBIAN
           | fedora           # RTE_FEDORA
           | nt63             # RTE_NT63
           | nt100            # RTE_NT100
           | openbsd          # RTE_OPENBSD
           | osx              # RTE_OSX
           | rhel             # RTE_RHEL
           | suse             # RTE_SUSE
           # and others
        )

.. index::
   triple: PlatformParameters; attributes; distrel

.. _attr_distrel:

* **distrel**

   A specific release of a packaged operating system.
   
      .. parsed-literal::
      
         distrel := (
              centos76       # CentOS-7.6 or CentOS-7.6-1804 
            | debian96       # Debian-9.6
            | fedora27       # Fedora27
            | openbsd63      # OpenBSD-6.3
            | rhel76         # RHEL-7.6
            | rhel8          # RHEL-8 / 8.0
            | snowleopard    # OS-X-10.6.8 / OS-X-10.6.0
            | windows10p     # Windows 10 Professional
            | windows2012r2  # Windows Server 2010R2
            | windows2016s   # Windows Server 2016
            | windows2019se  # Windows Server 2019 Essentials
            | windows7u      # Windows 7 Ultimate
            # and others
         )

.. index::
   triple: PlatformParameters; attributes; distrel_hexversion

.. _attr_distrel_hexversion:

* **distrel_hexversion**

   The numeric bitmask of the release version representing all previous
   attributes within one 32-bit integer. See
   :ref:`bitmasks <BITMASKSOSDIST>`:
   
      .. parsed-literal::
      
         distrel := (
              RTE_RHEL73     # RHEL 7.3
            | RTE_RHEL8      # RHEL 8.0
            | RTE_FEDORA27   # Fedora27
            | RTE_DEBIAN96   # Debian-9.6
            | RTE_W10P       # Windows 10 Professional
            | RTE_W2016      # Windows Server 2016
            | RTE_OSX1068    # OS-X Snowleopard
            # and others
         )

.. index::
   triple: PlatformParameters; attributes; distrel_version

.. _attr_distrel_version:

* **distrel_version**

   3-valued integer version of the distribution 

.. index::
   triple: PlatformParameters; attributes; ostype_version

.. _attr_ostype_version:

* **ostype_version**

   3-valued integer version of the OS kernel


__init__
^^^^^^^^
.. automethod:: PlatformParameters.__init__

__and__
^^^^^^^
.. automethod:: PlatformParameters.__and__

__eq__
^^^^^^
.. automethod:: PlatformParameters.__eq__

__getitem__
^^^^^^^^^^^
.. automethod:: PlatformParameters.__getitem__

__iand__
^^^^^^^^
.. automethod:: PlatformParameters.__iand__

__int__
^^^^^^^
.. automethod:: PlatformParameters.__int__

__ior__
^^^^^^^
.. automethod:: PlatformParameters.__ior__

__iter__
^^^^^^^^
.. automethod:: PlatformParameters.__iter__

__len__
^^^^^^^
.. automethod:: PlatformParameters.__len__

__ne__
^^^^^^
.. automethod:: PlatformParameters.__ne__

   See *__eq__*.

__or__
^^^^^^
.. automethod:: PlatformParameters.__or__

__rand__
^^^^^^^^
.. automethod:: PlatformParameters.__rand__

__repr__
^^^^^^^^
.. automethod:: PlatformParameters.__repr__

__ror__
^^^^^^^
.. automethod:: PlatformParameters.__ror__

__setitem__
^^^^^^^^^^^
.. automethod:: PlatformParameters.__setitem__

__str__
^^^^^^^
.. automethod:: PlatformParameters.__str__


get_hexversion
^^^^^^^^^^^^^^
.. automethod:: PlatformParameters.get_hexversion

get_oshexversion
^^^^^^^^^^^^^^^^
.. automethod:: PlatformParameters.get_oshexversion

get_json
^^^^^^^^
.. automethod:: PlatformParameters.get_json

items
^^^^^
.. automethod:: PlatformParameters.items

keys
^^^^
.. automethod:: PlatformParameters.keys

pretty_format
^^^^^^^^^^^^^
.. automethod:: PlatformParameters.pretty_format

scan
^^^^
.. automethod:: PlatformParameters.scan

   Sets the member attributes:
   
   * *distrel_version*:
      Three-value segments of ditribution version
      as numeric tuple.

         .. parsed-literal::

            distrel_version := (<#major>, <#minor>, <#micro>)

   * *distrel_id*
      String identifier of the complete distribution.
      This varies in dependency of the distribution.
      The state reflects commonly the distribution release, and when available the update/upgrade releases.
      Which varies and is for some rolling distributions currently not available.

      For example:

         .. parsed-literal::

            'Ubuntu1904'     - :ref:`Ubuntu-19.04 <enumUBUNTU>`
            'arch20190401'   - :ref:`ArchLinux-2019.04.01 <enumARCHLIN>`
            'armbian550'     - :ref:`Armbian-5.50 <enumARMBIAN>`
            'centos76'       - :ref:`CentOS-7.6.1810 <enumCENTOS>`
            'cygwin268'      - :ref:`Cygwin-2.6.8 <enumCYGWIN>`
            'fedora29'       - :ref:`Fedora29 <enumFEDORA>`
            'kali20191'      - :ref:`KaliLinux-2019.1 <secnetKALILINUX>`
            'nt1001809'      - :ref:`NT-10.0.1809 <enumWINNT>`
            'osx1068'        - :ref:`OSX-10.6.8 <enumOSX>`

   * *dist*:
      String identifier of the distributions '*dist*' value.

   * *distrel*:
      The human readable distribution release:

         .. parsed-literal::

            distrel := <dist>-<major>.<minor>.<micro>

   * *ostype*:
      The string identifier of the '*ostype*'.
      For example:

         .. parsed-literal::

            'nt', 'linux', ...

   * *ostype_id*:
      Same as '*ostype*'.

   * *ostype_version*:
      The numeric tuple of the os release:

         .. parsed-literal::

            ostype_version := (<#major>, <#minor>, <#micro>)

   * *distrel_hexversion*
      The calculated hexadcimal identifier ot the distribution.

values
^^^^^^
.. automethod:: PlatformParameters.values

Exceptions
----------

.. autoexception:: PlatformParametersError

.. raw:: html

   </div>

