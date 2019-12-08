.. _CUSTOM_MODULE_PENTOO:

platformids.custom.pentoo
=========================

Module ParrotLinux \[:ref:`doc <enumPENTOO>`].

Module
------
.. automodule:: platformids.custom.pentoo

Data
----

RTE_PENTOO
^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_PENTOO        = RTE_LINUX   + custom_dist.add_enum()

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
           RTE_PENTOO: my_distrel2tuple,  #: the callback to be registered
       }
   )

Functions
---------

my_distrel2tuple
^^^^^^^^^^^^^^^^

.. autofunction:: my_distrel2tuple
 

Source
------


.. literalincludewrap:: _static/custom/pentoo.py
   :language: python
   :linenos:

Download
--------
`custom pentoo.py <../_static/custom/pentoo.py>`_

