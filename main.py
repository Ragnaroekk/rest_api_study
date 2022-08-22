# From https://realpython.com/python-api/
# Just some simple code to practice api requests in python

import requests, os
from random import randint
from datetime import date

# retrieve the api key
key = os.environ.get("nasa_api")

def save_photo(response, file_extension):
    '''Creates a new image file from a response and 
    appends the file extension to the file name'''
    file = open("".join(["nasa_photo#", str(num)," ", str(query_params["earth_date"]), file_extension]), "wb")
    file.write(response.content)
    file.close()

def get_request(endpoint, params):
    '''send a basic get request and returns the response'''
    return requests.get(endpoint, params=query_params)

# make the initial request with today's date
headers = {"api_key": key}
query_params = {"api_key": key, "earth_date": date.today().strftime("%Y-%m-%d")}
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
response = get_request(endpoint, params=query_params)

# request the random photo from the response
result = response.json()["photos"]
num = randint(0, len(result) - 1)
endpoint = result[num]["img_src"]
response = get_request(endpoint, params=query_params)

# Save the file with correct extension
if response.headers.get("Content-Type") == "image/jpeg":
    save_photo(response, ".jpeg")
elif response.headers.get("Content-Type") == "image/png":
    save_photo(response, ".png")


