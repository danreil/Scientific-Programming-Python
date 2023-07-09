# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:37:36 2023
From book "A Primer on Scientific Programming with Python"
https://link.springer.com/chapter/10.1007/978-3-030-16877-3_3

Exercise 6.9 - Adaptive Integration
@author: danre
"""

from midpoint import midpoint
from trapezoidal import trapezoidal
import numpy as np

def adaptive_integration(f, a, b, eps, method=midpoint):
    """
    Function to perform a direct integral with a step size small enough for a given error
    To answer this question, we may enter an iterative procedure where we compare the results
    produced by n and 2n intervals, and if the difference is smaller than 𝜖, the value corresponding 
    to 2n is returned. Otherwise, we increase n and repeat the procedure
    Parameters
    ----------
    f : Callable function
        Function to be integrated
    a : Double
        Endpoint.
    b : Double
        Endpoint.
    eps : Double
        Tolerance, or error, in the answer.
    method : Callable function
        Integration method. The default is midpoint.

    Returns
    -------
    Value of integral and n, the number of intervals needed

    """
    n = 1
    error = 100  # pick a random large error value at first
    while error > eps:
        int_val_1 = method(f, a, b, n)  # integral value with n steps
        int_val_2 = method(f, a, b, 2*n)  # integral value with 2*n steps
        error = np.abs(int_val_1-int_val_2)  # error is absolute val of diff
        n*=2  # double n, and the loop repeats if error is too large
    
    return int_val_2, n

func = lambda x: x**2 
a, b = 0, 2 
eps = 10**(-5)
int_numeric, n = adaptive_integration(func, a, b, eps)
antideriv = lambda x: x**3/3
int_exact = antideriv(b) - antideriv(a) 
print(f'Exact integral is {int_exact} and adaptive numerical integral is {int_numeric}')
actual_error = np.abs(int_numeric - int_exact)
print(f'Actual error is {actual_error} and needed {n} intervals')

