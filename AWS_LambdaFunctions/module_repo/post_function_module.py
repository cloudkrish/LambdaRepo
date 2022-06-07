from aws_lambda_powertools import Logger, Tracer
import boto3

tracer = Tracer()
logger = Logger()

def post_func_detail(payload):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('CloudEngineers')    
  response = table.put_item(
    Item={
        'emp_id' : payload["emp_id"],
        'csp': payload["csp"],
        'designation' : payload["designation"],
        'location' : payload["location"],
        'name' : payload["name"]
    }   )
  return {'success': " Data inserted to the table successfully"        }