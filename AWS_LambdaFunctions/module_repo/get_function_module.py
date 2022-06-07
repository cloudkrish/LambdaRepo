from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key


tracer = Tracer()
logger = Logger()


def get_func_detail(emp_id):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('CloudEngineers')    
  if emp_id:
      result = table.query(KeyConditionExpression=Key('emp_id').eq(emp_id))
      logger.info(result)
      if result['Items']:
         return result['Items']
      else:
         return {'message': "No rows found for given input"}
  else:   
      result = table.scan()
      return result['Items'] 