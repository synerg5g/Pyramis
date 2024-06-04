Pyramis-Translator
==================
A source-to-source compiler used to demonstrate the feasibility of Pyramis 
as a DSL for 3GPP multi-tier systems.

Usage
-----
Create a venv, pip install from source.
https://realpython.com/python-virtual-environments-a-primer/
0. `python3 -m venv .pyramis` -> `source .pyramis/bin/activate`
1. `pip install .`                                  # run setup.py in cwd
2. `pyramis <NODE> <options>`                      # default will be translate to C++.
                                          # NODE: single directory containing the .pyr processing file.
                                          # OPTIONS: --llevel, --olevel


Path requirements:
- Translator must be run from the folder containing the `<node.dsl>` file.
- Any C++ utilities/source directories must be present just outside this directory.

Input files: `node/<node>.dsl`, `node/udf.h`, `node/udf.cpp`
Output files: `<node>_linking.cpp`, `linkingheader.h`, `contexts.h`, `<node>platform.cpp` 

Functionality
-------------
Verifies type consistency in the processing-file specification.
Enforces the asn-standard-types-only restriction. (i.e. all UDFs must have an interface that uses asn-standard-types)
