import json
import csv


def save(json_data):
    # Write data to json file
    try:
        with open('map.json', 'w') as json_file:
            json.dump(json_data, json_file)
    except:
        pass

    # Convert json to csv
    try:
        with open('map.csv', 'w') as file:
            csv_writer = csv.writer(file)

            # Add headers in the csv file
            header = ['floor', 'x', 'y', 'networks']
            csv_writer.writerow(header)

            for floor in json_data:
                for point in json_data[floor]['points']:
                    x = point['x']
                    y = point['y']
                    networks = point['networks']

                    row = list((floor, x, y, networks))
                    csv_writer.writerow(row)
    except:
        pass


def load():
    try:
        with open('map.json') as json_file:
            json_data = json.load(json_file)

        return json_data
    except:
        return {
            'floors': [
                {
                    'name': 'F1',
                    'points': [

                    ]
                }
            ]
        }
