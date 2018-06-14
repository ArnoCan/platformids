.. raw:: html

   <div class="shortcuttab">


'platformids.__init__' - Module
===============================

Module
------

.. automodule:: platformids.__init__

Constants
---------

Python Version
^^^^^^^^^^^^^^
.. index::
   pair: Python; V3K
   pair: Python; PYVxyz

* **V3K**: Python3.5+, else Python2.7

  .. parsed-literal::

     V3K := (
          True  # Python3.5+
        | False # Python2.7
     )

     # raises exception *platformids.PlatformIDsError* when version < 2.7 or in 3.0.0 < 3.5

* **PYVxyz**: Bit encoded current Python version:

  .. parsed-literal::

     Vxyz := xxxyyyyyzzzzzzzz
     
     xxx      := major version
     yyyyy    := minor version
     zzzzzzzz := build

     For example for the version "3.6.5": ::

     xxx      = 3 = 011
     yyyyy    = 6 = 00110
     zzzzzzzz = 5 = 00000101  
     
     xxxyyyyyzzzzzzzz = 26117 = 0b0110011000000101 

  This enables the binary checks with pre-defined integer values for fast frequent
  evaluation:

  .. parsed-literal::

     if Vxyz & 26117:  # 0b0110011000000101
        # this is version 3.6.5

     if Vxyz & 26112:  # 0b0110011000000000
        # this is version 3.6

     if Vxyz < 26112:
        # this is pre-version 3.6, e.g. 3.5.x

  The use of numerical reference values is here perfectly applicable because of the 
  static nature of version dependencies. 

* **PYVxyz**: Predefined values

   .. index::
      pair: Python; PYV2
      pair: Python; PYV26
      pair: Python; PYV27
      pair: Python; PYV3
      pair: Python; PYV32
      pair: Python; PYV34
      pair: Python; PYV35
      pair: Python; PYV36
      pair: Python; PYV362
      pair: Python; PYV365

   .. parsed-literal::
   
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

String Encoding
^^^^^^^^^^^^^^^

.. index::
   pair: Python; ISSTR
   pair: Python; unicode

* **ISSTR**: string and unicode for type comparison:

  .. parsed-literal::

     if V3K:
        ISSTR = (str, bytes,)
     else:
        ISSTR = (str, unicode,)

* **unicode**: for Python3, remaps *unicode* to *str*:

  .. parsed-literal::

     if V3K:
        unicode = str

.. _ENUM_PLATFORM:

Platform Definitions
^^^^^^^^^^^^^^^^^^^^
The internal representation of the platform parameter is an *int* used 
as bit-array for binary logic operations.
The most interfaces support the bit-array representation as well as the
alternatively string name macros as defined by the *sys.platform* interface.


Structure of bit masks
""""""""""""""""""""""
The predefined bitmasks are provided as a label of form *RTE_<name>*, which covers
the grouping of bit-mask blocks and the increments within these groups.

.. raw:: html

   The comitted 
   <span class="textmarker"><bold>interface is<bold></span>
   the
   <span class="textmarker"><bold>NAMED ENUMERATION only<bold></span>
   ,
   <span class="textmarker"><bold>NOT the assigned numeric value<bold></span>
   .
   Therefore the values must never be accessed explicitly.
   The same principle with relative offsets as values for enumerations has to 
   be applied when defining custom values.

The general algorithm of the calculation for the bit-mask is based on the grouping
of categories, type sets, and members into nested bit-blocks.
The combination of category bit masks for bit-blocks and the addition of sub-blocks
for context-bitmasks of it's members combines the performance of logical bit-operations
with the reduction of the number of required bits.
The principle is similar to the network addresses of TCP networks.
The lower 16 bits are reserved for the groups and members of a category, which is similar
to a class-B network address schema.
This is required due to the vast number of permutations of possible OS releases, which else would lead to  
bit arrays of astronomical dimensions. 


Bit-Mask Definitions
""""""""""""""""""""
The following additional definitions are introduced.

* The following aliasses are defined in addition:

  +----------------+---------+
  | *sys.platform* | *alias* |
  +================+=========+
  | win32          | win     |
  +----------------+---------+
  | darwin         | osx     |
  +----------------+---------+

* The bit-mask provides the bit for the OS as well as the bit for the 
  base category and the set.  

  +---------------+----------------+-------------+---------------------------+
  | Syntax Domain | *sys.platform* | Category    | set                       |
  +===============+================+=============+===========================+
  | Windows       | win            | RTE_WIN32   | RTE_WIN32                 |
  +---------------+----------------+-------------+---------------------------+
  | Cygwin        | cygwin         | RTE_POSIX   | RTE_CYGWIN                |
  +---------------+----------------+-------------+---------------------------+
  | Linux         | linux, linux2  | RTE_POSIX   | RTE_LINUX                 |
  +---------------+----------------+-------------+---------------------------+
  | Solaris       | sunos          | RTE_POSIX   | RTE_SOLARIS               |
  +---------------+----------------+-------------+---------------------------+
  | BSD           | bsd            | RTE_POSIX   | RTE_BSD                   |
  +---------------+----------------+-------------+---------------------------+
  | OS-X          | darwin         | RTE_POSIX   | RTE_OSX                   |
  +---------------+----------------+-------------+---------------------------+
  | GENERIC       | n.a.           | RTE_GENERIC |                           |
  +---------------+----------------+-------------+---------------------------+


.. index::
   pair: platform; RTE
   pair: platform; RTE_BSD
   pair: platform; RTE_CYGWIN
   pair: platform; RTE_DARWIN
   pair: platform; RTE_GENERIC
   pair: platform; RTE_LINUX
   pair: platform; RTE_OSX
   pair: platform; RTE_POSIX
   pair: platform; RTE_SOLARIS
   pair: platform; RTE_WIN32

* Enum Values:

  * Base type blocks:

    * **RTE_CYGWIN** - **cygwin**: Cygwin [CYGWIN]_
    * **RTE_POSIX** - **posix**: Posix systems using *fcntl* [POSIX]_.
    * **RTE_WIN32** - **win**: All Windows systems [MS-DTYP]_
    * **RTE_GENERIC**: Undefined platform for special cases

  * Sets of POSIX base system platformids:

    * **RTE_BSD** - **bsd**: BSD, - OpenBSD, FreeBSD, NetBSD - as Posix system [POSIX]_.
    * **RTE_DARWIN** - **darwin**: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
    * **RTE_DEBIAN** - **debian**: debian - as Posix system [POSIX]_.
    * **RTE_LINUX** - **linux**: Linux with specific add-ons - OS, DIST, GNU - as Posix system [POSIX]_.
    * **RTE_OSX** - **osx**: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
    * **RTE_SOLARIS** - **solaris**: UNIX/Solaris, as Posix system [POSIX]_.

    .

  * **RTE_GENERIC**: Undefined platform for special cases.

* Control Variables:

  * **RTE**: Current runtime-environment variable.

For the complete list refer to the sources [`platformids.__init__.py <_modules/platformids/__init__.html#>`_].

Calculation of bit masks
""""""""""""""""""""""""
A typical example for the base of the mapping and algorithms is:

.. parsed-literal::

   # category: posix
   RTE_POSIX = 8192  #: Posix systems using *fcntl* [POSIX]_.

   # set: OS-X
   # bit-block: Apple - OS-X
   RTE_DARWIN = RTE_POSIX + 1  #: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
   RTE_OSX = RTE_POSIX + 2  #: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.

   # set: Sun - Solaris
   RTE_SOLARIS = RTE_POSIX + 16  #: UNIX/Solaris, as Posix system [POSIX]_.

   # set: BSD
   RTE_BSD = RTE_POSIX + 32  #: BSD, - OpenBSD, FreeBSD, NetBSD - as Posix system [POSIX]_.

   # set: Linux
   RTE_LINUX = RTE_POSIX + 64  #: Linux with specific add-ons - OS, DIST, GNU - as Posix system [POSIX]_.
   
   # members" Linux
   RTE_CENTOS  = RTE_LINUX + 1  #: CentOS
   RTE_CENTOS4 = RTE_LINUX + 2  #: CentOS-4
   RTE_CENTOS5 = RTE_LINUX + 3  #: CentOS-5
   RTE_CENTOS6 = RTE_LINUX + 4  #: CentOS-6
   RTE_CENTOS7 = RTE_LINUX + 5  #: CentOS-7
   
   RTE_FEDORA = RTE_LINUX + 32  #: Fedora
   RTE_FEDORA19 = RTE_LINUX + 33  #: Fedora-19
   RTE_FEDORA27 = RTE_LINUX + 34  #: Fedora-27
   
   RTE_DEBIAN = RTE_LINUX + 64  #: Debian
   RTE_DEBIAN6 = RTE_LINUX + 65  #: Debian - squeeze
   RTE_DEBIAN7 = RTE_LINUX + 66  #: Debian - wheezy
   RTE_DEBIAN8 = RTE_LINUX + 67  #: Debian - jessy
   RTE_DEBIAN9 = RTE_LINUX + 68  #: Debian - stretch
   
The calculations are for OS and distributions:

.. parsed-literal::

   #
   # explicit
   #
   if RTE & RTE_POSIX: # use category
      pass
   
   if RTE & RTE_LINUX: # use set
      pass
      
   if RTE & RTE_CENTOS: # use distro
      pass

   if RTE & RTE_CENTOS7: # use release
      pass

   #
   # hierarchical
   #
   if RTE & RTE_POSIX: # use category
      if RTE & RTE_LINUX: # use set
         # do s.th. ...
               
         if RTE & RTE_CENTOS7: # use release
            pass
         else:
            # do s.th. ...

      elif RTE & RTE_BSD: # use set
         # do s.th. else...

         if RTE & RTE_OPENBSD: # use release
            pass
         else:
            # do s.th. else...
               

The calculations are for URI and schemes:

.. parsed-literal::

   if RTE & RTE_URI: # use category
      pass
   
   if RTE & RTE_HTTP: # use scheme
      pass
      

Memory Management
"""""""""""""""""
The custom bit-mask blocks are managed by the assignment of reserved value ranges.
These has to be handled cooperative by the application, no range checks for the assignment of
net key/value/pairs is done.

The values are readonly once assigned.
A basic protection is implemented, where a reassignment attempt raises an exception.  

Attributes
----------
The following attributes are official interface and could be used alternively
to the access functions.

RTE
^^^
The *RTE* variable is assigned during the initial load of the module.
The value indicated the current runtime platform as a bit-mask and could be used
for bit-operations.
For possible values refer to the constants '*RTE_\**',
see `Platform Definitions <#platform-definitions>`_. 

rte2num
^^^^^^^
The map of string and for smart coding of the integer values too onto
the defined numerical enum values. 

.. parsed-literal::

   rte2num = {
     <str-or-num>: RTE_<*>,
   }

   # application:

   rte2num['bsd']   == RTE_BSD 
   rte2num[RTE_BSD] == RTE_BSD

For the complete list refer to the sources [`platformids.__init__.py <_modules/platformids/__init__.html#>`_].

num2rte
^^^^^^^
The map of numerical values onto
the defined string values. 

.. parsed-literal::

   num2rte = {
     RTE_<*>: <str-or-num>,
   }

   # application:

   rte2num[RTE_BSD] == 'bsd'  

For the complete list refer to the sources [`platformids.__init__.py <_modules/platformids/__init__.html#>`_].

V3K
^^^
Adjust to current major Python version to Python3 vs. Python2.

.. code-block:: python
   :linenos:

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


The definition includes also the helper variables *ISSTR* and *unicode*,
which support basic multiplatform encoding checks for Python2 and Python3. 


PYVxyz
^^^^^^
The bit encoded Python version of current executable for bit mask operations.

.. code-block:: python
   :linenos:

   PYVxyz = getPYVxyz(*sys.version_info[:3])

   e.g. for Python-3.6.5
   
   xxx:      011
   yyyyy:    00110
   zzzzzzzz: 00000101

   PYVxyz = 0b0110011000000101 = 0x6605 = 26117

Du to the static nature of the version number code dependencies the reference values could be 
provided as integer constants when frequent evaluation is required.

Pre-Defined PYVxyz Constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Predefined values for comon dependencies of changed *Python* and/or *CPython* interfaces.

.. code-block:: python
   :linenos:

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


Functions
---------
get_custom_num_base
^^^^^^^^^^^^^^^^^^^
.. autofunction:: get_custom_num_base

get_custom_num_range
^^^^^^^^^^^^^^^^^^^^
.. autofunction:: get_custom_num_range

get_num2rte
^^^^^^^^^^^
.. autofunction:: get_num2rte

get_rte2num
^^^^^^^^^^^
.. autofunction:: get_rte2num

getPYVxyz
^^^^^^^^^

.. code-block:: python
   :linenos:

   from platformids import PYV35, PYVxyz  # pre-defined values 

   from platformids import getPYVxyz      # function interface for the calculation
                                          # of bit masks for releases

   # calculate non-pre-defined values
   pyv33 = getPYVxyz(3, 3)
   pyv362 = getPYVxyz(3, 6, 2)

   if PYVxyz & pyv33:
      # do s.th....
      
   elif PyVxyz & pyv362:
      # do s.th. else...
      
   elif PyVxyz >= PYV35:
      # do s.th. else...
      
   else:
      # support the minimal and/or legacy spec....

.. autofunction:: getPYVxyz

set_num2rte
^^^^^^^^^^^
.. autofunction:: set_num2rte

set_rte2num
^^^^^^^^^^^
.. autofunction:: set_rte2num


Exceptions
----------

.. autoexception:: PlatformIDsError

.. raw:: html

   </div>

