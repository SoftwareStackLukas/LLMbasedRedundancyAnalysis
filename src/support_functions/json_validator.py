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

# This part checks if at last one trigger is set for a redundancy
# has to be done also for the benefit as we can not determine here if it is a full or partial redundancy
# {
#     "if": {
#         "properties": {
#             "partialRedundancy": {
#                 "const": True
#             }
#         }
#     },
#     "then": {
#         "properties": {
#              --> Maybe add here Contains and Triggers
#             "pairsOfTargetsRedundancies": { 
#                 "minItems": 1
#             }
#         }
#     }
# },

# Check if this fullfills the expected behaviour
# {
#     "if": {
#         "properties": {
#             "partialRedundancy": {
#                 "const": True
#             }
#         }
#     },
#     "then": {
#         "properties": {
#             "pairsOfTargetsRedundancies": {
#                 "minItems": 1
#             }
#         }
#     }, 
#     "else": {
#         "if": {
#             "properties": {
#                 "fullRedundancy": {
#                     "const": True
#                 }
#             }
#         },
#         "then": {
#             "properties": {
#                 "pairsOfTargetsRedundancies": {
#                     "minItems": 1
#                 }
#             }
#         }
#     }
# },

# This part is not correct
# "allOf": [
#     {
#         "if": {
#             "properties": {
#                 "redundantMainPart": {
#                     "const": True
#                 }
#             }
#         },
#         "then": {
#             "anyOf": [
#                 {
#                     "properties": {
#                         "partialRedundancy": {
#                             "const": True
#                         }
#                     }
#                 },
#                 {
#                     "properties": {
#                         "fullRedundancy": {
#                             "const": True
#                         }
#                     }
#                 }
#             ]
#         },
#         "else": {
#             "properties": {
#                 "partialRedundancy": {
#                     "const": False
#                 },
#                 "fullRedundancy": {
#                     "const": False
#                 }
#             }
#         }
#     }
# ]

## Just an example --> Check if the neste condition checks it
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
        "redundantMainPart": {
            "type": "boolean"
        },
        "mainPartRedundancies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "partialRedundancy": {
                        "type": "boolean"
                    },
                    "fullRedundancy": {
                        "type": "boolean"
                    },
                    "pairsOfTriggerRedundancies": {
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
                    "pairsOfTContainesdundancies": {
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
                "required": ["pairsOfTriggerRedundancies", "pairsOfTargetsRedundancies", "pairsOfTContainsredundancies"],
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
                                "pairsOfTargetsRedundancies": {
                                    "maxItems": 0
                                },
                                "pairsOfTriggersRedundancies": {
                                    "maxItems": 0
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
                ]
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
                    "partialRedundancy": {
                        "type": "boolean"
                    },
                    "fullRedundancy": {
                        "type": "boolean"
                    },
                    "pairsOfTriggerRedundancies": {
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
                    "pairsOfTContainesdundancies": {
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
                "required": ["pairsOfTriggerRedundancies", "pairsOfTargetsRedundancies", "pairsOfTContainsredundancies"],
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
                                "pairsOfTargetsRedundancies": {
                                    "maxItems": 0
                                },
                                "pairsOfTriggersRedundancies": {
                                    "maxItems": 0
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
                ]
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
                "anyOf": [
                    {
                        "properties": {
                            "mainPartRedundancies": {
                                "items": {
                                    "properties": {
                                        "partialRedundancy": {
                                            "const": True
                                        }
                                    }
                                }
                            }
                        }
                    },
                    {
                        "properties": {
                            "mainPartRedundancies": {
                                "items": {
                                    "properties": {
                                        "fullRedundancy": {
                                            "const": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            "else": {
                "properties": {
                    "mainPartRedundancies": {
                        "items": {
                            "properties": {
                                "partialRedundancy": {
                                    "const": False
                                },
                                "fullRedundancy": {
                                    "const": False
                                }
                            }
                        }
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
                "anyOf": [
                    {
                        "properties": {
                            "benefitRedundancies": {
                                "items": {
                                    "properties": {
                                        "partialRedundancy": {
                                            "const": True
                                        }
                                    }
                                }
                            }
                        }
                    },
                    {
                        "properties": {
                            "benefitRedundancies": {
                                "items": {
                                    "properties": {
                                        "fullRedundancy": {
                                            "const": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            "else": {
                "properties": {
                    "benefitRedundancies": {
                        "items": {
                            "properties": {
                                "partialRedundancy": {
                                    "const": False
                                },
                                "fullRedundancy": {
                                    "const": False
                                }
                            }
                        }
                    }
                }
            }
        }
    ]
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