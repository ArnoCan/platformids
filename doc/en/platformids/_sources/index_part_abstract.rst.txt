
********
Abstract
********

Modern landscapes of information infrastructures are commonly designed 
and organized as stacks of runtime service environments.
The technical architecture of the service stacks consists of a wide range of
heterogenous landscapes of components frequently requiring adaptation and mediation.

.. figure:: _static/systems-ids.png
   :figwidth: 400
   :align: center
   :target: _static/systems-ids.png
   
   Figure: Service Layers |figurelayers_zoom| :ref:`more... <REFERENCE_ARCHITECTURE>`

.. |figurelayers_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/systems-ids.png
   :width: 16

This requires commonly the integration by wrappers and add-on coding  for various operating systems and their
specific distribution releases.
The *platformids* provides the automated technical detection and enumeration
of a comprehensive list of standard OS and distribution, e.g. 'Linux', 'BSD', 'Unix', 'OS-X', and 'Windows'. 
For first details refer to the :ref:`Blueprint <BLUEPRINT>`.

The provided components comprise:

* **Platform as 32bit Integer Bit-Mask**
   The core module :ref:`platformids <PLATFORMIDSINIT>` provides the functions
   and constant(var) definitions for the encoding and decoding of the complete
   distribution information into bitmasks. 
   [:ref:`doc <BITMASKSOSDIST>`]

* **Platform as Python Class**
   The :ref:`platformids.platforms <PLATFORMSMODULE>` module provides the class representation.
   
* **Standard Platform Plugins**
   The submodules provides OS and distribution specific data definitions and adapter interfaces. 

      * *platformids.dist* [:ref:`standard <STANDARDOSDIST>`] / [:ref:`net+security <SECURITYANDNETWORK>`] 
      * *platformids.embed* [:ref:`IoT <EMDEDDEDANDIOT>`]
      
* **Custom Platform Plugins**
   The custom submodules provide less often used OS and distribution data as custom modules,
   serving also as pattern and templates for individual extensions. 
 
      * *platformids.custom* [:ref:`custom <CUSTOM_NUMBERING_SCHEMES>`]

For tested standard OS and distributions see help on `installation <install.html>`_ / :ref:`Tested OS and Python Implementations <TESTED_OS_PYTHON>`.
For other stack layers refer to [machineids]_, [pythonids]_, [resourceids]_, and [extensionids]_.

Concepts and enumeration values are migrated from the 

* *UnifiedSessionsManager* (C) 2008 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez [UnifiedSessionsManager]_  
