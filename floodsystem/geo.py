"""This module contains a collection of functions related to
geographical data.

"""
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
    




