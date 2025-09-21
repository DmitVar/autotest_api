from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}


data = {
    "name": "Olga",
    "age": 22
}

user_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string", "minLength": 5, "maxLength": 15}
    },
    "required": ["username"]
}

validate(instance=data, schema=schema)