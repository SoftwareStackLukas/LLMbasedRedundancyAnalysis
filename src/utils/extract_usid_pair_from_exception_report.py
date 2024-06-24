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

temp = extract_usid_pair(exception_data_one)
print(temp)
# From Exception Data 1 (G22): [[1299, 1302], [1225, 1226], [1228, 1235], [1228, 1290], [1232, 1281], [1235, 1246], [1237, 1264], [1242, 1243], [1244, 1290], [1246, 1291], [1246, 1294], [1246, 1307], [1247, 1291], [1250, 1291], [1254, 1259], [1256, 1281], [1263, 1281], [1267, 1290], [1268, 1290], [1270, 1271], [1269, 1294], [1275, 1289], [1275, 1287], [1276, 1281], [1282, 1285], [1285, 1288], [1285, 1289], [1284, 1287], [1285, 1290], [1285, 1294], [1285, 1307], [1287, 1291], [1288, 1291], [1290, 1291], [1291, 1296], [1291, 1300], [1292, 1301]]

print("\n\n")

# {"Reason": "Error code: 400 - {'error': {'message': \"This model's maximum context length is 16385 tokens. However, your messages resulted in 16609 tokens. Please reduce the length of the messages.\", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}", "USID1": "1026", "USID2": "1115"} 

temp = extract_usid_pair(exception_data_two)
print(temp)
# From Exception Data 2 (G19): [[1151, 1155], [1019, 1029], [1019, 1085], [1021, 1059], [1021, 1081], [1021, 1087], [1022, 1039], [1022, 1025], [1022, 1030], [1022, 1056], [1022, 1099], [1024, 1045], [1025, 1028], [1024, 1115], [1025, 1026], [1025, 1038], [1025, 1116], [1026, 1030], [1026, 1029], [1026, 1031], [1026, 1040], [1026, 1038], [1026, 1042], [1026, 1045], [1026, 1049], [1026, 1044], [1026, 1075], [1026, 1107], [1026, 1105], [1026, 1106], [1026, 1108], [1026, 1129], [1027, 1031], [1027, 1029], [1027, 1032], [1027, 1030], [1027, 1028], [1027, 1038], [1027, 1041], [1027, 1040], [1027, 1048], [1027, 1045], [1027, 1049], [1027, 1106], [1027, 1108], [1027, 1110], [1027, 1107], [1027, 1098], [1027, 1122], [1027, 1126], [1027, 1128], [1028, 1041], [1028, 1039], [1028, 1044], [1028, 1098], [1028, 1105], [1029, 1038], [1029, 1039], [1029, 1068], [1030, 1040], [1030, 1041], [1032, 1039], [1032, 1040], [1032, 1078], [1032, 1115], [1037, 1042], [1037, 1049], [1037, 1045], [1037, 1125], [1038, 1105], [1039, 1041], [1039, 1068], [1039, 1124], [1040, 1041], [1040, 1049], [1040, 1068], [1040, 1075], [1040, 1115], [1041, 1105], [1041, 1106], [1042, 1048], [1042, 1049], [1045, 1077], [1046, 1098], [1048, 1075], [1048, 1105], [1048, 1106], [1049, 1075], [1049, 1103], [1049, 1106], [1049, 1105], [1053, 1085], [1054, 1085], [1057, 1089], [1057, 1121], [1057, 1135], [1059, 1087], [1059, 1098], [1061, 1134], [1062, 1090], [1062, 1091], [1063, 1091], [1064, 1081], [1064, 1088], [1064, 1090], [1065, 1090], [1066, 1090], [1068, 1075], [1068, 1078], [1068, 1098], [1068, 1125], [1071, 1072], [1073, 1091], [1073, 1093], [1074, 1129], [1075, 1108], [1075, 1106], [1075, 1116], [1075, 1119], [1075, 1125], [1076, 1078], [1077, 1078], [1077, 1091], [1077, 1098], [1077, 1110], [1077, 1119], [1078, 1108], [1078, 1105], [1078, 1106], [1078, 1107], [1078, 1122], [1078, 1124], [1078, 1121], [1084, 1085], [1084, 1120], [1086, 1121], [1086, 1122], [1087, 1093], [1088, 1090], [1089, 1091], [1089, 1093], [1089, 1095], [1092, 1095], [1092, 1093], [1098, 1106], [1098, 1105], [1098, 1110], [1098, 1112], [1098, 1115], [1098, 1122], [1106, 1116], [1107, 1129], [1108, 1134], [1108, 1129], [1109, 1134], [1110, 1129], [1111, 1129], [1115, 1134], [1116, 1119], [1121, 1125], [1137, 1140], [1139, 1146], [1140, 1141], [1148, 1150], [1026, 1115] 

