import boto3
import json

s3 = boto3.client('s3')
BUCKET_NAME = 'photo-sharing-storage'

def lambda_handler(event, context):
    origin = 'http://photo-sharing-dima.s3-website.eu-north-1.amazonaws.com'

    # Step 1: Handle preflight request
    if event['httpMethod'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': origin,
                'Access-Control-Allow-Headers': 'Content-Type, filename',
                'Access-Control-Allow-Methods': 'POST, OPTIONS, PUT, GET'
            },
            'body': json.dumps('Preflight OK')
        }

    # Step 2: Handle actual upload
    try:
        file_content = event['body']
        file_name = event['queryStringParameters']['fileName']

        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': origin,
                'Access-Control-Allow-Headers': 'Content-Type, filename',
                'Access-Control-Allow-Methods': 'POST, OPTIONS, PUT, GET'
            },
            'body': json.dumps('File uploaded successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': origin,
                'Access-Control-Allow-Headers': 'Content-Type, filename',
                'Access-Control-Allow-Methods': 'POST, OPTIONS, PUT, GET'
            },
            'body': json.dumps('Error uploading file: ' + str(e))
        }
