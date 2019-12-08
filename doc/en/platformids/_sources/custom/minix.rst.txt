.. _CUSTOM_MODULE_MINIX:

platformids.custom.minix
========================

Module Minix \[:ref:`doc <enumMINIX>`].

Module
------
.. automodule:: platformids.custom.minix

Data
----

RTE_MINIX
^^^^^^^^^

Registration of the *ostype* value:

.. parsed-literal::

   RTE_MINIX         = RTE_POSIX   + custom_ostype.add_enum()

RTE_MINIX3
^^^^^^^^^^
Registration of the *dist* value:

.. parsed-literal::

   RTE_MINIX3        = RTE_MINIX   + custom_dist.add_enum()


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
           RTE_MINIX3: my_distrel2tuple,  #: the callback to be registered
       }
   )


custom_ostype
^^^^^^^^^^^^^
Dynamic registry for custom *ostype*.

.. parsed-literal::

   custom_ostype.update(
       {
           RTE_MINIX: RTE_MINIX,
       }
   )

custom_dist
^^^^^^^^^^^
Dynamic registry for custom *dist*.

.. parsed-literal::

   custom_dist.update(
       {
           RTE_MINIX3: RTE_MINIX3,
       }
   )

Functions
---------

my_distrel2tuple
^^^^^^^^^^^^^^^^

.. autofunction:: my_distrel2tuple
 
Source
------


.. literalincludewrap:: _static/custom/minix.py
   :language: python
   :linenos:

Download
--------
`custom minix.py <../_static/custom/minix.py>`_

