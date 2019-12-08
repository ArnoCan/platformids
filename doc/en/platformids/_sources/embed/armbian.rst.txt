
.. _EMBED_MODULE_ARMBIAN:

platformids.embed.armbian
=========================

Module Armbian \[:ref:`doc <enumARMBIAN>`].

Module
------
.. automodule:: platformids.embed.armbian

Data
----

RTE_ARMBIAN
^^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_ARMBIAN        = RTE_LINUX   + :ref:`custom_dist.add_enum()`


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
           RTE_ARMBIAN: my_distrel2tuple,  #: the callback to be registered
       }
   )

Functions
---------

my_distrel2tuple
^^^^^^^^^^^^^^^^

.. autofunction:: my_distrel2tuple
 

Source
------


.. literalincludewrap:: _static/embed/armbian.py
   :language: python
   :linenos:

Download
--------
`armbian.py <../_static/embed/armbian.py>`_

