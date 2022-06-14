from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key


tracer = Tracer()
logger = Logger()


def get_func_detail(pid):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('stock_inventory')    
  if pid:
      result = table.query(KeyConditionExpression=Key('pid').eq(pid))
      logger.info(result)
      if result['Items']:
         return result['Items']
      else:
         return {'message': "No rows found for given input"}
  else:   
      result = table.scan()
      return result['Items'] 