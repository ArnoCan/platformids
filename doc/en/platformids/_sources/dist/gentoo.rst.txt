.. _DIST_MODULE_GENTOO:

platformids.dist.gentoo
=======================
Module Gentoo Linux \[:ref:`doc <enumGENTOO>`].

Description
-----------

.. _GENTOOLINUX_VERSIONID:

Rolling Version Identifier
^^^^^^^^^^^^^^^^^^^^^^^^^^
The current version of *GentooLinux* does not seem to support the current state of the installation,
even not the build release of the install medium by the runtime system.
Thus the *platformids* provide as the basic information of the installation state for
now the last modification time of the package database *mtimedb* of the *emerge* command:


   .. parsed-literal:: 

      /var/cache/edb/mtimedb

With the values by *os.stat*:

   .. parsed-literal:: 

      release-version := (<time.struct_time.tm_year>, <time.struct_time.tm_month>, <time.struct_time.tm_mday>)

or as a formatted string in accordance to the ISO naming convention:

   .. parsed-literal:: 

      release-version-str := "%d%02d%02d" (<time.struct_time.tm_year>, <time.struct_time.tm_month>, <time.struct_time.tm_mday>)

This information is due to several scenarios not reliable, but to say 

1. better than none
2. probably not so bad, even though not each mod results from a full upgrade       

.. warning::

   Do not mixup this release state information with the release of the actual installation media.
   And once again, the provided release information by *platformids* is basically reliable after 
   an upgrade only, e.g.:
   
      emerge --update --deep --with-bdeps=y @world

Source
------


.. literalincludewrap:: _static/dist/gentoo.py
   :language: python
   :linenos:

Download
--------
`gentoo.py <../_static/dist/gentoo.py>`_

