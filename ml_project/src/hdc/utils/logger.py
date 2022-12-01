import logging
import os
import pathlib
import sys

curr_folder = pathlib.Path(".")
logger = logging.getLogger(__name__)
os.makedirs(curr_folder / "logs", exist_ok=True)

file_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler = logging.FileHandler(curr_folder / "logs" / 'cache.log')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

stream_formatter = logging.Formatter('%(levelname)s : %(name)s : %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

logger.setLevel(logging.INFO)
