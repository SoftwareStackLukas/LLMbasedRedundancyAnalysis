import json, os, copy

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
        
        self._DEFINITION_US: str = ("A user story is a semi-structured sentence containing the following information:\n"
                                    "(1) the persona involved in the story,\n"
                                    "(2) the main part containing the actions that the persona will perform on the system and the entities involved in the actions, and optionally\n"
                                    "(3) a benefit that the persona will receive after having completed these actions. The benefit may also include actions and entities.\n"
                                    "Classically, a user story is expressed in the following form: 'As a <persona>, I can <Actions> over <entities>, so that <benefit>.'\n"
                                    "An example of a User Story is:"
                                    "As an API User, I want to be able to understand if a user is a Publisher, so that I can offer functionality based on Dataset Publisher privileges."
                                    "An annotated user story is a user story together with a conceptual model that makes the following concepts explicit: "
                                    "The persona, a set of actions, a set of entities, a set of trigger references running from"
                                    "the persona to the actions, a set of target references running from"
                                    "the action to the entities, and a set of contains references between"
                                    "entities. The sets of actions and entities are divided between the"
                                    "main part and the optional benefit of a user story.\n"
                                    "An example of an annotated User Story in a JSON format is:\n"
                                        """{'PID': '#G05#',
                                            'USID': '399',
                                            'Text': 'As an API User, I want to be able to get bordering regions|cities when I query a region|city, So that I can provider wider visual context for mapping visualisations.',
                                            'Main Part': 'As an API User, I want to be able to get bordering regions|cities when I query a region|city, So that I can provider wider visual context for mapping visualisations.',
                                            'Benefit': 'I can provider wider visual context for mapping visualisations',
                                            "Action": {"Main Part": ["get"], "Benefit": ["query", "provider"]},
                                            "Entity": {"Main Part": ["cities", "bordering regions"], "Benefit": ["region", "city,", "wider visual context", "mapping visualisations"]},
                                            'Triggers': {'Main Part': [['API User', 'get']], 'Benefit': []},
                                            'Targets': {'Main Part': [['get', 'cities'], ['get', 'bordering regions']], 'Benefit': [['provider', 'wider visual context'], ['query', 'city,'], ['query', 'region']]},
                                            'Contains': {'Main Part': [], 'Benefit': [['mapping visualisations', 'wider visual context']]}}
                                        """
                                    )
        
        self._SYSTEM_SIMULATION_DEFINITION_US: str = ("Understood. You provide me with a pair of two user stories and its annotations, represented in JSON format with conceptual modeling, similar to the provided example. "
                                                      "This User Stories will be analysed. Anything to know more?")
        
        self._TASK_DEFINTION: str = (
            "Please, analyse redundancies in the 'Main Part' and 'Benefit' of a pair of two given User Stories which are entered as JSON objects. "
            "Note that a User Story pair may include multiple redundancies in the 'Main Part' as well as the 'Benefit'. The redundancies of the 'Main Part' and 'Benefit' are disjoint sets. "
            "Hence, a 'Main Part' can be redundant while a 'Benefit' is not and vice versa. " 
            "However, in some cases the 'Main Part' and the 'Benefit' can be at the same time redundant, but they do not depend on each other and therefore they are independent redundant. "
            "Focus on this aspects in the 'Main Part':"
        )
        
        self._DEFINITION_FOCUS_ASPECTS_MAIN_PART_BENEFIT: str = (
            "The 'Main Part' of the user Story describes the core action that a persona wishes to accomplish. "
            "It is the value of the key called 'Main Part'. "
            "The definition of a benefit is as follows: The benefit of the User Story is contained the value of the key 'Benefit'." 
        )

        self._DEFINITION__FOCUS_ASPECTS_USER_STORY_RELATIONSHIPS: str = (
            "Relationships within the user Stories are contained as values of 'Triggers', 'Targets' and 'Contains'." #, 'Benefit'
        )
        
        self._SYSTEM_SIMULATION_DEFINITION_FOCUS_ASPECTS_USER_STORY: str = ("I will analyse redundancies in the 'Main Part' and 'Benefit' of two User Stories. Each story might include multiple redundancies. "
            "The main part typically describes the desired functionality by the persona, while the 'Benefit' details the positive outcomes from the functionality. What is your definition of redundancies in a pair of User Stories?"
        )
        
        #This can also include partial redundancies in 'Triggers'.'Main Part' and 'Contains'.'Main Part', where not all 'Triggers'.'Main Part' and 'Contains'.'Main Part' occure in the second User Story.
        ### Consider that also targets and contains can be included
        self._DEFINITION_PARTIAL_FULL_REDUNDANCY: str = (
            "We distinguish between full and partial 'Main Part' redundancies and full and partial 'Benefits' redundancies. Thus, a 'Main Part' can be either full and partial redundant, which is also valid for the 'Benefits'"
            "1.) A partial main part redundancy occurs if one value of 'Targets'.'Main Part' of the first User Story also occur in the second User Story. \n"
            "2.) A full main part redundancy occurs if the values of 'Targets'.'Main Part', 'Triggers'.'Main Part' and 'Contains'.'Main Part' of the first User Story also occur in the second User story and vice versa.\n"
            "3.) A partial benefit redundancy occurs if one value of of 'Targets'.'Benefit' of the first User Story also occur in the second User Story.\n"
            "4.) A full benefit redundancy occurs if the values of 'Triggers'.'Benefit' and 'Targets'.'Benefit' and 'Contains'.'Benefit' also occur in the second User Story and vice versa."
        )
        
        self._SYSTEM_SIMULATION_DEFINITION_PARTIAL_FULL_REDUNDANCY: str = ("I'll review the User Stories for redundancies given by your definition. What shall the JSON output format look like?")
        
        self._INTRODUCING_JSON_FORMAT_DEFINITION: str = ("The following  JSON output format which organizes information about redundancies of a pair of User Stories, "
                                                  "focusing on both the 'Main Part's and the 'Benefit's regarding full and partial redundancies:")

        ### Should contain the definition of the redundancies to not overshaddow the definition from before
        ### Redefine the fields pairsOfTriggersRedundancies, pairsOfTargetsRedundancies, pairsOfContainsRedundancies
        self._DEFINITION_JSON_FORMAT_DEFINITION: str = (
            "1.) The field 'relatedStories' is an array of exactly two integer values. These values are the user story IDs (usids) of the User Stories, and this field is mandatory.\n"
            "2.) The 'mainPartRedundancies' field is a JSON object that provides detailed information about redundancies in the main parts of the User Stories pair. "
                "Conditions and Dependencies: If both 'partialRedundancy' and 'fullRedundancy' are false, then the arrays 'pairsOfTriggersRedundancies', 'pairsOfTargetsRedundancies', and 'pairsOfContainsRedundancies' must all have a maximum of 0 items. "
                "If 'partialRedundancy' is true, 'fullRedundancy' must be false, and vice versa. "
                "If 'fullRedundancy' is true, the 'pairsOfTriggersRedundancies' and 'pairsOfTargetsRedundancies' arrays -- Insert here again the defintion to not over shadow def. --"
                "If 'partialRedundancy' is true, the 'pairsOfTargetsRedundancies' array must have -- Insert here again the defintion to not over shadow def. --"
                "It is mandatory and contains the following fields:\n"
                "\t2.1) The 'partialRedundancy' field is of the type boolean. A value of true indicates that a pair of User Stories has a partial redundancy in the main part, while a value of false indicates no partial redundancy. This field can only be true when the main part is not fully redundant. It is a mandatory field.\n"
                "\t2.2) The 'fullRedundancy' field is of the type boolean. A value of true indicates that a pair of User Stories has full redundancy in the main part, while a value of false indicates no full redundancy. It is a mandatory field.\n"
                "\t2.3) The 'pairsOfTriggersRedundancies' field is an array of objects, each containing: \n"
                    "\t\t2.3.1) A 'descriptionOfTriggerPairRedundancies' field. This is a string that provides a description explaining the reason for the trigger redundancies. It must have a minimum length of 1 character.\n"
                    "\t\t2.3.2) A 'firstUserStoryTriggerPair' field. This is an array of exactly two string values representing the first pair of user story triggers which is \n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t2.3.3) A 'secondUserStoryTriggerPair' field. This is an array of exactly two string values representing the second pair of user story triggers.\n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t2.3.4) Each object in this array must contain the fields 'descriptionOfTriggerPairRedundancies', 'firstUserStoryTriggerPair', and 'secondUserStoryTriggerPair'. The array must contain unique items and can have zero or multiple elements.\n"
                "\t2.4) The 'pairsOfTargetsRedundancies' field is an array of objects, each containing:\n"
                    "\t\t2.4.1) A 'descriptionOfTargetPairRedundancies' field. This is a string that provides a description explaining the reason for the target redundancies. It must have a minimum length of 1 character.\n"
                    "\t\t2.4.2) A 'firstUserStoryTargetPair' field. This is an array of exactly two string values representing the first pair of user story targets.\n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t2.4.3) A 'secondUserStoryTargetPair' field. This is an array of exactly two string values representing the second pair of user story targets.\n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t2.4.4) Each object in this array must contain the fields 'descriptionOfTriggerPairRedundancies', 'firstUserStoryTriggerPair', and 'secondUserStoryTriggerPair'. The array must contain unique items and can have zero or multiple elements.\n"
                "\t2.5) The 'pairsOfTriggersRedundancies' field is an array of objects, each containing:\n"
                    "\t\t2.5.1) A 'descriptionOfContainPairsRedundancies' field.\n"
                    "\t\t2.5.2) A 'firstUserStoryContainPair' field. This is an array of exactly two string values representing the first pair of user story contains. \n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t2.5.3) A 'secondUserStoryContainPair' field. This is an array of exactly two string values representing the second pair of user story contains. \n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t2.5.4) Each object in this array must contain the fields 'descriptionOfTriggerPairRedundancies', 'firstUserStoryTriggerPair', and 'secondUserStoryTriggerPair'. The array must contain unique items and can have zero or multiple elements.\n"
            "3.) The 'mainPartRedundancies' field is a JSON object that provides detailed information about redundancies in the main parts of the User Stories pair. "
                "Conditions and Dependencies: If both 'partialRedundancy' and 'fullRedundancy' are false, then the arrays 'pairsOfTriggersRedundancies', 'pairsOfTargetsRedundancies', and 'pairsOfContainsRedundancies' must all have a maximum of 0 items. "
                "If 'partialRedundancy' is true, 'fullRedundancy' must be false, and vice versa. "
                "If 'fullRedundancy' is true, the 'pairsOfTargetsRedundancies' arrays -- Insert here again the defintion to not over shadow def. --"
                "If 'partialRedundancy' is true, the 'pairsOfTargetsRedundancies' array must have -- Insert here again the defintion to not over shadow def. --"
                "It is mandatory and contains the following fields:\n"
                "\t3.1) The 'partialRedundancy' field is of the type boolean. A value of true indicates that a pair of User Stories has a partial redundancy in the main part, while a value of false indicates no partial redundancy. This field can only be true when the main part is not fully redundant. It is a mandatory field.\n"
                "\t3.2) The 'fullRedundancy' field is of the type boolean. A value of true indicates that a pair of User Stories has full redundancy in the main part, while a value of false indicates no full redundancy. It is a mandatory field.\n"
                "\t3.3) The 'pairsOfTriggersRedundancies' field is an array of objects, each containing: \n"
                    "\t\t3.3.1) A 'descriptionOfTriggerPairRedundancies' field. This is a string that provides a description explaining the reason for the trigger redundancies. It must have a minimum length of 1 character.\n"
                    "\t\t3.3.2) A 'firstUserStoryTriggerPair' field. This is an array of exactly two string values representing the first pair of user story triggers.\n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t3.3.3) A 'secondUserStoryTriggerPair' field. This is an array of exactly two string values representing the second pair of user story triggers.\n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t3.3.4) Each object in this array must contain the fields 'descriptionOfTriggerPairRedundancies', 'firstUserStoryTriggerPair', and 'secondUserStoryTriggerPair'. The array must contain unique items and can have zero or multiple elements.\n"
                "\t2.4) The 'pairsOfTargetsRedundancies' field is an array of objects, each containing:\n"
                    "\t\t3.4.1) A 'descriptionOfTargetPairRedundancies' field. This is a string that provides a description explaining the reason for the target redundancies. It must have a minimum length of 1 character.\n"
                    "\t\t3.4.2) A 'firstUserStoryTargetPair' field. This is an array of exactly two string values representing the first pair of user story targets.\n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t3.4.3) A 'secondUserStoryTargetPair' field. This is an array of exactly two string values representing the second pair of user story targets.\n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t3.4.4) Each object in this array must contain the fields 'descriptionOfTriggerPairRedundancies', 'firstUserStoryTriggerPair', and 'secondUserStoryTriggerPair'. The array must contain unique items and can have zero or multiple elements.\n"
                "\t2.5) The 'pairsOfTriggersRedundancies' field is an array of objects, each containing:\n"
                    "\t\t3.5.1) A 'descriptionOfContainPairsRedundancies' field.\n"
                    "\t\t3.5.2) A 'firstUserStoryContainPair' field. This is an array of exactly two string values representing the first pair of user story contains. \n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t3.5.3) A 'secondUserStoryContainPair' field. This is an array of exactly two string values representing the second pair of user story contains. \n" # Think how to improve - should contain the definition of the redundancies to not overshaddow the definition from before
                    "\t\t3.5.4) Each object in this array must contain the fields 'descriptionOfTriggerPairRedundancies', 'firstUserStoryTriggerPair', and 'secondUserStoryTriggerPair'. The array must contain unique items and can have zero or multiple elements.\n"
        )
        
        self._SYSTEM_SIMULATION_DEFINITION_JSON_FORMAT: str = "I've noted the JSON output format specified and will deliver a valid output. Can you provide some examples?"
        
        self._FILE_PATH_INPUT_EXAMPLES: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompt_examples", "input_examples.json")
        self._FILE_PATH_OUTPUT_EXAMPLES: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompt_examples", "output_examples.json")
        self._json_input_examples: list[dict] = None
        self._json_output_examples: list[dict] = None
        with open(self._FILE_PATH_INPUT_EXAMPLES, 'r', encoding='utf-8') as file:
            self._json_input_examples = json.load(file)
        with open(self._FILE_PATH_OUTPUT_EXAMPLES, 'r', encoding='utf-8') as file:
            self._json_output_examples = json.load(file)

        self._INTRO_OF_EXAMPLES: str = "Yes, here are some examples:"
        
        self._SYSTEM_SIMULATION_EXAMPLE_CONSIDERATION: str = ("Got it. "
                                                              "The examples provided align with the definitions and JSON format description for identifying redundancies in user stories. "
                                                              "Ready to proceed?")

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of PromptHelperBuilder.

        Returns:
            PromptHelperBuilder: The singleton instance of the PromptHelperBuilder class.
        """
        return PromptBuilder()

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
        temp: str = self._SYSTEM_SIMULATION_ACTOR_ROLE
        return {
            "role": "system",
            "content": temp,
        }

    def get_user_story_definition(self) -> dict:
        """
            Returns the user story definition, including redundancy, main part, and relationships.
            
            Returns:
                dict: A dictionary containing the role and content for the user story definition.
        """
        temp: str = self._DEFINITION_US
        return {
            "role": "user",
            "content": temp,
        }

    def get_system_simulation_user_story_definition(self) -> dict:
        """
            Returns the system simulation redundancy definition.
            
            Returns:
                dict: A dictionary containing the role and content for the redundancy definition.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_US
        return {
            "role": "system",
            "content": temp,
        }
        
    def get_task_focus_definition(self) -> dict:
        """
        Constructs a dictionary representing a user's task focus definition. The definition is a 
        concatenation of task-related aspects, including the main part benefit and user story relationships.

        Returns:
            dict: A dictionary with two keys:
                - "role": A string set to "user" indicating the role.
                - "content": A string containing the concatenated task focus definition.
        """
        temp: str = f"{self._TASK_DEFINTION} {self._DEFINITION_FOCUS_ASPECTS_MAIN_PART_BENEFIT} {self._DEFINITION__FOCUS_ASPECTS_USER_STORY_RELATIONSHIPS}"
        return {
            "role": "user",
            "content": temp,
        }

    def get_system_simulation_task_focus_definition(self) -> dict:
        """
        Constructs a dictionary representing a system's simulation task focus definition. The definition
        is based on the user story aspects related to system simulation.

        Returns:
            dict: A dictionary with two keys:
                - "role": A string set to "system" indicating the role.
                - "content": A string containing the system's simulation task focus definition.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_FOCUS_ASPECTS_USER_STORY
        return {
            "role": "system",
            "content": temp,
        }

    def get_redundancy_full_partial_definition(self) -> dict:
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

    def get_system_simulation_redundancy_full_partial_definition(self) -> dict:
        """
            Returns the system simulation definition for partial and full redundancies.
            
            Returns:
                dict: A dictionary containing the role and content for the full and partial redundancy definitions.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_PARTIAL_FULL_REDUNDANCY
        return {
            "role": "system",
            "content": temp,
        }

    def get_json_format_defintion(self) -> dict:
        """
            Returns the JSON schema definition for redundancies in user stories.
            
            Returns:
                dict: A dictionary containing the role and content for the JSON schema definition.
        """
        temp: str = f"{self._INTRODUCING_JSON_FORMAT_DEFINITION}\n{self._DEFINITION_JSON_FORMAT_DEFINITION}"
        return {
            "role": "user",
            "content": temp,
        }

    def get_system_simulation_json_format_defintion(self) -> dict:
        """
            Returns the system simulation JSON format definition.
            
            Returns:
                dict: A dictionary containing the role and content for the JSON format definition.
        """
        temp: str = self._SYSTEM_SIMULATION_DEFINITION_JSON_FORMAT
        return {
            "role": "system",
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
        temp_intro = f"{self._INTRO_OF_EXAMPLES}\n"
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
            "role": "system",
            "content": temp,
        }