# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:49:53 2017

@author: user
"""

from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    #Create empty list that will hold station that is above the tolerance
    flood_stations = []
    for station in stations:
        #Ignore stations where there is no relative water level
        if station.relative_water_level() == None:
            pass
        else:
            #Add station and the water level to list if the relative water level is above tolerance
            if station.relative_water_level() > tol:
                high_station_level = (station.name, station.relative_water_level())
                flood_stations.append(high_station_level)
    #Return list sorted by relative water level
    return sorted_by_key(flood_stations, 1, True)

def stations_highest_rel_level(stations, N):
    station_rel_level = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        else:
            #Same as previous but this time does not check if above tolerance, do for all stations
            name_level = (station.name, station.relative_water_level())
            station_rel_level.append(name_level)
    sorted_station = sorted_by_key(station_rel_level, 1, True)
    return sorted_station[:N]