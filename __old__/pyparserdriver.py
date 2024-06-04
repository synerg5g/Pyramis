from argparse import ArgumentParser, SUPPRESS
import pytranslator
import preprocessing as pre
from __old__.logger import logger

def py_convert(py_script_filename, cpp_output_filename, node_dir):
    """
    The entry point of the translator. Call this function to 
    translate a python script to C++.

    Parameters
    ----------
    script_path : str
        The relative path to the python script to convert
    output_path : str
        The relative path to the directory to output to
    """
    translator = pytranslator.PyTranslator(py_script_filename,
                                           cpp_output_filename,
                                           node_dir) # adds main file obj, filename from cmd
    
    # Generates AST, assigns AST nodes with usable types, 
    # generates an intermediate representation and 
    # converts IR to stored C++ code.
    finalIRGlobalScope = translator.run()
    logger.debug("IR Generation Complete")

    # Perhaps translator.generate_header_files()?
 
    # Writes c++ code from CPPFile object to output_filename.cpp.
    translator.write_cpp_files(finalIRGlobalScope) # contains info needed to give types to maps
    
if __name__ == "__main__":
    """
    Accept the inputs
    syntax to run:
            python3 parserdriver.py --dir "directoryOfDSL" --node "NodeName" --input "InputDSLFile" --output "OutputCppFileName" 

    First generate intermediate.py from AMF.dsl. 
    Then use intermediate.py as input to pytranslator for AST generation.
    """
    parser = ArgumentParser(add_help=False)
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    optional.add_argument(
        '-h',
        '--help',
        action='help',
        default=SUPPRESS,
        help='show this help message and exit'
    )
    required.add_argument('--dir', default= "../AMF", help="Input directory name for the translation")
    required.add_argument('--node', default="AMF", help="Network function name for the translation")
    required.add_argument('--input', default="amf.dsl", help="Input DSL file name for the translation")
    optional.add_argument('--output', default="amf_linking_d.cpp", help="Destination for the output")

    # parser.set_defaults(method = py_convert)

    args = parser.parse_args()
    # args.method(**vars(args)

    inter = args.input.split(".")
    input_filename = f"{args.dir}/{args.input}"
    intermediate_filename = f"{args.dir}/{inter[0]}-intermediate.py" #specified by user.
    output_filename = f"{args.dir}/{args.output}"

    logger.debug("Node Directory: %s", args.dir)
    logger.debug("Node Name: %s", args.node)
    logger.debug("Pyramis Input Filename: %s", input_filename)
    logger.debug("C++ Output Filename: %s", output_filename)

    pre.processing(input_filename, intermediate_filename) #converts Pyramis to Python Syntax

    py_convert(intermediate_filename, output_filename, args.dir)

    
    
