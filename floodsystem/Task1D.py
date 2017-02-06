from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations=build_station_list()

def run():
    
    # Build list of stations
    stations=build_station_list()
    
    rivers = rivers_with_station(stations)
    d = stations_by_river(stations)
    print(rivers[:10])
    print(d['River Aire'])
    print(d['River Cam'])
    print(d['Thames'])

if __name__ == "__main__":
    
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    
    run()