.. _CUSTOM_MODULE_AIX:

.. _docAIXX86:

pythonids.dist.aix
==================
Module AIX \[:ref:`doc <enumAIX>`].

Description
-----------
The *AIX* OS release for the *x86* [AIX13PS2]_ platform is a bit outdated, but for basic experiences and eductaion purposes
of future *AIX* admins perfectly OK.
This in particular as it is easily installable within a virtual machine, e.g. *VirtualBox* on almost any host-platform.

Release History
^^^^^^^^^^^^^^^

The origianl product data of AIX [AIX]_ is for the *x86* [AIX13PS2]_ platform - still usable, e.g. within *VirtualBox*:

.. parsed-literal::

   **IBM Sales Manual (US) - Document 5765-160**
      5765-160 IBM AIX PS/2 OPERATING SYSTEM V1.3
   
   **IBM U.S. Product Life Cycle Dates**

      **Program                                  Marketing   Service      Replaced**
      **Number   VRM     Announced   Available   Withdrawn   Discontinued    By**
      5765-160 1.03.0  1992/09/21  1992/10/02  1995/03/10      -            -
   
with the components:

.. parsed-literal::

   **Program Number**

      5765-160 53G0218 AIX PS/2 Operating System Version 1.3 (Diskette)
      5765-160 53G0219 AIX PS/2 Operating System Version 1.3 (Tape)
      5765-161 52G9954 AIX PS/2 Operating System Version 1.3 (Diskette)
      5765-161 52G9965 AIX PS/2 Operating System Version 1.3 (Tape)
      5765-162 52G9945 AIX PS/2 Application Development Toolkit Version 1.3
      5765-163 52G9946 AIX PS/2 Text Formatting System Version 1.3
      5765-164 52G9947 AIX PS/2 DOS Merge Version 1.3
      5765-165 52G9953 AIX PS/2 INmail/INed/INnet/INftp Version 1.3
      5765-166 52G9948 AIX PS/2 Network File System Version 1.3
      5765-167 52G9949 AIX PS/2 Transmission Control Protocol/Internet Protocol Version 1.3
      5765-168 52G9950 AIX PS/2 X.25 Version 1.3
      5765-169 52G9952 AIX PS/2 X-Windows Version 1.3
      5765-170 52G9951 AIXwindows Environment for PS/2 Version 1.3
      5765-171 52G9955 AIX PS/2 X-Windows Version 1.3 

The extract from the original product sheet (C)IBM Corp.:

.. parsed-literal::

   **Abstract**
   
      (For IBM US, No Longer Available as of March 10, 1995)
      
      IBM reaffirms its commitment to open systems by announcing Advanced Interactive Executive (AIX)* PS/2* 
      Version 1.3, its entry level member of the AIX family.
      
      AIX PS/2 Operating System Version 1.3 and its associated Licensed Program Products (LPPs) provide full
      hardware support and exploitation for all models of IBM PS/2 system units based on the 32-bit INTEL** 386sx-16MHz
       up through the INTEL 486DX2-66MHz, utilizing both IBM Microchannel or IBM AT-Bus architectures. AIX PS/2 
       Operating System Version 1.3 will offer support for selected OEM hardware configurations, certifying them on a per bid basis.
      
      Support is offered for numerous new options, adapters, hardfiles and displays listed in the Growth Enablement Section.
      
      Support is also provided for the IBM GEARBOX* Model 800 486 Industrial Computer.
      
      Performance tuning in AIX PS/2 Operating System Version 1.3 offers increased throughput for input/output.
      
      The windowing and Graphical User Interface (GUI) areas have been improved with the X Window System V11 R5** and OSF/Motif 1.1.3**
      
      AIX PS/2 Operating System Version 1.3 provides interoperability with other versions of AIX, UNIX* and other IBM and non-IBM 
      Operating Systems through AIX PS/2 Transmission Control Protocol/Internet Protocol Version 1.3 and AIX PS/2 Network File 
      System Version 1.3.
      
      Also provided are enhanced installation, backup and update procedures aptly named the EZ-UTILITIES which are targeted
      specifically for IBM Business Partners, and large installations to simplify operating system installation and maintenance.
      Refer to the Systems Management Section for more details on the EZ-UTILITIES.
      
      AIX PS/2 Operating System Version 1.3 and AIX PS/2 Operating System Extensions Version 1.3 are again offered on
      Internal Tape Backup Unit (ITBU) mini-cartridge tape, to ease installation.
      
      AIX PS/2 Operating System Version 1.3 provides full POSIX IEEE 1003.1-1988 standard compliance as specified in
      Section 2.1.2.2 of the IEEE standard.
      
      The programs announced today replace Version 1.2.1 of the AIX PS/2 Operating System and Version 1.2.1 of the
      Extensions and selected Related Licensed Program Products. Upgrades from AIX PS/2 Operating System Version 1.2.1,
      Version 1.2, Version 1.1 and Related Licensed Program Products Version 1.2.1, Version 1.2, Version 1.1 are offered
      to encourage migration.
      
      NOTE: Transparent Computing Facility (TCF) is NOT supported in AIX PS/2 Operating System Version 1.3
      
      NOTE: Usability Services Version 1.1.1 is NOT supported in AIX PS/2 Operating System Version 1.3
   
   **Product Positioning**
   
      AIX PS/2 Operating System Version 1.3 offers an entry level UNIX product targeted for the price-
      performance conscious INTEL processor based system market. The enhanced functions and quality 
      improvements make AIX PS/2 Operating System Version 1.3 very competitive in the UNIX-on-INTEL market.

   **Highlights**

       Provides full PS/2 Hardware exploitation for 386, 486 and SLC processors
   
       Offers limited support for selected IBM compatible systems
   
       Improves windowing and Graphical User Interface capabilities through X Windows V11R5 and Motif 1.1.3
   
       Provides DOS 5.0 support under DOS Merge
   
       Improves performance
   
       Connects easily to IBM and non-IBM networks
   
       Simplifies installation and system management
   
       Adds Korn Shell support 

   **Business Solutions**

      Performance tuning in AIX PS/2 Operating System Version 1.3 offers increased throughput for Input/Output (I/O)
      in both raw and block mode, in addition to kernel performance enhancements and smaller size requirements 
      available through the availability of serviceable shared libraries usage in applications written to utilize
      them. Enhancements have also been made to the pager and swapper areas of memory management that have 
      resulted in performance increases.
      
      Improvements in the windowing and Graphical User Interface (GUI) areas are highlighted with the introduction
      of the X Windowing System V11 R5 from MIT available in AIX PS/2 X-Windows Version 1.3 and AIXwindows Environment
      for PS/2 Version 1.3 and OSF's Motif 1.1.3 available in AIXwindows Environment for PS/2 Version 1.3 along with 
      AIXwindows Desktop. Support for the IBM Xstation 120 and Xstation 130 is provided in the AIX PS/2 X-Windows 
      Version 1.3ST. Support for XGA-2 provides non-interlaced, high resolution graphics on those displays that support it.
      
      AIX PS/2 Operating System Version 1.3 provides interoperability with other versions of AIX, UNIX, and other
      IBM and non-IBM operating systems, through the use of AIX PS/2 Transmission Control Protocol/Internet Protocol
      Version 1.3 and AIX PS/2 Network File System Version 1.3 over Ethernet or Token Ring. NFS allows remote file 
      system mounting and files can be copied and data shared between systems engaged in these connections. The use
      of AIX PS/2 X-Windows Version 1.3 or AIXwindows Environment for PS/2 Version 1.3 allows clients to be opened 
      and run on all participating machines.
      
      The Korn Shell is newly offered and supported in AIX PS/2 Operating System Version 1.3, in addition to
      the 'C' and Bourne Shells already offered.
   
   **Systems Management**

      AIX PS/2 Operating System Version 1.3 provides a set of six primary tools called EZ-UTILITIES, used to assist
      in the system management and distribution of AIX PS/2 Operating System Version 1.3. An enhanced installation 
      procedure decreases the time spent installing and reduces the possibility of installation error. 
      The following utilities are provided:

          ezbackup
          ezcustom
          ezinstall
          ezmkverify & ezverify
          ezfilter
          ezupdate 

      Ezbackup, ezcustom, ezinstall, and ezmkverify/ezverify are used when building distribution 
      media (boot diskette, installation diskette and backup media) perform routine system and/or
      user data backups and produce new distribution media when a system configuration change is made.
      Ezfilter and ezupdate are used to update existing AIX configurations.
      
      The EZ-UTILITIES package is designed to aid in the propagation of a master system to a target machine.
      The use of these utilities assumes that the master system is fully installed and configured, then 
      cloned or minimally tailored. The purpose of the EZ-UTILITIES is to make this cloning process easier.
      
      In addition, the EZ-UTILITIES package is designed as an aid in updating target machines as new 
      versions/PTFs of AIX are made available. Special utilities are provided to allow individual elements
      of PTFs to be selected and repackaged into customized media, which is then used when updating target machines.
      
      The EZ-UTILITIES support both the ITBU and 6157 family of tape devices


   **Investment Protection**

      AIX PS/2 Operating System Version 1.3 offers binary compatibility in applications from AIX PS/2
      Operating System Version 1.2.1 and AIX PS/2 Operating System Version 1.2. POSIX IEEE 1003.1-1988
      conformance may require applications from AIX PS/2 Operating System Version 1.1 to be recompiled or modified.

      The following AIX PS/2 Operating System Version 1.1.1 programs will execute on AIX PS/2
      Operating System Version 1.3:


          AIX PS/2 VS C Language Version 1.1.1
      
          AIX PS/2 VS FORTRAN Version 1.1.1
      
          AIX PS/2 VS Pascal Version 1.1.1
      
          AIX PS/2 Workstation Host Interface Program Version 1.1.1
      
          AIX PS/2 Extended C Language Version 1.2.1 

      NOTE: Transparent Computing Facility (TCF) is NOT supported in AIX PS/2 Operating System Version 1.3. 


   **Trademarks**
      
      (R), (TM), \* Trademark or registered trademark of International Business Machines Corporation.
      
      \*\* Company, product, or service name may be a trademark or service mark of others.
      
      Windows is a trademark of Microsoft Corporation.
      
      UNIX is a registered trademark in the United States and other countries licensed exclusively through X/Open Company Limited.


Available Compilers
^^^^^^^^^^^^^^^^^^^

With the available compilers, not the latest releases of course - released about 1993:

   .. raw:: html
   
      <div class="shortcuttab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +-----------------------------------------------------------+--------+-------------+
   | compiler                                                  | status | description |
   +===========================================================+========+=============+
   | AIX PS/2 VS C Language Version 1.1.1                      |        |             |
   +-----------------------------------------------------------+--------+-------------+
   | AIX PS/2 VS FORTRAN Version 1.1.1                         |        |             |
   +-----------------------------------------------------------+--------+-------------+
   | AIX PS/2 VS Pascal Version 1.1.1                          |        |             |
   +-----------------------------------------------------------+--------+-------------+
   | AIX PS/2 Workstation Host Interface Program Version 1.1.1 |        |             |
   +-----------------------------------------------------------+--------+-------------+
   | AIX PS/2 Extended C Language Version 1.2.1                |        |             |
   +-----------------------------------------------------------+--------+-------------+

   .. raw:: html
   
      </div>
      </div>
      </div>


Available Python Releases
^^^^^^^^^^^^^^^^^^^^^^^^^
Let's see... - probably coming soon |smilecool|.

HowTo Get It
^^^^^^^^^^^^
Use a search engine |smilecool|.

HowTo Install It
^^^^^^^^^^^^^^^^
There are some pitfalls for the setup within a *VirtualBox*, the workarounds will be posted soon.

The basic installation and operations works fine, while the network stack requires some outdated NICs,
which are currently not available for *VirtualBox*.
Other platforms may provide a supported type, in particular with a supported original card.

The compiler collection is not latest, and missing *Python* by default - it is the year of 1993 |smilecool|.


Module
------
.. automodule:: platformids.custom.aix

Data
----

RTE_AIX
^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_AIX        = RTE_UNIX   + custom_dist.add_enum()


rte2num
^^^^^^^
Mapping of the rte string and numeric representation to the numeric value.

num2rte
^^^^^^^
Mapping of the rte numeric representation to the string value.

num2pretty
^^^^^^^^^^
Mapping of the rte numeric representation to the pretty string value.

Source
------


.. literalincludewrap:: _static/custom/aix.py
   :language: python
   :linenos:

Download
--------
`aix.py <../_static/custom/aix.py>`_


.. |smilecool| image:: ../_static/smiling-face-with-sunglasses-32x32.png
   :width: 16
   :alt: :-)
