import sys
import json
import csv

json_input = json.load(sys.stdin)
csv_output = csv.writer(sys.stdout)

csv_output.writerow(['Library', 'URL', 'License'])

for package_name, data in json_input.items():
    name = package_name.split('@')[0]

    url = ''
    if 'homepage' in data:
        if type(data['homepage']) is str:
            url = data['homepage']
    elif 'repository' in data:
        if type(data['repository']) is str:
            url = data['repository']
        elif type(data['repository']) is dict:
            url = data['repository']['url']

    csv_output.writerow([name, url, ';'.join(data['licenses'])])
