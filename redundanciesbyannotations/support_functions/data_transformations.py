import pandas as pd
from itertools import combinations

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