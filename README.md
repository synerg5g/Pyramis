Pyramis
==================
**Pyramis** is a Domain-Specific language that can specify multi-tier systems of variying complexities. 

**The Pyramis-to-C++ compiler** provided converts a NF

Usage
-----
Create a venv, pip install from source.
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

<details>
    <summary>Async Projections</summary>

### Async Projections
this and that and this and that
</details>

## :rocket: Performance