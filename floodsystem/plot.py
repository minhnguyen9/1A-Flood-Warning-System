# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:00:06 2017

@author: user
"""

import matplotlib.pyplot as plt

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