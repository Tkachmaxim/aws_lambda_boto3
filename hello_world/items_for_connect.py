import requests
import json

# https://airtable.com/shrp5Xhe3bkzWkkhz/tblX1jGmYZoqyHrlE
AIRTABLE_BASE_ID = 'shrp5Xhe3bkzWkkhz'
AIRTABLE_NAME = 'MainTable'
API_KEY = 'keylMkRVCV25NxOBl'


# create url for connect
END_POINT = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_NAME}'

# create headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# get request in json formats
params=()
r = requests.get(END_POINT, params=params, headers=headers)

