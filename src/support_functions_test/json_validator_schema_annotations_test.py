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
            "mainPartRedundancies": [{
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }],
            "benefitRedundancies": [{
                "partialRedundancy": false,
                "fullRedundancy": false,
                "descriptionOfTargetsRedundancies": "",
                "pairsOfTargetsRedundancies": [],
                "descriptionOfTriggersRedundancies": "",
                "pairsOfTriggersRedundancies": [],
                "descriptionOfContainsRedundancies": "",
                "pairsOfContainsRedundancies": []
            }]
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertFalse(bool(_))
        self.assertTrue(results)
        
    def test_invalid_data1(self):
        test_data = '''
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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_with_annotations)
        self.assertTrue(bool(_))
        self.assertFalse(results)

if __name__ == "__main__":
    unittest.main()