import os
import json

def save_to_json_persistent(folderName: str, json_collection: any):
    base_path = os.getcwd()
    folder_path = base_path + '/results/' + folderName
    os.makedirs(folder_path, exist_ok=True)

    json_file_path:str = ""
    idx: int = 0
    for key in json_collection:
        idx = 0
        while os.path.exists(f"{folder_path}/{idx:02d}_{key}.json"):
            idx += 1
        json_file_path = f"{folder_path}/{idx:02d}_{key}.json"
        with open(json_file_path, 'w') as json_file:
            json.dump(json_collection[key], json_file, indent=4)