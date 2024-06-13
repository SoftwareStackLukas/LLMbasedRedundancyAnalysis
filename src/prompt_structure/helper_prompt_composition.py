import json

REPAIR_REQUEST = {"role": "user", "content": "Please, check and repair the json format as it is not correct and return me the correct json output with the correct values. I used jsonschema libary from python to check the json. "}


def combine_chat_history_repair_request(message: list[dict[str, str]], answer: str, current_repair_request: dict) -> None:
    message.append({"role": "assistent", "content": answer})
    message.append({"role": "user", "content": current_repair_request})

def parsing_to_pair_requests(json_us_one: dict, json_us_two: dict) -> dict[str, str]:
    return {
        "role": "user",
        "content": "Yes. Please, analyse the redundancies from the following pair of user stories:\n"
        f"First User Story JSON-Data: {json.dumps(json_us_one)};\n"
        f"Second User Story JSON-Data: {json.dumps(json_us_two)}",
        #f"id: {json_us_one["USID"]}, jsonData: {json.dumps(json_us_one)};\n"
        #f"id: {json_us_two["USID"]}, jsonData: {json.dumps(json_us_two)}",
    }