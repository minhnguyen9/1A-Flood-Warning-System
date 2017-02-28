# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:01:54 2017

@author: user
"""

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

#Getting the 5 stations with the highest water level
at_risk = stations_highest_rel_level(stations, 5)
dt = 10

#Finding dates and levels data for the 5 stations and plotting them
for item in at_risk:
    for station in stations:
        if station.name == item[0]:
            dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
            plot_water_levels(station.name, dates, levels)