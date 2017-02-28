# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:21:55 2017

@author: Minh
"""
import numpy as np
import matplotlib

#Task 2F
def polyfit(dates, levels, p):
    #Convert dates into number
    numdates = matplotlib.dates.date2num(dates)
    #Finding the polynomial function
    p_coeff = np.polyfit(numdates - numdates[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, numdates, numdates[0]

def check_rise_fall(dates, levels, p):
    #Collects the polynomial function fitted to graph of dates and water level
    poly, numdates, d0 = polyfit(dates, levels, p)
    #Find the derivative of the polynomial function
    gradientf = np.polyder(poly)
    #Using the derivative function, find the gradient of the plot at the most
    #recent point so that I can determine whether it is rising or falling
    return gradientf(numdates[-1])