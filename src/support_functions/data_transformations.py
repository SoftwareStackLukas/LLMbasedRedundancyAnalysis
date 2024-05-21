import pandas as pd
from itertools import combinations
import json

### This way of working with pandas is not recommend
### It has to be optimized to find a way to store for each text ther enteties and relations

def transform_data(data):
    rows = []
    row_enteties = []
    row_relations = []
    for line in data:
        for entity in line['entities']:
            entity_row = {
                "id": entity["id"],
                "label": entity["label"],
                "start_offset": entity["start_offset"],
                "end_offset": entity["end_offset"]
            }
            row_enteties.append(entity_row)
        for relation in line['relations']:
            relation_row = {
                "id": relation["id"],
                "type": relation["type"],
                "from id": relation["from_id"],
                "to id": relation["to_id"]
            }
            row_relations.append(relation_row)
        row = {
            'ID': line['id'],
            'User Story': line['text'],
            'Enteties': row_enteties,
            'Relations': row_relations
        }
        rows.append(row)
    return pd.DataFrame(rows)


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


def convert_single_entry(item: dict, tiggers: dict, targets: dict, contains: dict) -> str:
    new_data = {
        "PID": item["PID"],
        "User Story Text": item["Text"],
        "Main Part": item["Text"].split(", so that")[0].split("#G04# ")[1],
        "Benefit": item["Benefit"],
        "Triggers": {
            "Main Part": tiggers["mainpart"],
            "Benefit": tiggers["benefit"]
        },
        "Targets": {
            "Main Part": targets["mainpart"],
            "Benefit": targets["benefit"]
        },
        "Contains": {
            "Main Part": contains["mainpart"],
            "Benefit": contains["benefit"]
        }
    }

    return json.dumps(new_data, indent=4)

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
        if trigger[0] in item["Action"]["Primary Action"]:
            triggers["Primary Action"].append(trigger)
        elif trigger[1] == item["Action"]["Benefit"]:
            triggers["Benefit"].append(trigger)
        else:
            raise ValueError("No entry mapped.")
        
    for target in item["Targets"]:
        if target[0] in item["Entity"]["Main Part"]:
            targets["Main Part"].append(target)
        elif target[1] == item["Action"]["Benefit"]:
            targets["Benefit"].append(target)
        else:
            raise ValueError("No entry mapped.")
        
    for contain in item["Contains"]:
        if contain[0] in item["Action"]["Main Part"]:
            triggers["Main Part"].append(contain)
        elif contain[1] == item["Action"]["Benefit"]:
            triggers["Benefit"].append(contain)
        else:
            raise ValueError("No entry mapped.")
    
    return triggers, targets, contains

def convert_annotation_dataset(datasets: dict[list]) -> dict[list]:
    items_to_append: list = []
    current_item: str = None
    for key, item in datasets.items():
        items_to_append.clear()
        for json_entry in item:
            trigger, targets, contains = create_tiggers_targets_contains_mapping(item)
            current_item = convert_single_entry(json_entry, trigger, targets, contains)
            
            items_to_append.append(current_item)
        item.clear()
        item.extend(items_to_append)
        