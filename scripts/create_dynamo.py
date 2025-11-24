import boto3
import dynamodbgeo
import uuid

dynamodb = boto3.client('dynamodb', region_name='ap-northeast-2')
config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, 'geo_test_8')
geoDataManager = dynamodbgeo.GeoDataManager(config)

# Pick a hashKeyLength appropriate to your usage
config.hashKeyLength = 6

# Use GeoTableUtil to help construct a CreateTableInput.
table_util = dynamodbgeo.GeoTableUtil(config)
create_table_input=table_util.getCreateTableRequest()

#tweaking the base table parameters as a dict
create_table_input["ProvisionedThroughput"]['ReadCapacityUnits']=5

# Use GeoTableUtil to create the table
table_util.create_table(create_table_input)