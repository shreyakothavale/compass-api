import json
import csv

def upload(json_data):
    try:
        # Write into json file
        with open('map.json', 'w') as json_file:
            json.dump(json_data, json_file)

    except:       
        with open('map.json', 'w') as json_file:
            json.dump("{}", json_file)

    try:
        # Header field yet to test
        # Write into csv file
        with open('map.csv', 'w') as file:
            csv_writer = csv.writer(file)
            # Add header in csv file
            header = ['floor', 'x', 'y', 'network']
            csv_writer.writerow(header)

            for floor in json_data:
                for point in json_data[floor]['points']:
                    x = point['x']
                    y = point['y']
                    network = point['meta']

                    row = list((floor, x, y, network))
                    csv_writer.writerow(row)
        
    except:
        with open('map.csv', 'w') as csv_file:
            csv.writer(csv_file).writerow("")   
            
def download():
    try:
        with open('map.json') as json_file:
            json_data = json.load(json_file)

        return json_data
    except:
        return {}