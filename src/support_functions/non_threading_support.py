

def templat_request_two_user_stories(current_message: list[dict], user_story_one: str, user_story_two: str, user_story_one_id: str, user_story_two_id: str):
    request: dict = {"role":"user", "content":"Yes. Please, process the following pair of user stories:\n"
    f"id: {user_story_one_id}, describtion:  {user_story_one}\n"
    f"id: {user_story_two_id}, describtion: {user_story_two}"}
    current_message.append(request)