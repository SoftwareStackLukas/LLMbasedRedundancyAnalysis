import json

REPAIR_REQUEST = {"role": "user", "content": "Please, check and repair the json format as it is not correct and return me the correct json output with the correct values. I used jsonschema libary from python to check the json. "}


def combine_chat_history_repair_request(message: list[dict[str, str]], answer: str, current_repair_request: dict) -> None:
    message.append({"role": "assistent", "content": answer})
    message.append({"role": "user", "content": current_repair_request})

def parsing_to_pair_requests(json_us_one: dict, json_us_two: dict) -> dict[str, str]:
    return {
        "role": "user",
        "content": "Yes. Please, process the following pairs of user story annotations:\n"
        f"id: {json_us_one["USID"]}, annotations: {json.dumps(json_us_one)};\n"
        f"id: {json_us_two["USID"]}, annotations: {json.dumps(json_us_two)}",
    }