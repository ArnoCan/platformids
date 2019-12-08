
.. _PYTHONIMPLEMENTATION:

Python Implementations
======================
Overview
--------
The various Python implementations require some more or less specific handling for the
detection of the release.


.. raw:: html

   <div class="shortcuttab">
   <div class="nonbreakheadtab">
   <div class="autocoltab">

+----------------+---------------------------------------------------------------------------------------------------------------+
| implementation | remarks                                                                                                       |
+================+===============================================================================================================+
| *CPython*      | standard procedures based on standard modules, specials for some distributions, registry based on *WindowsNT* |
+----------------+---------------------------------------------------------------------------------------------------------------+
| *IPython*      | basically the same as *CPython*, requires special detection for release                                       |
+----------------+---------------------------------------------------------------------------------------------------------------+
| *IronPython*   | based on registry, available on *WindowsNT* only                                                              |
+----------------+---------------------------------------------------------------------------------------------------------------+
| *Jython*       | implements for *WindowsNT* *Java* modules for the registry access, *POSIX* platforms same as *CPython*        |
+----------------+---------------------------------------------------------------------------------------------------------------+
| *PyPy*         | same procedures as *CPython*                                                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------+

.. raw:: html

   </div>
   </div>
   </div>

See also [pythonids]_.

.. _PYTHONJYTHONIMPLEMENTATION:

Jython
------
The *platformids* supports in general the *Jython* implementation,
which is on *POSIX* based platforms commonly based on the standard libraries and the common exceptions
of detection of the underlying OS platforms.
These are handled by the native standard *Python* interfaces as provided by the *Jython* implementation.

The standard information provided by *System* covers not the full required scope. 
Therefore  some *Java* modules are provided for the registry access.

The *Jython* implementation on *Windows NT* (*Jython-2.7.0*) does not support registry access, which is
cruicial for the fast and reliable acquisition of the full scope of the platform information.

For details see :ref:`Data Acquisition on Windows-NT <WINNTDATAACQUISITION>`, and 
:ref:`Jython on Windows-NT <JYTHONONWINNTREG>`.


.. _SETUPTOOLSIMPLEMENTATION:

setuptools / distutils
----------------------

This also requires the extension of the *setup.py* by the additional command *build_java* for the compilation and 
distribution of the included *java* modules.
