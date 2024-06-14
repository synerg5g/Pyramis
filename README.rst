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

   Please read our `Pyramis Keyword Reference <docs/pyramis-keywords.rst>`_ for a complete list of processing keywords.

The recommended workflow is as follows:

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Task                                          | Action                                                                                              |
+===============================================+=====================================================================================================+
| Create Pyramis Specification                  || In a parent directory,                                                                             |                     
|                                               ||  Fix names and interfaces of individual nodes, define ``interfaces.json``.                         |
|                                               ||  For each node, use Pyramis keywords to define a processing file ``node_name.dsl``.                |         
|                                               ||  UDFs, if any must be consolidated into a single ``udf.h``, `udf.cpp`` pair.                       |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Analyze Pyramis Specification                 || To validate a pyramis specification of node *NF_A*, do:                                            |
|                                               ||  ``$ pyramis translate NF_A``                                                                      |
|                                               || The Pyramis Compiler will generate an error-report for any irregularities                          |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Build C++ Implementation                      || To generate a compilable C++ node implementation for *NF_A*, do:                                   |
|                                               ||  ``$ pyramis build NF_A``                                                                          |
|                                               || A set of .cpp and .h files will be generated along with a base Makefile.                           |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Run C++ NFs                                   || To run a translated node *NF_A* on *num_threads* threads, do:                                      |
|                                               ||  ``$ pyramis run NF_A num_threads``                                                                |
|                                               || Your NF specification has been converted to a running NF instance.                                 |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------+

💡 How Pyramis Works
=================

   Please read our `Pyramis Developer Reference <docs/dev-docs.rst>`_ for a more detailed treatment.
