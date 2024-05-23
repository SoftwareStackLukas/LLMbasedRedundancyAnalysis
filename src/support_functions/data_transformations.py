from .load_data import load_datasets_with_out_annotations

ONE_WHITESPACE: str = "\u0020"

### Used for Datasets with no modification
def return_usid(DATASET_WITH_ID: dict, story: dict) -> int:
    text1: str = None
    text2: str = None
    local_key: str = None
    for key, _ in DATASET_WITH_ID.items():
        if (str(story["PID"]).lower() in str(key).lower()):
            for item in _:
                local_key = str(key)
                text1 = str(item['text']).lower()
                text2 = str(story['Text']).replace(f"{local_key}{ONE_WHITESPACE}", "").lower()
                if text1 == text2:
                    return int(item['id'])
    raise ValueError(f"No USID found for: {story['Text']}")   

def remove_pov_and_add_usid(dataset: dict) -> dict:
    DATASET_WITH_USID = load_datasets_with_out_annotations()
    
    usid: str = None
    new_entries: list[dict] = []
    for _ in dataset.values():
        for item in _:
            # if "Persona POS" in item:
            #     del item["Persona POS"]
            # if "Action POS" in item:
            #     del item["Action POS"]
            # if "Entity POS" in item:
            #     del item["Entity POS"]
            usid = return_usid(DATASET_WITH_ID=DATASET_WITH_USID, story=item)
            new_entries.append({'usid': usid, **item})
        _.clear()
        _ += new_entries
        new_entries.clear()
    return dataset

### Used for Datasets with reorganizing the datasets for annotations
def convert_single_entry(item: dict, tiggers: dict, targets: dict, contains: dict) -> dict:
    new_data = {
        "PID": item["PID"],
        "USID": "",
        "User Story Text": item["Text"].replace(f"{item["PID"]}{ONE_WHITESPACE}", ""),
        "Main Part": item["Text"].split(", so that")[0].split(f"{item["PID"]}{ONE_WHITESPACE}")[1],
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
        