"""This module contains a collection of functions related to
geographical data.

"""
                
from haversine import haversine
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list

#For Task1B
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
    

stations = build_station_list()

#For Task1D
def rivers_with_station(stations): 
    
    #create empty set and list
    river_set = set()
    river_list = []
    
    # Add river names into set (prevent repeats)
    for station in stations:
        river_set.add(station.river)
        
    # Convert the set to a list
    for river in river_set:
        river_list.append(river)
    river_list.sort()
    return river_list

def stations_by_river(stations):
    
    # Create empty dict and list of rivers using the previous function
    river_keys = rivers_with_station(stations)
    stations_by_river_dict = {}
    
    for river in river_keys:
        # Store river names as keys and empty lists as values
        stations_by_river_dict[river] = []
        for station in stations:
            if station.river == river:
                stations_by_river_dict[river].append(station.name)
            else :
                pass
        stations_by_river_dict[river].sort()
    return stations_by_river_dict

def stations_within_radius(stations,centre, r):
    
    stationdistance =  stations_by_distance(stations, centre)
#Using the stations_by_distance function to get the required values
    stationwithin = [x[0] for x in stationdistance if x[2] <= r]
#Only include the names of stations whose distance is less than r
    
    return sorted(stationwithin)



#For Task 1E
def rivers_by_station_number(stations, N):
    # Define variables and create empty list
    river_names = rivers_with_station(stations)
    n = 0
    list_of_tuples = []
    
    for river in river_names:
        
        # Create empty list and store river names into first element of each small list
        list_1 = []
        list_1.append(river)
        n = 0
        
        # Iterate through list of stations' rivers and count the number of rivers
        for station in stations:
            if station.river == river:
                n += 1
            else:
                pass
        list_1.append(n)
        
        # Convert a list of lists to a list of tuples
        tup = tuple(list_1)
        list_of_tuples.append(tup)
        
    # Sort the list of tuples by their second elements    
    list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1], reverse = True)
    
    # For special cases where there are more rivers with the same number of stations as the N th entry
    list_of_lists = []
    for t in list_of_tuples:
        list_of_lists.append(list(t))
    while N < len(list_of_lists):
        if list_of_lists[N-1][1] == list_of_lists[N][1]:
            N += 1
        else:
            break
    list_of_tuples = list_of_lists[:N]
    return list_of_tuples