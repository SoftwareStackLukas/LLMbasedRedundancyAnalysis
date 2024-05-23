import pandas as pd
from itertools import combinations
import json
from .load_data import load_datasets_with_out_annotations

### This way of working with pandas is not recommend
### It has to be optimized to find a way to store for each text ther enteties and relations

def transform_data_id_text(data: list):
    rows = []
    for entry in data:
        row = {
            'ID': entry['id'],
            'User Story': entry['text']
        }
        rows.append(row)
    return pd.DataFrame(rows)

def transform_pairwise(df: pd.DataFrame):
    rows = []
    for i, j in combinations(range(df.shape[0]), 2):
        row = {
            'First ID': df.iloc[i, 0],
            'First User Story': df.iloc[i, 1],
            'Second ID': df.iloc[j, 0],
            'Second User Story': df.iloc[j, 1]
        }
        rows.append(row)
    return pd.DataFrame(rows)

def convert_single_entry(item: dict, tiggers: dict, targets: dict, contains: dict) -> dict:
    new_data = {
        "PID": item["PID"],
        "USID": "",
        "User Story Text": item["Text"].replace(f"{item["PID"]}\u0020", ""),
        "Main Part": item["Text"].split(", so that")[0].split(f"{item["PID"]}\u0020")[1],
        "Benefit": item["Benefit"],
        "Triggers": {
            "Main Part": tiggers["Main Part"],
            "Benefit": tiggers["Benefit"]
        },
        "Targets": {
            "Main Part": targets["Main Part"],
            "Benefit": targets["Benefit"]
        },
        "Contains": {
            "Main Part": contains["Main Part"],
            "Benefit": contains["Benefit"]
        }
    }

    return new_data

def create_tiggers_targets_contains_mapping(item: dict) -> tuple[dict, dict, dict]:
    triggers: dict = {
        "Main Part": [],
        "Benefit": []
    }
    targets: dict = {
        "Main Part": [],
        "Benefit": []
    }
    contains: dict = {
        "Main Part": [],
        "Benefit": []
    }
    
    for trigger in item["Triggers"]:
        if (trigger[0] in item["Persona"] and 
                trigger[1] in item["Action"]["Primary Action"]):
            triggers["Main Part"].append(trigger)
        # elif trigger[1] == item["Action"]["Benefit"]:
        #     triggers["Benefit"].append(trigger)
        else:
            print(f"No entry mapped (trigger). For PID: {item["PID"]} and Text: {item["Text"]}")
            #raise ValueError(f"No entry mapped (trigger). For PID: {item["PID"]} and Text: {item["Text"]}")
        
    for target in item["Targets"]:
        if (target[0] in item["Action"]["Primary Action"] and
                target[1] in item["Entity"]["Primary Entity"]):
            targets["Main Part"].append(target)
        elif (target[0] in item["Action"]["Secondary Action"] and
                target[1] in item["Entity"]["Secondary Entity"]):
            targets["Benefit"].append(target)
        else:
            print(f"No entry mapped (target). For PID: {item["PID"]} and Text: {item["Text"]}")
            #raise ValueError(f"No entry mapped (target). For PID: {item["PID"]} and Text: {item["Text"]}")
        
    for contain in item["Contains"]:
        if (contain[0] in item["Entity"]["Primary Entity"] and
                contain[1] in item["Entity"]["Primary Entity"]):
            triggers["Main Part"].append(contain)
        elif (contain[0] in item["Entity"]["Secondary Entity"] and
                contain[1] in item["Entity"]["Secondary Entity"]):
            triggers["Benefit"].append(contain)
        else:
            print(f"No entry mapped (contains). For PID: {item["PID"]} and Text: {item["Text"]}")
            #raise ValueError(f"No entry mapped (contains). For PID: {item["PID"]} and Text: {item["Text"]}")
    
    return triggers, targets, contains

def convert_annotation_dataset(datasets: dict[list]) -> dict[list]:
    DATASET_WITH_USID = load_datasets_with_out_annotations()
    
    items_to_append: list = []
    current_item: dict = None
    for key, item in datasets.items():
        items_to_append.clear()
        for json_entry in item:
            trigger, targets, contains = create_tiggers_targets_contains_mapping(json_entry)
            current_item = convert_single_entry(json_entry, trigger, targets, contains)
            
            items_to_append.append(current_item)
        item.clear()
        item.extend(items_to_append)
        
    return datasets
        