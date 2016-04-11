import json


def read_geojson(input_file):

    with open(input_file, 'r') as f:
        gj = json.load(f)

    return gj

