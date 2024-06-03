import unittest
import json

from support_functions.json_validator import validation, chat_gpt_schema_with_annotations

class TestJSONValidationSchemaWithAnnotations(unittest.TestCase):
    test_data: str = ""
    
    def test_valid_data1(self):
        '''
            Covering the schema when no redundancy is detected
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data2(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        print(_)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
        
    def test_valid_data3(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data4(self):
        '''
           ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
        
    def test_valid_data5(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
        
    def test_valid_data6(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
        
    def test_valid_data7(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data8(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
    
    def test_valid_data9(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data10(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data11(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data12(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data13(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
    
    def test_valid_data14(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data15(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data16(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data17(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": true,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data18(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_valid_data19(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
        
    def test_valid_data20(self):
        '''
            Test where pairsOf*Redundancies have exactly the minimum required items when partialRedundancy is true
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))  # Expecting no validation errors
        self.assertTrue(results)
        
    def test_valid_data21(self):
        '''
            Test where pairsOf*Redundancies have exactly the minimum required items when partialRedundancy is true
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))  # Expecting no validation errors
        self.assertTrue(results)
        
    def test_valid_data22(self):
        '''
            Test where pairsOf*Redundancies more then the the minimum required items when partialRedundancy is true
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))  # Expecting no validation errors
        self.assertTrue(results)
        
    def test_valid_data23(self):
        '''
            Test where pairsOf*Redundancies more then the the minimum required items when partialRedundancy is true
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))  # Expecting no validation errors
        self.assertTrue(results)

    # From here the negative Schema tests start
    def test_invalid_data1(self):
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": true,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)

    def test_invalid_data2(self):
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": true,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data3(self):
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": true,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": true,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"], ["have", "have"], ["have", "have"], ["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)

    def test_invalid_data4_1(self):
        test_data = '''
        {
            "relatedStories": [1],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data4_2(self):
        test_data = '''
        {
            "relatedStories": [],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data4_3(self):
        test_data = '''
        {
            "relatedStories": [4,4,4],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data4_4(self):
        test_data = '''
        {
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data5_1(self):
        '''
            Missing required field: partialRedundancy
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data5_2(self):
        '''
            Missing required field: fullRedundancy
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    
    def test_invalid_data5_3(self):
        '''
            Missing required field: descriptionOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data5_4(self):
        '''
            Missing required field: pairsOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data5_5(self):
        '''
            Missing required field: descriptionOfTriggersRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data5_6(self):
        '''
            Missing required field: pairsOfTriggersRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
    
    def test_invalid_data5_7(self):
        '''
            Missing required field: descriptionOfContainsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data5_8(self):
        '''
            Missing required field: pairsOfContainsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": ""
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data6_1(self):
        '''
            Missing required field: partialRedundancy
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data6_2(self):
        '''
            Missing required field: fullRedundancy
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    
    def test_invalid_data6_3(self):
        '''
            Missing required field: descriptionOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data6_4(self):
        '''
            Missing required field: pairsOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data6_5(self):
        '''
            Missing required field: descriptionOfTriggersRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data6_6(self):
        '''
            Missing required field: pairsOfTriggersRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
    
    def test_invalid_data6_7(self):
        '''
            Missing required field: descriptionOfContainsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data6_8(self):
        '''
            Missing required field: pairsOfContainsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": ""
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
        
    def test_invalid_data7_1(self):
        '''
            Incorrect data type: partialRedundancy as string
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": "false",
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data7_2(self):
        '''
            Incorrect data type: partialRedundancy as string
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": "false",
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data7_3(self):
        '''
            Incorrect data type: partialRedundancy as string
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": "false",
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
    
    def test_invalid_data7_4(self):
        '''
            Incorrect data type: partialRedundancy as string
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": "false",
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data8_1(self):
        '''
            Empty descriptionOfTargetsRedundancies when partialRedundancy is true
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data8_2(self):
        '''
            ... 
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data8_3(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data8_4(self):
        '''
            ... 
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data8_5(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": [["have", "have"]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data8_6(self):
        '''
            ... 
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
        
        
    def test_invalid_data9_1(self):
        '''
            Empty descriptionOfTargetsRedundancies when partialRedundancy is true
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data9_2(self):
        '''
            ... 
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data9_3(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data9_4(self):
        '''
            ... 
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data9_5(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test string",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": [["have", "have"]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data9_6(self):
        '''
            ... 
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [["have", "have"]],
                "descriptionOfTriggersRedundancies": "Test string",
                "pairsOfTriggersRedundancies": [["have", "have"]],
                "descriptionOfContainsRedundancies": "Test string",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data10_1(self):
        '''
            Invalid item type in pairsOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [["have", 1]],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data10_2(self):
        '''
            Invalid item type in pairsOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "Test String",
                "pairsOfTriggersRedundancies": [["have", 1]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data10_3(self):
        '''
            Invalid item type in pairsOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "Test String",
                "pairsOfContainsRedundancies": [["have", 1]]
            },
            "benefitRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
        
    def test_invalid_data11_1(self):
        '''
            ...
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "Test String",
                "pairsOfTargetsRedundancies": [["have", 1]],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))  
        self.assertFalse(results)
        
    def test_invalid_data11_2(self):
        '''
            Invalid item type in pairsOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "Test String",
                "pairsOfTriggersRedundancies": [["have", 1]],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []                
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)
      
    def test_invalid_data11_3(self):
        '''
            Invalid item type in pairsOfTargetsRedundancies
        '''
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            },
            "benefitRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [["have", 1]],
                "descriptionOfContainsRedundancies": "Test String",
                "pairsOfContainsRedundancies": [["have", 1]]
            }
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)


    
if __name__ == "__main__":
    unittest.main()