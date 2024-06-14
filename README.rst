**Pyramis** is a Domain-Specific language that enables you to specify multi-tier systems of variying complexities with minimal ambiguity:

#. **Specify** the nodes of your multi-tier system.
#. **Analyze** each node specification to ensure validity under Pyramis rules.
#. **Translate** each node specification to a C++ implementation.

⚙️ Installation
============
At present, Pyramis can only be installed from source.

PyPI (Python)
-------------
.. code-block:: bash

   pip install git+https://github.com/armaanchowfin/pyramis.git

⚡️ Quick start
===========

   Please read our `Pyramis Keyword Reference <docs/pyramis-keywords.md>`_ for tips on writing Pyramis specifications

The recommended workflow is as follows:

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Task                                          | Action                                                                                              | Result                                                                      |
+===============================================+=====================================================================================================+=============================================================================+
| Create Pyramis Specification                  || In a parent directory,                                                                             || You now have a complete but not correct Pyramis multi-tier system          |   
|                                               ||  a. Fix names and interfaces of individual nodes, define ``interfaces.json``.                      ||                                                                            |   
|                                               ||  b. For each node, use Pyramis keywords to define a processing file ``node_name.dsl``.             ||                                                                            |
|                                               ||  c. UDFs, if any must be consolidated into a single ``udf.h``, ``udf.cpp`` pair.                   ||                                                                            |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Validate Pyramis Specification                || ``$ pyramis translate NF_A``                                                                       || The Pyramis Compiler will generate an error-report for any irregularities  |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Build C++ Implementation                      ||  ``$ pyramis build NF_A``                                                                          || A set of .cpp and .h files will be generated along with a base Makefile.   |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Run C++ NFs                                   ||  ``$ pyramis run NF_A num_threads``                                                                || Your NF specification is now a running NF instance                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

💡 How Pyramis Works
=================

   Please read our `Pyramis Developer Reference <docs/dev-docs.md>`_ for a more detailed treatment.
