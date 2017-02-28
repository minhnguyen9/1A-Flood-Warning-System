# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:58:14 2017

@author: user
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)

for item in stations_highest_rel_level(stations, 10):
    print(item)
