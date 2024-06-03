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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # From here the negative Schema tests start
        
    def test_invalid_data1(self):
        test_data = '''
        {
            "relatedStories": [1, 3],
            "mainPartRedundancies": {
                "partialRedundancy": true,
                "fullRedundancy": true,
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
        
if __name__ == "__main__":
    unittest.main()