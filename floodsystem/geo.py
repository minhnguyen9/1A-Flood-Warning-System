"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.stationdata import build_station_list
stations = build_station_list()

def rivers_with_station(stations):
    river_name = set()
    for station in stations:
        river_name.add(station.river)
    return river_name
    
print(rivers_with_station(stations))
                
from haversine import haversine
from floodsystem.utils import sorted_by_key

def stations_by_distance(station, p):
    
    distance_list = []

    for i in station:
        name = i.name
        town = i.town
        coordinate = i.coord
#Taking the desired values from the list of monitoring stations
        distance = haversine(coordinate, p)
        d = (name, town, distance)
        
        distance_list.append(d)
#Putting the desired value into a new list, along with the distance
    return sorted_by_key(distance_list, 2)
    
def stations_within_radius(stations,centre, r):
    
    stationdistance =  stations_by_distance(stations, centre)
#Using the stations_by_distance function to get the required values
    stationwithin = [x[0] for x in stationdistance if x[2] <= r]
#Only include the names of stations whose distance is less than r
    
    return sorted(stationwithin)

    


