import googlemaps
from datetime import datetime
import config
import json

with open('2020_SEPTEMBER.json') as json_file:
    data = json.load(json_file)

gmaps = googlemaps.Client(key=config.api_key)

result = gmaps.reverse_geocode((42.6825081, 23.3568578))

def get_address(data):
    #print(data["timelineObjects"][5]["placeVisit"]["location"]["address"])
    result = []
    for a in range(315):
        if 'placeVisit' in data["timelineObjects"][a]:
            #print(data["timelineObjects"][a]["placeVisit"]["location"]["address"])
            #print("-------------------------")
            result.append(data["timelineObjects"][a]["placeVisit"]["location"]["address"])
    return result

print(get_address(data))
