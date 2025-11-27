import dynamodbgeo
import boto3
import json


s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2') 
config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, 'geo_test_8')

def lambda_handler(event, conetxt):
    geoDataManager = dynamodbgeo.GeoDataManager(config)
    params = event.get('queryStringParameters', {})
    lat = float(params.get('lat', 0))
    lon = float(params.get('lon', 0)) 


    # 반경 500m 쿼리
    query_reduis_result=geoDataManager.queryRadius(
        dynamodbgeo.QueryRadiusRequest(
            dynamodbgeo.GeoPoint(lat, lon),
            500, sort = True)) 
            
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*"
        },
        'body': json.dumps({"result": query_reduis_result})
    }