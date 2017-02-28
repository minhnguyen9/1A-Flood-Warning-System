# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:54:08 2017

@author: user
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)

for item in stations_level_over_threshold(stations, 0.8):
    print(item)