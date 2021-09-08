import json
import requests
import time


def lambda_handler(event, context):
    # connect to the table
    AIRTABLE_BASE_ID = 'appYQAU5CcytTTkKs'
    AIRTABLE_NAME = 'MainTable'
    API_KEY = 'keyrT0V59Ejlc9JaH'

    #create url for connect_
    END_POINT = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_NAME}'


    # create headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # get request in json formats
    r = requests.get(END_POINT, headers=headers)

    # get data from dictionary
    z_data = r.json()['records']

    # sort data_by_id and get sorted list that contain dictionary
    sort_list = sorted(z_data, key=lambda x: x['fields']['ID'])

    # make list from sort list that contain only title field
    new_list = [(z['fields']['title']) for z in sort_list]

    # create algorithm of extraction data as circle buffer that change sequently every second
    # if we get time in second and divide on lenght of data getting remainder we will get index
    start_index = (int(time.time())) % len(new_list)
    # and index should be more on 3 as we get 3 records
    end_index = start_index + 3
    # but if we get  end index that more len of our list data make another list
    # (get end of list and extend it from start list)
    if end_index > len(new_list):
        result = new_list[start_index:end_index]
        result.extend(new_list[:end_index - len(new_list)])
    else:
        result = new_list[start_index:end_index]

    return {
        "statusCode": 200,
        "body": json.dumps(result, ensure_ascii=False)
    }
