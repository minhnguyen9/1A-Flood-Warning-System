# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Sun Feb 26 17:30:18 2017

@author: Minh
"""
from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
    
def plot_water_level_with_fit(station, dates, levels, p):
    #Collect outputs from polyfit function
    poly, numdates, d0 = polyfit(dates, levels, p)
    #Plot the dates against the output function
    plt.plot(dates, poly(numdates - d0))
    #plot the actual value of 
    plot_water_levels(station, dates, levels)
    plt.show()
    

def plot_water_levels(station, dates, levels):
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('time')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()