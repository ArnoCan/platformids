.. _EMBED_MODULE_MICROPY:

platformids.embed.micropython
=============================

.. warning::

   Experimental - Currently under development, do not yet use it - coming soon. 


Module MicroPython \[:ref:`doc <embeddedMICROPY>`].

Module
------
.. automodule:: platformids.embed.micropython

Data
----

RTE_MICROPYTHON
^^^^^^^^^^^^^^^

Registration of the *ostype* value:

.. parsed-literal::

   RTE_MICROPYTHON        = RTE_EMBEDDED   + :ref:`custom_ostype.add_enum() <add_enum>`

RTE_MICROPYTHON3
^^^^^^^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_MICROPYTHON3        = RTE_MICROPYTHON   + :ref:`custom_dist.add_enum() <add_enum>`


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


.. literalincludewrap:: _static/embed/micropython.py
   :language: python
   :linenos:

Download
--------
`micropython.py <../_static/embed/micropython.py>`_

