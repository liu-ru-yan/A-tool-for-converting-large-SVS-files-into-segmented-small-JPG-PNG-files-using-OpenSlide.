from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Process Files',
    ext_modules=cythonize("process_files.pyx"),
)
