# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:06:48 2017

@author: user
"""

import pytest
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as fl

#Testing stations_level_over_threshold
def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    stations_water_levels = fl.stations_level_over_threshold(stations, 0.8)
    #Testing if the list is ordered
    assert all(stations_water_levels[i][1] >= stations_water_levels[i+1][1] for i in range(len(stations_water_levels)-1))
    #Testing if the output is a list of tuples and if the tuples have 2 elements each
    assert type(stations_water_levels) == list
    if len(stations_water_levels) >= 0:
        assert type(stations_water_levels[0]) == tuple
        assert len(stations_water_levels[0]) == 2
    #Testing that none of the water levels are None
    for item in stations_water_levels:
        assert item[1] != None

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    N=10
    stations_highest_level = fl.stations_highest_rel_level(stations, N)
    #Testing if the list has length N
    assert len(stations_highest_level) == N
    #Testing if the list is ordered
    assert all(stations_highest_level[i][1] >= stations_highest_level[i+1][1] for i in range(len(stations_highest_level)-1))
    #Testing if the output is a list of tuples and if the tuples have 2 elements each
    assert type(stations_highest_level) == list
    if len(stations_highest_level) >= 0:
        assert type(stations_highest_level[0]) == tuple
        assert len(stations_highest_level[0]) == 2
    #Testing that none of the water levels are None
    for item in stations_highest_level:
        assert item[1] != None