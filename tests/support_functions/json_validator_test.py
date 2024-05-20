import unittest
import json
from src.support_functions.json_validator import validation, chat_gpt_schema_no_annotations

class TestJSONValidation(unittest.TestCase):
    def test_valid_data1(self):
        test_data = '''
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
        self.assertTrue(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

    def test_valid_data2(self):
        test_data = '''
        {
            "relatedStories": [
                326,
                353
            ],
            "redundantMainPart": true,
            "mainPartRedundancies": [
                {
                    "reasonDescribtion": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
                    "referenceToOriginalText": [
                        "As a Staff member, I want to Assign an Application for Detailed Review",
                        "As a Plan Review Staff member, I want to Review Plans"
                    ]
                }
            ],
            "redundantBenefit": true,
            "benefitRedundancies": [
                {
                    "reasonDescribtion": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
                    "referenceToOriginalText": [
                        "so that I can review the for compliance and subsequently approved or denied",
                        "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
                    ]
                }
            ]
        }
        '''
        self.assertTrue(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

    def test_valid_data3(self):
        test_data = '''
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
                    "reasonDescribtion": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
                    "referenceToOriginalText": [
                        "so that I can review the for compliance and subsequently approved or denied",
                        "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
                    ]
                }
            ]
        }
        '''
        self.assertTrue(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

    def test_valid_data4(self):
        test_data = '''
        {
            "relatedStories": [
                326,
                353
            ],
            "redundantMainPart": true,
            "mainPartRedundancies": [
                {
                    "reasonDescribtion": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
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
        self.assertTrue(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

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
                    "reasonDescribtion": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
                    "referenceToOriginalText": [
                        "so that I can review the for compliance and subsequently approved or denied",
                        "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
                    ]
                }
            ]
        }
        '''
        self.assertFalse(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

    def test_invalid_data2(self):
        test_data = '''
        {
            "relatedStories": [
                326,
                353
            ],
            "redundantMainPart": false,
            "mainPartRedundancies": [
                {
                    "reasonDescribtion": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
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
        self.assertFalse(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

    def test_invalid_data3(self):
        test_data = '''
        {
            "relatedStories": [],
            "redundantMainPart": true,
            "mainPartRedundancies": [
                {
                    "reasonDescribtion": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
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
        self.assertFalse(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

    def test_invalid_data4(self):
        test_data = '''
        {
            "relatedStories": [],
            "redundantMainPart": false,
            "mainPartRedundancies": [],
            "redundantBenefit": false,
            "benefitRedundancies": []
        }
        '''
        self.assertFalse(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

def test_invalid_data5(self):
        test_data = '''
        {
            "relatedStories": [111],
            "redundantMainPart": false,
            "mainPartRedundancies": [],
            "redundantBenefit": false,
            "benefitRedundancies": []
        }
        '''
        self.assertFalse(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

def test_invalid_data6(self):
    test_data = '''
    {
        "relatedStories": [ ,111],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
    '''
    with self.assertRaises(json.JSONDecodeError):
        json.loads(test_data)

def test_invalid_data7(self):
    test_data = '''
    {
        "relatedStories": [453,111],
        "redundantMainPart": true,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
    '''
    self.assertFalse(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

def test_invalid_data8(self):
    test_data = '''
    {
        "relatedStories": [453,111],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": true,
        "benefitRedundancies": []
    }
    '''
    self.assertFalse(validation(json.loads(test_data), chat_gpt_schema_no_annotations))

if __name__ == "__main__":
    unittest.main()