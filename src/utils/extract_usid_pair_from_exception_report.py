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
------------
Current Exception-Count: 37
----
{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1299", "USID2": "1302"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1225", "USID2": "1226"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1228", "USID2": "1235"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1228", "USID2": "1290"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1232", "USID2": "1281"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1235", "USID2": "1246"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1237", "USID2": "1264"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1242", "USID2": "1243"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1244", "USID2": "1290"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1246", "USID2": "1291"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1246", "USID2": "1294"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1246", "USID2": "1307"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1247", "USID2": "1291"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1250", "USID2": "1291"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1254", "USID2": "1259"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1256", "USID2": "1281"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1263", "USID2": "1281"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1267", "USID2": "1290"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1268", "USID2": "1290"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1270", "USID2": "1271"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1269", "USID2": "1294"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1275", "USID2": "1289"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1275", "USID2": "1287"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1276", "USID2": "1281"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1282", "USID2": "1285"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1285", "USID2": "1288"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1285", "USID2": "1289"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1284", "USID2": "1287"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1285", "USID2": "1290"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1285", "USID2": "1294"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1285", "USID2": "1307"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1287", "USID2": "1291"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1288", "USID2": "1291"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1290", "USID2": "1291"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1291", "USID2": "1296"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1291", "USID2": "1300"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1292", "USID2": "1301"}

------------
"""

exception_data_two: str = """
------------
Current Exception-Count: 165
----
{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1151", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1029"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1025"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1030"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1056"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1024", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1028"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1024", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1026"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1038"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1030"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1029"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1031"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1038"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1031"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1029"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1032"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1030"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1028"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1038"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1126"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1038"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1032", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1032", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1032", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1032", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1042", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1042", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1077"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1046", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1061", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1062", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1062", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1063", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1064", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1064", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1064", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1065", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1066", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1071", "USID2": "1072"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1074", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1075", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1075", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1075", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1075", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1075", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1084", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1084", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1086", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1086", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1092", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1092", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1112"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1106", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1107", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1108", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1108", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1109", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1110", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1115", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1121", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1137", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1139", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1140", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1148", "USID2": "1150"}

------------

"""

exception_data_three: str = """




------------
Current Exception-Count: 1541
----
{"Reason": "Connection error.", "USID1": "1152", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1022"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1021"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1028"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1019"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1026"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1032"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1037"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1036"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1034"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1043"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1066"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1132"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1142"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1145"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1144"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1141"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1138"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1134"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1143"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1137"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1140"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1135"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1136"}

------------



{"Reason": "Connection error.", "USID1": "1018", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1018", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1022"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1026"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1021"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1028"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1033"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1034"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1035"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1038"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1037"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1050"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1069"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1019", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1033"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1036"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1131"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1020", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1029"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1022"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1025"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1031"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1028"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1033"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1036"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1037"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1035"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1038"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1043"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1056"}

------------



{"Reason": "ValueError", "USID1": "1021", "USID2": "1023"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1048"}

------------



{"Reason": "ValueError", "USID1": "1021", "USID2": "1034"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1052"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1058"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1062"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1069"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1071"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1086"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1097"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1112"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1131"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1126"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1021", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1033"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1048"}

------------



{"Reason": "ValueError", "USID1": "1021", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1050"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1022", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1023", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1023", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1023", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1023", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1023", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1024", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1027"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1034"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1025", "USID2": "1132"}

------------



{"Reason": "ValueError", "USID1": "1025", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1028"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1029"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1033"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1037"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1061"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1109"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1030"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1026", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1031"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1056"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1027", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1033"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1028", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1033"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1029", "USID2": "1131"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1030", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1031", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1031", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1031", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1032", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1032", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1038"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1035"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1043"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1037"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1047"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1046"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1050"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1051"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1058"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1055"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1061"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1056"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1067"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1063"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1065"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1073"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1069"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1077"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1097"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1109"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1153"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1033", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1037"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1046"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1051"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1050"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1056"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1061"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1066"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1073"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1096"}

------------



{"Reason": "ValueError", "USID1": "1034", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1034", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1055"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1035", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1036", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1036", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1036", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1036", "USID2": "1126"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1039"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1062"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1091"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1037", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1042"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1043"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1050"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1040"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1046"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1038", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1056"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1063"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1067"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1069"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1090"}

------------



{"Reason": "ValueError", "USID1": "1039", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1039", "USID2": "1142"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1041"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1044"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1056"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1065"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1072"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1112"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1142"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1040", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1051"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1056"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1065"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1061"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1062"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1073"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1069"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1072"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1089"}

------------



{"Reason": "ValueError", "USID1": "1041", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1105"}

------------



{"Reason": "ValueError", "USID1": "1041", "USID2": "1079"}

------------



{"Reason": "ValueError", "USID1": "1041", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1142"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1041", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1042", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1042", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1042", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1042", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1042", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1043", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1043", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1043", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1043", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1050"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1051"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1045"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1048"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1066"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1109"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1044", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1045", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1046", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1046", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1046", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1046", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1047", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1047", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1047", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1047", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1049"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1051"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1061"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1066"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1073"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1048", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1053"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1061"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1097"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1131"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1049", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1051"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1065"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1076"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1120"}

------------



{"Reason": "ValueError", "USID1": "1050", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1050", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1067"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1051", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1052", "USID2": "1054"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1052", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1052", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1052", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1052", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1052", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1097"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1053", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1063"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1059"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1067"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1072"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1077"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1097"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1054", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1056", "USID2": "1057"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1056", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1056", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1056", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1056", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1056", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1060"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1065"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1063"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1061"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1066"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1077"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1069"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1068"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1109"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1112"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1057", "USID2": "1153"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1058", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1058", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1067"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1059", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1064"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1060", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1061", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1061", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1062", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1063", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1064", "USID2": "1077"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1064", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1064", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1065", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1065", "USID2": "1153"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1066", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1066", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1067", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1067", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1067", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1067", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1068", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1069", "USID2": "1070"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1069", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1069", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1069", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1069", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1069", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1070", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1071", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1071", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1073"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1077"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1074"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1081"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1109"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1112"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1126"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1142"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1072", "USID2": "1153"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1075"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1073", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1074", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1074", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1075", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1075", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1078"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1076", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1077", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1079"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1082"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1080"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1089"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1084"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1085"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1078", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1079", "USID2": "1083"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1079", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1079", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1079", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1080", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1080", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1081", "USID2": "1086"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1081", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1081", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1081", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1081", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1082", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1088"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1083", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1084", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1084", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1084", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1084", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1087"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1085", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1086", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1086", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1094"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1098"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1087", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1095"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1088", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1090"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1092"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1089", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1090", "USID2": "1097"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1090", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1090", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1090", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1090", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1090", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1090", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1092", "USID2": "1093"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1092", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1092", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1092", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1093", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1093", "USID2": "1102"}

------------



{"Reason": "Request timed out.", "USID1": "1093", "USID2": "1119"}

------------



{"Reason": "Connection error.", "USID1": "1093", "USID2": "1118"}

------------



{"Reason": "Connection error.", "USID1": "1093", "USID2": "1121"}

------------



{"Reason": "Connection error.", "USID1": "1093", "USID2": "1120"}

------------



{"Reason": "Connection error.", "USID1": "1093", "USID2": "1117"}

------------



{"Reason": "Connection error.", "USID1": "1093", "USID2": "1106"}

------------



{"Reason": "Connection error.", "USID1": "1093", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1093", "USID2": "1131"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1093", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1093", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1093", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1094", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1094", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1094", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1094", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1096"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1100"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1105"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1095", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1102"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1133"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1096", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1099"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1101"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1097", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1098", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1099", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1100", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1100", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1100", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1103"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1105"}

------------



{"Reason": "ValueError", "USID1": "1101", "USID2": "1106"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1125"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1130"}

------------



{"Reason": "ValueError", "USID1": "1101", "USID2": "1117"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1135"}

------------



{"Reason": "ValueError", "USID1": "1101", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1101", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1104"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1110"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1108"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1109"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1112"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1115"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1122"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1126"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1129"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1131"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1142"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1102", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1103", "USID2": "1111"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1103", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1103", "USID2": "1119"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1103", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1103", "USID2": "1132"}

------------



{"Reason": "ValueError", "USID1": "1103", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1103", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1103", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1104", "USID2": "1107"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1104", "USID2": "1118"}

------------



{"Reason": "ValueError", "USID1": "1103", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1104", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1104", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1104", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1104", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1105", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1106", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1106", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1106", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1107", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1108", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1108", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1109", "USID2": "1113"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1109", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1109", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1109", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1114"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1116"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1124"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1126"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1152"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1111", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1113", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1114", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1114", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1114", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1114", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1114", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1115", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1118"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1127"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1116", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1117", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1120"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1123"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1121"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1133"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1148"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1119", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1136"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1120", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1121", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1121", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1124", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1124", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1125", "USID2": "1126"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1125", "USID2": "1128"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1125", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1125", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1125", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1126", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1126", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1126", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1126", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1126", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1127", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1128", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1128", "USID2": "1139"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1128", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1128", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1129", "USID2": "1130"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1129", "USID2": "1137"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1129", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1129", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1129", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1130", "USID2": "1135"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1129", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1130", "USID2": "1146"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1130", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1130", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1130", "USID2": "1149"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1131", "USID2": "1132"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1131", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1130", "USID2": "1155"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1131", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1131", "USID2": "1140"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1131", "USID2": "1144"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1131", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1132", "USID2": "1134"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1132", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1132", "USID2": "1138"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1132", "USID2": "1145"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1132", "USID2": "1151"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1136", "USID2": "1143"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1137", "USID2": "1147"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1138", "USID2": "1141"}

------------



{"Reason": "Not stopped exception from ChatGPT Endpoint", "USID1": "1138", "USID2": "1143"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1144"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1138", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1141"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1144"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1143"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1142"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1140"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1145"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1139", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1141"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1142"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1145"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1144"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1143"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1140", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1142"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1143"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1144"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1145"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1141", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1143"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1145"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1144"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1144"}

------------



{"Reason": "Connection error.", "USID1": "1142", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1145"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1143", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1145"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1144", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1146"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1145", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1147"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1147", "USID2": "1148"}

------------



{"Reason": "Connection error.", "USID1": "1146", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1147", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1147", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1147", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1147", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1147", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1147", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1148", "USID2": "1149"}

------------



{"Reason": "Connection error.", "USID1": "1148", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1148", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1148", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1148", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1148", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1149", "USID2": "1150"}

------------



{"Reason": "Connection error.", "USID1": "1149", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1149", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1149", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1150", "USID2": "1151"}

------------



{"Reason": "Connection error.", "USID1": "1149", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1150", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1150", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1150", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1151", "USID2": "1152"}

------------



{"Reason": "Connection error.", "USID1": "1151", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1151", "USID2": "1155"}

------------



{"Reason": "Connection error.", "USID1": "1152", "USID2": "1153"}

------------



{"Reason": "Connection error.", "USID1": "1153", "USID2": "1155"}

------------

"""

# temp = extract_usid_pair(exception_data_one)
# print(temp)
# # From Exception Data 1 (G22): [[1299, 1302], [1225, 1226], [1228, 1235], [1228, 1290], [1232, 1281], [1235, 1246], [1237, 1264], [1242, 1243], [1244, 1290], [1246, 1291], [1246, 1294], [1246, 1307], [1247, 1291], [1250, 1291], [1254, 1259], [1256, 1281], [1263, 1281], [1267, 1290], [1268, 1290], [1270, 1271], [1269, 1294], [1275, 1289], [1275, 1287], [1276, 1281], [1282, 1285], [1285, 1288], [1285, 1289], [1284, 1287], [1285, 1290], [1285, 1294], [1285, 1307], [1287, 1291], [1288, 1291], [1290, 1291], [1291, 1296], [1291, 1300], [1292, 1301]]

# print("\n\n")

# # {"Reason": "Error code: 400 - {'error': {'message': \"This model's maximum context length is 16385 tokens. However, your messages resulted in 16609 tokens. Please reduce the length of the messages.\", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}", "USID1": "1026", "USID2": "1115"} 

# temp = extract_usid_pair(exception_data_two)
# print(temp)
# From Exception Data 2 (G19): [[1151, 1155], [1019, 1029], [1019, 1085], [1021, 1059], [1021, 1081], [1021, 1087], [1022, 1039], [1022, 1025], [1022, 1030], [1022, 1056], [1022, 1099], [1024, 1045], [1025, 1028], [1024, 1115], [1025, 1026], [1025, 1038], [1025, 1116], [1026, 1030], [1026, 1029], [1026, 1031], [1026, 1040], [1026, 1038], [1026, 1042], [1026, 1045], [1026, 1049], [1026, 1044], [1026, 1075], [1026, 1107], [1026, 1105], [1026, 1106], [1026, 1108], [1026, 1129], [1027, 1031], [1027, 1029], [1027, 1032], [1027, 1030], [1027, 1028], [1027, 1038], [1027, 1041], [1027, 1040], [1027, 1048], [1027, 1045], [1027, 1049], [1027, 1106], [1027, 1108], [1027, 1110], [1027, 1107], [1027, 1098], [1027, 1122], [1027, 1126], [1027, 1128], [1028, 1041], [1028, 1039], [1028, 1044], [1028, 1098], [1028, 1105], [1029, 1038], [1029, 1039], [1029, 1068], [1030, 1040], [1030, 1041], [1032, 1039], [1032, 1040], [1032, 1078], [1032, 1115], [1037, 1042], [1037, 1049], [1037, 1045], [1037, 1125], [1038, 1105], [1039, 1041], [1039, 1068], [1039, 1124], [1040, 1041], [1040, 1049], [1040, 1068], [1040, 1075], [1040, 1115], [1041, 1105], [1041, 1106], [1042, 1048], [1042, 1049], [1045, 1077], [1046, 1098], [1048, 1075], [1048, 1105], [1048, 1106], [1049, 1075], [1049, 1103], [1049, 1106], [1049, 1105], [1053, 1085], [1054, 1085], [1057, 1089], [1057, 1121], [1057, 1135], [1059, 1087], [1059, 1098], [1061, 1134], [1062, 1090], [1062, 1091], [1063, 1091], [1064, 1081], [1064, 1088], [1064, 1090], [1065, 1090], [1066, 1090], [1068, 1075], [1068, 1078], [1068, 1098], [1068, 1125], [1071, 1072], [1073, 1091], [1073, 1093], [1074, 1129], [1075, 1108], [1075, 1106], [1075, 1116], [1075, 1119], [1075, 1125], [1076, 1078], [1077, 1078], [1077, 1091], [1077, 1098], [1077, 1110], [1077, 1119], [1078, 1108], [1078, 1105], [1078, 1106], [1078, 1107], [1078, 1122], [1078, 1124], [1078, 1121], [1084, 1085], [1084, 1120], [1086, 1121], [1086, 1122], [1087, 1093], [1088, 1090], [1089, 1091], [1089, 1093], [1089, 1095], [1092, 1095], [1092, 1093], [1098, 1106], [1098, 1105], [1098, 1110], [1098, 1112], [1098, 1115], [1098, 1122], [1106, 1116], [1107, 1129], [1108, 1134], [1108, 1129], [1109, 1134], [1110, 1129], [1111, 1129], [1115, 1134], [1116, 1119], [1121, 1125], [1137, 1140], [1139, 1146], [1140, 1141], [1148, 1150], [1026, 1115]]

temp = extract_usid_pair(exception_data_three)
print(temp)
# From Exception Data 3 (G19 + text): [[1152, 1155], [1018, 1022], [1018, 1021], [1018, 1028], [1018, 1019], [1018, 1026], [1018, 1032], [1018, 1042], [1018, 1041], [1018, 1037], [1018, 1036], [1018, 1034], [1018, 1043], [1018, 1045], [1018, 1044], [1018, 1048], [1018, 1057], [1018, 1053], [1018, 1066], [1018, 1070], [1018, 1074], [1018, 1079], [1018, 1078], [1018, 1080], [1018, 1083], [1018, 1085], [1018, 1103], [1018, 1094], [1018, 1104], [1018, 1106], [1018, 1125], [1018, 1129], [1018, 1132], [1018, 1142], [1018, 1145], [1018, 1144], [1018, 1141], [1018, 1138], [1018, 1134], [1018, 1143], [1018, 1137], [1018, 1140], [1018, 1135], [1018, 1136], [1018, 1139], [1018, 1151], [1018, 1147], [1018, 1152], [1019, 1022], [1019, 1026], [1019, 1021], [1019, 1028], [1019, 1033], [1019, 1034], [1019, 1035], [1019, 1038], [1019, 1037], [1019, 1041], [1019, 1040], [1019, 1039], [1019, 1048], [1019, 1050], [1019, 1053], [1019, 1059], [1019, 1069], [1019, 1080], [1019, 1083], [1019, 1085], [1019, 1102], [1019, 1101], [1019, 1114], [1019, 1125], [1019, 1108], [1019, 1118], [1019, 1134], [1019, 1132], [1019, 1139], [1019, 1143], [1019, 1148], [1019, 1149], [1020, 1033], [1020, 1036], [1020, 1039], [1020, 1041], [1020, 1054], [1020, 1085], [1020, 1131], [1020, 1130], [1021, 1029], [1021, 1022], [1021, 1025], [1021, 1031], [1021, 1028], [1021, 1033], [1021, 1036], [1021, 1037], [1021, 1035], [1021, 1042], [1021, 1040], [1021, 1039], [1021, 1041], [1021, 1038], [1021, 1043], [1021, 1044], [1021, 1045], [1021, 1056], [1021, 1023], [1021, 1048], [1021, 1034], [1021, 1054], [1021, 1052], [1021, 1053], [1021, 1058], [1021, 1060], [1021, 1062], [1021, 1064], [1021, 1068], [1021, 1069], [1021, 1070], [1021, 1071], [1021, 1074], [1021, 1076], [1021, 1075], [1021, 1080], [1021, 1084], [1021, 1079], [1021, 1082], [1021, 1083], [1021, 1087], [1021, 1078], [1021, 1090], [1021, 1088], [1021, 1086], [1021, 1091], [1021, 1094], [1021, 1096], [1021, 1092], [1021, 1093], [1021, 1101], [1021, 1097], [1021, 1103], [1021, 1105], [1021, 1098], [1021, 1100], [1021, 1111], [1021, 1107], [1021, 1108], [1021, 1112], [1021, 1115], [1021, 1116], [1021, 1117], [1021, 1118], [1021, 1113], [1021, 1120], [1021, 1119], [1021, 1121], [1021, 1123], [1021, 1125], [1021, 1124], [1021, 1131], [1021, 1130], [1021, 1138], [1021, 1132], [1021, 1137], [1021, 1128], [1021, 1126], [1021, 1134], [1021, 1140], [1021, 1135], [1021, 1136], [1021, 1139], [1021, 1151], [1021, 1144], [1021, 1145], [1021, 1143], [1021, 1149], [1022, 1033], [1022, 1041], [1022, 1044], [1022, 1048], [1021, 1147], [1022, 1050], [1022, 1053], [1022, 1083], [1022, 1085], [1022, 1101], [1022, 1110], [1022, 1130], [1022, 1145], [1022, 1149], [1023, 1040], [1023, 1057], [1023, 1102], [1023, 1111], [1023, 1130], [1024, 1090], [1025, 1027], [1025, 1034], [1025, 1070], [1025, 1103], [1025, 1114], [1025, 1118], [1025, 1132], [1025, 1080], [1026, 1028], [1026, 1029], [1026, 1033], [1026, 1048], [1026, 1041], [1026, 1045], [1026, 1037], [1026, 1044], [1026, 1060], [1026, 1059], [1026, 1061], [1026, 1081], [1026, 1076], [1026, 1078], [1026, 1088], [1026, 1108], [1026, 1105], [1026, 1110], [1026, 1098], [1026, 1109], [1026, 1116], [1026, 1115], [1026, 1139], [1027, 1030], [1027, 1042], [1026, 1143], [1027, 1040], [1026, 1155], [1027, 1039], [1027, 1041], [1027, 1031], [1027, 1056], [1027, 1076], [1027, 1080], [1027, 1103], [1027, 1122], [1027, 1106], [1027, 1128], [1027, 1129], [1028, 1033], [1028, 1103], [1028, 1130], [1028, 1149], [1029, 1039], [1029, 1033], [1029, 1042], [1029, 1040], [1029, 1070], [1029, 1078], [1029, 1102], [1029, 1114], [1029, 1138], [1029, 1131], [1030, 1039], [1030, 1049], [1030, 1068], [1030, 1057], [1030, 1103], [1030, 1144], [1030, 1143], [1031, 1103], [1031, 1132], [1031, 1115], [1032, 1089], [1032, 1113], [1033, 1040], [1033, 1041], [1033, 1038], [1033, 1035], [1033, 1043], [1033, 1042], [1033, 1037], [1033, 1039], [1033, 1044], [1033, 1047], [1033, 1046], [1033, 1050], [1033, 1051], [1033, 1049], [1033, 1057], [1033, 1058], [1033, 1060], [1033, 1054], [1033, 1059], [1033, 1055], [1033, 1061], [1033, 1056], [1033, 1053], [1033, 1067], [1033, 1063], [1033, 1065], [1033, 1074], [1033, 1068], [1033, 1073], [1033, 1070], [1033, 1069], [1033, 1076], [1033, 1077], [1033, 1075], [1033, 1078], [1033, 1079], [1033, 1082], [1033, 1081], [1033, 1083], [1033, 1084], [1033, 1085], [1033, 1091], [1033, 1088], [1033, 1090], [1033, 1089], [1033, 1093], [1033, 1094], [1033, 1095], [1033, 1092], [1033, 1096], [1033, 1097], [1033, 1099], [1033, 1100], [1033, 1101], [1033, 1103], [1033, 1104], [1033, 1106], [1033, 1105], [1033, 1107], [1033, 1109], [1033, 1111], [1033, 1119], [1033, 1110], [1033, 1116], [1033, 1113], [1033, 1118], [1033, 1117], [1033, 1115], [1033, 1123], [1033, 1120], [1033, 1125], [1033, 1122], [1033, 1127], [1033, 1124], [1033, 1129], [1033, 1136], [1033, 1130], [1033, 1128], [1033, 1132], [1033, 1141], [1033, 1137], [1033, 1139], [1033, 1140], [1033, 1138], [1033, 1143], [1033, 1145], [1033, 1146], [1033, 1147], [1033, 1149], [1033, 1153], [1033, 1155], [1033, 1151], [1034, 1037], [1034, 1044], [1034, 1039], [1034, 1046], [1034, 1051], [1034, 1049], [1034, 1048], [1034, 1050], [1034, 1054], [1034, 1056], [1034, 1059], [1034, 1061], [1034, 1068], [1034, 1066], [1034, 1076], [1034, 1073], [1034, 1074], [1034, 1084], [1034, 1080], [1034, 1083], [1034, 1082], [1034, 1088], [1034, 1085], [1034, 1089], [1034, 1087], [1034, 1090], [1034, 1094], [1034, 1092], [1034, 1096], [1034, 1079], [1034, 1095], [1034, 1098], [1034, 1103], [1034, 1116], [1034, 1111], [1034, 1118], [1034, 1127], [1034, 1123], [1034, 1130], [1034, 1120], [1034, 1124], [1034, 1129], [1034, 1136], [1034, 1139], [1034, 1138], [1034, 1140], [1034, 1151], [1034, 1145], [1034, 1149], [1034, 1147], [1034, 1155], [1035, 1039], [1035, 1048], [1035, 1055], [1035, 1057], [1035, 1078], [1035, 1085], [1035, 1101], [1035, 1129], [1035, 1145], [1036, 1060], [1036, 1092], [1036, 1101], [1036, 1126], [1037, 1039], [1037, 1041], [1037, 1044], [1037, 1054], [1037, 1059], [1037, 1062], [1037, 1080], [1037, 1085], [1037, 1104], [1037, 1091], [1037, 1106], [1037, 1118], [1037, 1115], [1037, 1120], [1037, 1128], [1037, 1139], [1037, 1144], [1037, 1145], [1038, 1040], [1038, 1042], [1038, 1043], [1038, 1050], [1038, 1054], [1038, 1057], [1038, 1078], [1038, 1083], [1038, 1085], [1038, 1103], [1038, 1101], [1038, 1119], [1038, 1118], [1038, 1129], [1039, 1040], [1039, 1041], [1038, 1145], [1039, 1046], [1038, 1155], [1039, 1054], [1039, 1056], [1039, 1053], [1039, 1070], [1039, 1063], [1039, 1067], [1039, 1057], [1039, 1069], [1039, 1075], [1039, 1079], [1039, 1082], [1039, 1085], [1039, 1078], [1039, 1095], [1039, 1089], [1039, 1090], [1039, 1064], [1039, 1092], [1039, 1096], [1039, 1101], [1039, 1111], [1039, 1099], [1039, 1106], [1039, 1119], [1039, 1118], [1039, 1124], [1039, 1136], [1039, 1132], [1039, 1137], [1039, 1130], [1039, 1127], [1039, 1139], [1039, 1129], [1039, 1142], [1040, 1041], [1040, 1054], [1040, 1045], [1040, 1044], [1040, 1056], [1040, 1065], [1040, 1068], [1040, 1072], [1040, 1074], [1040, 1079], [1040, 1082], [1040, 1080], [1040, 1092], [1040, 1101], [1040, 1100], [1040, 1096], [1040, 1106], [1040, 1111], [1040, 1103], [1040, 1112], [1040, 1095], [1040, 1115], [1040, 1120], [1040, 1132], [1040, 1123], [1040, 1127], [1040, 1135], [1040, 1128], [1040, 1130], [1040, 1137], [1040, 1144], [1040, 1129], [1040, 1142], [1040, 1145], [1040, 1143], [1041, 1049], [1041, 1051], [1041, 1056], [1041, 1053], [1041, 1054], [1041, 1064], [1041, 1065], [1041, 1061], [1041, 1062], [1041, 1076], [1041, 1073], [1041, 1069], [1041, 1072], [1041, 1070], [1041, 1068], [1041, 1078], [1041, 1084], [1041, 1082], [1041, 1089], [1041, 1074], [1041, 1099], [1041, 1101], [1041, 1103], [1041, 1106], [1041, 1105], [1041, 1079], [1041, 1094], [1041, 1118], [1041, 1127], [1041, 1117], [1041, 1120], [1041, 1119], [1041, 1130], [1041, 1124], [1041, 1132], [1041, 1137], [1041, 1135], [1041, 1145], [1041, 1139], [1041, 1142], [1041, 1138], [1041, 1147], [1042, 1096], [1042, 1103], [1042, 1130], [1042, 1145], [1042, 1151], [1043, 1085], [1043, 1102], [1043, 1118], [1043, 1145], [1044, 1049], [1044, 1050], [1044, 1051], [1044, 1045], [1044, 1048], [1044, 1054], [1044, 1053], [1044, 1057], [1044, 1060], [1044, 1064], [1044, 1066], [1044, 1070], [1044, 1074], [1044, 1079], [1044, 1080], [1044, 1083], [1044, 1101], [1044, 1106], [1044, 1111], [1044, 1105], [1044, 1109], [1044, 1117], [1044, 1110], [1044, 1125], [1044, 1121], [1044, 1129], [1044, 1132], [1044, 1139], [1044, 1138], [1044, 1149], [1044, 1152], [1045, 1054], [1045, 1053], [1045, 1057], [1045, 1070], [1045, 1080], [1045, 1088], [1045, 1103], [1045, 1102], [1045, 1111], [1045, 1132], [1045, 1135], [1045, 1151], [1046, 1057], [1046, 1104], [1046, 1130], [1046, 1145], [1047, 1054], [1047, 1102], [1047, 1111], [1047, 1118], [1048, 1049], [1048, 1051], [1048, 1060], [1048, 1057], [1048, 1054], [1048, 1061], [1048, 1066], [1048, 1068], [1048, 1070], [1048, 1074], [1048, 1073], [1048, 1079], [1048, 1075], [1048, 1076], [1048, 1080], [1048, 1081], [1048, 1083], [1048, 1084], [1048, 1085], [1048, 1087], [1048, 1090], [1048, 1103], [1048, 1095], [1048, 1096], [1048, 1099], [1048, 1098], [1048, 1120], [1048, 1111], [1048, 1116], [1048, 1119], [1048, 1121], [1048, 1127], [1048, 1134], [1048, 1136], [1048, 1137], [1048, 1139], [1048, 1144], [1048, 1147], [1048, 1152], [1048, 1151], [1049, 1057], [1049, 1053], [1049, 1054], [1049, 1061], [1049, 1064], [1049, 1059], [1049, 1060], [1049, 1087], [1049, 1078], [1049, 1080], [1049, 1083], [1049, 1089], [1049, 1090], [1049, 1092], [1049, 1095], [1049, 1097], [1049, 1117], [1049, 1107], [1049, 1119], [1049, 1111], [1049, 1120], [1049, 1114], [1049, 1115], [1049, 1118], [1049, 1125], [1049, 1121], [1049, 1123], [1049, 1135], [1049, 1127], [1049, 1128], [1049, 1131], [1049, 1134], [1049, 1139], [1049, 1144], [1049, 1147], [1049, 1151], [1050, 1051], [1050, 1054], [1050, 1065], [1050, 1076], [1050, 1070], [1050, 1083], [1050, 1099], [1050, 1120], [1050, 1111], [1050, 1128], [1050, 1138], [1050, 1146], [1050, 1149], [1050, 1148], [1051, 1067], [1051, 1059], [1051, 1093], [1051, 1078], [1051, 1085], [1051, 1092], [1051, 1103], [1051, 1102], [1051, 1108], [1051, 1111], [1051, 1118], [1051, 1115], [1051, 1130], [1051, 1122], [1051, 1134], [1051, 1135], [1051, 1145], [1051, 1147], [1052, 1054], [1052, 1082], [1052, 1078], [1052, 1104], [1052, 1138], [1052, 1151], [1053, 1060], [1053, 1070], [1053, 1068], [1053, 1080], [1053, 1078], [1053, 1081], [1053, 1085], [1053, 1090], [1053, 1093], [1053, 1095], [1053, 1097], [1053, 1101], [1053, 1104], [1053, 1111], [1053, 1114], [1053, 1118], [1053, 1130], [1053, 1138], [1053, 1144], [1053, 1139], [1053, 1143], [1053, 1145], [1053, 1149], [1053, 1151], [1054, 1063], [1054, 1059], [1054, 1060], [1054, 1064], [1054, 1067], [1054, 1057], [1054, 1068], [1054, 1070], [1054, 1074], [1054, 1072], [1054, 1075], [1054, 1077], [1054, 1078], [1054, 1080], [1054, 1083], [1054, 1081], [1054, 1088], [1054, 1087], [1054, 1090], [1054, 1097], [1054, 1093], [1054, 1095], [1054, 1096], [1054, 1103], [1054, 1107], [1054, 1108], [1054, 1115], [1054, 1117], [1054, 1116], [1054, 1125], [1054, 1118], [1054, 1123], [1054, 1128], [1054, 1129], [1054, 1132], [1054, 1135], [1054, 1137], [1054, 1139], [1054, 1140], [1054, 1143], [1054, 1145], [1054, 1149], [1054, 1147], [1054, 1151], [1054, 1155], [1056, 1057], [1056, 1082], [1056, 1068], [1056, 1093], [1056, 1102], [1056, 1114], [1057, 1060], [1057, 1064], [1057, 1065], [1057, 1063], [1057, 1061], [1057, 1066], [1057, 1077], [1057, 1070], [1057, 1082], [1057, 1069], [1057, 1080], [1057, 1068], [1057, 1079], [1057, 1074], [1057, 1078], [1057, 1089], [1057, 1083], [1057, 1088], [1057, 1084], [1057, 1087], [1057, 1085], [1057, 1101], [1057, 1107], [1057, 1096], [1057, 1108], [1057, 1105], [1057, 1103], [1057, 1100], [1057, 1098], [1057, 1109], [1057, 1115], [1057, 1119], [1057, 1118], [1057, 1124], [1057, 1113], [1057, 1116], [1057, 1117], [1057, 1112], [1057, 1123], [1057, 1121], [1057, 1137], [1057, 1130], [1057, 1128], [1057, 1127], [1057, 1134], [1057, 1136], [1057, 1129], [1057, 1141], [1057, 1140], [1057, 1145], [1057, 1139], [1057, 1146], [1057, 1143], [1057, 1144], [1057, 1147], [1057, 1151], [1057, 1155], [1057, 1149], [1057, 1153], [1058, 1085], [1058, 1130], [1059, 1067], [1059, 1099], [1059, 1103], [1059, 1125], [1059, 1130], [1059, 1144], [1059, 1148], [1059, 1145], [1059, 1151], [1059, 1152], [1059, 1149], [1060, 1064], [1060, 1074], [1060, 1075], [1060, 1078], [1060, 1084], [1060, 1111], [1060, 1118], [1060, 1138], [1060, 1130], [1060, 1145], [1060, 1141], [1060, 1147], [1061, 1090], [1061, 1139], [1062, 1130], [1063, 1145], [1064, 1077], [1064, 1098], [1064, 1101], [1065, 1113], [1065, 1153], [1066, 1093], [1066, 1114], [1067, 1070], [1067, 1102], [1067, 1118], [1067, 1130], [1068, 1103], [1068, 1120], [1068, 1113], [1068, 1132], [1069, 1070], [1069, 1085], [1069, 1088], [1069, 1102], [1069, 1111], [1069, 1118], [1070, 1078], [1070, 1083], [1070, 1085], [1070, 1095], [1070, 1101], [1070, 1111], [1070, 1118], [1070, 1138], [1070, 1139], [1070, 1149], [1071, 1123], [1071, 1124], [1072, 1073], [1072, 1075], [1072, 1077], [1072, 1078], [1072, 1074], [1072, 1079], [1072, 1080], [1072, 1081], [1072, 1084], [1072, 1082], [1072, 1083], [1072, 1087], [1072, 1090], [1072, 1094], [1072, 1092], [1072, 1085], [1072, 1093], [1072, 1095], [1072, 1096], [1072, 1099], [1072, 1100], [1072, 1102], [1072, 1103], [1072, 1105], [1072, 1109], [1072, 1108], [1072, 1107], [1072, 1112], [1072, 1110], [1072, 1111], [1072, 1115], [1072, 1114], [1072, 1116], [1072, 1117], [1072, 1118], [1072, 1119], [1072, 1125], [1072, 1124], [1072, 1122], [1072, 1126], [1072, 1129], [1072, 1128], [1072, 1130], [1072, 1132], [1072, 1134], [1072, 1135], [1072, 1139], [1072, 1138], [1072, 1145], [1072, 1144], [1072, 1142], [1072, 1140], [1072, 1146], [1072, 1141], [1072, 1148], [1072, 1151], [1072, 1152], [1072, 1155], [1072, 1153], [1073, 1075], [1073, 1101], [1073, 1103], [1073, 1102], [1073, 1114], [1073, 1118], [1073, 1151], [1074, 1090], [1074, 1093], [1075, 1123], [1075, 1135], [1076, 1078], [1076, 1090], [1076, 1093], [1076, 1102], [1076, 1118], [1076, 1129], [1076, 1139], [1076, 1145], [1076, 1148], [1076, 1151], [1077, 1111], [1077, 1143], [1078, 1079], [1078, 1082], [1078, 1080], [1078, 1089], [1078, 1084], [1078, 1088], [1078, 1083], [1078, 1087], [1078, 1085], [1078, 1093], [1078, 1096], [1078, 1090], [1078, 1094], [1078, 1095], [1078, 1098], [1078, 1092], [1078, 1099], [1078, 1101], [1078, 1100], [1078, 1106], [1078, 1103], [1078, 1119], [1078, 1105], [1078, 1113], [1078, 1118], [1078, 1115], [1078, 1116], [1078, 1123], [1078, 1124], [1078, 1127], [1078, 1130], [1078, 1128], [1078, 1137], [1078, 1141], [1078, 1144], [1078, 1139], [1079, 1083], [1079, 1102], [1079, 1116], [1079, 1118], [1080, 1101], [1080, 1138], [1081, 1086], [1081, 1100], [1081, 1111], [1081, 1119], [1081, 1144], [1082, 1090], [1083, 1088], [1083, 1093], [1083, 1101], [1083, 1106], [1083, 1118], [1083, 1124], [1083, 1127], [1083, 1138], [1084, 1095], [1084, 1111], [1084, 1132], [1084, 1145], [1085, 1087], [1085, 1093], [1085, 1092], [1085, 1118], [1085, 1121], [1085, 1135], [1085, 1144], [1085, 1147], [1085, 1145], [1085, 1151], [1086, 1130], [1086, 1141], [1087, 1095], [1087, 1094], [1087, 1093], [1087, 1098], [1087, 1104], [1087, 1100], [1087, 1106], [1087, 1101], [1087, 1103], [1087, 1111], [1087, 1115], [1087, 1118], [1087, 1136], [1087, 1137], [1087, 1128], [1087, 1130], [1087, 1134], [1087, 1138], [1087, 1145], [1088, 1095], [1088, 1101], [1088, 1106], [1088, 1119], [1088, 1110], [1088, 1130], [1088, 1123], [1088, 1135], [1088, 1144], [1088, 1145], [1088, 1147], [1088, 1146], [1088, 1151], [1089, 1090], [1089, 1101], [1089, 1092], [1089, 1114], [1090, 1097], [1090, 1130], [1090, 1125], [1090, 1132], [1090, 1138], [1090, 1144], [1090, 1143], [1092, 1093], [1092, 1103], [1092, 1134], [1092, 1145], [1093, 1104], [1093, 1102], [1093, 1119], [1093, 1118], [1093, 1121], [1093, 1120], [1093, 1117], [1093, 1106], [1093, 1111], [1093, 1131], [1093, 1123], [1093, 1138], [1093, 1149], [1094, 1103], [1094, 1118], [1094, 1130], [1094, 1144], [1095, 1096], [1095, 1100], [1095, 1101], [1095, 1104], [1095, 1106], [1095, 1105], [1095, 1121], [1095, 1115], [1095, 1127], [1095, 1138], [1095, 1128], [1095, 1135], [1095, 1134], [1095, 1143], [1095, 1145], [1096, 1102], [1096, 1111], [1096, 1120], [1096, 1118], [1096, 1130], [1096, 1133], [1096, 1135], [1096, 1138], [1096, 1143], [1096, 1145], [1097, 1099], [1097, 1101], [1097, 1103], [1097, 1106], [1097, 1111], [1097, 1114], [1097, 1115], [1097, 1120], [1097, 1119], [1097, 1124], [1097, 1123], [1097, 1125], [1097, 1127], [1097, 1130], [1097, 1128], [1097, 1137], [1097, 1139], [1097, 1138], [1097, 1143], [1097, 1145], [1097, 1144], [1097, 1148], [1098, 1106], [1098, 1125], [1098, 1128], [1099, 1118], [1100, 1103], [1100, 1119], [1100, 1130], [1101, 1103], [1101, 1104], [1101, 1105], [1101, 1106], [1101, 1111], [1101, 1113], [1101, 1114], [1101, 1115], [1101, 1116], [1101, 1118], [1101, 1120], [1101, 1121], [1101, 1125], [1101, 1127], [1101, 1130], [1101, 1117], [1101, 1132], [1101, 1136], [1101, 1135], [1101, 1123], [1101, 1139], [1101, 1144], [1101, 1146], [1101, 1143], [1101, 1147], [1101, 1145], [1101, 1152], [1101, 1151], [1101, 1155], [1102, 1104], [1102, 1111], [1102, 1110], [1102, 1108], [1102, 1109], [1102, 1112], [1102, 1107], [1102, 1115], [1102, 1120], [1102, 1114], [1102, 1121], [1102, 1122], [1102, 1113], [1102, 1124], [1102, 1123], [1102, 1126], [1102, 1128], [1102, 1129], [1102, 1130], [1102, 1132], [1102, 1131], [1102, 1136], [1102, 1134], [1102, 1135], [1102, 1140], [1102, 1143], [1102, 1138], [1102, 1145], [1102, 1142], [1102, 1144], [1102, 1147], [1102, 1146], [1102, 1148], [1102, 1151], [1102, 1149], [1102, 1152], [1102, 1155], [1103, 1111], [1103, 1113], [1103, 1119], [1103, 1130], [1103, 1132], [1103, 1124], [1103, 1143], [1103, 1149], [1104, 1107], [1104, 1118], [1103, 1155], [1104, 1130], [1104, 1135], [1104, 1138], [1104, 1149], [1105, 1114], [1106, 1118], [1106, 1138], [1106, 1130], [1107, 1113], [1108, 1113], [1108, 1151], [1109, 1113], [1109, 1139], [1109, 1145], [1109, 1151], [1111, 1114], [1111, 1116], [1111, 1120], [1111, 1118], [1111, 1124], [1111, 1123], [1111, 1126], [1111, 1132], [1111, 1136], [1111, 1134], [1111, 1135], [1111, 1137], [1111, 1141], [1111, 1140], [1111, 1139], [1111, 1138], [1111, 1144], [1111, 1145], [1111, 1152], [1111, 1155], [1113, 1130], [1114, 1118], [1114, 1120], [1114, 1130], [1114, 1138], [1114, 1143], [1115, 1145], [1116, 1118], [1116, 1121], [1116, 1127], [1116, 1128], [1116, 1140], [1116, 1144], [1116, 1155], [1116, 1151], [1117, 1151], [1119, 1120], [1119, 1123], [1119, 1121], [1119, 1128], [1119, 1133], [1119, 1130], [1119, 1137], [1119, 1138], [1119, 1143], [1119, 1148], [1119, 1147], [1119, 1149], [1119, 1155], [1120, 1128], [1120, 1130], [1120, 1135], [1120, 1132], [1120, 1138], [1120, 1136], [1120, 1141], [1120, 1145], [1120, 1143], [1120, 1149], [1121, 1140], [1121, 1145], [1124, 1139], [1124, 1143], [1125, 1126], [1125, 1128], [1125, 1132], [1125, 1151], [1125, 1149], [1126, 1130], [1126, 1132], [1126, 1134], [1126, 1139], [1126, 1149], [1127, 1130], [1128, 1130], [1128, 1139], [1128, 1141], [1128, 1144], [1129, 1130], [1129, 1137], [1129, 1144], [1129, 1147], [1129, 1149], [1130, 1135], [1129, 1155], [1130, 1146], [1130, 1145], [1130, 1147], [1130, 1149], [1131, 1132], [1131, 1134], [1130, 1155], [1131, 1145], [1131, 1140], [1131, 1144], [1131, 1151], [1132, 1134], [1132, 1143], [1132, 1138], [1132, 1145], [1132, 1151], [1136, 1143], [1137, 1147], [1138, 1141], [1138, 1143], [1138, 1146], [1138, 1147], [1138, 1148], [1138, 1149], [1138, 1144], [1138, 1153], [1138, 1151], [1138, 1152], [1138, 1150], [1138, 1155], [1139, 1141], [1139, 1144], [1139, 1143], [1139, 1142], [1139, 1140], [1139, 1145], [1139, 1146], [1139, 1148], [1139, 1147], [1139, 1149], [1139, 1150], [1139, 1151], [1139, 1155], [1139, 1152], [1139, 1153], [1140, 1141], [1140, 1142], [1140, 1145], [1140, 1144], [1140, 1143], [1140, 1146], [1140, 1147], [1140, 1148], [1140, 1150], [1140, 1149], [1140, 1151], [1140, 1152], [1140, 1153], [1140, 1155], [1141, 1142], [1141, 1143], [1141, 1144], [1141, 1145], [1141, 1146], [1141, 1147], [1141, 1148], [1141, 1150], [1141, 1149], [1141, 1151], [1141, 1152], [1141, 1153], [1141, 1155], [1142, 1143], [1142, 1145], [1142, 1144], [1142, 1146], [1142, 1147], [1142, 1148], [1142, 1149], [1142, 1150], [1142, 1151], [1142, 1152], [1142, 1153], [1143, 1144], [1142, 1155], [1143, 1145], [1143, 1146], [1143, 1147], [1143, 1149], [1143, 1148], [1143, 1150], [1143, 1152], [1143, 1151], [1143, 1153], [1143, 1155], [1144, 1145], [1144, 1147], [1144, 1146], [1144, 1149], [1144, 1148], [1144, 1150], [1144, 1151], [1144, 1153], [1144, 1152], [1144, 1155], [1145, 1146], [1145, 1147], [1145, 1148], [1145, 1150], [1145, 1149], [1145, 1151], [1145, 1152], [1145, 1153], [1145, 1155], [1146, 1147], [1146, 1148], [1146, 1149], [1146, 1151], [1146, 1150], [1146, 1152], [1146, 1153], [1147, 1148], [1146, 1155], [1147, 1149], [1147, 1150], [1147, 1151], [1147, 1153], [1147, 1152], [1147, 1155], [1148, 1149], [1148, 1150], [1148, 1151], [1148, 1152], [1148, 1153], [1148, 1155], [1149, 1150], [1149, 1151], [1149, 1152], [1149, 1153], [1150, 1151], [1149, 1155], [1150, 1152], [1150, 1153], [1150, 1155], [1151, 1152], [1151, 1153], [1151, 1155], [1152, 1153], [1153, 1155]]