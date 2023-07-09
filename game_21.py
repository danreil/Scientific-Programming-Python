# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 13:57:39 2023
From book "A Primer on Scientific Programming with Python"
https://link.springer.com/chapter/10.1007/978-3-030-16877-3_3

Exercise 3.8
Consider some game where each participant draws a series of random integers evenly 
distributed between 0 and 10, with the aim of getting the sum as close as possible to 21, 
but not larger than 21. You are out of the game if the sum passes 21.

After each draw, you are told the number and your total sum, and are asked whether 
you want another draw or not. The one coming closest to 21 is the winner.

@author: danre
"""

import random

total = 0
limit = 21

while total <= 21:
    num = int(input)