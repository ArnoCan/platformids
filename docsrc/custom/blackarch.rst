.. _CUSTOM_MODULE_BLACKARCH:

pythonids.dist.blackarch
========================
Module BlackArch Linux \[:ref:`doc <enumBLACKARCH>`].

Description
-----------
The securtity distribution based on :ref:`ArchLinux <enumARCHLIN>`.

Module
------
.. automodule:: platformids.custom.blackarch

Data
----

RTE_BLACKARCH
^^^^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_BLACKARCH        = RTE_LINUX   + custom_dist.add_enum()


rte2num
^^^^^^^
Mapping of the rte string and numeric representation to the numeric value.

num2rte
^^^^^^^
Mapping of the rte numeric representation to the string value.

num2pretty
^^^^^^^^^^
Mapping of the rte numeric representation to the pretty string value.


custom_rte_distrel2tuple
^^^^^^^^^^^^^^^^^^^^^^^^
Registered callbacks for special handling of custom layout.

.. parsed-literal::

   custom_rte_distrel2tuple.update(
       {
           RTE_MINIX2: my_distrel2tuple,  #: the callback to be registered
       }
   )

Functions
---------

my_distrel2tuple
^^^^^^^^^^^^^^^^

.. autofunction:: my_distrel2tuple
 

Source
------


.. literalincludewrap:: _static/custom/blackarch.py
   :language: python
   :linenos:

Download
--------
`blackarch.py <../_static/custom/blackarch.py>`_

