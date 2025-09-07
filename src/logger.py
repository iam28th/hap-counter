import logging

fmt = "[%(levelname)s %(asctime)s]: %(message)s"
logging.basicConfig(format=fmt, level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)
