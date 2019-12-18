
.. _HOWTO_MULTIPLATFORM:

Howto Develop for Multiple Platforms
====================================

Calculation of bit masks
------------------------

A typical example for the base of the mapping and algorithms is:

.. parsed-literal::

   # category: posix
   RTE_POSIX = 8192  #: Posix systems using *fcntl* [POSIX]_.

   # set: OS-X
   # bit-block: Apple - OS-X
   RTE_OSX = RTE_POSIX + 1  #: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
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
               


