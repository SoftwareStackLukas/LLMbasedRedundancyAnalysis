import os
import jsonlines


def load_datasets_with_annotations() -> dict[str, list]:
    current_directory = os.getcwd()
    suffix = '\\redundanciesbyannotations'
    directory = current_directory[:-len(suffix)] if current_directory.endswith(suffix) else current_directory

    sub_directories = {"g02_federal_funding", "g03_loudoun", "g04_recycling", "g05_open_spending", "g08_frictionless", "g10_scrum_alliance", 
                    "g11_nsf", "g12_camperplus", "g13_planning_poker", "g14_datahub", "g16_mis", "g17_cask", "g18_neurohub", "g19_alfred",
                    "g21_badcamp", "g22_rdadmp", "g23_archives_space", "g24_unibath", "g25_duraspace", "g26_racdam", "g27_culrepo", "g28_zooniverse"}

    datasets: dict = {}
    for sub_directory in sub_directories:
        jsonl_file_path = directory + f"\\Dataset\\doccano_files\\final_annotated_datasets\\{sub_directory}\\admin.jsonl"
        json_data = []
        prefix:str = ""
        with jsonlines.open(jsonl_file_path) as reader:
            for line in reader:
                #the line is interpretated as a dict
                json_data.append(line)
                space_index = line['text'].find(" ")
                #Here the prefix #GXY# will be removed
                if space_index != -1:
                    prefix = line['text'][:space_index]
                    line['text'] = line['text'][len(prefix):] if line['text'].startswith(prefix) else line['text']
                    line['text'] = line['text'].strip()
        key_id:str = prefix
        datasets[key_id] = json_data
    return datasets