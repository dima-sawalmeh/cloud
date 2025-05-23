import boto3
import json

s3 = boto3.client('s3')
BUCKET_NAME = 'photo-sharing-storage'

def lambda_handler(event, context):
    try:
        file_content = event['body']
        file_name = event['queryStringParameters']['fileName']

        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': 'http://photo-sharing-dima.s3-website.eu-north-1.amazonaws.com',
                'Access-Control-Allow-Headers': 'content-type, filename',
                'Access-Control-Allow-Methods': 'POST, OPTIONS, PUT, GET'
            },
            'body': json.dumps('File uploaded successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': 'http://photo-sharing-dima.s3-website.eu-north-1.amazonaws.com',
                'Access-Control-Allow-Headers': 'content-type, filename',
                'Access-Control-Allow-Methods': 'POST, OPTIONS, PUT, GET'
            },
            'body': json.dumps('Error uploading file: ' + str(e))
        }
