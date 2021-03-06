import json
import time
import datetime
import requests
import os
import boto3


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
    # before getting index make 5 sec pause for correct data
    time.sleep(5)
    # get index from logs event
    client = boto3.client('logs')
    stream_response = client.describe_log_streams(
        logGroupName="/aws/lambda/sam-hello-world-HelloWorldFunction-YhDOKxjYdMDy",  # Can be dynamic]
        orderBy='LastEventTime',  # For the latest events
        limit=50
    )
    name_of_logs = stream_response['logStreams'][-1:][0]['logStreamName']

    response = client.get_log_events(
        logGroupName="/aws/lambda/sam-hello-world-HelloWorldFunction-YhDOKxjYdMDy",
        logStreamName=f'{name_of_logs}'
    )
    start_index = int((len(response['events']) / 4))
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



