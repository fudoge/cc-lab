import json
import boto3
import uuid
import dynamodbgeo
import csv
import io

s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2') 
config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, 'geo_test_8')

def lambda_handler(event, context):
    # create connection
    geoDataManager = dynamodbgeo.GeoDataManager(config)
    
    # get s3 info
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    
    obj = s3.get_object(Bucket=bucket, Key=key)
    body = obj['Body'].read().decode('utf-8')
    
    csv_reader = csv.DictReader(io.StringIO(body))
    
    for row in csv_reader:
        name = row.get("restroom_name", "")
        phone = row.get("phone_number", "")
        open_time = row.get("open_time", "")
        lat = row.get("latitude", "")
        lon = row.get("longitude", "")
        
        item_data = {
            "restroomName": {"S": name},
            "phoneNumber": {"S": phone},
            "openTime": {"S": open_time}
        }
        
        PutItemInput = {
            'Item': { **item_data },
            'ConditionExpression': "attribute_not_exists(hashKey)"
        }
        
        # GeoData Insert
        geoDataManager.put_Point(
            dynamodbgeo.PutPointInput(
                dynamodbgeo.GeoPoint(float(lat), float(lon)),
                str(uuid.uuid4()),
                PutItemInput
            )
        )
        
    
    return {"status": "done"}
    

    