from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key


tracer = Tracer()
logger = Logger()


def delete_func_detail(emp_id):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('CloudEngineers')
  if emp_id:
      result = table.delete_item(Key = {'emp_id': emp_id})
      return {'success': "Specific row was deleted based on provided input"}
  else:   
      return {'message': "'emp_id' parameter missing to perform delete operation"}