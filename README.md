# Abstract
User stories (USs) are a widely used notation for requirements in agile development. 
However, it can easily happen that two USs are redundant, at least partially. 
While some form of redundancy may be acceptable, the user should keep an eye on redundancy in USs for the sake of conciseness and to reduce the risk of inconsistencies.
We present two different approaches to analysing USs for redundancy and compare their potential and limitations.
The first approach translates annotated USs into graph transformation rules, which are then analysed for conflicts to infer redundancies.
The second approach uses a large language model (LLM), here \emph{GPT}, to analyse annotated USs for redundancy. 
We compare the results of these redundancy analyses and discuss their similarities and differences. 
We found that the graph transformation (GT)-based approach is particularly suitable for syntactic analysis, whereas the LLM-based approach seems to find semantic redundancies.
  
## Redundancy Detection with LLMs
Redundant requierments can be paired and between this pairs redundancies can be found. 

We use the User Stories from [nlp-stories](https://github.com/ace-design/nlp-stories/tree/main) and [user story repo](https://zenodo.org/records/8136975) 
We compared our LLM approach against a formal approach from [Alexander Lauer, Amir Rabieyan Nejad, Lukas Hofmann](https://github.com/amirrabieyannejad/USs_Annotation.git) 

## Folder explanation
- Datasets: Contains the annotaited [nlp-stories](https://github.com/ace-design/nlp-stories/tree/main)
- ExperimentsWordSimilarity: Contains a future project ideas
- results: Important results shown in the paper for [MDE Intelligence - 6th Workshop on Artificial Intelligence and Model-driven Engineering](https://mde-intelligence.github.io/)
- src: containg the source code of our implementation. Please, consider for installation our installation and dependecies decriptiong
  - [ ] /controller: Implementation of the Fask API endpoint.
  - [ ] /future_work: Contains future experiments in jupyter notebook form (partly done).
  - [X] /prompt_structure : Containing the prompts used for our expirements.  
  - [X] /results: All results achieved during our developments.
  - [X] /support_functions: As our implementation is based on a functional approach this src folder contains all abstracted functions. 
  - [X] /support_functions_test: Tests for the support functions (pythonic style to organise tests).
  - [X] /utils: Utility functions.
  - [X] /Various Jupyter Notebooks: To connect and execute to our progam logic.
  - [X] /setup.py: -

## IDE + Plugins
- VSCode
- Jupyter
- Jupyter Cell Tags
- Jupyter Keymap
- Pylint
- Pylance
- Python
- Python Debugger
- Python Enviorment Manager

## Dependencies
- Listed in the requirements.txt

## Installation guide
- Install python >= 3.12
- Create a .venv
- pip pip install -r /<usr_path>/requirements.txt
- pip install . in src
- start jupyter notebook in src

## Env.
You have to create a *.env*-file in the *src* folder. The following entries have to be consideres:
- MODEL_VERSION (GPT 3.5 = gpt-3.5-turbo points to gpt-3.5-turbo-0125, GPT-4o = gpt-4o-2024-05-13)
- OPENAI_API_KEY # Enter here your API key
- OUTPUT_EXCEL_NAME_WITHOUT_ANNOTATIONS #Insert here the name of the .xlsx-file which stores the results of results from without annoations
- OUTPUT_EXCEL_NAME_WITH_ANNOTATIONS #Insert here the name of the .xlsx-file which stores the results of results from with annoations
- OUTPUT_EXCEL_NAME_WITH_PLAIN_ANNOTATIONS #Insert here the name of the .xlsx-file which stores the results of results from with plain annoations
- THRESHOLD_REPAIR #Any number of repairs e.g. "3"
- THREADING # "1" = ON, "2" = OFF
- LIMIT  #"-1" =None, ""n" = any number
  

This Repo was creafter for 'Agile Development in the Era of GenAI: Redundancy Analysis of User Stories with Graph Approaches and Large Language Models' for the [MDE Intelligence - 6th Workshop on Artificial Intelligence and Model-driven Engineering](https://mde-intelligence.github.io/)
