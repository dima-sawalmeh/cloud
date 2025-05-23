import base64
import boto3

s3 = boto3.client('s3')
BUCKET_NAME = 'photo-sharing-storage'

def lambda_handler(event, context):
    filename = event['queryStringParameters']['filename']
    response = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
    content = response['Body'].read()

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type, filename',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            'Content-Type': 'application/octet-stream'
        },
        'body': base64.b64encode(content).decode('utf-8'),
        'isBase64Encoded': True
    }
