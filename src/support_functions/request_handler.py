### Own modules
from prompt_structure.helper_prompt_composition import (
    REPAIR_REQUEST,
    combine_chat_history_repair_request)

from .time_recorder import TimeRecorder
from .save_data import save_to_json_persistent
from .json_validator import validation

### Third party modules
import os
import time
import json
import pandas as pd

from dotenv import load_dotenv
from openai import OpenAI
from multiprocessing import Process, Queue, Manager
from typing import Callable
import copy

# .Env const.
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_CODE = os.getenv("MODEL_VERSION")
TEMPERATURE = float(os.getenv("TEMPERATURE"))
LIMIT_OF_REQUESTS: int = int(os.getenv("LIMIT"))
THRESHOLD_REPAIR: int = int(os.getenv("THRESHOLD_REPAIR"))

# Const. for processing
REDUNDANCY_MODEL: str = "redundancy-model-"
EXCEPTION: str = "Exceptions"
SEPERATOR: str = "-"
REASON_KEY = "Reason"
NOT_STOPPED_EXCEPTION_CHAT_GPT = "Not stopped exception from ChatGPT Endpoint"
USID_ONE = "UID1"
USID2_TWO = "UID2"
VALUE_ERROR = "ValueError"
ELIPSED_TIME = "elipsedTimeNs"
REPAIR_RUNS_JSON_FIELD = "repairRuns"

class StoppedAnswerException(Exception):
    """
    Exception raised when the ChatGPT API response indicates that 
    the answer was stopped prematurely.

    This exception should be raised when the `finish_reason` of 
    the response from the ChatGPT API is not 'stop'.

    Attributes:
    ----------
    message : str
        Explanation of the error.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

def check_for_stopped_resonse(system_is_r_eng):
    if system_is_r_eng.choices[0].finish_reason != "stop":
        raise StoppedAnswerException(
            "Response error message: The finish reason is not 'stop'. It is: "
            + system_is_r_eng.choices[0].finish_reason
        )

def add_repair_runs_count(answer: str, repair_run: int) -> str:
    return json.dumps({REPAIR_RUNS_JSON_FIELD: repair_run, **json.loads(answer)})

def repair_json_by_gpt(
    message: list[dict],
    answer: str,
    not_correct_json_reason: str,
    client,
    json_validation: Callable[[dict], bool]
    ) -> str:
    repair_run: int = 1
    message = copy.deepcopy(message)
    correct: bool = False
    current_repair_request: dict = None
    for _ in range(THRESHOLD_REPAIR):
        current_repair_request = copy.deepcopy(REPAIR_REQUEST)
        current_repair_request["content"] = current_repair_request["content"] + not_correct_json_reason
        if not correct:
            combine_chat_history_repair_request(message=message, answer=answer,
                                                current_repair_request=current_repair_request)
            system_is_r_eng = client.chat.completions.create(
                model=MODEL_CODE,
                stream=False,
                temperature=TEMPERATURE,
                response_format={"type": "json_object"},
                messages=message,
            )
            check_for_stopped_resonse(system_is_r_eng)
            answer = system_is_r_eng.choices[0].message.content
            correct, not_correct_json_reason = json_validation(json.loads(answer))
            if correct:
                return add_repair_runs_count(answer, repair_run)
            repair_run += 1
    raise StoppedAnswerException(
        "Response error message: The schema could not been correctly generated and not been repaired"
    )

def send_requierment_to_chatgpt(
    message: list[dict],
    json_validation: Callable[[dict], bool],
    time_recorder: TimeRecorder = None
) -> str:
    """
    Sends a requirement to the ChatGPT API and returns the response.

    This function uses the OpenAI API to send a list of messages to 
    the ChatGPT model and obtain a response.
    It also measures the time taken for the request if a TimeRecorder object is provided.

    Parameters:
    ----------
    message : list[dict]
        A list of dictionaries representing the messages to be sent to the ChatGPT model.
        Each dictionary should contain the message content and other relevant information.
    time_recorder : TimeRecorder, optional
        An instance of the TimeRecorder class to record the elapsed time for the request.
        If provided, the elapsed time in nanoseconds will be stored in the `nanoseconds` attribute of the TimeRecorder.

    Returns:
    -------
    str
        The content of the response message from the ChatGPT model.

    Raises:
    ------
    StoppedAnswerException
        If the finish reason of the response is not 'stop'.
    """
    answer: str = None
    correct: bool = False
    not_correct_json_reason: str = None
    client = OpenAI()
    start_time = time.time_ns()
    system_is_r_eng = client.chat.completions.create(
        model=MODEL_CODE,
        stream=False,
        temperature=TEMPERATURE,
        response_format={"type": "json_object"},
        messages=message,
    )
    check_for_stopped_resonse(system_is_r_eng)
    answer = system_is_r_eng.choices[0].message.content
    correct, not_correct_json_reason = json_validation(json.loads(answer))
    if THRESHOLD_REPAIR > 0 and not correct:
        answer = repair_json_by_gpt(message, answer, not_correct_json_reason, client, json_validation)
    else:
        answer = add_repair_runs_count(answer=answer, repair_run=0)
    client.close()
    end_time = time.time_ns()
    if time_recorder:
        elapsed_time_ns = end_time - start_time
        time_recorder.nanoseconds = elapsed_time_ns
    return answer

## Data Processing Definition Pipline for User Stories
### General Function for data requests
def manage_single_request(
    index_usid1: int,
    index_usid2: int,
    message: list[dict],
    pairs: pd.DataFrame,
    results: list,
    exceptions_during_processing: list,
    template_request_two_user_stories: Callable[[list[dict], int, pd.DataFrame], None],
    json_validation: Callable[[dict], bool]
) -> None:
    """
    Processes multiple user story pairs by sending requests to 
    Sthe ChatGPT API and recording the results.

    This function iterates over pairs of user stories, constructs the request messages, 
    sends them to the ChatGPT API, and records the responses and any exceptions 
    that occur during processing. The number of requests is controlled by 
    the `LIMIT_OF_REQUESTS` variable of .env.

    Parameters:
    ----------
    message : list[dict]
        A list of dictionaries representing the initial messages to be used 
        as a template for each request.
    pairs : pd.DataFrame
        A DataFrame containing pairs of user stories. Each row represents 
        a pair of user stories with their IDs.
    results : list
        A list to store the results of the requests. Each result is a 
        dictionary containing the response and elapsed time.
    exceptions_during_processing : list
        A list to store the exceptions that occur during processing. 
        Each exception is a dictionary with details about the error.

    Raises:
    ------
    StoppedAnswerException
        If the ChatGPT API response indicates that the answer was stopped prematurely.
    ValueError
        If there is a ValueError during processing.
    """
    time_recorder: TimeRecorder = None
    count_of_requests: int = None
    if LIMIT_OF_REQUESTS == -1:
        count_of_requests = range(len(pairs))
    else:
        count_of_requests = range(LIMIT_OF_REQUESTS)

    for idx in count_of_requests:
        current_message: list[dict] = copy.deepcopy(message)
        template_request_two_user_stories(
            current_message=current_message,
            idx=idx,
            pairs=pairs
        )
        try:
            time_recorder = TimeRecorder()
            resonse = send_requierment_to_chatgpt(message=current_message, json_validation=json_validation, time_recorder=time_recorder)
            json_object = json.loads(resonse)
            json_object = {ELIPSED_TIME: time_recorder.nanoseconds, **json_object}
            results.append(json_object)
        except StoppedAnswerException:  # Handle StoppedAnswerException
            exceptions_during_processing_data = {
                REASON_KEY: NOT_STOPPED_EXCEPTION_CHAT_GPT,
                USID_ONE: str(pairs.iat[idx, index_usid1]),
                USID2_TWO: str(pairs.iat[idx, index_usid2]),
            }
            exceptions_during_processing.append(
                json.loads(exceptions_during_processing_data)
            )
        except ValueError:
            exceptions_during_processing_data = {
                REASON_KEY: VALUE_ERROR,
                USID_ONE: str(pairs.iat[idx, index_usid1]),
                USID2_TWO: str(pairs.iat[idx, index_usid2]),
            }
            exceptions_during_processing.append(
                json.loads(exceptions_during_processing_data)
            )
        except Exception as e:
            exceptions_during_processing_data = {
                REASON_KEY: str(e),
                USID_ONE: str(pairs.iat[idx, index_usid1]),
                USID2_TWO: str(pairs.iat[idx, index_usid2]),
            }
            exceptions_during_processing.append(
                json.loads(exceptions_during_processing_data)
            )


def process_user_stories(
    index_usid1: int,
    index_usid2: int,
    message: list[dict],
    pairs: pd.DataFrame,
    key: str,
    model_version_name: str,
    template_request_two_user_stories: Callable[[list[dict], int, pd.DataFrame], None],
    json_validation: Callable[[dict], bool],
    redundancy_prefix: str = "",
    time_recorder: TimeRecorder = None
) -> None:
    """
    Manages the processing of multiple user story pairs by sending requests 
    to the ChatGPT API and recording the results.

    This function iterates over pairs of user stories, constructs the request messages, 
    sends them to the ChatGPT API,
    and records the responses and any exceptions that occur during processing. 
    The number of requests is controlled by the `LIMIT_OF_REQUESTS` variable from the .env.

    Parameters:
    ----------
    message : list[dict]
        A list of dictionaries representing the initial messages to be used 
        as a template for each request.
    pairs : pd.DataFrame
        A DataFrame containing pairs of user stories. Each row represents 
        a pair of user stories with their IDs.
    results : list
        A list to store the results of the requests. Each result is a 
        dictionary containing the response and elapsed time.
    exceptions_during_processing : list
        A list to store the exceptions that occur during processing. 
        Each exception is a dictionary with details about the error.

    Raises:
    ------
    StoppedAnswerException
        If the ChatGPT API response indicates that the answer was stopped prematurely.
    ValueError
        If there is a ValueError during processing.
    """
    results: list = []
    exceptions_during_processing: list = []
    start_time = time.time_ns()
    
    manage_single_request(index_usid1=index_usid1, index_usid2=index_usid2, message=message, pairs=pairs, results=results, exceptions_during_processing=exceptions_during_processing, 
                          template_request_two_user_stories=template_request_two_user_stories, json_validation=json_validation)
    
    end_time = time.time_ns()
    elapsed_time_ns = end_time - start_time
    if time_recorder:
        time_recorder.nanoseconds = elapsed_time_ns
    
    results_collection: dict = {}
    results_collection[key] = results
    if len(exceptions_during_processing) != 0:
        results_collection[key + EXCEPTION] = exceptions_during_processing
    if redundancy_prefix:
        redundancy_prefix += SEPERATOR
    save_to_json_persistent(
        f"{redundancy_prefix}{REDUNDANCY_MODEL}{model_version_name}", results_collection
    )

### Threading functions for data request
def manage_parallel_request(
    q_messages,
    results,
    exceptions_during_processing,
    json_schema: str
    ) -> None:
    """
    Processes a set of user stories by sending requests to the ChatGPT API and saves the results.

    This function manages the processing of user story pairs by calling `manage_single_request` 
    to send requests to the ChatGPT API.
    It collects the results and any exceptions that occur during processing. 
    The results are then saved to a JSON file.

    Parameters:
    ----------
    message : list[dict]
        A list of dictionaries representing the initial messages to be used 
        as a template for each request.
    pairs : pd.DataFrame
        A DataFrame containing pairs of user stories. Each row represents 
        a pair of user stories with their IDs.
    key : str
        A unique key used to identify the results in the saved JSON file.
    model_version_name : str
        The version name of the ChatGPT model used for processing the requests.
    redundancy_prefix : str, optional
        A prefix added to the file name of the saved results. Default is an empty string.
    """
    def json_validation(json_data: dict) -> tuple[bool, str]:
        return validation(json_data, json_schema)
    time_recorder: TimeRecorder = None
    while not q_messages.empty():
        d: dict = dict(q_messages.get())
        usid1, usid2 = str(list(dict(d).keys())[0]).split(";")
        local_messages = list(dict(d).values())[0]
        try:
            time_recorder = TimeRecorder()
            resonse = send_requierment_to_chatgpt(message=local_messages, json_validation=json_validation, time_recorder=time_recorder)
            json_object = json.loads(resonse)
            json_object = {ELIPSED_TIME: time_recorder.nanoseconds, **json_object}
            results.append(json_object)
        except StoppedAnswerException:
            exceptions_during_processing_data = {
                REASON_KEY: NOT_STOPPED_EXCEPTION_CHAT_GPT,
                USID_ONE: usid1,
                USID2_TWO: usid2,
            }
            exceptions_during_processing.append(
                json.loads(exceptions_during_processing_data)
            )
        except ValueError:
            exceptions_during_processing_data = {
                REASON_KEY: VALUE_ERROR,
                USID_ONE: usid1,
                USID2_TWO: usid2,
            }
            exceptions_during_processing.append(
                json.loads(exceptions_during_processing_data)
            )
        except Exception as e:
            exceptions_during_processing_data = {
                REASON_KEY: str(e),
                USID_ONE: usid1,
                USID2_TWO: usid2,
            }
            exceptions_during_processing.append(
                json.loads(exceptions_during_processing_data)
            )

def process_user_stories_parallel(
    index_usid1: int,
    index_usid2: int,
    message: list[dict],
    pairs: pd.DataFrame,
    key: str,
    model_version_name: str,
    template_request_two_user_stories: Callable[[list[dict], int, pd.DataFrame], None],
    sort_threaded_results: Callable[[dict[list]], None],
    json_schema: str,
    redundancy_prefix: str = "",
    time_recorder: TimeRecorder = None
):
    """
    Manages parallel processing of multiple user story pairs,
    sends requests to the ChatGPT API, and saves the results.

    This function sets up multiprocessing resources to handle multiple user story pairs in parallel.
    It initializes queues and shared lists, spawns multiple processes to handle the requests,
    collects the results and any exceptions that occur during processing,
    and saves the results to a JSON file.

    Parameters
    ----------
    message : list[dict]
        A list of dictionaries representing the initial messages to be used as 
        a template for each request.
    pairs : pd.DataFrame
        A DataFrame containing pairs of user stories. Each row represents 
        a pair of user stories with their IDs.
    key : str
        A unique key used to identify the results in the saved JSON file.
    model_version_name : str
        The version name of the ChatGPT model used for processing the requests.
    index_usid1 : int
        The column index in the DataFrame 'pairs' that contains the first user story ID.
    index_usid2 : int
        The column index in the DataFrame 'pairs' that contains the second user story ID.
    template_request_two_user_stories : Callable[[List[Dict], int, pd.DataFrame], None]
        A function that templates a request for two user stories. It takes the current message,
        the index of the pair, and the DataFrame of pairs as arguments.
    sort_threaded_results : Callable[[dict[list]], None]
        A function that sorts the results from the threads. It takes a dictionary with lists as values
        and returns None
    redundancy_prefix : str, optional
        A prefix added to the file name of the saved results. Default is an empty string.
    time_recorder : TimeRecorder, optional
        An object to record the elapsed time of the processing in nanoseconds. Default is None.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the input parameters do not meet the required conditions.
    
    Notes
    -----
    - This function uses the Python multiprocessing module to handle parallel processing.
    - The function assumes the existence of constants `LIMIT_OF_REQUESTS`, `EXCEPTION`, `SEPERATOR`, 
      and `REDUNDANCY_MODEL`, which should be defined elsewhere in the code.
    - The results and exceptions are saved in a JSON file with a naming convention that includes
      the `redundancy_prefix`, `REDUNDANCY_MODEL`, and `model_version_name`.
    """
    with Manager() as manager:
        # Data types for threading
        requests_to_accomplish = Queue()
        processes: list = []
        results_thread_save = manager.list()
        exceptions_thread_save = manager.list()

        current_message: list[dict] = []
        count_of_requests: int = None
        if LIMIT_OF_REQUESTS == -1:
            count_of_requests = range(len(pairs))
        else:
            count_of_requests = range(LIMIT_OF_REQUESTS)

        for idx in count_of_requests:
            current_message = copy.deepcopy(message)
            template_request_two_user_stories(
                current_message=current_message,
                idx=idx,
                pairs=pairs
            )
            
            requests_to_accomplish.put(
                {str(pairs.iat[idx, index_usid1]) + ";" + str(pairs.iat[idx, index_usid2]): current_message}
            )

        start_time = time.time_ns()
        for _ in range(os.cpu_count() * 2):
            process = Process(
                target=manage_parallel_request,
                args=(
                    requests_to_accomplish,
                    results_thread_save,
                    exceptions_thread_save,
                    json_schema,
                ),
            )
            processes.append(process)
            process.start()

        for _ in processes:
            _.join()
        
        end_time = time.time_ns()
        elapsed_time_ns = end_time - start_time
        if time_recorder:
            time_recorder.nanoseconds = elapsed_time_ns

        results_collection: dict = {}
        results_collection[key] = list(results_thread_save)
        if len(list(exceptions_thread_save)) != 0:
            results_collection[key + EXCEPTION] = list(exceptions_thread_save)
        if redundancy_prefix:
            redundancy_prefix += SEPERATOR
        print(results_collection.items())
        sort_threaded_results(results_collection)
        save_to_json_persistent(
            f"{redundancy_prefix}{REDUNDANCY_MODEL}{model_version_name}",
            results_collection,
        )


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
