# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:33:56 2023

From book "A Primer on Scientific Programming with Python"
https://link.springer.com/chapter/10.1007/978-3-030-16877-3_3

Exercise 5.3: Taylor Series, sympy and Documentation

In this exercise, you are supposed to develop a Python function that 
approximates sin(x) when x is near zero. To do this, write a program that 
utilizes sympy to develop a Taylor series for sin(x) around x = 0, keeping
only 5 terms from the resulting expression. Then, use sympy to turn the
 expression into a function. Let the program also plot sin(x) and the 
 developed function together for x in [−π, π].
@author: danre
"""

import sympy as sym
from sympy.plotting import *
from sympy import pi

x = sym.symbols('x')
f = sym.sin(x)

s = f.series(x, x0=0, n = 7).removeO()

plot(s, sym.sin(x), (x,-pi, pi))