INPUT= {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "pid": {
      "type": "string"
    },
    "brand": {
      "type": "string"
    },
    "category": {
      "type": "string"
    },
    "model": {
      "type": "string"
    },
    "product_name": {
      "type": "string"
    },
    "purchased_on": {
      "type": "string"
    },
    "quantity": {
      "type": "integer"
    }
  },
  "required": [
    "pid",
    "brand",
    "category",
    "model",
    "product_name",
    "purchased_on",
    "quantity"
  ]
}