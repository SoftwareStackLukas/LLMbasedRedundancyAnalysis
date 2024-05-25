import unittest
import json

from support_functions.json_validator import validation, chat_gpt_schema_no_annotations

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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertTrue(results)

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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertTrue(results)

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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertTrue(results)

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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertTrue(results)

    def test_invalid_data5(self):
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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertFalse(results)

    def test_invalid_data6(self):
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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertFalse(results)

    def test_invalid_data7(self):
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
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertFalse(results)

    def test_invalid_data8(self):
        test_data = '''
        {
            "relatedStories": [],
            "redundantMainPart": false,
            "mainPartRedundancies": [],
            "redundantBenefit": false,
            "benefitRedundancies": []
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertFalse(results)

def test_invalid_data9(self):
        test_data = '''
        {
            "relatedStories": [111],
            "redundantMainPart": false,
            "mainPartRedundancies": [],
            "redundantBenefit": false,
            "benefitRedundancies": []
        }
        '''
        results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
        self.assertFalse(results)

def test_invalid_data10(self):
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

def test_invalid_data11(self):
    test_data = '''
    {
        "relatedStories": [453,111],
        "redundantMainPart": true,
        "mainPartRedundancies": [],
        "redundantBenefit": false,
        "benefitRedundancies": []
    }
    '''
    results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
    self.assertFalse(results)

def test_invalid_data12(self):
    test_data = '''
    {
        "relatedStories": [453,111],
        "redundantMainPart": false,
        "mainPartRedundancies": [],
        "redundantBenefit": true,
        "benefitRedundancies": []
    }
    '''
    results, _ = validation(json.loads(test_data), chat_gpt_schema_no_annotations)
    self.assertFalse(results)
    
  
# Convert to unittest functions  
# test_data9 = '''
#     {
#         "relatedStories": [111],
#         "redundantMainPart": false,
#         "mainPartRedundancies": [],
#         "redundantBenefit": false,
#         "benefitRedundancies": []
#     }
# '''
# print(validation(json.loads(test_data9), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

# test_data10 = '''
#     {
#         "relatedStories": [ ,111],
#         "redundantMainPart": false,
#         "mainPartRedundancies": [],
#         "redundantBenefit": false,
#         "benefitRedundancies": []
#     }
# '''
# try: 
#     print(validation(json.loads(test_data10), chat_gpt_schema_no_annotations))
#     print("true")
# except:
#     print("false")

# test_data11 = '''
#     {
#         "relatedStories": [453,111],
#         "redundantMainPart": true,
#         "mainPartRedundancies": [],
#         "redundantBenefit": false,
#         "benefitRedundancies": []
#     }
# '''
# print(validation(json.loads(test_data9), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

# test_data12 = '''
#     {
#         "relatedStories": [453,111],
#         "redundantMainPart": false,
#         "mainPartRedundancies": [],
#         "redundantBenefit": true,
#         "benefitRedundancies": []
#     }
# '''
# print(validation(json.loads(test_data12), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)


# test_data13 = '''
#     {
#         "relatedStories": [
#             326,
#             353
#         ],
#         "redundantMainPart": true,
#         "mainPartRedundancies": [],
#         "redundantBenefit": false,
#         "benefitRedundancies": [
#             {
#                 "reasonDescription": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
#                 "referenceToOriginalText": [
#                     "so that I can review the for compliance and subsequently approved or denied"
#                 ]
#             }
#         ]
#     }
# '''
# print(validation(json.loads(test_data13), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

# test_data13 = '''
#     {
#         "relatedStories": [
#             326,
#             353
#         ],
#         "redundantMainPart": true,
#         "mainPartRedundancies": [
#             {
#                 "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
#                 "referenceToOriginalText": [
#                     "As a Staff member, I want to Assign an Application for Detailed Review"
#                 ]
#             }
#         ],
#         "redundantBenefit": false,
#         "benefitRedundancies": []
#     }
# '''
# print(validation(json.loads(test_data13), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

# test_data14 = '''
#     {
#         "relatedStories": [
#             326,
#             353
#         ],
#         "redundantMainPart": false,
#         "mainPartRedundancies": [],
#         "redundantBenefit": true,
#         "benefitRedundancies": [
#             {
#                 "referenceToOriginalText": [
#                     "so that I can review the for compliance and subsequently approved or denied",
#                     "so that I can review them for compliance and either approve, or fail or deny the plans and record any conditions, clearances, or corrections needed from the Applicant"
#                 ]
#             }
#         ]
#     }
# '''
# print(validation(json.loads(test_data5), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

# test_data15 = '''
#     {
#         "relatedStories": [
#             326,
#             353
#         ],
#         "redundantMainPart": true,
#         "mainPartRedundancies": [
#             {
#                 "referenceToOriginalText": [
#                     "As a Staff member, I want to Assign an Application for Detailed Review",
#                     "As a Plan Review Staff member, I want to Review Plans"
#                 ]
#             }
#         ],
#         "redundantBenefit": false,
#         "benefitRedundancies": []
#     }
# '''
# print(validation(json.loads(test_data6), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

# test_data16 = '''
#     {
#         "relatedStories": [
#             326,
#             353
#         ],
#         "redundantMainPart": false,
#         "mainPartRedundancies": [],
#         "redundantBenefit": true,
#         "benefitRedundancies": [
#             {
#                 "reasonDescription": "The redundancy in these sentences lies in the repetition of the outcome ('review for compliance') and the actions ('approve' and 'deny'), which convey the same idea using slightly different wording.",
#             }
#         ]
#     }
# '''
# print(validation(json.loads(test_data5), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

# test_data17 = '''
#     {
#         "relatedStories": [
#             326,
#             353
#         ],
#         "redundantMainPart": true,
#         "mainPartRedundancies": [
#             {
#                 "reasonDescription": "The redundancy arises from the repetition of the concept of reviewing for compliance expressed in slightly different ways for emphasis or to cater to different audiences.",
#         ],
#         "redundantBenefit": false,
#         "benefitRedundancies": []
#     }
# '''
# print(validation(json.loads(test_data6), chat_gpt_schema_no_annotations))
# print("Should be: false")
# print("-" * 10)

if __name__ == "__main__":
    unittest.main()