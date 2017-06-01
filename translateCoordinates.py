import os
import json
import time
import datetime

def __main__():
    f = open('coordinates.txt')

    features = []
    for line in f:
        obj = {
        "type": "Feature",
        "geometry":{
          "type": "Point"
        },
        "properties": {
                "icon": "circle"
            }
        }
        # print line.split('=')
        if len(line.split('=')) == 1:
            continue


        obj["geometry"]["coordinates"] = [
            line.split('=')[1].split(',')[1].strip(),
            line.split('=')[1].split(',')[0].strip()
        ]

        features.append(obj)

    outf = open('sewerCoordinates.geojson', 'w')

    outf.write('{\n')
    outf.write('"type": "FeatureCollection",\n')
    outf.write('"features": [\n')
    for item in features:
        outf.write('{},\n'.format(json.dumps(item, indent=4)))
    outf.write(']\n}')

__main__()
