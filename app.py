from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities import parameters
import boto3


tracer = Tracer()
logger = Logger()
app = APIGatewayRestResolver()



# You can continue to use other utilities just as before
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
    
@app.get("/")
@tracer.capture_method
def get_hello_universe():
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('Sampl')    
  sno = app.current_event.get_query_string_value(name="sno", default_value="")
  if sno:
      response = table.get_item(Key={'sno': sno})
  else:   
      response = table.scan()
  return {'statusCode': 200,
          'result': response["Item"]
        }      
      
      
@app.put("/")
@tracer.capture_method
def get_hello_universe():
    return {"message": "hello universe - PUT"}
    
#arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPython:13  
    


