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
                "describtionOfTriggersRedundancies": {
                    "type": "string"
                },
                "pairsOfTriggersRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "minItems": 0,
                },
                "descriptionOfTargetsRedundancies": {
                    "type": "string"
                },
                "pairsOfTargetsRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "minItems": 0,
                },
                "descriptionOfContainsRedundancies": {
                    "type": "string"
                },
                "pairsOfTContainesRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "minItems": 0,
                }
            },
            "required": [
                "partialRedundancy",
                "fullRedundancy",
                "descriptionOfTargetsRedundancies",
                "pairsOfTargetsRedundancies",
                "descriptionOfTriggersRedundancies",
                "pairsOfTriggersRedundancies",
                "descriptionOfContainsRedundancies",
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
                            "descriptionOfTriggersRedundancies": {
                                "const": ""
                            },
                            "pairsOfTriggersRedundancies": {
                                "maxItems": 0
                            },
                            "descriptionOfTargetsRedundancies": {
                                "const": ""
                            },
                            "pairsOfTargetsRedundancies": {
                                "maxItems": 0
                            },
                            "descriptionOfContainsRedundancies": {
                                "const": ""
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
                        "not": {
                            "properties": {
                                "partialRedundancy": {
                                    "const": True
                                }
                            }
                        }
                    },
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
                        "properties": {
                            "pairsOfTargetsRedundancies": {
                                "minItems": 1
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
                            "properties": {
                                "pairsOfTargetsRedundancies": {
                                    "minItems": 1
                                }
                            }
                        }
                    }
                },
                {
                "if": {
                    "properties": {
                    "descriptionOfTriggersRedundancies": {
                        "not": {
                            "const": ""
                        }
                    }
                    }
                },
                "then": {
                    "required": ["pairsOfTriggersRedundancies"],
                    "properties": {
                        "pairsOfTriggersRedundancies": {
                            "minItems": 1
                        }
                    }
                },
                "else": {
                    "if": {
                        "properties": {
                            "pairsOfTriggersRedundancies": {
                            "minItems": 1
                            }
                        }
                    },
                    "then": {
                        "required": ["descriptionOfTriggersRedundancies"],
                            "properties": {
                                "descriptionOfTriggersRedundancies": {
                                    "not": {
                                        "const": ""
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    "if": {
                        "properties": {
                            "descriptionOfTargetsRedundancies": {
                                "not": {
                                    "const": ""
                                }
                            }
                        }
                },
                "then": {
                    "required": ["pairsOfTargetsRedundancies"],
                    "properties": {
                        "pairsOfTargetsRedundancies": {
                            "minItems": 1
                        }
                    }
                },
                "else": {
                    "if": {
                        "properties": {
                            "pairsOfTargetsRedundancies": {
                                "minItems": 1
                            }
                        }
                    },
                    "then": {
                        "required": ["descriptionOfTargetsRedundancies"],
                            "properties": {
                                "descriptionOfTargetsRedundancies": {
                                    "not": {
                                        "const": ""
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    "if": {
                        "properties": {
                            "descriptionOfContainsRedundancies": {
                                "not": {
                                    "const": ""
                                }
                            }
                        }
                    },
                    "then": {
                        "required": ["pairsOfContainsRedundancies"],
                        "properties": {
                            "pairsOfContainsRedundancies": {
                                "minItems": 1
                            }
                        }
                    },
                "else": {
                    "if": {
                        "properties": {
                            "pairsOfContainsRedundancies": {
                            "minItems": 1
                            }
                        }
                    },
                    "then": {
                        "required": ["descriptionOfContainsRedundancies"],
                            "properties": {
                                "descriptionOfContainsRedundancies": {
                                    "not": {
                                        "const": ""
                                    }
                                }
                            }
                        }
                    }
                }
            ]
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
                "descriptionOfTriggersRedundancies": {
                    "type": "string"
                },
                "pairsOfTriggersRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "minItems": 0,
                },
                "descriptionOfTargetsRedundancies": {
                    "type": "string"
                },
                "pairsOfTargetsRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "minItems": 0,
                },
                "descriptionOfContainsRedundancies": {
                    "type": "string"
                },
                "pairsOfTContainesRedundancies": {
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "minItems": 2,
                        "maxItems": 2
                    },
                    "minItems": 0,
                }
            },
            "required": [
                "partialRedundancy",
                "fullRedundancy",
                "descriptionOfTargetsRedundancies",
                "pairsOfTargetsRedundancies",
                "descriptionOfTriggersRedundancies",
                "pairsOfTriggersRedundancies",
                "descriptionOfContainsRedundancies",
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
                            "descriptionOfTriggersRedundancies": {
                                "const": ""
                            },
                            "pairsOfTriggersRedundancies": {
                                "maxItems": 0
                            },
                            "descriptionOfTargetsRedundancies": {
                                "const": ""
                            },
                            "pairsOfTargetsRedundancies": {
                                "maxItems": 0
                            },
                            "descriptionOfContainsRedundancies": {
                                "const": ""
                            },
                            "pairsOfTContainsedundancies": {
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
                        "not": {
                            "properties": {
                                "partialRedundancy": {
                                    "const": True
                                }
                            }
                        }
                    },
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
                        "properties": {
                            "pairsOfTargetsRedundancies": {
                                "minItems": 1
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
                            "properties": {
                                "pairsOfTargetsRedundancies": {
                                    "minItems": 1
                                }
                            }
                        }
                    }
                },
                {
                "if": {
                    "properties": {
                    "descriptionOfTriggersRedundancies": {
                        "not": {
                            "const": ""
                        }
                    }
                    }
                },
                "then": {
                    "required": ["pairsOfTriggersRedundancies"],
                    "properties": {
                        "pairsOfTriggersRedundancies": {
                            "minItems": 1
                        }
                    }
                },
                "else": {
                    "if": {
                        "properties": {
                            "pairsOfTriggersRedundancies": {
                            "minItems": 1
                            }
                        }
                    },
                    "then": {
                        "required": ["descriptionOfTriggersRedundancies"],
                            "properties": {
                                "descriptionOfTriggersRedundancies": {
                                    "not": {
                                        "const": ""
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    "if": {
                        "properties": {
                            "descriptionOfTargetsRedundancies": {
                                "not": {
                                    "const": ""
                                }
                            }
                        }
                },
                "then": {
                    "required": ["pairsOfTargetsRedundancies"],
                    "properties": {
                        "pairsOfTargetsRedundancies": {
                            "minItems": 1
                        }
                    }
                },
                "else": {
                    "if": {
                        "properties": {
                            "pairsOfTargetsRedundancies": {
                                "minItems": 1
                            }
                        }
                    },
                    "then": {
                        "required": ["descriptionOfTargetsRedundancies"],
                            "properties": {
                                "descriptionOfTargetsRedundancies": {
                                    "not": {
                                        "const": ""
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    "if": {
                        "properties": {
                            "descriptionOfContainsRedundancies": {
                                "not": {
                                    "const": ""
                                }
                            }
                        }
                    },
                    "then": {
                        "required": ["pairsOfContainsRedundancies"],
                        "properties": {
                            "pairsOfContainsRedundancies": {
                                "minItems": 1
                            }
                        }
                    },
                "else": {
                    "if": {
                        "properties": {
                            "pairsOfContainsRedundancies": {
                            "minItems": 1
                            }
                        }
                    },
                    "then": {
                        "required": ["descriptionOfContainsRedundancies"],
                            "properties": {
                                "descriptionOfContainsRedundancies": {
                                    "not": {
                                        "const": ""
                                    }
                                }
                            }
                        }
                    }
                }
            ]
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