import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
model_code = os.getenv('MODEL_VERSION')

class StoppedAnswerException(Exception):
    pass

def send_requierment_to_chatgpt(message: list[dict]) -> str:
    client = OpenAI()
    system_is_r_eng = client.chat.completions.create(
        model=model_code,
        stream=False,
        temperature=0.2,
        response_format={ "type": "json_object" },
        messages=message
    )
    client.close()
    if system_is_r_eng.choices[0].finish_reason != 'stop':
        raise StoppedAnswerException("Response error message: The finish reason is not 'stop'. It is: " + system_is_r_eng.choices[0].finish_reason)
    print(system_is_r_eng.choices[0].message.content)
    return system_is_r_eng.choices[0].message.content

# #### Structure of the completion response:
# ```json
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
#         "role": "assistant"
#       },
#       "logprobs": null
#     }
#   ],
#   "created": 1677664795,
#   "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
#   "model": "gpt-3.5-turbo-0613",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 17,
#     "prompt_tokens": 57,
#     "total_tokens": 74
#   }
# }
# ```