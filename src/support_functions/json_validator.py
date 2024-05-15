import json
import jsonschema
from jsonschema import validate

### Just an example --> Has to be checked and understood as it was generated from ChatGPT
chat_gpt_schema_no_annotations = {
    "type": "object",
    "properties": {
        "relatedStories": {
            "type": "array",
            "items": {
                "type": "integer"
            }
        },
        "redundantMainPart": {
            "type": "boolean"
        },
        "mainPartRedundancies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "reasonDescribtion": {
                        "type": "string"
                    },
                    "referenceToOriginalText": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            }
        },
        "redundantBenefit": {
            "type": "boolean"
        },
        "benefitRedundancies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "reasonDescribtion": {
                        "type": "string"
                    },
                    "referenceToOriginalText": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    },
    "required": [
        "relatedStories",
        "redundantMainPart",
        "mainPartRedundancies",
        "redundantBenefit",
        "benefitRedundancies"
    ]
}


### Just an example --> Has to be changed
chat_gpt_schema_with_annotations = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"},
    },
}


def validation(json_data: str, current_schema: dict) -> bool:
    try:
        validate(instance=json_data, schema=current_schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


def validate_chat_gpt_json_no_annotations(json_data: str) -> bool:
    return validation(json_data, chat_gpt_schema_no_annotations)

def validate_chat_gpt_json_with_annotations(json_data: str) -> bool:
    return validation(json_data, chat_gpt_schema_with_annotations)


d = '''{
        "relatedStories": [
            315,
            316
        ],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }'''
print(validate_chat_gpt_json_no_annotations(d))