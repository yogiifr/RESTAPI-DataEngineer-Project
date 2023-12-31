# Importing the requests Library
import requests

# Setting the Base URL and Endpoint
baseurl     = 'https://rickandmortyapi.com/api/'
endpoint    = 'location'

# Extracts the total number of pages
def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()

# Extracts the total number of pages
def get_pages(response):
    return response['info']['pages']

# Extracts relevant information about each location
def parse_json(response):
    location_list = []
    for item in response['results']:
        location = {
            'id'            : item['id'],
            'name'          : item['name'],
            'type'          : item['type'],
            'dimension'     : item['dimension'],
            'no_resident'   : len(item['residents']),
        }
        location_list.append(location)
    return location_list

# Getting the First Page
data        = main_request(baseurl, endpoint, 1)

# Loop iterates through all pages
mainlist = []
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))

# Convert to Dataframe
import pandas as pd
df = pd.DataFrame(mainlist)

# Extract to csv
df.to_csv('rickandmortylocations.csv', index=False)




