INPUT = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "emp_id": {
      "type": "string"
    },
    "csp": {
      "type": "string"
    },
    "designation": {
      "type": "string"
    },
    "location": {
      "type": "string"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "emp_id",
    "csp",
    "designation",
    "location",
    "name"
  ]
}