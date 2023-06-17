id = "davinci:ft-personal-2023-06-14-15-04-40"
id = "davinci:ft-personal-2023-06-14-15-38-2"
id = "davinci:ft-personal-2023-06-14-17-07-46"
id = "davinci:ft-personal-2023-06-15-10-31-47"

"ft-q8HsiagtJ7DhmstjTJs9OLEt"

import openai
from difflib import SequenceMatcher

API_KEY = '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'
openai.api_key = API_KEY


response = openai.Completion.create(
        model=id,
        prompt=user_prompt
    )

print(response)


# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()
#
# training_prompts = ["What are the opening hours of the store on weekdays?",
#                     "Does the store carry organic fruits?",
#                     "What is the store's return policy for fresh produce?",
#                     "Tell me more about the loyalty program.",
#                     "What measures has the store taken in response to COVID-19?"]
#
# def validate_prompt(user_prompt):
#     for prompt in training_prompts:
#         # Check if the incoming prompt is similar to any of the training prompts
#         if similar(user_prompt, prompt) > 0.7:  # Adjust this threshold as necessary
#             return True
#     return False
#
# user_prompt = "What are the opening hours of the store on weekdays?"  # Example user prompt
#
# if validate_prompt(user_prompt):
#     # If the user's prompt is similar to a training prompt, pass it to the model
#     response = openai.Completion.create(
#         model=id,
#         prompt=user_prompt
#     )
#     print(response)
# else:
#     # Otherwise, handle the prompt differently (e.g., send a default response)
#     print("I'm sorry, I can only answer specific questions about the store.")
