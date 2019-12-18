
.. _RTPLATFORMIDS_CLI:

rtplatformids - Command line interface
--------------------------------------

The *rtplatformids* executable provides the command line interface to the
library modules.

* User options:

   The default output is the display of the complete set of parameters.
   The following options constraint the default output when at least one
   is selected.
   The order of the output for multiple selections is defined static by the alphabetic order. 
   The option :ref:`--terse <terse>` suppresses in addition the display of the attribute name.
   
   .. parsed-literal::
   
      :ref:`--category <category>`        :ref:`--ostype <ostype>`               :ref:`--dist <dist>`
      :ref:`--distrel <distrel>`         :ref:`--distrel-name <distrel-name>`         :ref:`--distrel-key <distrel-key>`
      :ref:`--dist-vers <dist-vers>`       :ref:`--ostype-id <ostype-id>`             :ref:`--ostype-version <ostype-version>`

   Support options.

   .. parsed-literal::

      :ref:`--out-format <outformat>`      :ref:`--verbose <verbose>`              :ref:`--version <versionl>`

* Developer options:

   .. parsed-literal::
   
      :ref:`--distrel-hexversion <distrel-hexversion>`    :ref:`--debug <debug>`          :ref:`--debug-options <debug-options>`
      :ref:`--enumerate <enumerate>`             :ref:`--environ <environ>`        :ref:`--fromfile <fromfile>`
      :ref:`--load <load>`                  :ref:`--platform <platform>`       :ref:`--terse <terse>`
      :ref:`--Version <Version>`

.. _platformidsCLISYNOPSIS:

SYNOPSIS
^^^^^^^^
.. parsed-literal::

   rtplatformids    :ref:`[OPTIONS] <multicoCLIOPTIONS>`

.. _platformidsCLIOPTIONS:

OPTIONS
^^^^^^^

.. index::
   pair: options; --category
   pair: rtplatformids; --category

.. _category:

-\-category
"""""""""""
Display category.

.. index::
   pair: options; --debug
   pair: rtplatformids; --debug

.. _debug:

-\-debug
""""""""
Activates debug output including stacktrace,
multiple raise the debug level. ::

   -d --debug[=#level]

     initial := 0,  sys.stacktrace=0
     default := +1, sys.stacktrace += 3

     When level the debug > 2: sys.stacktrace=1000


.. index::
   pair: options; --debug-options
   pair: rtplatformids; --debug-options

.. _debug-options:

-\-debug-options
""""""""""""""""
Displays the internal commandline options data
with optional output format. ::

   --debug-options[=('json' | 'repr' | 'str')[ cont]]

     default := 'json'

For export streams refer to :ref:`--out-format <outformat>`.

.. index::
   pair: options; --dist
   pair: rtplatformids; --dist

.. _dist:

-\-dist
"""""""
Display distribution.

.. index::
   pair: options; --distrel
   pair: rtplatformids; --distrel

.. _distrel:

-\-distrel
""""""""""
Display release of the distribution.

.. index::
   pair: options; --distrel-hexversion
   pair: rtplatformids; --distrel-hexversion

.. _distrel-hexversion:

-\-distrel-hexversion
"""""""""""""""""""""
Display the release of the distribution including the canonical version as hex-bit-array.

.. index::
   pair: options; --distrel-key
   pair: rtplatformids; --distrel-key

.. _distrel-key:

-\-distrel-key
""""""""""""""
Display name of the selection key of the distribution release.
Used for internal mapping-tables to be used as debugging support.

.. index::
   pair: options; --distrel-name
   pair: rtplatformids; --distrel-name

.. _distrel-name:

-\-distrel-name
"""""""""""""""
Display name of the distribution release.

.. index::
   pair: options; --dist-vers
   pair: rtplatformids; --dist-vers

.. _dist-vers:

-\-dist-vers
""""""""""""
Display the version array the distribution release.

.. index::
   pair: options; --enumerate
   pair: rtplatformids; --enumerate

.. _enumerate:

-\-enumerate
""""""""""""
Enumerates the known platform entries.

.. parsed-literal::
    
    --enumerate [<type>] [num=<num>] [scope=<scope>]

      filter:
         type := (
            all
            | category
            | ostype
            | dist
            | distrel
         )

      number format:
         num := (
            int       # integer
            | hex     # hex
            | bit     # bitarray
            | sym     # symbolic enum names
         )

      filter:
         scope := (
            all       # all
            | numkey  # numeric keys
            | strkey  # string keys
         )

      num padding:
         pad := (
            on | 1 | true       # show all
            | off | 0 | false   # suppress padding entries with "k == v" 
         )

      reverse mapping:
         reverse := (
            on | 1 | true       # num2rte
            | off | 0 | false   # rte2num 
         )

.. index::
   pair: options; --environ
   pair: rtplatformids; --environ

.. _environ:

-\-environ
""""""""""
Print environ.

.. index::
   pair: options; --fromfile
   pair: rtplatformids; --fromfile

.. _fromfile:

-\-fromfile
"""""""""""
Enables the read of options from an options file.
For details refer to *argparse.ArgumentParse*
constructor option  *fromfile_prefix_chars*.

.. index::
   pair: options; --help
   pair: rtplatformids; --help

.. _help:

-\-help
"""""""
This help. ::

    --help
    -h

.. index::
   pair: options; --load
   pair: rtplatformids; --load

.. _load:

-\-load
"""""""
Loads additional modules: ::

   --load <filepathname>

     filepathname:  The file system path name of the source module to be loaded.
                    The file path must be fully qualified including extension,
                    either absolute, or relative.

The interface of current version supports the load bitmask mapping onto
string names.
The interface is simply the loadtime update of one of the following 
dictionaries *platformids.ProtectedDict*.
The maps are:

* *platformids.num2rte*
* *platformids.rte2num*
* *platformids.num2enumstr*

For examples and templates refer to *platformids/map_enum_labels* and
the directory *platformids/dist*.

The basic principle is as for example in case of Solaris:

.. code-block:: python
   :linenos:

   from platformids import RTE_SOLARIS, rte2num, num2rte

   RTE_SOLARIS10 = RTE_SOLARIS  + 0x00000100  #: Solaris-10
   RTE_SOLARIS11 = RTE_SOLARIS  + 0x00000200  #: Solaris-11
    
   rte2num.update(
       {
           'SunOS5': RTE_SOLARIS,
           'sunos5': RTE_SOLARIS,
           'sunos5.10': RTE_SOLARIS10,
           'sunos5.11': RTE_SOLARIS11,
           'solaris10': RTE_SOLARIS10,
           'solaris11': RTE_SOLARIS11,
           RTE_SOLARIS10: RTE_SOLARIS10,
           RTE_SOLARIS11: RTE_SOLARIS11,
       }
   )

   num2rte.update(
       {
           RTE_SOLARIS: 'solaris',
           RTE_SOLARIS10: 'solaris10',
           RTE_SOLARIS11: 'solaris11',
       }
   )


The optional mapping of symbolic enumeration labels for bitmasks 
e.g. in case of *platformids.dist.solaris_enum_labels* is:

.. code-block:: python
   :linenos:

   from __future__ import absolute_import

   from platformids import *  # @UnusedWildImport
   from platformids.dist import *  # @UnusedWildImport

   from platformids.dist.solaris import *  # @UnusedWildImport

   num2enumstr.update(
       {
           RTE_SOLARIS10: "RTE_SOLARIS10",
           RTE_SOLARIS11: "RTE_SOLARIS11",
       }
   )
   
   
.. index::
   pair: options; --ostype-id
   pair: rtplatformids; --ostype-id

.. _ostype-id:

-\-ostype-id
""""""""""""
Display the ID of the OS release.

.. index::
   pair: options; --ostype-version
   pair: rtplatformids; --ostype-version

.. _ostype-version:

-\-ostype-version
"""""""""""""""""
Display the version array the OS release.

.. index::
   pair: options; --ostype
   pair: rtplatformids; --ostype

.. _ostype:

-\-ostype
"""""""""
Display ostype.

.. index::
   pair: options; --out-format
   pair: rtplatformids; --out-format

.. _outformat:

-\-out-format
"""""""""""""
Defines the processed output format. ::

   --out-format=<format>
     
     format := (
        'json' 
        | 'raw' 
        | 'repr' | 'str' 
        | 'basharray' | 'bashvars'
     )

Supports normal data display, not the '--platform' and '--enumerate' options. 

.. index::
   pair: options; --platform
   pair: rtplatformids; --platform

.. _platform:

-\-platform
"""""""""""
Display selected parameters from standard libraries:

* *os*
* *sys*
* *platform*


.. index::
   pair: options; --quiet
   pair: rtplatformids; --quiet

.. _quiet:

-\-quiet
""""""""
Suppress output.

.. index::
   pair: options; --Version
   pair: rtplatformids; --Version

.. _Version:

-\-Version
""""""""""
Current version - detailed. ::

    --Version
    -Version

.. index::
   pair: options; --verbose
   pair: rtplatformids; --verbose

.. _verbose:

-\-verbose
""""""""""
Verbose, some relevant states for basic analysis.
When '--selftest' is set, repetition raises the display 
level. ::

    --verbose
    -v

.. index::
   pair: options; --version
   pair: rtplatformids; --version

.. _versionl:

-\-version
""""""""""
Current version - terse. ::

    --version
    -version

.. index::
   pair: options; --terse
   pair: options; -X
   pair: rtplatformids; --terse
   pair: rtplatformids; -X

.. _terse:

-\-terse
""""""""
Print short - terse.

DESCRIPTION
^^^^^^^^^^^

The call interface 'rtplatformids' provides the commandline interface for
the platform scanner.

.. _platformidsEXAMPLES:
 
EXAMPLES
^^^^^^^^

.. _examples:

Some simple call examples are:

.. parsed-literal::

   platformids  :ref:`--help <help>` 
   
   rtplatformids 
   rtplatformids  :ref:`--platform <platform>` 
   rtplatformids  :ref:`--out-format json <outformat>`

Some more elaborate call examples with custom load:

.. parsed-literal::

   rtplatformids.py :ref:`--enumerate  all  pad=off reverse=0 num=sym <enumerate>` \\
      :ref:`--load platformids/dist/fedora_enum_labels.py <load>` \\
      :ref:`--load platformids/dist/windows_enum_labels.py <load>`

SEE ALSO
^^^^^^^^
[machineids]_, [platformids]_, [pythonids]_, [resourceids]_, [extensionids]_

COPYRIGHT
^^^^^^^^^
Copyright (C)2008-2018 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
