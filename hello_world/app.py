import json
import requests

# import requests


def lambda_handler(event, context):
    AIRTABLE_BASE_ID = 'appYQAU5CcytTTkKs'
    AIRTABLE_NAME = 'MainTable'
    API_KEY = 'keyrT0V59Ejlc9JaH'
    END_POINT = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_NAME}'

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "records": [
            {
                "fields": {
                    "ID": 1,
                    "title": "Проверка 1"
                }
            },
            {
                "fields": {
                    "ID": 2,
                    "title": "Проверка 2"
                }
            }
        ]
    }

    r = requests.get(END_POINT, json=data, headers=headers)
    z_data = r.json()['records']
    new_list = sorted(z_data, key=lambda x: x['fields']['ID'])
    result = ((z['fields'])['title'] for z in new_list)


    return {
        "statusCode": 200,
        "body": json.dumps(
            result.__next__()
    ),
    }
