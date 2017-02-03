# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:43:25 2017

@author: Minh
"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()
p = (52.2053, 0.1218)
distance = stations_by_distance(stations, p)
print(distance[:10])
print(distance[-10:])