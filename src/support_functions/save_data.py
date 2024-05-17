import os
import json


def save_to_json_persistent(
    folder_name: str, json_collection: any, 
    param_base_path: str = os.getcwd()
):
    """
    Save a collection of JSON serializable objects to files in a specified folder, 
    ensuring unique filenames.

    This function creates a directory structure 
    (if it does not already exist) and writes each item in the
    `json_collection` to a JSON file in the specified folder. 
    If a file with the same name already exists,
    it increments an index to create a unique filename.

    Parameters:
    ----------
    folder_name : str
        The name of the folder where JSON files will be saved. 
        This folder will be created inside a 'results'
        directory in the current working directory.
    json_collection : Union[dict, Any]
        A collection of JSON serializable objects. 
        Each key in the collection will be used as part of the
        filename for the corresponding JSON file.

    Returns:
    -------
    None
    """
    base_path: str = param_base_path
    folder_path: str = os.path.join(base_path, "results", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    unique_json_file_path: str = ""
    idx: int = 0
    for key in json_collection:
        idx = 0
        unique_json_file_path: str = os.path.join(folder_path, f"{idx:02d}_{key}.json")
        while os.path.exists(unique_json_file_path):
            idx += 1
            unique_json_file_path = os.path.join(folder_path, f"{idx:02d}_{key}.json")
        with open(unique_json_file_path, "w") as json_file:
            json.dump(json_collection[key], json_file, indent=4)
        unique_json_file_path = None
