.. _CUSTOM_MODULE_PARROT:

platformids.custom.parrot
=========================

Module ParrotLinux \[:ref:`doc <enumPARROTOS>`].

Module
------
.. automodule:: platformids.custom.parrot

Data
----

RTE_PARROT
^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_PARROT        = RTE_LINUX   + custom_dist.add_enum()

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
           RTE_PARROT: my_distrel2tuple,  #: the callback to be registered
       }
   )

Functions
---------

my_distrel2tuple
^^^^^^^^^^^^^^^^

.. autofunction:: my_distrel2tuple
 

Source
------


.. literalincludewrap:: _static/custom/parrot.py
   :language: python
   :linenos:

Download
--------
`custom parrot.py <../_static/custom/parrot.py>`_

