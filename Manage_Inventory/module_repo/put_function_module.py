from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

tracer = Tracer()
logger = Logger()


def put_func_detail(pid,quantity):
  if pid: 
     dynamodb = boto3.resource('dynamodb')
     table = dynamodb.Table('stock_inventory') 
     valid = table.query(KeyConditionExpression=Key('pid').eq(pid))
     if valid['Items']:
        response = table.update_item(
        Key={
        'pid': pid
        },
        UpdateExpression="SET quantity = :newquantity",
        ExpressionAttributeValues={
        ':newquantity': quantity
        }    )
        return {'success': "Data Updated succeffuly for the given item"}
     else:
        return {'message': "No rows found for given input"} 
         
  else:
     return {'message': "No 'emp_id' parameter provided"}