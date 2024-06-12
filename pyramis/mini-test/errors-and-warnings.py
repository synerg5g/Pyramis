import logging
import sys
import os
import datetime

log_dir = "./__logs/"

logger = logging.getLogger("Pyramis")
# os.makedirs(log_dir, exist_ok=True)
# timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
# error_file = logging.FileHandler(filename=os.path.join(log_dir, f"error_log_{timestamp}.txt"))
# error_file.setLevel(logging.WARNING)
# formatter = logging.Formatter("*%(levelname)s* %(message)s")
# error_file.setFormatter(formatter)
# logger.addHandler(error_file) 
log_console = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(log_console)

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

class CustomFormatter(logging.Formatter):
    """
    class for coloured logs based on log level
    
    Ref: https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
    """

    # https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
    # ANSI escape codes, hex.
    white = "\x1b[97;20m" # bright white
    GREY = "\x1b[38;20m" 
    GREEN = "\x1b[32;20m"
    CYAN = "\x1b[36;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    RED_BOLD = "\x1b[31;1m"
    RESET = "\x1b[0m"

    fmt = "{}%(levelname)-5s{}: %(message)s"

    FORMATS = {
        logging.DEBUG: fmt.format(GREEN, RESET),
        logging.INFO: fmt.format(white, RESET),
        logging.WARNING: fmt.format(YELLOW, RESET),
        logging.ERROR: fmt.format(RED, RESET),
        logging.CRITICAL: fmt.format(RED_BOLD, RESET),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)
    
#print(self.__class__.__name__) # name of current class

# log_error = logging.getLogger(__name__) 
# log_error_console = logging.StreamHandler(stream=sys.stdout)
# log_error_console.setFormatter(CustomFormatter())
# log_error.addHandler(log_error_console)
# # set the default log level
# log_error.setLevel(logging.ERROR)

# create "Pyramis" Logger object
log_dbg = logging.getLogger(__name__) 
log_dbg_console = logging.StreamHandler(stream=sys.stdout)
log_dbg_console.setFormatter(CustomFormatter())
log_dbg.addHandler(log_dbg_console)
# set the default log level
log_dbg.setLevel(logging.DEBUG)


# log_warn = logging.getLogger(__name__) 
# log_warn_console = logging.StreamHandler(stream=sys.stdout)
# log_warn_console.setFormatter(CustomFormatter())
# log_warn.addHandler(log_warn_console)
# # set the default log level
# log_warn.setLevel(logging.WARN)

# log_info = logging.getLogger(__name__) 
# log_info_console = logging.StreamHandler(stream=sys.stdout)
# log_info_console.setFormatter(CustomFormatter())
# log_info.addHandler(log_info_console)
# # set the default log level
# log_info.setLevel(logging.INFO)

cmd = "SET_ALL"
lineno = 33
file = "NF_A.dsl"

# error("`%s` is not a valid Pyramis action, abort." %cmd, 
#                         filename=file, lineno=lineno)

log_dbg.error("utils.py:process_line(): `SET_ALL` is not a valid Pyramis action, abort")
log_dbg.warning("graph.py:validate_IR(): Event `server_entry` has incomplete types.")
log_dbg.info("config.py:visit_Module():  Pyramis IR generated successfuly.")
log_dbg.debug("infer.py:get_type_from_type_str(): None")




