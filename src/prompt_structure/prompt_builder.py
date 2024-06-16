import json, os, copy

# Example for short answer:
#   Absolutely, I'd be happy to help you with your Python needs. What do you need assistance with today?


class PromptBuilder:
    """
    Singleton class to manage and generate prompt templates for analyzing user story redundancies.

    Attributes:
        _instance (PromptBuilder): Singleton instance of the PromptBuilder class.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PromptBuilder, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._PRE_SET_UP_AS_REQ_ENG: str = ("Act as a Requirements Engineer focused on identifying redundancies. "
            "Please review pairs of two User Stories and pinpoint any unnecessary duplications that obscure clarity or add no distinct value.")
        
        ### Addapt to new defintions
        self._SYSTEM_SIMULATION_ACTOR_ROLE: str = ("As a requirements engineer in agile development, it is my responsibility to review user stories for redundancies. My goal is to identify and report any overlapping or duplicate requirements. " 
        "By carefully analysing the user stories in depth, I ensure that each requirement is necessary and contributes uniquely, increasing the coherence of the product.")
        
        self._DEFINITION_BASE_REDUNDANCY: str = (
            "Please, analyse redundancies in the main part and benefit of a pair of two given User Stories which are entered as JSON objects. "
            "Note that a User Story may include multiple redundancies in the main part as well as the benefit. The redundancies of the main part and benefit are disjoint sets. "
            "Hence, a main part can be redundant while a benefit is not and vice versa. " 
            "However, in some cases the main part and the benefit can be at the same time redundant, but they do not depend on each other and therefore they are independent redundant. "
            "The definition of the main part is: "
        )
        
        self._DEFINITION_MAIN_PART_BENEFIT: str = (
            "The main part of the user Story describes the core action that a persona wishes to accomplish. "
            "It is the value of the key called 'Main Part'. "
            "The definition of a benefit is as follows: The benefit of the User Story is contained the value of the key 'Benefit'." 
        )

        self._DEFINITION_USER_STORY_RELATIONSHIPS: str = (
            "Relationships within the user Stories are contained as values of Triggers, Targets, Benefit and Contains."
        )
        
        ### Adapt to new defintions
        self._SYSTEM_SIMULATION_DEFINITION_USER_STORY: str = ("I will analyse redundancies in the main parts and benefits of two User Stories. Each story might include multiple redundancies. "
            "The main part typically describes the desired functionality by the persona, while the benefit details the positive outcomes from the functionality."
        )
        
        # Defining the handtel pair?
        # at last one / minium of one?
        # Something is broken with the second, third, forth, sentence
        self._DEFINITION_PARTIAL_FULL_REDUNDANCY: str = (
            "1.) A partial main part redundancy occurs if one value of 'Targets'.'Main Part' of the first User Story also occur in the second User Story.\n"
            "2.) A full main part redundancy occurs if the values of 'Targets'.'Main Part', 'Triggers'.'Main Part' and 'Contains'.'Main Part' of the first User Story also occur in the second User story and vice versa.\n"
            "3.) A partial benefit redundancy occurs if one value of of 'Targets'.'Benefit' of the first User Story also occur in the second User Story.\n"
            "4.) A full benefit redundancy occurs if the values of 'Triggers'.'Benefit' and 'Targets'.'Benefit' and 'Contains'.'Benefit' also occur in the second User Story and vice versa."
        )
        
        ### Adapt to new defintions full / partial in main and benefit - rempove Ready to proceed or change it in the next step as proceed is not process
        self._SYSTEM_SIMULATION_DEFINITION_PARTIAL_FULL_REDUNDANCY: str = ("I'll review the User Stories for redundancies in main parts and benefits, using the specified definitions. Ready to proceed?")
        
        ## Add Gabis definitions
        ## Maybe examples for the format. and improving the sentences
        ## Defining the JSON output format and provide an example

        # print(DEFINITION_PARTIAL_FULL_REDUNDANCY)

        self._INTRODUCING_JSON_DEFINITION: str = ("Before we proceed, consider the following JSON output format:\n"
            "This JSON structure organizes information about redundancies in User Stories, focusing on both the main parts and the benefits regarding full and partial redundancies. "
            "Each section includes descriptions of the redundancies and specific text references to illustrate where these redundancies occur within the stories.")

        ### Redefine the fields pairsOfTriggersRedundancies, pairsOfTargetsRedundancies, pairsOfContainsRedundancies
        self._DEFINITION_JSON_SCHEMA: str = (
            "1.) The field 'relatedStories' is an array of two integer value. The value are the usids of the User Stories and this field is also mandatory.\n"
            "2.) The 'mainPartRedundancies' is an json object which containes the following fields:\n"
                "2.1) The field 'partialRedundancy' is of the type bool. true indicates that a pair of User Stories has a partial redundancy (partialRedundancy) in the main part and otherwise false. It just can be true when the main part is not full redundant. It is a mandatory field. \n"
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
        
        ### Adapt to new defintions
        self._SYSTEM_SIMULATION_DEFINITION_JSON_FORMAT: str = "I've noted the JSON output format specified and will deliver the defined output. Can you provide some examples for me?"
        
        self._FILE_PATH_INPUT_EXAMPLES: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompt_examples", "input_examples.json")
        self._FILE_PATH_OUTPUT_EXAMPLES: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompt_examples", "output_examples.json")
        self._json_input_examples: list[dict] = None
        self._json_output_examples: list[dict] = None
        with open(self._FILE_PATH_INPUT_EXAMPLES, 'r', encoding='utf-8') as file:
            self._json_input_examples = json.load(file)
        with open(self._FILE_PATH_OUTPUT_EXAMPLES, 'r', encoding='utf-8') as file:
            self._json_output_examples = json.load(file)

        self._INTRO_OF_EXAMPLES: str = "Yes, here are some examples:\n"
        
        ### Needs to be defined
        self._SYSTEM_SIMULATION_EXAMPLE_CONSIDERATION: str = ""
        
        self._PROCESS_REQUEST = "Yes. Please, process the following pairs of user story with annotations:\n"

    def get_actor_role(self) -> dict:
        """
            Returns the predefined actor role for the requirements engineer.
            
            Returns:
                dict: A dictionary containing the role and content for the actor.
        """
        temp: str = self._PRE_SET_UP_AS_REQ_ENG
        return {
            "role": "user",
            "content": temp,
        }
        
    def get_system_simulation_actor_role(self) -> dict:
        """
            Returns the system simulation actor role definition.
            
            Returns:
                dict: A dictionary containing the role and content for the system simulation actor.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_USER_STORY
        return {
            "role": "user",
            "content": temp,
        }

    def get_user_story_definition(self) -> dict:
        """
            Returns the user story definition, including redundancy, main part, and relationships.
            
            Returns:
                dict: A dictionary containing the role and content for the user story definition.
        """
        temp: str = self._DEFINITION_BASE_REDUNDANCY + self._DEFINITION_MAIN_PART_BENEFIT + self._DEFINITION_USER_STORY_RELATIONSHIPS
        return {
            "role": "user",
            "content": temp,
        }

    def get_system_simulation_redundancy_definition(self) -> dict:
        """
            Returns the system simulation redundancy definition.
            
            Returns:
                dict: A dictionary containing the role and content for the redundancy definition.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_USER_STORY
        return {
            "role": "user",
            "content": temp,
        }

    def get_redundancy_definition(self) -> dict:
        """
            Returns the definition of partial and full redundancies in user stories.
            
            Returns:
                dict: A dictionary containing the role and content for the redundancy definition.
        """
        temp: str = self._DEFINITION_PARTIAL_FULL_REDUNDANCY
        return {
            "role": "user",
            "content": temp,
        }

    def get_system_simulation_full_partial_definition(self) -> dict:
        """
            Returns the system simulation definition for partial and full redundancies.
            
            Returns:
                dict: A dictionary containing the role and content for the full and partial redundancy definitions.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_PARTIAL_FULL_REDUNDANCY
        return {
            "role": "user",
            "content": temp,
        }

    def get_json_defintion(self) -> dict:
        """
            Returns the JSON schema definition for redundancies in user stories.
            
            Returns:
                dict: A dictionary containing the role and content for the JSON schema definition.
        """
        temp: str = self._INTRODUCING_JSON_DEFINITION + self._DEFINITION_JSON_SCHEMA
        return {
            "role": "user",
            "content": temp,
        }

    def get_system_simulation_json_format(self) -> dict:
        """
            Returns the system simulation JSON format definition.
            
            Returns:
                dict: A dictionary containing the role and content for the JSON format definition.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_JSON_FORMAT
        return {
            "role": "user",
            "content": temp,
        }

    def get_input_output_examples(self, schema_keys: list[str]) -> dict:
        """
        Generates a structured example text showing input-output relationships based on the provided schema keys.

        Args:
            schema_keys (list[str]): A list of keys that should be included in the input examples.

        Returns:
            dict: A dictionary with a role and content, where the content is a formatted string of input-output examples.

        Raises:
            ValueError: If no related user stories are found for any output example.

        Description:
            This function performs the following steps:
            1. Copies the global variable `json_input_examples` and filters each entry to retain only keys specified in `schema_keys`.
            2. Initializes a string with introductory content from the global variable `INTRO_OF_EXAMPLES`.
            3. Iterates through each entry in the global variable `json_output_examples`, retrieves the related user stories by `USID`, 
            and constructs a formatted example text showing the input examples and their expected output.
            4. Constructs a dictionary with a user role and the formatted content.
        """
        temp_intro = self._INTRO_OF_EXAMPLES
        temp_input = copy.deepcopy(self._json_input_examples)
        temp_input = [{k: v for k, v in entry.items() if k in schema_keys} for entry in temp_input]
        
        temp_examples: str = temp_intro
        first_one: dict = None
        second_one: dict = None
        i: int = 1
        for out_example in self._json_output_examples:
            key1, key2 = map(str, out_example["relatedStories"])
            for inp_example in self._json_input_examples:
                if not first_one and str(inp_example["USID"]) == str(key1):
                    first_one = inp_example
                elif not second_one and str(inp_example["USID"]) == str(key2):
                    second_one = inp_example
            if not first_one or not second_one:
                raise ValueError("No releated US found for output json")
            temp_examples += f"Example {i}.):\n"
            temp_examples += f"The input json is {json.dumps(first_one)} and {json.dumps(second_one)}\n"
            temp_examples += f"The expected output is: {json.dumps(out_example)}\n"
            first_one = second_one = None
            i += 1
        
        input_output_examples: dict = {
            "role": "user",
            "content": temp_examples
        }
        
        return input_output_examples

    def get_system_simulation_example_consideration(self) -> dict:
        """
            Returns the system simulation example consideration definition.
            
            Returns:
                dict: A dictionary containing the role and content for the example consideration definition.
        """
        temp: str = self._SYSTEM_SIMULATION_EXAMPLE_CONSIDERATION
        return {
            "role": "user",
            "content": temp,
        }

    def process_request(self, json_us_one, json_us_two) -> dict:
        """
            Generates a structured request to process pairs of user story annotations.

            Args:
            json_us_one (dict): The first user story JSON object containing annotations.
            json_us_two (dict): The second user story JSON object containing annotations.

            Returns:
            dict: A dictionary with a role and content, where the content is a formatted string describing the user story pairs.

            Description:
            This function performs the following steps:
            1. Constructs a formatted string that includes the user story IDs and their respective annotations.
            2. Returns a dictionary containing the role as "user" and the constructed string as the content.
        """
        temp: str = (self._PROCESS_REQUEST +
            f"id: {json_us_one["USID"]}, annotations: {json.dumps(json_us_one)};\n"
            f"id: {json_us_two["USID"]}, annotations: {json.dumps(json_us_two)}")

        return {
            "role": "user",
            "content": temp,
        }
        
    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of PromptBuilder.

        Returns:
            PromptBuilder: The singleton instance of the PromptBuilder class.
        """
        return PromptBuilder()