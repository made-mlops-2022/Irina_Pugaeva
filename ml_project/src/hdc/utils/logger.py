import os
import sys
import logging
import pathlib

curr_folder = pathlib.Path(".")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
os.makedirs(curr_folder / "logs", exist_ok=True)
file_handler = logging.FileHandler(curr_folder / "logs" / 'cache.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler(sys.stdout))