# Rick and Morty API

## Project Description
This project involves working with the Rick and Morty API using Python. The goal is to extract and organize data from the API, demonstrating the basics of making API requests, handling JSON responses, and exporting data to a CSV file.

## Steps
1. **Importing the requests Library:** 
```python
# Importing the requests Library
import requests
```
This step imports the requests library, which is commonly used in Python for making HTTP requests, including API requests.

2. **Setting the Base URL and Endpoint:** 
```python
# Setting the Base URL and Endpoint
baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'location'
```
These lines set the base URL and endpoint for the Rick and Morty API. In this case, the base URL is 'https://rickandmortyapi.com/api/' and the endpoint is 'location'.

3. **Defining the Main Request Function:** 
```python
# Extracts the total number of pages
def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()
```
This function, `main_request`, takes the base URL, endpoint, and page number (`x`) as parameters. It makes a GET request to the API with the specified page number and returns the JSON response.

4. **Defining the get_pages Function:** 
```python
# Extracts the total number of pages
def get_pages(response):
    return response['info']['pages']
```
This function, `get_pages`, takes the API response as input and extracts the total number of pages from the 'info' key in the response JSON.

5. **Defining the `parse_json` Function:** 
```python
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
```
This function, `parse_json`, takes the API response as input and extracts relevant information about each location from the 'results' key in the response JSON. It creates a list of dictionaries containing location details.

6. **Getting the First Page:** 
```python
# Getting the First Page
data = main_request(baseurl, endpoint, 1)
```
This line makes an API request to get the data for the first page using the `main_request` function and stores the response in the variable `data`.

7. **Looping Through All Pages and Parsing Data:** 
```python
# Loop iterates through all pages
mainlist = []
for x in range(1, get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))
```
This loop iterates through all pages (from 1 to the total number of pages) and calls the `parse_json` function for each page using the `main_request` function. It prints the page number and extends the `mainlist` with the parsed data.

8. **Convert to DataFrame:** 
```python
# Convert to DataFrame
import pandas as pd
df = pd.DataFrame(mainlist)
```
These lines use the Pandas library to convert the list of dictionaries (`mainlist`) into a Pandas DataFrame, which is a tabular data structure in Python.

9. **Extract to CSV:** 
```python
# Extract to csv
df.to_csv('rickandmortylocations.csv', index=False)
```
This line exports the Pandas DataFrame to a CSV file named `'rickandmortylocations.csv'` without including the index column.

## Lessons Learned
- Understanding the basics of making API requests in Python
- Extracting data from JSON responses and navigating through nested structures.
- Handling pagination in API responses for comprehensive data retrieval.
- Exporting data to CSV files using Pandas in Python.

## Video Reference
For a visual guide and additional insights, you can refer to the following video:

**Title:** Youtube API for Python: How to Create a Unique Data Portfolio Project

**Link:** [Watch Video](https://www.youtube.com/watch?v=D56_Cx36oGY&t=630s)
