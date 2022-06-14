from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key


tracer = Tracer()
logger = Logger()


def delete_func_detail(pid):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('stock_inventory')
  if pid:
      result = table.delete_item(Key = {'pid': pid})
      return {'success': "Specific row was deleted based on provided input"}
  else:   
      return {'message': "'emp_id' parameter missing to perform delete operation"}