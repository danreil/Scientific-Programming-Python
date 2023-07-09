# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 14:13:32 2023
From book "A Primer on Scientific Programming with Python"
https://link.springer.com/chapter/10.1007/978-3-030-16877-3_3

Exercise 3.11
Compute pi in 2 different methods, compare and plot error

@author: danre
"""

import numpy as np
import matplotlib.pyplot as plt

def leibniz(N):
    """
    Compute pi approx array with leibniz formula
    """
    pi_approx = np.zeros(N)
    pi_temp = 0
    pi_running_total = 0
    
    for k in np.arange(N):
        pi_temp = 8*(1/((4*k+1)*(4*k+3)))
        pi_running_total += pi_temp
        pi_approx[k] = pi_running_total
    
    return pi_approx

def euler(N):
    """
    Compute pi approx array with euler formula
    """
    pi_approx = np.zeros(N)
    pi_temp = 0
    pi_running_total = 0
    
    for k in np.arange(0, N):
        pi_temp = 1/(k+1)**2
        pi_running_total += pi_temp
        pi_approx[k] = np.sqrt(6*pi_running_total)
    
    return pi_approx

N=2500
start_index=100  # start not at first index if desired, to narrow the plot range
iters = np.arange(N)

pi_array_lieb = leibniz(N)
pi_array_euler = euler(N)

pi_lieb_error = np.pi - pi_array_lieb
pi_euler_error = np.pi - pi_array_euler

plt.subplot(2,1,1)
plt.plot(iters[start_index:N], pi_array_lieb[start_index:N],'k', iters[start_index:N], pi_array_euler[start_index:N], 'r')
plt.subplot(2,1,2)
plt.plot(iters[start_index:N], pi_lieb_error[start_index:N], 'k', iters[start_index:N], pi_euler_error[start_index:N], 'r')
final_lieb_error = np.pi - pi_array_lieb[-1]
final_euler_error = np.pi - pi_array_euler[-1]
print(f'Total error with Leibniz method is {final_lieb_error} and with Euler method is {final_euler_error}')


        