Bit Masks for Numeric Vectors
=============================
In programming languages the hierarchical information is typically represented as
an ordered vector with hierrachical semantics of items defined by their position.
This is in general a very common representation for naturally hierarchical information
as for paths for example in filesystems, but also for example for version numbers
combined by multiple major and minor subnumbers as the Python version itself.
 
In case of the combined version number the common hierarchical numeric values
constitute a vector of a logical number assembled with a series of independent
numbers based on a set of ordered  heterogeneous virtual radix values.
The following version

.. math:: 
   :label: hierarchical_integer_vector

   \begin{split}
   V(A, B, C) = (A, B, C)
   \end{split}

is commonly expressed also by the string

.. math:: 
   :label: hierarchical_integer_vector

   \begin{split}
   V(A, B, C) := 'A.B.C'
   \end{split}

The resulting vector requires in programming languages a number of comparison operations
for logical processing, and the combination into one overall result with eventual additional
processing for semantical slices.
This increases linear with the incremental number of required processing, and could sumup
considerably in larger loops.
It could result in an overall exponential performance degradation when applied in
non-linear algorithms.

The *platformids* package provides a tiny core library with integer enumerations to be
commonly used in order to enhance the performance.
Thus the provided library is designed for minimized overall performance degradation
for non-matching cases when generally applied.
The overall performance enhancement should be present after the 2nd. or 3rd. processing
of the integer replacement value, while the static one-time calculation of the
enum value is normally negligble impact due to the single-shot
static calculation.

Scalar Representation of Hierarchical Integer Vectors
-----------------------------------------------------
The required operations on hierarchical integer vectors is in a number of cases
the static comparison of ranges of selected single and combined items.
The following simple comparison of two static integer vectors example:

.. code-block:: python
   :linenos:

   V0 = (A0, B0, C0)
   V1 = (A1, B1, C1)

   if V0 < V1:
      doCode0()
   else:
      doCode1()

results actually in the logical hierarchical item comparison:

.. code-block:: python
   :linenos:

   V0 = (A, B, C)
   V1 = (D, E, F)

   if (
           V0[0] < V1[0] 
        or (
              V0[0] == V1[0] 
              and (
                 V0[1] < V1[1]
                 or 
                   (V0[1] == V1[1] and V0[2] < V1[2])
              )
           )
       ):
      doCode0()
   else:
      doCode1()

Because these could be fragmented over code parts of local scopes and across multiple functions
and threads, the optimization by a compiler could be tricky or prove to be impossible.

The reference values to be processed by comparison including the variable value are frequently
static for the lifetime of the processing systems process or the scope of the relevant code, 
while the results of these comparison operations are applied as a selection criteria
for distinguished code segments.
This is in particular the case for version vectors in order to control adaption of variants
of code segments for compatibility reasons.
The most obvious version dependency is for Python the *CPython* interpreter of the
version *Python3* itself.
In particular in case of the *Python3.Y(Z)* releases a frequently required process due
to the ongoing incremental agile development.
It is even more common when Python2 releases are also to be supported by a common
shared code base.
Thus the resulting gain of performance could become quickly more than considerable only. 

The basic idea in the enhancement of processing these types of common hierarchical integer
vectors is to transform these once into a single integer scalar value and process the
required comparison operations from than on as a single integer operation.
This proves in particular for short vectors as a fast replacement, while longer
vectors would still benefit due to the reduction of than large numbers of permutations. 
The following example demonstrates the difference:

.. code-block:: python
   :linenos:

   V0 = getPYVxyz(A, B, C) # (A, B, C) => 0b(aaaabbbbbbccccccc)
   V1 = getPYVxyz(D, E, F) # (D, E, F) => 0b(ddddeeeeeefffffff)

   # => type(V0) == type(V1) == int

   if V0 < V1:
      doCode0()
   else:
      doCode1()

which becomes e.g. in case of the following loop a dominant enhancement:

.. code-block:: python
   :linenos:

   V0 = getPYVxyz(A, B, C) # (A, B, C) => 0b(aaaabbbbbbccccccc)
   V1 = getPYVxyz(D, E, F) # (D, E, F) => 0b(ddddeeeeeefffffff)

   # => type(V0) == type(V1) == int

   for x in range(1000000000)
      if V0 < V1:
         doCode0(x)
      else:
         doCode1(x)

Similar for 

.. code-block:: python
   :linenos:

   V0 = getPYVxyz(A, B, C) # (A, B, C) => 0b(aaaabbbbbbccccccc)
   V1 = getPYVxyz(D, E, F) # (D, E, F) => 0b(ddddeeeeeefffffff)
   V2 = getPYVxyz(D, E, G) # (D, E, G) => 0b(ddddeeeeeeggggggg)

   #
   # from here on V0, V1, and V2 are constant integer values
   #


   def mySubversionHandler(x):
      if V0 == V1:
         doCode1(x)
      elif V0 < V2:
         doCode1(x)
      else:
         doCode1(x)

   # => type(V0) == type(V1) == int

   for x in range(1000000000)
      if V0 < V1:
         doCode0(x)
      else:
         mySubversionHandler(x)


In this vector representation each item is virtually a logical superscript of the dynamic
radix represented by the righthand sums of the vector items.
Each resulting radix value is based on it's location in the vector and the sum of the bit-mask
widths of the right-hand side items and in case of an eventual overflow also on the item itself.

.. math::
   :label: scalar_of_hoerarchical_integer_vector

   |V(A, B, C)| = |(A, B, C)| = X_{2}(A, B, C){^{A}} + X_{1}(B, C){^{B}} + X_{0}(C){^{C}} 

Or expressed as a general equotation for the defined adaptive polynominal of fixed size
bit masks:
 
.. math::
   :label: datextime_vector_absolute

   |V(x_{i}){_{\substack{0<=i<n}}}| =  \sum_{\substack{0<=i<=n\\\text{$i$ item}}}{X_{i}(x_{j})}{^{x_{i}}|{_{\substack{0<=j<=i}}} }:
   n = items(V);  x \in\mathbb{N}{_0}; i,j \in\mathbb{N}{_0}.

where the resulting numeric value is defined by the sum of each value of the vector items
once these are moved to their coreesponding bit position via a shift operation.
E.g.:

.. code-block:: python
   :linenos:

   V = (3, 2, 1)  # 0b aaaa bbbbb cccccc

    => (3, 2, 1) => 0b 0011 00010 000001 == 6273


This assembly of resulting representation suits particularly for mathematical 
single-shot operations of literal match and threshold passing calculations.
The maximum gain of performance is given in particular for sizes of overall bit masks
fitting completely into CPU registers.
Thus modern CPUs on commercial machines of up to 64bit get the most benefit.
The advance in case of GPU based processing with wider vectors could be even better
when thoroughly desined.
Overall values with larger resulting bit-widths on commercial CPUs will still benefit largely,
when these consist of a larger number of short-fragmented items with small or moderate individual
number ranges.
Here libraries such as *decimal* provide additional enhancements. 

The corresponding fixed segment of each vector item is defined as it's
shifted bit mask at the final segment-position.
The concatenated bit-representations of the integer value of each item
found the resulting integer value.
The gain of performance is at least proportional to the number of calls with
a little initial overhead for a few increments only.
The resulting gain may even benefit exponentially for short bit masks compared
to the raw processing of the items.

The already mentioned most typical application of these operations is depicted
in the following examples.
These also figure out an easy to go future migration path when the support
for the older versions is dropped as these pass their end-of-life milestone. 

.. code-block:: python
   :linenos:

   from platformids import V3K, getPYVxyz

   # bit-mask values               # 0bxxxxyyyyyzzzzzzz
   vref363  = getPYVxyz(3, 6, 3)     # 0b0011001100000011 == 13,059
   vref32   = getPYVxyz(3, 2)        # 0b0011000100000000 == 12,544
   vref27   = getPYVxyz(2, 7)        # 0b0010011100000000 ==  9,984
   vref2714 = getPYVxyz(2, 7, 14)    # 0b0010011100001110 ==  9,998
   vref26   = getPYVxyz(2, 6)        # 0b0010001100000000 ==  8,960
   vref245  = getPYVxyz(2, 4, 5)     # 0b0010001000000101 ==  8,709

   myStaticScalar = getPYVxyz(  #      0bxxxxyyyyyzzzzzzz
      *sys.version_info[:3]   # e.g. 0b0010010000000011 == 8,709 := (2, 4, 5) 
   )   
   
   def myTempPrePython3Handler():
      if myStaticScalar >= vref2714:
         # for 2.7.14+
         alternative1a()

      elif myStaticScalar & vref27:
         # for 2.7.0 - 2.7.13
         alternative1b()

      elif myStaticScalar < vref27:
         # for pre-2.7
         alternative2()


   for i in range(1000000):  # 1.000.000

      if not V3K:
         # for PythonX < Python3
         myTempPrePython3Handler()

      elif myStaticScalar > vref363:
         # for the introduced new feature of 3.6.4+
         #
         # the only remaining variant for the revision once
         # the support for the Python2 and Python 3.0.0 - 3.6.3
         # variants are canceld
         #
         target_variant()

      else:
         # for 3.0 <= x <= 3.6.2
         temporary_alternative_python3_migration()

This code could be later easily modified to *Python3* support only:

.. code-block:: python
   :linenos:

   # bit-mask values               # 0bxxxxyyyyyzzzzzzz
   vref363  = getPYVxyz(3, 6, 3)     # 0b0011001100000011 == 13,059
   vref32   = getPYVxyz(3, 2)        # 0b0011000100000000 == 12,544

   myStaticScalar = getPYVxyz(  #      0bxxxxyyyyyzzzzzzz
      *sys.version_info[:3]   # e.g. 0b0011010000000011 == 8,709 := (3, 4, 5) 
   )   
   
   for i in range(1000000):  # 1.000.000

      if myStaticScalar > vref363:
         # for 3.6.4+
         target_variant()

      else:
         # for 3.0 <= x <= 3.6.2
         temporary_alternative_python3_migration()

and later as easy migrated to the final target of stable *Python3* features only.

.. code-block:: python
   :linenos:

   for i in range(1000000):  # 1.000.000
      target_variant()

Remember that this code history does not require distributed or nested
version checks, just simply a cascading of code segments with
flat integer comparisons.
Thus the legacy parts could be canceled by simple deletion and could be as
easily peer-reviewed.

Bit Masks for Python Releases
-----------------------------
The bit-mask operations provide a simple means for the efficient bulk-processing of
static numerical threshold dependencies of vectors.
This is in particular applicable for short and static vectors as in particular
common release numbers.
The Python release itsel is here is a quite good example and actually the originator
for this package.
The release dependency of multiple features of the Python library features
and it's implementaiotn by *CPython*, with all deviations to other interpreters
such as *PyPy* *IronPython* and *Jytjon* with the additional dependency on the
runtime environment of the OS is a frequent challange when it comes to the development
of multi-platform applications and systems layer libraries.

.. code-block:: python
   :linenos:

   import sys

   sys.version_info[0]  # major version
   sys.version_info[1]  # minor version
   sys.version_info[2]  # micro version  or build-tag
   sys.version_info[3]  # textual label of release level, current:
                        # ('alpha' | 'beta' | 'candidate' | 'final') 
   sys.version_info[4]  # serial number, frequently '0'


The specific bit masks designed for Python releases are of fixed sizes,
representing the standard values with an appropriate spare range.
The overall size is designed to fit into a 16bit register.
The current supported value ranges are:

.. code-block:: python
   :linenos:

   import sys

   sys.version_info[0]  # major version - 3bits:  0-7
   sys.version_info[1]  # minor version - 5bits:  0-31
   sys.version_info[2]  # micro version - 8bits:  0-255

.. note::

   The implementation of the comparison operations could be based on static
   integer constants as reference values. This is suitable because of the
   static code dependencies.
   But future implementations may change the bit mask composition. Therefore
   it is recommended that either the constants should be implemented as
   shared constant values, or by the function interfaces only.


The features  may in addition vary by the specific platform, which results  
in several system dependent libraries with a few to significant differences.
The ongoing development of the version Python3 evolves with a continous
change of major and minor features including dependency on the micro versions.
The system platform is represented by the standard library *sys* as:

.. parsed-literal::

   sys.platform  # the label of current platform
                 # e.g. 'linux2', 'win32', 'darwin'

The *platformids* provides canonical numerical values on a higher granularity
for the supported system platforms.
This enables in addition for code system dependent variants controlled by
simple and fast integer comparison operations too.
For the implementation details refer to [`getPYVxyz() <package_init.html#getPYVxyz>`_].

The following code-example depicts an example for the combined application:

.. parsed-literal::

   import sys

   if sys.version_info[0] > 2:
      # Python3
      # prepare loop
   
   for i in range(100000):
      if sys.version_info[0] > 2:
         # Python3
   
         if sys.version_info[1] < 5:
            # Python - 3.0 < 3.5
            
            if sys.platform in ('linux2', 'darwin'):
               # do s. th.
            else:
               # do s.th. else.

         if sys.version_info[1] < 6 an sys.version_info[2] < 4:
            # Python - 3.5.0 < 3.5.3
            # do s. th.
   
         if sys.version_info[2] < 3:
            # Python - 3.5.4 < 3.6.3
            # do s. th.

      elif sys.version_info[1] > 6:
         # Python2.7

         if sys.platform == 'linux2':
            # do s. th.

         elif sys.platform == 'darwin':
            # do s. th.

         elif sys.platform == 'win32':
            # do s. th.

         else:
            # do s.th. else.

      else:
         # PythonX <= Python2.6  

         if sys.platform == 'win32':
            raise Exceptio("Not supported.")

         # do s.th....

The same based on static bit masks of version dependency:  

.. parsed-literal::

   from platformids import V3K, Vxyz, getPYVxyz

   if V3K:
      # Python3
      # prepare loop

   v27  = getPYVxyz(2, 7)
   v35  = getPYVxyz(3, 5)
   v353 = getPYVxyz(3, 5, 3)
   v363 = getPYVxyz(3, 6, 3)
    
   for i in range(100000):
      if V3K:
         # Python3
   
         if not Vxyz & v35:
            # Python - 3.0 < 3.5

            if RTE & RTE_POSIX:
               # do s. th.
            else:
               # do s.th. else.
   
         elif  Vxyz & v353:
            # Python - 3.5.0 < 3.5.3
            # do s. th.
   
         elif not Vxyz & v363:
            # Python - 3.5.4 < 3.6.3
            # do s. th.


      elif Vxyz & v27:
         # Python2.7

         if RTE & RTE_LINUX:
            # do s. th.

         elif RTE & RTE_DARWIN:
            # do s. th.

         elif RTE & RTE_WIN32:
            # do s. th.

         else:
            # do s.th. else.

      else:
         # PythonX <= Python2.6  

         if not RTE & RTE_WIN32:
            raise Exceptio("Not supported.")

         # do s.th....

