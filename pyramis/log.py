import logging

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

    fmt = "{}%(levelname)-5s{} %(lineno)-4d %(module)s.%(funcName)-8s: %(message)s"

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