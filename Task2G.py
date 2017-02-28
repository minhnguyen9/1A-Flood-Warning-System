# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:53:45 2017

@author: Minh
"""
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import check_rise_fall
from floodsystem.utils import sorted_by_key

stations = build_station_list()
update_water_levels(stations)
#using data from the past 5 days
dt = 5
lowcheck = []
modcheck = []
highcheck = []
low = []
moderate = []
high = []
severe = []

#Getting a list of station names for station above the following tolerances
for station in stations_level_over_threshold(stations, 0.5):
    lowcheck.append(station[0])
for station in stations_level_over_threshold(stations, 1.0):
    modcheck.append(station[0])
for station in stations_level_over_threshold(stations, 1.5):
    highcheck.append(station[0])

for station in stations:
    #Iterating over list of stations
    #If station not above 0.5 relative water level, statition is low risk
    if station.name not in lowcheck:
        stationlowname = station.name
        stationlevel = station.relative_water_level()
        stationlow = (stationlowname, stationlevel)
        low.append(stationlow)
    #If station between 0.5 and 1.0 relative water level, station is moderate risk
    elif station.name not in modcheck:
        stationmodname = station.name
        stationlevel = station.relative_water_level()
        stationmod = (stationmodname, stationlevel)
        moderate.append(stationmod)
    else:
        dates, levels = fetch_measure_levels(station.measure_id,
                                    dt=datetime.timedelta(days=dt)) 
        #Ignore stations with no data for the past 5 days
        if len(dates) == 0 or len(levels) == 0:
            pass
        #If relative water level is above 1.5 or above 1.0 and rising
        #(found using gradient at the latest datapoint) then station is severe risk
        elif station.name in highcheck or check_rise_fall(dates, levels, 4) > 0:
            stationseverename = station.name
            stationlevel = station.relative_water_level()
            stationsevere = (stationseverename, stationlevel)
            severe.append(stationsevere)
        #If station has relative level between 1.0 and 1.5 and not rising, station is high risk
        else:
            stationhighname = station.name
            stationlevel = station.relative_water_level()
            stationhigh = (stationhighname, stationlevel)
            high.append(stationhigh)

print(len(severe), " weather stations with severe risk of flooding, they are:", sorted_by_key(severe, 1, True))

        