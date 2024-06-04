# FILE: __main__.py
# -----------------
# Translation entry point
from . import Pyramis
import pathlib

def run():
    pyramis_aux_dir_path = pathlib.Path().home() / ".pyramis"
    Pyramis.commandline(pyramis_aux_dir_path) # Interactive command-line

if __name__ == "__main__":
    # delete .deps, .test
    run()