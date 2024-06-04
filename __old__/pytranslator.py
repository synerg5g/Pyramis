import os
import ast
import json
from cppfile import *
from cppfunction import *
import pyanalyzer
from pyramisexceptions import *
import operator
import contextmanager as ctxt


class PyTranslator:
    """
    A driver class to perform the code translation. Stores file-level information
    as attributes, and writes text to output .cpp file
    """

    output_files = {}  # main file for translated code.

    def __init__(self, py_script_filename, cpp_output_filename, node_dir):
        """
        The constructor. Adds a main file to project level file list,
        and adds main() as a function object to that file object's function dict.
        """
        self.node_dir = node_dir
        self.py_script_filename = py_script_filename
        self.cpp_output_filename = cpp_output_filename
        PyTranslator.output_files[0] = cfile.CPPFile(cpp_output_filename)

    def run(self):
        """
        Entry point for python file parsing. Generates a python AST
        and walks the tree line by line, storing node information
        into appropriate data structures.
        Generates the IR.
        """

        # Index for main file and key for main function
        file_index = 0

        with open(
            self.py_script_filename, "r"
        ) as py_source:  # go to parent dir, find py_script_name file.
            tree = ast.parse(
                py_source.read()
            )  # tree stores the AST. Throws error if incorrect indentation
            py_source.seek(0)
            all_lines = (
                py_source.read().splitlines()
            )  # store py exprs in a list of line strings.

            with open(f"{self.node_dir}/pyAST.py", "w") as f:
                f.write(f"{ast.dump(tree, indent = 4)}")  # store AST in a new file.

        udfpath = f"{self.node_dir}/udf.h"
        archpath = f"{self.node_dir}/Utils/arch.json"
        configpath = f"{self.node_dir}/Utils/amfconfig.json"  # use approp. config for node. Get from CLI
        IRContextManager = ctxt.ContextManager(udfpath, archpath, configpath)

        analyzer = pyanalyzer.PyAnalyzer(
            PyTranslator.output_files, all_lines
        )  # analyzer is a nodevisitor object.
        # parse .py file, annotate. Maps have incomplete types.
        analyzer.analyzeAST(
            tree, file_index, IRContextManager
        )  # modify translator frontedn.

        finalIRContext = analyzer.getIRContext()

        head_scope = finalIRContext.gethead()
        failed_events = finalIRContext._failed  # dict {fname: PyramisEvent}

        file = PyTranslator.output_files[0]

        # search for event in head scope symbols:
        for ename, event in failed_events.items():
            call = head_scope.get_symbol_from_scope(ename)

            if call:
                assert isinstance(call, K_CALL)
                for _p in call.parameters:
                    event.parameters.append(_p)
                    event._header.parameters.append(_p)

            else:
                raise PyramisEventNotCalledError()

            file._events[ename] = (
                event  # some events point to a event object originally in context. others were directly added to file during Walk.
            )

        # return reference to global scope
        return head_scope

    """
    ------------------------------------------
    Below functions drive code-generation.
    ------------------------------------------
    """

    def generate_file_text(self, finalIRGlobalScope):
        """
        This is where codegen begins.
        Consolidates code from IR, stores as a long list for easier printing.
        """
        hcount = 0
        cppcount = len(PyTranslator.output_files)
        for cppfile in [
            *PyTranslator.output_files.values()
        ]:  # list only contains desired output files .cpp
            fcount = hcount + cppcount

            cppfile.generate_header_files(
                finalIRGlobalScope
            )  # creates a header file entry, assigns map types in cfile.maps

            # could do infertypes from here during expansion
            for event in sorted(
                cppfile._events.values(), key=operator.attrgetter("_index")
            ):
                assert type(event) is PyramisEvent
                event.generate_event_text()  # needs typed maps
                cppfile.lines.append(event.converted_cpp_code)

            hcount += 1

    def write_cpp_files(self, finalIRGlobalScope):
        """
        Reads file objects
        and writes them to the appropriate output file
        """
        # generates text-representation of the parsed data. This is
        self.generate_file_text(finalIRGlobalScope)

        for file in PyTranslator.output_files.values():
            fname = file.filename
            if fname.endswith(".h"):
                path = f"../codegen/{fname}"
                if not os.path.exists(os.path.dirname(path)):
                    os.makedirs(os.path.dirname(path))
                with open(path, "w") as hf:
                    for line in file.lines:
                        try:
                            hf.write(line)
                        except TypeError as t:
                            logger.debug("Error while writing to HeaderFile.")
            # write to a file in includes directory
            else:
                # write to src directory
                path = f"../{fname}"
                with open(path, "w") as f:
                    for line in file.lines:
                        try:
                            f.write(line)
                        except TypeError as t:
                            logger.debug("Error while writing to file")

        logger.info(
            "Output Files written Successfully"
        )  # cpp_output_path = dsl_linking.cpp
