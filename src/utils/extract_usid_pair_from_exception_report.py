import re
import json

def extract_usid_pair(data: str):
    # Extract the JSON objects from the data
    pattern = re.compile(r'\{.*?\}', re.DOTALL)
    matches = pattern.findall(data)

    extracted_data = []
    for match in matches:
        try:
            json_data = json.loads(match)
            extracted_data.append([int(json_data['USID1']), int(json_data['USID2'])])
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Problematic JSON string: {match}")
    return extracted_data

exception_data_one: str = """
----
{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1099"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1026"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1029"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1031"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1038"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1042"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1044"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1049"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1029"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1030"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1041"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1049"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1106"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1110"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1098"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1039"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1041"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1041"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1068"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1041"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1105"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1105"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1078"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1098"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1078"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1098"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1105"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1106"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1107"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1108"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1122"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1124"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1086", "USID2": "1122"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1093"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1092", "USID2": "1093"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1105"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1110"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1121", "USID2": "1125"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1140", "USID2": "1141"}
------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1148", "USID2": "1150"}
------------
"""

print(extract_usid_pair(exception_data_one))