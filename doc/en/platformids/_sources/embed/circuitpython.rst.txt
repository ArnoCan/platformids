.. _EMBED_MODULE_CIRCUITPY:

platformids.embed.circuitpython
===============================


.. warning::

   Experimental - Currently under development, do not yet use it - coming soon. 


Module CircuitPython \[:ref:`doc <embeddedCIRCUITPY>`].
Requires the *ostype* definition of  :ref:`MicroPython <embeddedMICROPY>`.

Module
------
.. automodule:: platformids.embed.circuitpython

Data
----

RTE_CIRCUIT
^^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_CIRCUIT        = RTE_MICROPYTHON   + :ref:`custom_dist.add_enum() <add_enum>`


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


.. literalincludewrap:: _static/embed/circuitpython.py
   :language: python
   :linenos:

Download
--------
`circuitpython.py <../_static/embed/circuitpython.py>`_

