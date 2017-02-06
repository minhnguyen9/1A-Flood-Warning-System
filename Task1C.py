# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 00:47:12 2017

@author: Minh
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

stations = build_station_list()
centre = (52.2053, 0.1218)

thing = stations_within_radius(stations, centre, 10)
print(thing)