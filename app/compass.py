import json
import csv
import itertools

def save(json_data):
    # Write data to json file
    try:
        with open('map.json', 'w') as json_file:
            json.dump(json_data, json_file)
    except:
        pass

    # Convert json to csv
    try:
        with open('map.csv', 'a') as file:
            csv_writer = csv.writer(file)

            # Add headers in the csv file
            # header = ['name', 'floor', 'x', 'y', 'networks']
            # csv_writer.writerow(header)

            floors = json_data["data"]["floors"]
            for floor in floors:
                points = floor['points']
                for point in points:
                    name = point['name']
                    x = point['x']
                    y = point['y']
                    network = point['network']

                    row = list((name, floor['name'], x, y, network))
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
            'whitelist': [],
            'floors': [
                {
                    'name': 'F1',
                    'points': [
        
                    ]
                }
            ]
        }

def load_csv():
    try:
        data = []
        with open('map.csv') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
        
            # for row in csv_data:
            #     data.extend(row)
            #     data.append('\n')

            data = list(csv_data) 
            
        #return ','.join(data)
        return list(itertools.chain.from_iterable(data))
    except:
        return ""