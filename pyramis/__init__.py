# FILE: __init__.py
# -----------------
# Initialise global configurations and objects.

import argparse
import sys
import logging
import os
import os.path
import pathlib
import subprocess

from . import log, config, utils, graph, python

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
        self.log.setLevel(logging.DEBUG)

    
    def configure(self, args, magic):
        """
        Set global options according to transpiler mode in the
        gx object. 
        
        gx parameters can be further used to choose
        translation path eg: c++ or eBPF. 
        
        Can override previously set default params here.
        """
        gx = config.GlobalInfo(magic, args) # create asn_base_types, udf parse
        # if args.debug:
        #     self.log.setLevel(logging.DEBUG) # run debug logs

        # if args.silent:
        #     gx.silent = True
        #     self.log.setLevel(logging.WARNING)
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

        parser_analyze = subparsers.add_parser('analyze', help="Perform base error checking and translation.")
        parser_analyze.add_argument("node", help="Name of the NF.dsl file to be translated.")

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
            if len(sys.argv) > 1 and sys.argv[1] not in ('analyze', 'build', 'run'):
                sys.argv.insert(1, 'analyze') # default is raw_translate
        
        args = parser.parse_args()
        print(args)

        translator = cls(args, magic) # init dirs, global configs.

        translator.log.info('*** Pyramis-to-C++ Transpiler 0.0.1 ***')
        translator.log.info('')

        if args.subcmd == 'analyze':
            translator.do_analyze()    # ast entry point, generate error report.
        
        if args.subcmd == "build":            
            # generate platform , makefile
            translator.do_build()
        
        if args.subcmd == "run":
            # first check if __BUILD__ contains all the required files,
            # If not, do_build
            if not translator.validate_build():
                print("no build")
                translator.gx.output_dir = translator.gx.build_dir
                translator.do_build() # mkdir __BUILD__, output to __BUILD__
                translator.output_dir = translator.gx.run_dir

            n_threads = args.threads
            translator.do_run(n_threads)
    
    def validate_build(self):
        nf = self.gx.nf_name
        required_files = ["Makefile", f"{nf}_contexts.h", f"{nf}_linking.cpp", f"{nf}_linking.h",
                          f"{nf}_platform.cpp", f"{nf}_platform.h"]  # Replace with your actual file names
        _build = self.gx.build_dir
        # Check if build directory exists
        if not _build.exists():
            return False

        # Check if each required file exists
        missing_files = []
        for filename in required_files:
            file_path = _build / filename
            if not file_path.exists():
                missing_files.append(file_path)

        if missing_files:
            print(f"Missing required files for NF '{nf}':")
            for file_path in missing_files:
                print(f"  - {file_path}")
            print("Creating Now")
            return False

        # All required files found
        return True


    def do_run(self, threads):
        # find the makefile in gx.build_dir, run make
        _build = self.gx.build_dir
        _mkf = _build / "Makefile"

        if not _mkf.exists():
            raise FileNotFoundError(f"Makefile not found: {_mkf}")
        
        _run = self.gx.run_dir
        if not _run.exists():
            _run.mkdir(parents=True)

        try:
            subprocess.run(["make"], cwd=_build, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during make: {e}")
            return
        
        _exec = _build / "build" / self.gx.nf_name    
        if not _exec.exists():
            print(f"Executable not found: {_exec}")
            return

        # run the exe from that folder via ./NF lo <n_threads>
        try:
            subprocess.run([str(_exec), "lo", str(threads)], cwd=_build, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during execution: {e}")
            return
    
    def do_analyze(self):
        # check notes
        # Parse the NODE.py file into python.py objects.
        # each module has an associated visitor.
        self.gx.py_module = graph.parse_module(self.gx)
    
    def do_raw_translate(self):
        assert(isinstance(self.gx.py_module, python.Module))  

        # contexts
        self.gx.py_module.generate_contexts()

        # linking.h
        self.gx.py_module.generate_linking_h()

        # linking.cpp
        self.gx.py_module.generate_linking_cpp()


    def do_build(self):
        self.do_analyze()
        
        self.do_raw_translate()  # C++ code-generation

        # # create platform file
        self.gx.py_module.generate_platform_h()

        self.gx.py_module.generate_platform_cpp()

        self.gx.py_module.fixup_udf_h()

        # create makefile
        self.gx.py_module.generate_makefile()

    def pyramis2py(self):
        """
        Create a syntactically correct python equivalent of the Pyramis 
        specification file. Store in .deps/<node>.py
        """
        path_to_py = self.gx._pyramis / ".deps"
        path_to_py.mkdir(exist_ok=True)

        _out = path_to_py / f"{self.gx.nf_name}.py"
        print(_out)
        
        _in = self.gx.nf_dsl
        print(_in)
        
        pre = utils.Preprocessor(_in, _out)
        pre.process()

        self.log.info("pre-processing complete.")

        return _out
