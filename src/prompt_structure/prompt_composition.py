
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
    "It is the value of the key called \"Main Part\". "
    "The definition of a benefit is as follows: The benefit of the User Story is contained the value of the key \"Benefit\"." 
)

DEFINITION_USER_STORY_RELATIONSHIPS: str = (
    "Relationships within the user Stories are contained as values of Triggers, Targets, Benefit and Contains."
)

### Something is broken with the second, third, forth, sentence (old version)
OLD_DEFINITION_PARTIAL_FULL_REDUNDANCY: str = (
    "1.) A partial main part redundancy occurs if the values of \"Targets\".\"Main Part\" of the first User Story also occur in the second User story.\n"
    "2.) A main part redundancy occurs if the values of \"Targets\".\"Main Part\", \"Triggers\". \"Main Part\" and \"Contains\". \"Main Part\" of the first User Story also occur in the second User story and vice versa.\n"
    "3.) A benefit partial redundancy occurs if one value of \"Triggers\". \"Benefit\" or \"Targets\". \"Benefit\" or \"Contains\". \"Benefit\" also occur in the second User Story.\n"
    "4.) A benefit redundancy occurs if the values of \"Triggers\". \"Benefit\" and \"Targets\". \"Benefit\" and \"Contains\". \"Benefit\" also occur in the second User Story and vice versa."
)

DEFINITION_PARTIAL_FULL_REDUNDANCY: str = (
    "1.) A partial main part redundancy occurs if the values of \"Targets\".\"Main Part\" of the first User Story also occur in the second User story.\n"
    "2.) A main part redundancy occurs if the values of \"Targets\".\"Main Part\", \"Triggers\". \"Main Part\" and \"Contains\". \"Main Part\" of the first User Story also occur in the second User story and vice versa.\n"
    "3.) A benefit partial redundancy occurs if one value of \"Triggers\". \"Benefit\" or \"Targets\". \"Benefit\" or \"Contains\". \"Benefit\" also occur in the second User Story.\n"
    "4.) A benefit redundancy occurs if the values of \"Triggers\". \"Benefit\" and \"Targets\". \"Benefit\" and \"Contains\". \"Benefit\" also occur in the second User Story and vice versa."
)

## Maybe examples for the format. and improving the sentences
## Defining the JSON output format and provide an example

print(DEFINITION_PARTIAL_FULL_REDUNDANCY)

##Provide input and output examples for the wanted results
EXAMPLE_OUTPUT_ONE: str = (
    ""
)

EXAMPLE_OUTPUT_TWO: str = (
    ""
)

EXAMPLE_OUTPUT_THREE: str = (
    ""
)

EXAMPLE_OUTPUT_FOUR: str = (
    ""
)

EXAMPLE_OUTPUT_FIVE: str = (
    ""
)

user_inital_message: dict = {
  "role": "user",
  "content": PRE_SET_UP_AS_REQ_ENG
}


# Create setters and getters. The setters shall throw an exception that no contained is changed from outside of this file