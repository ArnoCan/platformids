.. _CUSTOM_MODULE_MINIX2:

platformids.custom.minix2
=========================

Module Minix \[:ref:`doc <enumMINIX>`].

Module
------
.. automodule:: platformids.custom.minix2

Data
----

RTE_MINIX2
^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_MINIX2        = RTE_MINIX   + custom_dist.add_enum()


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


.. literalincludewrap:: _static/custom/minix2.py
   :language: python
   :linenos:

Download
--------
`custom minix2.py <../_static/custom/minix2.py>`_

