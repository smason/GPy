# Copyright (c) 2012, GPy authors (see AUTHORS.txt).
# Licensed under the BSD 3-clause license (see LICENSE.txt)


import linalg
import misc
import squashers
import warping_functions
import datasets
import mocap
import decorators
import classification
import subarray_and_sorting
import caching
import diag
import initialization
import multioutput
import linalg_gpu
# import parallel

try:
    import sympy
    _sympy_available = True
    del sympy
except ImportError as e:
    _sympy_available = False

if _sympy_available:
    import symbolic
