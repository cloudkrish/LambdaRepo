from aws_lambda_powertools import Logger, Tracer
import boto3

tracer = Tracer()
logger = Logger()

def post_func_detail(payload):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('stock_inventory')    
  response = table.put_item(
    Item={
        'pid' : payload["pid"],
        'brand': payload["brand"],
        'category' : payload["category"],
        'model' : payload["model"],
        'product_name' : payload["product_name"],
        'purchased_on' : payload["purchased_on"],
        'quantity' : payload["quantity"]
    }   )
  return {'success': " Data inserted to the table successfully"        }