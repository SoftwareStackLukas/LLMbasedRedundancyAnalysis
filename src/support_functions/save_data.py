import os
import json

def save_to_json_persistent(folder_name: str, json_collection: any):
    base_path: str = os.getcwd()
    folder_path: str = os.path.join(base_path, "results")
    os.makedirs(folder_path, exist_ok=True)
    folder_path += folder_name
    os.makedirs(folder_path, exist_ok=True)

    json_file_path:str = ""
    idx: int = 0
    for key in json_collection:
        idx = 0
        temp: str = os.path.join(folder_path, f"{idx:02d}_{key}.json")
        while os.path.exists(temp):
            idx += 1
            temp = os.path.join(folder_path, f"{idx:02d}_{key}.json")
        json_file_path = temp
        with open(json_file_path, 'w') as json_file:
            json.dump(json_collection[key], json_file, indent=4)