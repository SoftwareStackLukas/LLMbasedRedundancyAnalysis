REPAIR_REQUEST = {"role": "user", "content": "Please, check and repair the json format as it is not correct and return me the correct json output with the correct values. I used jsonschema libary from python to check the json. "}


def combine_chat_history_repair_request(message: list[dict[str, str]], answer: str, current_repair_request: dict) -> None:
    message.append({"role": "assistent", "content": answer})
    message.append({"role": "user", "content": current_repair_request})
