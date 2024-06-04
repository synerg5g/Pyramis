import logging

logging.basicConfig(
    filename="./Logs/transator_logs.log",
    filemode="w",
    format="%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)
