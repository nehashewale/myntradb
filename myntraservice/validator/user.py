from jsonschema import validate


schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "first_name": {"type": "string"},
    "middle_name": {"type": "string"},
    "last_name": { "type": "string"},
    "phone_number": {"type": "integer"},
    "gender": {"type": "string"},
    "primary_address": {
      "type": "object",
      "properties": {
        "village": {"type": "string"},
        "landmark": {"type": "string"},
        "taluka": { "type": "string"},
        "district": {"type": "string" },
        "state": {"type": "string"},
        "pincode": {"type": "integer" }
      },
      "required": [
        "village","landmark","taluka","district", "state", "pincode"
      ]
    },
    "shipping_address": {
      "type": "object",
      "properties": {
        "village": {"type": "string"},
        "landmark": {"type": "string"},
        "taluka": { "type": "string"},
        "district": {"type": "string" },
        "state": {"type": "string"},
        "pincode": {"type": "integer" }
      },
      "required": [
        "village","landmark","taluka","district", "state", "pincode"
      ]
    }
  }
}

def validate_user(payload):
    try:
        validate(payload,schema)
        return True
    except:
        return False