"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    try:
        check = open(neo_csv_path, 'r').read()
    except:
        while check != neo_csv_path:
            print("File couldn't be found or opened")
    else:
        with open(neo_csv_path, 'r') as f:
            data_csv = []
            reader = csv.DictReader(f) #need the header line
            for row in reader:
                if not row['name']:
                    row['name'] = None
                if not row['diameter']:
                    row['diameter'] = None #created huge amount of errors in the unit test by not checking for empty spaces in the csv
                        
                new_neo = NearEarthObject(row['pdes'], row['name'], row['neo'], row['pha'], row['diameter'])
                data_csv.append(new_neo)
        f.close()
    return data_csv


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    try:
        check = open(cad_json_path, 'r').read()
    except:
        while check != cad_json_path:
            print("File couldn't be found or opened")
    else:
        with open(cad_json_path, 'r') as f:
            data_json = []
            reader = json.load(f)
            intermediate_data = reader['data']
            for row in intermediate_data:
                new_close_approach = CloseApproach(row[0], row[3], row[4], row[7])
                data_json.append(new_close_approach)
        f.close()
    # TODO: Load alle close approaches from the file
    return data_json 
