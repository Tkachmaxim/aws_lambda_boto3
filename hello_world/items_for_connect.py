AIRTABLE_BASE_ID = 'appYQAU5CcytTTkKs'
AIRTABLE_NAME = 'MainTable'
API_KEY = 'keyrT0V59Ejlc9JaH'

# create url for connect
END_POINT = f'https://airtable.com/shrp5Xhe3bkzWkkhz/tblX1jGmYZoqyHrlE'

# create headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# get request in json formats
r = requests.get(END_POINT, headers=headers)