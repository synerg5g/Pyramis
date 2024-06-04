# FILE: __init__.py
# -----------------
# Initialise global configurations and objects.

import argparse
import sys
import logging
import os
import os.path
import pathlib

from . import log, config, utils, graph

class Pyramis:
    def __init__(self, options, magic):
        self.configure_logging()
        self.gx = self.configure(options, magic) # override default params if required.
        self.gx.py_module_path = self.pyramis2py() # .pyramis/node.py
        self.log.info(self.gx.py_module_path)

    def configure_logging(self):
        """
        silent -> WARNING only, (terminal failed type inference)
        
        debug -> DEBUG, (all logs)
        
        default -> INFO (procedure begin/end logs)
        """
        print(self.__class__.__name__) # name of current class

        # create "Pyramis" Logger object
        self.log = logging.getLogger(self.__class__.__name__) 

        # # create a formatted handler to print logs
        # os.makedirs("./__logs/", exist_ok=True)
        # log_file = logging.FileHandler(filename="./__logs/log.txt")
        # log_file.setFormatter(log.CustomFormatter())
        # self.log.addHandler(log_file) 
        
        log_console = logging.StreamHandler(stream=sys.stdout)
        log_console.setFormatter(log.CustomFormatter())
        self.log.addHandler(log_console)

        # set the default log level
        self.log.setLevel(logging.INFO)

    
    def configure(self, args, magic):
        """
        Set global options according to transpiler mode in the
        gx object. 
        
        gx parameters can be further used to choose
        translation path eg: c++ or eBPF. 
        
        Can override previously set default params here.
        """
        gx = config.GlobalInfo(magic, args) # create asn_base_types, udf parse
        # for u in gx.udfs.values():
        #     print(f"{u.name}: {[tp.ident for tp in u.arg_types]}"

        if args.debug:
            self.log.setLevel(logging.DEBUG) # run debug logs

        if args.silent:
            gx.silent = True
            self.log.setLevel(logging.WARNING)

        self.log.debug(gx.nf_dsl)
        self.log.debug(gx.output_dir)
        return gx

    @classmethod
    def commandline(cls, magic):
        # env

        # --- command-line options
        parser = argparse.ArgumentParser(
            prog="pyramis",
            description="Pyramis-to-C++ transpiler",
        )

        subparsers = parser.add_subparsers(
            title='subcommands',
            dest='subcmd')

        parser_translate = subparsers.add_parser('translate', help="Perform base error checking and translation.")
        parser_translate.add_argument("node", help="Name of the NF.dsl file to be translated.")

        parser_build = subparsers.add_parser("build", help="Generate platform files and MAKEFILE.")
        parser_build.add_argument("node", help="Name of the NF.dsl file to be translated.")

        parser_run = subparsers.add_parser("run", help="Compile and run a pyramis generated multithreaded NF.")
        parser_run.add_argument("node", help="Name of the NF.dsl file to be translated.")
        parser_run.add_argument("threads", help="# threads to run NF.")


        #arg("node", help="directory containing .dsl file for a single node") # must be present in interfaces.json
        # arg("mode", help="Specify processing codegen or eBPF codegen")
        
        # opt("-d", "--debug",            help="set debug level", action="store_true")
        # opt("-s", "--silent",           help="Silent mode, only show warnings", action="store_true")
        # opt("-o", "--olevel",           help="specify compiler optimizations", type=int, nargs='?', const=0)

        # make 'translate' the default subparser
        for arg in sys.argv[1:]:
            if arg in ('-h', '--help'):
                break
        else:
            if len(sys.argv) > 1 and sys.argv[1] not in ('translate', 'build', 'run'):
                sys.argv.insert(1, 'translate') # default is raw_translate
        
        args = parser.parse_args()
        print(args)

        translator = cls(args, magic) # Main translation class with all global configs.

        translator.log.info('*** Pyramis-to-C++ Transpiler 0.0.1 ***')
        translator.log.info('')

        if args.subcmd == 'translate':
            translator.do_analyze()    # ast entry point
            translator.raw_translate()  # C++ code-generation
        
        if args.subcmd == "build":
            translator.do_analyze()
            translator.do_raw_translate()
            # create platform file and makefile.
            translator.do_build()
    
    
    def do_analyze(self):
        # check notes
        # Parse the NODE.py file into python.py objects.
        # each module has an associated visitor.
        self.gx.py_module = graph.parse_module(self.gx)
    
    def do_raw_translate(self):
        self.log.debug("TODO: translate()")
        exit()

    def do_build(self):
        pass

    def pyramis2py(self):
        """
        Create a syntactically correct python equivalent of the Pyramis 
        specification file. Store in .deps/<node>.py
        """
        path_to_py = self.gx.___pyramis / ".deps"
        path_to_py.mkdir(exist_ok=True)

        _out = path_to_py / f"{self.gx.vnf_name}.py"
        
        _in = self.gx.nf_dsl
        
        pre = utils.Preprocessor(_in, _out)
        pre.process()

        self.log.info("pre-processing complete.")

        return _out
