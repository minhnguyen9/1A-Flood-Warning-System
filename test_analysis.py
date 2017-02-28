# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:43:17 2017

@author: Minh
"""
import pytest
import math
import numpy as np
import floodsystem.analysis as a
import matplotlib.dates as mpld

def test_polyfit():
    #Create dates by converting a series of number into dates
    x = np.linspace(10001, 10005, 20)
    dates = mpld.num2date(x)
    #Ensure that the levels follow a known function x^2
    levels = x**2
    #Retrieve function outputs from polyfit
    poly, numdates, d0 = a.polyfit(dates, levels, 2)
    for i in range(20):
        #Check if the polyfit function is approximately equal to x**2, up to a certain tolerance
        assert math.isclose(poly(numdates - d0)[i], x[i]**2, abs_tol=1e-3) == True