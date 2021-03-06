#!/usr/bin/env python
# coding: utf-8

"""Solves Langermann Multimodal Problem with Automatic Optimization Refinement.
"""

from __future__ import print_function

from numpy import cos, pi, exp

from pyOpt.optimization import Optimization
from pyOpt.pyNSGA2.pyNSGA2 import NSGA2
from pyOpt.pySLSQP.pySLSQP import SLSQP


def objfunc(x):
    r"""Objective function

    Parameters
    ----------
    x : iterable

    Returns
    -------
    tuple

    """
    a = [3, 5, 2, 1, 7]
    b = [5, 2, 1, 4, 9]
    c = [1, 2, 5, 2, 3]

    f = 0.0
    for i in range(5):
        f += -(c[i] * exp(-(1 / pi) * ((x[0] - a[i])**2 + (x[1] - b[i])**2)) * cos(pi * ((x[0] - a[i])**2 + (x[1] - b[i])**2)))

    g = [0.0]*1
    g[0] = 20.04895 - (x[0]+2.0)**2 - (x[1]+1.0)**2

    fail = 0

    return f, g, fail


opt_prob = Optimization('Langermann Function 11', objfunc)
opt_prob.addVar('x1', 'c', lower=-2.0, upper=10.0, value=8.0)
opt_prob.addVar('x2', 'c', lower=-2.0, upper=10.0, value=8.0)
opt_prob.addObj('f')
opt_prob.addCon('g', 'i')
print(opt_prob)

# Global Optimization
nsga2 = NSGA2()
nsga2(opt_prob)
print(opt_prob.solution(0))

# Local Optimization Refinement
slsqp = SLSQP()
slsqp(opt_prob.solution(0))
print(opt_prob.solution(0).solution(0))
