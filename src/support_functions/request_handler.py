import os
from dotenv import load_dotenv
from openai import OpenAI
import time
from support_functions.time_recorder import TimeRecorder

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
model_code = os.getenv('MODEL_VERSION')

class StoppedAnswerException(Exception):
    pass

def send_requierment_to_chatgpt(message: list[dict], time_recorder: TimeRecorder = None) -> str:
    client = OpenAI()
    start_time = time.time_ns()
    system_is_r_eng = client.chat.completions.create(
        model=model_code,
        stream=False,
        temperature=0.2,
        response_format={ "type": "json_object" },
        messages=message
    )
    end_time = time.time_ns()
    if time_recorder:
        elapsed_time_ns = end_time - start_time
        time_recorder.nanoseconds = elapsed_time_ns
    client.close()
    if system_is_r_eng.choices[0].finish_reason != 'stop':
        raise StoppedAnswerException("Response error message: The finish reason is not 'stop'. It is: " + system_is_r_eng.choices[0].finish_reason)
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

# import time 

# start_time = time.time_ns()
# print("Hello")
# time.sleep(2)
# end_time = time.time_ns()
# elapsed_time_ns = end_time - start_time
# elapsed_time_ms = elapsed_time_ns / 1_000_000
# elapsed_time_s = elapsed_time_ns / 1_000_000_000
# elapsed_time_m = elapsed_time_s / 60
# print("Elapsed time (ns):", elapsed_time_ns)
# print("Elapsed time (ms):", elapsed_time_ms)
# print("Elapsed time (s):", elapsed_time_s)
# print("Elapsed time (m):", elapsed_time_m)