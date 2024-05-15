from support_functions.request_handler import send_requierment_to_chatgpt, StoppedAnswerException
from support_functions.time_recorder import TimeRecorder
from support_functions.save_data import save_to_json_persistent
from support_functions.non_threading_support import templat_request_two_user_stories as tatarus
import pandas as pd
import json
import os
import multiprocessing
from multiprocessing import Lock, Process, Queue, Manager
import ctypes

GLOBAL_SAVE_LOCK = Lock
WAIT_FOR_REQUESTS_FINISHED: int = 3 #in seconds

def templat_request_two_user_stories(current_message: list[dict], user_story_one: str, user_story_two: str, user_story_one_id: str, user_story_two_id: str):
    tatarus(current_message, user_story_one, user_story_two, user_story_one_id, user_story_two_id)

def save_to_json_persistent_thread_save(folder_name, key, results_thread_save, exceptions_thread_save, lock):    
    results_collection: dict = {}
    results_collection[key] = list(results_thread_save)
    if len(list(exceptions_thread_save)) != 0:
        results_collection[key.value.decode('utf-8'), 'Exceptions'] = list(exceptions_thread_save)
    with lock:
        save_to_json_persistent(folder_name.value.decode('utf-8'), results_collection)
        
def manage_parallel_request(q_messages, results, exceptions_during_processing) -> None:
    time_recorder: TimeRecorder = None
    while not q_messages.empty():
        d: dict = dict(q_messages.get())
        usid1, usid2 = str(list(dict(d).keys())[0]).split(";")
        print(usid1 + " " + usid2)
        local_messages = list(dict(d).values())[0]
        try:
            time_recorder = TimeRecorder()
            resonse = send_requierment_to_chatgpt(local_messages, time_recorder)
            json_object = json.loads(resonse)
            json_object = {'elipsedTimeNs': time_recorder.nanoseconds, **json_object}
            results.append(json_object)
        except StoppedAnswerException:  # Handle StoppedAnswerException
            exceptions_during_processing_data = {"Reason" : "Not stopped exception from ChatGPT Endpoint", "UID1" : usid1,  "UID2" : usid2}
            exceptions_during_processing.append(json.loads(exceptions_during_processing_data))
        except ValueError:  # Handle ValueError
            exceptions_during_processing_data = {"Reason" : "ValueError", "UID1" : usid1,  "UID2" : usid2}
            exceptions_during_processing.append(json.loads(exceptions_during_processing_data))
           
def process_requests_parallel(message: list[dict], pairs: pd.DataFrame, folder_name: str, key: str):    
    with Manager() as manager:
        #Data types for threading
        requests_to_accomplish = Queue()
        processes: list = []
        results_thread_save = manager.list()
        exceptions_thread_save = manager.list()
        
        elements: int = 0
        current_message: list[dict] = []
        for idx in range(len(pairs)):
            current_message = message.copy()
            templat_request_two_user_stories(current_message, pairs.iat[idx, 1], pairs.iat[idx, 3], str(pairs.iat[idx, 0]), str(pairs.iat[idx, 2]))
            requests_to_accomplish.put({pairs.iat[idx, 1] + ";" + pairs.iat[idx, 3] : current_message})
            elements += 1
        
        for _ in range(os.cpu_count() * 2):
            process = Process(target=manage_parallel_request, args=(requests_to_accomplish, results_thread_save, exceptions_thread_save))
            processes.append(process)
            process.start()
        
        for _ in processes:
            print("Wait for thread")
            _.join()
            print("Thread terminated")
        
        shared_folder_name = multiprocessing.Array(ctypes.c_char, len(folder_name) + 1)
        shared_folder_name.value = folder_name.encode('utf-8')
        shared_key = multiprocessing.Array(ctypes.c_char, len(key) + 1)
        shared_key.value = key.encode('utf-8')

        process = Process(target=save_to_json_persistent_thread_save, args=(shared_folder_name, shared_key, results_thread_save, exceptions_thread_save, GLOBAL_SAVE_LOCK))
        process.start()
        process.join()
        print("Reached End")