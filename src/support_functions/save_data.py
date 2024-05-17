import os
import json

def save_to_json_persistent(folder_name: str, json_collection: any):
    base_path: str = os.getcwd()
    folder_path: str = os.path.join(base_path, "results", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    unique_json_file_path:str = ""
    idx: int = 0
    for key in json_collection:
        idx = 0
        unique_json_file_path: str = os.path.join(folder_path, f"{idx:02d}_{key}.json")
        while os.path.exists(unique_json_file_path):
            idx += 1
            unique_json_file_path = os.path.join(folder_path, f"{idx:02d}_{key}.json")
        with open(unique_json_file_path, 'w') as json_file:
            json.dump(json_collection[key], json_file, indent=4)
        unique_json_file_path = None