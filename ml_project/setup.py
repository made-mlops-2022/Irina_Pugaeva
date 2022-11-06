from setuptools import find_packages, setup
import pathlib

PROJECT = pathlib.Path(__file__).parent

setup(
    name='hdc',
    packages=find_packages("src"),
    version='0.1.0',
    description='Heart disease classifier',
    author='Irina Pugaeva',
    package_dir={"": "src"},
    install_requires=[module for module in PROJECT.joinpath("requirements.txt").read_text().split("\n") \
        if not module.startswith("--")],
    license='',
)
