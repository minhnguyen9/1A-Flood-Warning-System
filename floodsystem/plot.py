# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:30:18 2017

@author: Minh
"""
from floodsystem.analysis import polyfit
    
def plot_water_level_with_fit(station, dates, levels, p):
    #Collect outputs from polyfit function
    poly, numdates, d0 = polyfit(dates, levels, p)
    #Plot the dates against the output function
    plt.plot(dates, poly(numdates - d0))
    #plot the actual value of 
    plot_water_levels(station, dates, levels)
    plt.show()
    