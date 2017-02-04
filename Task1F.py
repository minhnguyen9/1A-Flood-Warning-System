# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:06:11 2017

@author: Minh
"""

from floodsystem.station import typical_range_consistent
from floodsystem.stationdata import build_station_list

stations = build_station_list()
inconsistency = typical_range_consistent(stations)
print(inconsistency)