
.. _DIST_WINDOWS_KERNEL32_DLL:

.. index::
   pair: nt; kernel32

dist.nt.windows_kernel32_dll
============================


Support module for the original Windows product enumerations \[:ref:`doc <enumWINNT>`]
including additional definitions.

Module
------

.. automodule:: platformids.dist.nt.windows_kernel32dll

Data Structures
---------------
This module defines product related data structures representing the namebinding and extensions. 

.. _WINNTPRODUCTIDENTIFIERS_KERN32:

Product Identifiers
^^^^^^^^^^^^^^^^^^^
The list of product identifiers provided by Microsoft.

* *prod_ext*
   A map of original const values defined by
   GetProductInfo function parameter values
   of *pwReturnedProductType*, see [GetProductInfo]_ and [pwReturnedProductType]_.
   This defines a proprietary category index of cumulated product types,
   see :ref:`Product Type Categories <WINNTPRODUCTTYPECATEGORIES>`.   

   .. parsed-literal::

      prod_ext = {
          0x00000006: 4,   # PRODUCT_BUSINESS
          0x00000010: 4,   # PRODUCT_BUSINESS_N
          0x00000012: 4,   # PRODUCT_CLUSTER_SERVER
          0x00000040: 4,   # PRODUCT_CLUSTER_SERVER_V
          0x00000065: 4,   # PRODUCT_CORE
          ... # see Source

   The *dict* values provide the cumulative index for :ref:`prod_type_categories <WINNTPRODUCTTYPECATEGORIES>`.  
   
.. _WINNTPRODUCTTYPECATEGORIES_kern32:

Product Type Categories
^^^^^^^^^^^^^^^^^^^^^^^

A proprietary category abstraction of cumulated product types by the *platformids*,
see :ref:`Product Identifiers <WINNTPRODUCTIDENTIFIERS>`.   

* *prod_type_categories*
   A cumulative abstraction of the defined product identifiers in order to 
   get more abstract and though less variants of products.
   The view is an attempt to a more technical categorization of the
   predefined enums.

   .. parsed-literal::
   
      #
      # see Source
      #
      prod_type_categories = (
          "H",     #  0:  Home
          "HS",    #  1:  Home Server
          "WS",    #  2:  Workstation
          "D",     #  3:  Data Center
          "E",     #  4:  Enterprise Server
          "STD",   #  5:  Standard Server 
          "BS",    #  6:  Basic Server: Small Business Server / Essential Server
          "VIRT",  #  7:  Virtualization
          "IOT",   #  8:  IoT
          "EDU",   #  9:  Education
          "EMB",   # 10:  Embedded 
      )

Product Enums
^^^^^^^^^^^^^
The provides values by the interface parameter *pwReturnedProductType* [pwReturnedProductType]_,
and their defining macros from the SDK are provided as Python constants with the same names.

.. parsed-literal::

   PRODUCT_BUSINESS = 0x00000006
   PRODUCT_BUSINESS_N = 0x00000010
   PRODUCT_CLUSTER_SERVER = 0x00000012
   ... # :ref:`see Source <DIST_WINDOWS_PRODUCTS_MODULE>`


Functions
---------

The following specific functions are available on the platforms
of "*category == Windows*" including "*Cygwin*".
The functions provide access to the native API of the platform library "*kernel32.dll*".
 
 
get_win32_OSVersionInfo
^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_win32_OSVersionInfo

   Gets the system information, by mapping the call onto *GetVersionExA*.
   See original *GetVersionExA* function description [GetVersionExA]_.
   
   Args:
       None

   Returns:
      The *ctypes.Structure* for current platform 

         .. parsed-literal::       
         
            class OSVersionInfo(ctypes.Structure):
               _fields_ = [
                   ("dwOSVersionInfoSize" , ctypes.c_int),        # DWORD
                   ("dwMajorVersion"      , ctypes.c_int),        # DWORD
                   ("dwMinorVersion"      , ctypes.c_int),        # DWORD
                   ("dwBuildNumber"       , ctypes.c_int),        # DWORD
                   ("dwPlatformId"        , ctypes.c_int),        # DWORD
                   ("szCSDVersion"        , ctypes.c_char * 128), # CHAR
               ]

      when on *RTE_NT*, returns *None* else.
    
   Raises:
       pass-through


get_win32_OSVersionInfoExa
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_win32_OSVersionInfoExa

   Gets the system information, by mapping the call onto *OSVersionInfoExa*.
   See original *OSVersionInfoExa* function description [OSVERSIONINFOEXA]_.
   
   Args:
       None

   Returns:
      The *ctypes.Structure* for current platform 

         .. parsed-literal::       
         
            class OSVersionInfoExa(ctypes.Structure):
               _fields_ = [
                   ("dwOSVersionInfoSize" , ctypes.c_int),        # DWORD
                   ("dwMajorVersion"      , ctypes.c_int),        # DWORD
                   ("dwMinorVersion"      , ctypes.c_int),        # DWORD
                   ("dwBuildNumber"       , ctypes.c_int),        # DWORD
                   ("dwPlatformId"        , ctypes.c_int),        # DWORD
                   ("szCSDVersion"        , ctypes.c_char * 128), # CHAR
            
                   ("wServicePackMajor"   , ctypes.c_int16),      # WORD
                   ("wServicePackMinor"   , ctypes.c_int16),      # WORD
                   ("wSuiteMask"          , ctypes.c_int16),      # WORD
                   ("wProductType"        , ctypes.c_int8),       # BYTE
                       # wProductType - one of:
                       # - VER_NT_DOMAIN_CONTROLLER
                       # - VER_NT_SERVER
                       # - VER_NT_WORKSTATION
                       #
                   ("wReserved"           , ctypes.c_int8),       # BYTE
            
                   ];

      when on *RTE_NT*, returns *None* else.
    
   Raises:
       pass-through


get_win32_OSProductInfo
^^^^^^^^^^^^^^^^^^^^^^^
   
.. autofunction:: get_win32_OSProductInfo

   Gets the system information, by mapping the call onto *OSProductInfo*.
   See original *OSProductInfo* function description [OSProductInfo]_.
   
   Args:
       None

   Returns:
      The *ctypes.Structure* for current platform 

         .. parsed-literal::       
         
            class OSProdInfo(ctypes.Structure):
               _fields_ = [
                   ("pdwReturnedProductType" , ctypes.c_int),        # PDWORD
                   ];

      when on *RTE_NT*, returns *None* else.
    
   Raises:
       pass-through


print_versinfo
^^^^^^^^^^^^^^

.. autofunction:: print_versinfo

   Prints the summerized version info. 

get_win32_IsWindowsXPSP1OrGreater
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_win32_IsWindowsXPSP1OrGreater

   Checks the system information, by mapping the call onto *IsWindowsXPSP1OrGreater*.
   See original *IsWindowsXPSP1OrGreater* function description [IsWindowsXPSP1OrGreater]_.
   
   Args:
       None

   Returns:
      The *ctypes.Structure* for current platform 

         .. parsed-literal::       
         
            class OSProdInfo(ctypes.Structure):
               _fields_ = [
                   ("pdwReturnedProductType" , ctypes.c_int),        # PDWORD
                   ];

      when on *RTE_NT*, returns *None* else.
    
   Raises:
       pass-through

   

Source
------


.. literalincludewrap:: _static/dist/nt/windows_kernel32dll.py
   :language: python
   :linenos:

Download
--------

`windows_kernel32dll.py <../../_static/dist/nt/windows_kernel32dll.py>`_


Resources
---------

* API: GetProductInfo - [GetProductInfo]_
* API: GetProductInfo parameter pwReturnedProductType - [pwReturnedProductType]_
* SDK: Macros for Conditional Declarations - [MACROSRELCOND]_

