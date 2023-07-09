# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:19:55 2023

From book "A Primer on Scientific Programming with Python"
https://link.springer.com/chapter/10.1007/978-3-030-16877-3_3

Exercise 5.4 - Fibonacci

@author: danre
"""
import numpy as np

def make_Fibonacci(N):
    """
    Parameters
    ----------
    N : Int
        Number of fibonacci numbers to print

    Returns
    -------
    Numpy array of first N fibonacci numbers

    """

    a, b = 1, 1
    fib_list = [a, b]
    
    for i in range(N):
        next_num = a + b
        fib_list.append(next_num)
        b, a = next_num, b        
    
    return np.array(fib_list)


def converging_ratio(fib_array):
    """
    Check if the limit of the ratio of consectutive fibonacci numbers
    approaches (1+sqrt(5))/2 - (i.e., the golden ratio)

    Parameters
    ----------
    fib_array : 1D Numpy array
        array as calculated in make_Fibonacci function

    Returns
    -------
    Numpy array showing the ratio of F_n/F_(n-1) for each n in the input array
    """
    phi = 1/2 + np.sqrt(5)/2
    
    # Calculate a new array with values equal to the ratio of consectutive values
    fib_ratio_array = np.ones(fib_array.size-1)
    for i in range(fib_array.size-1):
        fib_ratio_array[i] = fib_array[i+1]/fib_array[i]
    
    # Calculate absolute difference and relative difference from phi
    fib_abs_diff = np.abs(fib_ratio_array - phi)
    # fib_rel_diff = fib_abs_diff/phi
    
    return fib_abs_diff


def compute_rates(fib_array):
    """
    Compute the rate of convergence of the fib number consectutive ratio to phi
    Parameters
    ----------
    fib_array : 1D numpy array
        Calculated in make_Fibonacci, and inputed in the main function

    Returns
    -------
    Array of convergence rate, q, at each iteration
    """ 
    # Call converging ratio to function to get the absolute fib ratio errors 
    fib_errors = converging_ratio(fib_array)
    
    # Allocate arrays
    q_array_length = fib_errors.size - 2
    q_array = np.zeros(q_array_length)
    
    # Calculate the q array elementwise
    for i in range(q_array_length):
        q_value_top = np.log(fib_errors[i+2]/fib_errors[i+1]) # numerator of q
        q_value_bottom = np.log(fib_errors[i+1]/fib_errors[i])
        q_array[i] = q_value_top/q_value_bottom
    
    return q_array
        

if __name__ == '__main__':
    #fib_nums = int(input('Enter number of fibonacci numbers to calculate'))
    fib_nums=25  # number of fibonacci numbers to print
    fib_arr = make_Fibonacci(fib_nums)
    print(fib_arr)
    fib_abs = converging_ratio(fib_arr)
    print(fib_abs)
    q_arr = compute_rates(fib_arr)
    print(q_arr)
