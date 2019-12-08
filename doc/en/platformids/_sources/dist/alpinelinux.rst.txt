.. _DIST_MODULE_ALPINE:

platformids.dist.alpinelinux
============================

Module Alpine Linux \[:ref:`doc <enumALPINELIN>`].

Data
----

Files
^^^^^
* /etc/alpine-release

   .. parsed-literal::
   
      3.8.2

* /etc/os-release

   .. parsed-literal::
   
      NAME="Alpine Linux"
      ID=alpine
      VERSION_ID=3.8.2
      PRETTY_NAME="Alpine Linux v3.8"
      HOME_URL="http://alpinelinux.org"
      BUG_REPORT_URL="http://bugs.alpinelinux.org"

Python Libraries
^^^^^^^^^^^^^^^^
* platform

   .. parsed-literal::
   
      -> platform.dist()
      <-
      
      -> platform.uname()
      <-

* os

   .. parsed-literal::
   
      -> os.uname
      <- "posix"

Source
------


.. literalincludewrap:: _static/dist/alpinelinux.py
   :language: python
   :linenos:

Download
--------
`alpinelinux.py <../_static/dist/alpinelinux.py>`_

