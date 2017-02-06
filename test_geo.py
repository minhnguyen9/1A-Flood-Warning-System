# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 00:27:37 2017

@author: Minh
"""

import pytest
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    s = build_station_list()
    p = (0.0,0.0)
    a = stations_by_distance(s, p)
    
    assert a[0][2] <= a[-1][2]
    for item in a:
        assert type(item) == tuple
        assert type(item[0]) == str
        assert type(item[2]) == float

def test_stations_within_radius():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town1"
    coord1 = (2.0, 4.0)
    coord2 = (2.01, 3.99)
    coord3 = (200.0, -250.0)
    s1 = MonitoringStation(s_id, m_id, label, coord1, trange, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord2, trange, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord3, trange, river, town)
    s = (s1, s2, s3)
    a = stations_within_radius(s, coord1, 10)
    assert type(a[0]) == str
    assert len(a) == 2


