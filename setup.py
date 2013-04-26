#Setup file for cython LLL Algorithm

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("lattice_reduction", ["lattice_reduction.pyx", "lll_reduce.c"],
    include_dirs = [np.get_include()])]
)
