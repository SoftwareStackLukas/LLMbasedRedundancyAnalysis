import json
import jsonschema
from jsonschema import validate

### Needs validation
chat_gpt_schema_no_annotations = chat_gpt_schema_no_annotations = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "relatedStories": {
            "type": "array",
            "items": {
                "type": "integer"
            },
            "minItems": 2,
            "maxItems": 2
        },
        "redundantMainPart": {
            "type": "boolean"
        },
        "mainPartRedundancies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "reasonDescription": {
                        "type": "string"
                    },
                    "referenceToOriginalText": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    }
                },
                "required": ["reasonDescription", "referenceToOriginalText"]
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
                    "reasonDescription": {
                        "type": "string"
                    },
                    "referenceToOriginalText": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    }
                },
                "required": ["reasonDescription", "referenceToOriginalText"]
            }
        }
    },
    "required": [
        "relatedStories",
        "redundantMainPart",
        "mainPartRedundancies",
        "redundantBenefit",
        "benefitRedundancies"
    ],
    "allOf": [
        {
            "if": {
                "properties": {
                    "redundantMainPart": {
                        "const": True
                    }
                }
            },
            "then": {
                "properties": {
                    "mainPartRedundancies": {
                        "minItems": 1
                    }
                }
            }
        },
        {
            "if": {
                "properties": {
                    "redundantBenefit": {
                        "const": True
                    }
                }
            },
            "then": {
                "properties": {
                    "benefitRedundancies": {
                        "minItems": 1
                    }
                }
            }
        }
    ]
}

### Just an example --> Has to be changed
# chat_gpt_schema_with_annotations = {
#     "type": "object",
#     "properties": {
#         "name": {"type": "string"},
#         "rollnumber": {"type": "number"},
#         "marks": {"type": "number"},
#     },
# }

# JSON validation is based on this specifications: https://json-schema.org/specification
def validation(json_data: str, current_schema: dict) -> bool:
    try:
        validate(instance=json_data, schema=current_schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


test_data1 = '''
    {
        "relatedStories": [
            315,
            316
        ],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data1), chat_gpt_schema_no_annotations))
print("Should be: true")
print("-" * 10)

test_data2 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": true,
        "mainPartRedundancies": [
            {
                "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
                "referenceToOriginalText": [
                    "As a Staff member, I want to Assign an Application for Detailed Review",
                    "As a Plan Review Staff member, I want to Review Plans"
                ]
            }
        ],
        "redundantBenefit": true,
        "benefitRedundancies": [
            {
                "reasonDescription": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
                "referenceToOriginalText": [
                    "so that I can review the for compliance and subsequently approved or denied",
                    "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
                ]
            }
        ]
    }
'''
print(validation(json.loads(test_data2), chat_gpt_schema_no_annotations))
print("Should be: true")
print("-" * 10)

test_data3 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": true,
        "benefitRedundancies": [
            {
                "reasonDescription": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
                "referenceToOriginalText": [
                    "so that I can review the for compliance and subsequently approved or denied",
                    "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
                ]
            }
        ]
    }
'''
print(validation(json.loads(test_data3), chat_gpt_schema_no_annotations))
print("Should be: true")
print("-" * 10)

test_data4 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": true,
        "mainPartRedundancies": [
            {
                "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
                "referenceToOriginalText": [
                    "As a Staff member, I want to Assign an Application for Detailed Review",
                    "As a Plan Review Staff member, I want to Review Plans"
                ]
            }
        ],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data4), chat_gpt_schema_no_annotations))
print("Should be: true")
print("-" * 10)


test_data5 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": true,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": [
            {
                "reasonDescription": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
                "referenceToOriginalText": [
                    "so that I can review the for compliance and subsequently approved or denied",
                    "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
                ]
            }
        ]
    }
'''
print(validation(json.loads(test_data5), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data6 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": false,
        "mainPartRedundancies": [
            {
                "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
                "referenceToOriginalText": [
                    "As a Staff member, I want to Assign an Application for Detailed Review",
                    "As a Plan Review Staff member, I want to Review Plans"
                ]
            }
        ],
        "redundantBenefit": true,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data6), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data7 = '''
    {
        "relatedStories": [],
        "redundantMainPart": true,
        "mainPartRedundancies": [
            {
                "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
                "referenceToOriginalText": [
                    "As a Staff member, I want to Assign an Application for Detailed Review",
                    "As a Plan Review Staff member, I want to Review Plans"
                ]
            }
        ],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data7), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data8 = '''
    {
        "relatedStories": [],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data8), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data9 = '''
    {
        "relatedStories": [111],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data9), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data10 = '''
    {
        "relatedStories": [ ,111],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
try: 
    print(validation(json.loads(test_data10), chat_gpt_schema_no_annotations))
    print("true")
except:
    print("false")

test_data11 = '''
    {
        "relatedStories": [453,111],
        "redundantMainPart": true,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data9), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data12 = '''
    {
        "relatedStories": [453,111],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": true,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data12), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)


test_data13 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": true,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": [
            {
                "reasonDescription": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
                "referenceToOriginalText": [
                    "so that I can review the for compliance and subsequently approved or denied"
                ]
            }
        ]
    }
'''
print(validation(json.loads(test_data13), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data13 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": true,
        "mainPartRedundancies": [
            {
                "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
                "referenceToOriginalText": [
                    "As a Staff member, I want to Assign an Application for Detailed Review"
                ]
            }
        ],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data13), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data14 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": true,
        "benefitRedundancies": [
            {
                "referenceToOriginalText": [
                    "so that I can review the for compliance and subsequently approved or denied",
                    "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
                ]
            }
        ]
    }
'''
print(validation(json.loads(test_data5), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data15 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": true,
        "mainPartRedundancies": [
            {
                "referenceToOriginalText": [
                    "As a Staff member, I want to Assign an Application for Detailed Review",
                    "As a Plan Review Staff member, I want to Review Plans"
                ]
            }
        ],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data6), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data16 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": true,
        "benefitRedundancies": [
            {
                "reasonDescription": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
            }
        ]
    }
'''
print(validation(json.loads(test_data5), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)

test_data17 = '''
    {
        "relatedStories": [
            326,
            353
        ],
        "redundantMainPart": true,
        "mainPartRedundancies": [
            {
                "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
        ],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
'''
print(validation(json.loads(test_data6), chat_gpt_schema_no_annotations))
print("Should be: false")
print("-" * 10)