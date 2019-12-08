.. _CUSTOM_MODULE_REACTOS:

.. _docReactOS:

platformids.custom.reactos
==========================
Module ReactOS \[:ref:`doc <enumReactOS>`].

Module
------
.. automodule:: platformids.custom.reactos

Data
----

RTE_REACTOS
^^^^^^^^^^^

Registration of the *ostype* value:

.. parsed-literal::

   RTE_REACTOS        = RTE_WINDOWS   + custom_ostype.add_enum()

RTE_REACTOS5_2
^^^^^^^^^^^^^^

Registration of the *dist* value:

.. parsed-literal::

   RTE_REACTOS5_2        = RTE_REACTOS   + custom_dist.add_enum()

rte2num
^^^^^^^
Mapping of the rte string and numeric representation to the numeric value.

num2rte
^^^^^^^
Mapping of the rte numeric representation to the string value.

num2pretty
^^^^^^^^^^
Mapping of the rte numeric representation to the pretty string value.


Description
-----------
The *ReactOS* is basically a promissing OS, in particular it may serve as a pretty good replacement
for frozen legacy apps within virtual environments.
But the project still requires some work to do.

Source
------

.. literalincludewrap:: _static/custom/reactos.py
   :language: python
   :linenos:


Download
--------
`reactos.py <../_static/custom/reactos.py>`_

