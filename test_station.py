"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.station import typical_range_consistent


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    
def test_typical_range_consistent():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (2.0, 4.0)
    river = "River X"
    town = "My Town1"
    trange1 = (2.3, 3.4445)
    trange2 = (None)
    trange3 = (2, 0.5)
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)
    s = (s1, s2, s3)
    a = typical_range_consistent(s)
    assert type(a) == list
    assert type(a[0]) == str
    assert len(a) == 2