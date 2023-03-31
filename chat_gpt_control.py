## Jonathan Vazquez
## chat_gpt_control.py
##
## Desc: Class to get response from chat gpt

import openai
import os
from dotenv import load_dotenv

class Chat_GPT_Control():
    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv('OPENAI')
        

    ## Func to get psych eval
    def get_psycheval(self, input):
        openai.api_key = self.api_key

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content" : "You are a PyschEvalGPT. You give comedic pyschological evaluations based on messages sent by a person."},
                {"role": "user", "content": input}
            ]
        )
        
        return response['choices'][0]['message']['content']