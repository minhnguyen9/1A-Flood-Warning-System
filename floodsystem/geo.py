"""This module contains a collection of functions related to
geographical data.

"""
#from floodsystem.utils import sorted_by_key

from floodsystem.stationdata import build_station_list
stations = build_station_list()

def rivers_with_station(stations):
    river_name = set()
    for station in stations:
        river_name.add(station.river)
    return river_name
    
print(rivers_with_station(stations))
                
    
    

