# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:07:04 2017

@author: Minh
"""

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import floodsystem.plot as plot
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

#Getting the 5 stations with the highest water level
at_risk = stations_highest_rel_level(stations, 5)
dt = 5

#Finding dates and levels data for the 5 stations and plotting them with polyfit function
for item in at_risk:
    for station in stations:
        if station.name == item[0]:
            dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
            print(type(polyfit(dates, levels, 4)))
            plot.plot_water_level_with_fit(station.name, dates, levels, 4)