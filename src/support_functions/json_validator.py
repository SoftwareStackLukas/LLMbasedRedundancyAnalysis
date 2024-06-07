import json
import jsonschema
from jsonschema import validate

### Needs validation
chat_gpt_schema_no_annotations =  {
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

# Check if the uniqueItems constrain is correct here
# Consider extra checks for the unique keyword
chat_gpt_schema_with_annotations = {
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
        "mainPartRedundancies": {
            "type": "object",
            "properties": {
                "partialRedundancy": {
                    "type": "boolean"
                },
                "fullRedundancy": {
                    "type": "boolean"
                },
                "pairsOfTriggersRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "descriptionOfTriggerPairRedundancies": {
                                "type": "string",
                                "minLength": 1
                            },
                            "FirstUserStoryTriggerPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            },
                            "SecondUserStoryTriggerPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            }
                        },
                        "required": ["descriptionOfTriggerPairRedundancies",
                                     "FirstUserStoryTriggerPair",
                                     "SecondUserStoryTriggerPair"]
                    },
                    "minItems": 0,
                    "uniqueItems": True
                },
                "pairsOfTargetsRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "descriptionOfTargetPairRedundancies": {
                                "type": "string",
                                "minLength": 1
                            },
                            "FirstUserStoryTargetPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            },
                            "SecondUserStoryTargetPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            }
                        },
                        "required": ["descriptionOfTargetPairRedundancies",
                                     "FirstUserStoryTargetPair",
                                     "SecondUserStoryTargetPair"]
                    },
                    "minItems": 0,
                    "uniqueItems": True
                },
                "pairsOfContainsRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "descriptionOfContainPairsRedundancies": {
                                "type": "string",
                                "minLength": 1
                            },
                            "FirstUserStoryContainPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            },
                            "SecondUserStoryContainPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            }
                        },
                        "required": ["descriptionOfContainPairRedundancies",
                                     "FirstUserStoryContainPair",
                                     "SecondUserStoryContainPair"]
                    },
                    "minItems": 0,
                    "uniqueItems": True
                }
            },
            "required": [
                "partialRedundancy",
                "fullRedundancy",
                "pairsOfTargetsRedundancies",
                "pairsOfTriggersRedundancies",
                "pairsOfContainsRedundancies"],
            "allOf": [
                {
                    "if": {
                        "properties": {
                            "partialRedundancy": {
                                "const": False
                            },
                            "fullRedundancy": {
                                "const": False
                            }
                        }
                    },
                    "then": {
                        "properties": {
                            "pairsOfTriggersRedundancies": {
                                "maxItems": 0
                            },
                            "pairsOfTargetsRedundancies": {
                                "maxItems": 0
                            },
                            "pairsOfContainsRedundancies": {
                                "maxItems": 0
                            }
                        }
                    }
                },
                {
                    "if": {
                        "properties": {
                            "partialRedundancy": {
                                "const": True
                            }
                        }
                    },
                    "then": {
                        "not": {
                            "properties": {
                                "fullRedundancy": {
                                    "const": True
                                }
                            }
                        }
                    },
                    "else": {
                        "if": {
                            "properties": {
                                "fullRedundancy": {
                                    "const": True
                                }
                            }
                        },
                        "then": {
                            "not": {
                                "properties": {
                                    "partialRedundancy": {
                                        "const": True
                                    }
                                }
                            }
                        },
                    }
                },
                {
                    "if": {
                            "properties": {
                                "fullRedundancy": {
                                    "const": True
                                }
                            }
                        },
                    "then": {
                        "properties": {
                            "pairsOfTriggersRedundancies": {
                                "minItems": 1
                            },
                            "pairsOfTargetsRedundancies": {
                                "minItems": 1
                            },
                            "pairsOfContainsRedundancies": {
                                "minItems": 1
                            }
                        }
                    },
                    "else": {
                        "if": {
                            "properties": {
                                "partialRedundancy": {
                                    "const": True
                                }
                            }
                        },
                        "then": {
                            "properties": {
                                "pairsOfTargetsRedundancies": {
                                    "minItems": 1
                                },
                            }
                        },
                    }
                },
                
            ],
        },
        "benefitRedundancies": {
            "type": "object",
            "properties": {
                "partialRedundancy": {
                    "type": "boolean"
                },
                "fullRedundancy": {
                    "type": "boolean"
                },
                "pairsOfTriggersRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "descriptionOfTriggerPairRedundancies": {
                                "type": "string",
                                "minLength": 1
                            },
                            "FirstUserStoryTriggerPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            },
                            "SecondUserStoryTriggerPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            }
                        },
                        "required": ["descriptionOfTriggerPairRedundancies",
                                     "FirstUserStoryTriggerPair",
                                     "SecondUserStoryTriggerPair"]
                    },
                    "minItems": 0,
                    "uniqueItems": True
                },
                "pairsOfTargetsRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "descriptionOfTargetPairRedundancies": {
                                "type": "string",
                                "minLength": 1
                            },
                            "FirstUserStoryTargetPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            },
                            "SecondUserStoryTargetPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            }
                        },
                        "required": ["descriptionOfTargetPairRedundancies",
                                     "FirstUserStoryTargetPair",
                                     "SecondUserStoryTargetPair"]
                    },
                    "minItems": 0,
                    "uniqueItems": True
                },
                "pairsOfContainsRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "descriptionOfContainPairsRedundancies": {
                                "type": "string",
                                "minLength": 1
                            },
                            "FirstUserStoryContainPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            },
                            "SecondUserStoryContainPair": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "minItems": 2,
                                "maxItems": 2
                            }
                        },
                        "required": ["descriptionOfContainPairRedundancies",
                                     "FirstUserStoryContainPair",
                                     "SecondUserStoryContainPair"]
                    },
                    "minItems": 0,
                    "uniqueItems": True
                }
            },
            "required": [
                "partialRedundancy",
                "fullRedundancy",
                "pairsOfTargetsRedundancies",
                "pairsOfTriggersRedundancies",
                "pairsOfContainsRedundancies"],
            "allOf": [
                {
                    "if": {
                        "properties": {
                            "partialRedundancy": {
                                "const": False
                            },
                            "fullRedundancy": {
                                "const": False
                            }
                        }
                    },
                    "then": {
                        "properties": {
                            "pairsOfTriggersRedundancies": {
                                "maxItems": 0
                            },
                            "pairsOfTargetsRedundancies": {
                                "maxItems": 0
                            },
                            "pairsOfContainsRedundancies": {
                                "maxItems": 0
                            }
                        }
                    }
                },
                {
                    "if": {
                        "properties": {
                            "partialRedundancy": {
                                "const": True
                            }
                        }
                    },
                    "then": {
                        "not": {
                            "properties": {
                                "fullRedundancy": {
                                    "const": True
                                }
                            }
                        }
                    },
                    "else": {
                        "if": {
                            "properties": {
                                "fullRedundancy": {
                                    "const": True
                                }
                            }
                        },
                        "then": {
                            "not": {
                                "properties": {
                                    "partialRedundancy": {
                                        "const": True
                                    }
                                }
                            }
                        },
                    }
                },
                {
                    "if": {
                            "properties": {
                                "fullRedundancy": {
                                    "const": True
                                }
                            }
                        },
                    "then": {
                        "properties": {
                            "pairsOfTriggersRedundancies": {
                                "minItems": 1
                            },
                            "pairsOfTargetsRedundancies": {
                                "minItems": 1
                            },
                            "pairsOfContainsRedundancies": {
                                "minItems": 1
                            }
                        }
                    },
                    "else": {
                        "if": {
                            "properties": {
                                "partialRedundancy": {
                                    "const": True
                                }
                            }
                        },
                        "then": {
                            "properties": {
                                "pairsOfTargetsRedundancies": {
                                    "minItems": 1
                                },
                            }
                        },
                    }
                },
                
            ],
        }
    },
    "required": [
            "relatedStories",
            "mainPartRedundancies",
            "benefitRedundancies"]
}

# JSON validation is based on this specifications: https://json-schema.org/specification
def validation(json_data: str, current_schema: dict) -> tuple[bool, str]:
    """
    Validates a JSON object against a provided JSON schema.

    This function attempts to validate the given JSON data against the specified schema.
    If the validation fails, it catches the `ValidationError` and constructs a detailed error message,
    including information about the validation failure and any sub-errors that occurred.

    Parameters
    ----------
    json_data : str
        The JSON data to be validated, represented as a string.
    current_schema : dict
        The JSON schema to validate against, represented as a dictionary.

    Returns
    -------
    tuple[bool, str]
        A tuple containing:
        - A boolean indicating whether the JSON data is valid (True if valid, False otherwise).
        - A string containing the error message if the validation fails, or an empty string if the validation is successful.
    """
    try:
        validate(instance=json_data, schema=current_schema)
    except jsonschema.exceptions.ValidationError as e:
        error_message = (
            f"Message: {e.message}, "
            f"Validator: {e.validator}, "
            f"Validator Value: {e.validator_value}, "
            f"Schema: {e.schema}, "
            f"Relative Schema Path: {list(e.relative_schema_path)}, "
            f"Absolute Schema Path: {list(e.absolute_schema_path)}"
        )
        
        # If there are sub-errors, add their details as well
        if e.context:
            error_message += "Suberrors:\n"
            for suberror in sorted(e.context, key=lambda sub: list(sub.schema_path)):
                error_message += (
                    f"  Path: {list(suberror.schema_path)}\n"
                    f"  Message: {suberror.message}\n"
                )
        return False, f"The schema and error is: Schema: {current_schema} and Error-Content: {error_message}"
    return True, ""