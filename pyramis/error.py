import logging
import sys
import os
import datetime

log_dir = "./__logs/"

logger = logging.getLogger("Pyramis")
os.makedirs(log_dir, exist_ok=True)
timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
error_file = logging.FileHandler(filename=os.path.join(log_dir, f"error_log_{timestamp}.txt"))
error_file.setLevel(logging.WARNING)
formatter = logging.Formatter("*%(levelname)s* %(message)s")
error_file.setFormatter(formatter)
logger.addHandler(error_file) 

ERRORS = set()

def error(msg, node=None, warning=False, mv=None, 
          filename=None, lineno=None):
    if warning:
        kind = logging.WARNING
    else:
        kind = logging.ERROR
    
    if mv:
        filename = mv.module.relative_filename
        if node and hasattr(node, "lineno"):
            lineno = node.lineno
    elif filename and lineno:
        filename = os.path.basename(filename)
        lineno = lineno
    result = (kind, str(filename or ''), lineno, msg)
    
    if result not in ERRORS:
        ERRORS.add(result)
    # Compiler inidicated catastrophic failure
    # EXIT COMPILATION
    if not warning:
        print_error(result)
        # sys.exit(1)

def print_error(error):
    (kind, filename, lineno, msg) = error
    result = ""
    if filename:
        result += str(filename) + ":"
        if lineno is not None:
            result += str(lineno) + ":"
        result += " "
    logger.log(kind, result + msg)