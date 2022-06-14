from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools.utilities.validation import validate
from aws_lambda_powertools.utilities.validation.exceptions import SchemaValidationError
import boto3

from module_repo.get_function_module import get_func_detail
from module_repo.post_function_module import post_func_detail
from module_repo.put_function_module import put_func_detail
from module_repo.delete_function_module import delete_func_detail
from module_repo import schemas


tracer = Tracer()
logger = Logger()
app = APIGatewayRestResolver()


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)


@app.get("/manage_inventory")
@tracer.capture_method
def get_function():
  pid = app.current_event.get_query_string_value(name="pid", default_value="")
  response = get_func_detail(pid)
  return {'statusCode': 200,
          'result': response
        }

 

@app.post("/manage_inventory")
@tracer.capture_method
def post_function():
    payload = app.current_event.json_body
    try:
        validate(event= payload, schema=schemas.INPUT)
        response = post_func_detail(payload)
        return {'statusCode': 200,
          'result': response
        }
    except SchemaValidationError as e:
        return {'statusCode': 400,
          'failed': "Parameter missing in the request body, please check" 
        }


@app.put("/manage_inventory")
@tracer.capture_method
def put_function():
  pid = app.current_event.get_query_string_value(name="pid", default_value="")
  quantity = app.current_event.get_query_string_value(name="quantity", default_value="")
  response = put_func_detail(pid,quantity)
  return {'statusCode': 200,
          'result': response
        }
        
@app.delete("/manage_inventory")
@tracer.capture_method
def delete_function():
  pid = app.current_event.get_query_string_value(name="pid", default_value="")
  response = delete_func_detail(pid)
  return {'statusCode': 200,
          'result': response
        }