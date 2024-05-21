# Clustering
Redundant requierments can be clustered together 

We use the User Stories from [nlp-stories](https://github.com/ace-design/nlp-stories/tree/main)
We use for the formal approach [Amirs Repo](https://github.com/amirrabieyannejad/USs_Annotation.git) 
 - Linke the project to this project
 - Use either:
     - Git-Submodules
     - Just cloning the importent code

## Env.
You have to create a *.env*-file in the *src* folder. The following entries have to be consideres:
- MODEL_VERSION (GPT 3.5 = gpt-3.5-turbo points to gpt-3.5-turbo-0125, GPT-4o = gpt-4o-2024-05-13)
- OPENAI_API_KEY # Enter here your API key
- OUTPUT_EXCEL_NAME_WITHOUT_ANNOTATIONS #Insert here the name of the .xlsx-file which stores the results of results from without annoations
- OUTPUT_EXCEL_NAME_WITH_ANNOTATIONS #Insert here the name of the .xlsx-file which stores the results of results from with annoations
- THREADING # "1" = ON, "2" = OFF
- LIMIT  #"-1" =None, ""n" = any number
  

This Repo was creafter for 'Insert here the title of the paper' for the [MDE Intelligence - 6th Workshop on Artificial Intelligence and Model-driven Engineering](https://mde-intelligence.github.io/)
