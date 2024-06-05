
PRE_SET_UP_AS_REQ_ENG: str = "Act as a Requirements Engineer focused on identifying redundancies. Please review pairs of two User Stories and pinpoint any unnecessary duplications that obscure clarity or add no distinct value."

DEFINITION_BASE_REDUNDANCY: str = (
    "Please, analyse redundancies in the main part and benefit of a pair of two given User Stories which are entered as JSON objects. "
    "Note that a User Story may include multiple redundancies in the main part as well as the benefit. The redundancies of the main part and benefit are disjoint sets. "
    "Hence, a main part can be redundant while a benefit is not and vice versa. " 
    "However, in some cases the main part and the benefit can be at the same time redundant, but they do not depend on each other and therefore they are independent redundant. "
    "The definition of the main part is: "
)

DEFINITION_MAIN_PART_BENEFIT: str = (
    "The main part of the user Story describes the core action that a persona wishes to accomplish. "
    "It is the value of the key called 'Main Part'. "
    "The definition of a benefit is as follows: The benefit of the User Story is contained the value of the key 'Benefit'." 
)

DEFINITION_USER_STORY_RELATIONSHIPS: str = (
    "Relationships within the user Stories are contained as values of Triggers, Targets, Benefit and Contains."
)

### Something is broken with the second, third, forth, sentence (old version)
OLD_DEFINITION_PARTIAL_FULL_REDUNDANCY: str = (
    "1.) A partial main part redundancy occurs if the values of 'Targets'.'Main Part' of the first User Story also occur in the second User Story.\n"
    "2.) A main part redundancy occurs if the values of 'Targets'.'Main Part', 'Triggers'. 'Main Part' and 'Contains'. 'Main Part' of the first User Story also occur in the second User story and vice versa.\n"
    "3.) A benefit partial redundancy occurs if one value of 'Triggers'. 'Benefit' or 'Targets'. 'Benefit' or 'Contains'. 'Benefit' also occur in the second User Story.\n"
    "4.) A benefit redundancy occurs if the values of 'Triggers'. 'Benefit' and 'Targets'. 'Benefit' and 'Contains'. 'Benefit' also occur in the second User Story and vice versa."
)

# Defining the handtel pair?
# at last one / minium of one?
# Something is broken with the second, third, forth, sentence
DEFINITION_PARTIAL_FULL_REDUNDANCY: str = (
    "1.) A partial main part redundancy occurs if one value of 'Targets'. 'Main Part' of the first User Story also occur in the second User Story.\n"
    "2.) A main part redundancy occurs if the values of 'Targets'. 'Main Part', 'Triggers'. 'Main Part' and 'Contains'. 'Main Part' of the first User Story also occur in the second User story and vice versa.\n"
    "3.) A benefit partial redundancy occurs if one value of of 'Targets'. 'Benefit' of the first User Story also occur in the second User Story. \n"
    "4.) A benefit redundancy occurs if the values of 'Triggers'. 'Benefit' and 'Targets'. 'Benefit' and 'Contains'. 'Benefit' also occur in the second User Story and vice versa."
)

## Add Gabis definitions
## Maybe examples for the format. and improving the sentences
## Defining the JSON output format and provide an example

print(DEFINITION_PARTIAL_FULL_REDUNDANCY)

### Redefine the fields pairsOfTriggersRedundancies, pairsOfTargetsRedundancies, pairsOfContainsRedundancies
DEFINITION_JSON_SCHEMA: str = (
    "Before we proceed, consider the following JSON output format:\n"
    "This JSON structure organizes information about redundancies in User Stories, focusing on both the main parts and the benefits regarding full and partial redundancies. "
    "Each section includes descriptions of the redundancies and specific text references to illustrate where these redundancies occur within the stories."
    "1.) The field 'relatedStories' is an array of two integer value. The value are the ids of the User Stories and this field is also mandatory.\n"
    "2.) The 'mainPartRedundancies' is an json object which containes the following fields:\n"
        "2.1) The field 'partialRedundancy' is of the type bool. true indicates that a pair of User Stories has a partial redundancy (partialRedundancy) in the main part and otherwise false. It can just be true when the main part is not full redundant. It is a mandatory field. \n"
        "2.2) The field 'fullRedundancy' is of the type bool. true indicates that a pair of User Stories has a full redundancy (fullRedundancy) in the main part and otherwise false. It is a mandatory field."
        "2.3) The field 'descriptionOfTriggersRedundancies' is of the type string. The value of this field contains a description that is explaining the reason for the trigger redundancies and when no trigger redundancy exists it is an empty string. It is a mandatory field and has a dependency with pairsOfTriggersRedundancies. \n"
        "2.4) The field 'pairsOfTriggersRedundancies' is \n"
        "2.5) The field 'descriptionOfTargetsRedundancies' is of the type string. The value of this field contains a description that is explaining the reason for the target redundancies and when no target redundancy exists it is an empty string. It is a mandatory field and has a dependency with pairsOfTargetsRedundancies.\n"
        "2.6) The field 'pairsOfTargetsRedundancies' \n"
        "2.7) The field 'descriptionOfContainsRedundancies' is of the type string. The value of this field contains a description that is explaining the reason for the contain redundancies and when no contain redundancy exists it is an empty string. It is a mandatory field and has a dependency with pairsOfContainsRedundancies.\n"
        "2.8) The field 'pairsOfContainsRedundancies' \n"
    "3.) The 'mainPartRedundancies' is an json object which containes the following fields:\n"
        "3.1) The field 'partialRedundancy' is of the type bool. true indicates that a pair of User Stories has a partial redundancy (partialRedundancy) in the main part and otherwise false. It can just be true when the main part is not full redundant. It is a mandatory field. \n"
        "3.2) The field 'fullRedundancy' is of the type bool. true indicates that a pair of User Stories has a full redundancy (fullRedundancy) in the main part and otherwise false. It is a mandatory field."
        "3.3) The field 'descriptionOfTriggersRedundancies' is of the type string. The value of this field contains a description that is explaining the reason for the trigger redundancies and when no trigger redundancy exists it is an empty string. It is a mandatory field and has a dependency with pairsOfTriggersRedundancies.\n"
        "3.4) The field 'pairsOfTriggersRedundancies' \n"
        "3.5) The field 'descriptionOfTargetsRedundancies' is of the type string. The value of this field contains a description that is explaining the reason for the target redundancies and when no target redundancy exists it is an empty string. It is a mandatory field and has a dependency with pairsOfTargetsRedundancies.\n"
        "3.6) The field 'pairsOfTargetsRedundancies' \n"
        "3.7) The field 'descriptionOfContainsRedundancies' is of the type string. The value of this field contains a description that is explaining the reason for the contain redundancies and when no contain redundancy exists it is an empty string. It is a mandatory field and has a dependency with pairsOfContainsRedundancies.\n"
        "3.8) The field 'pairsOfContainsRedundancies' \n"
)

INTRODUCING_EXAMPLES: str = (
    ""
)

##Provide input and output examples for the wanted results
EXAMPLE_INPUT_OUTPUT_ONE: str = (
    ""
)

EXAMPLE_INPUT_OUTPUT_TWO: str = (
    ""
)

EXAMPLE_INPUT_OUTPUT_THREE: str = (
    ""
)

EXAMPLE_INPUT_OUTPUT_FOUR: str = (
    ""
)

EXAMPLE_INPUT_OUTPUT_FIVE: str = (
    ""
)

user_inital_message: dict = {
  "role": "user",
  "content": PRE_SET_UP_AS_REQ_ENG
}


# Create setters and getters. The setters shall throw an exception that no contained is changed from outside of this file