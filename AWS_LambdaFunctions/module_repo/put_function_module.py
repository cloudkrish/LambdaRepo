from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

tracer = Tracer()
logger = Logger()


def put_func_detail(emp_id):
  if emp_id: 
     dynamodb = boto3.resource('dynamodb')
     table = dynamodb.Table('CloudEngineers') 
     valid = table.query(KeyConditionExpression=Key('emp_id').eq(emp_id))
     if valid['Items']:
        response = table.update_item(
        Key={
        'emp_id': emp_id
        },
        UpdateExpression="SET csp = :newcsp",
        ExpressionAttributeValues={
        ':newcsp': "aws"
        }    )
        return {'success': "Data Updated succeffuly for the given item"}
     else:
        return {'message': "No rows found for given input"} 
         
  else:
     return {'message': "No 'emp_id' parameter provided"}