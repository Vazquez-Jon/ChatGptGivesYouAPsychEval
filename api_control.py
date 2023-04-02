## Jonathan Vazquez
## api_control.py
## 
## Desc: Class that will handle interacting with database and gpt. Also will do initial setup for both api's

import db_io
import chat_gpt_control

class API_Control():
    def __init__(self) -> None:
        ## Database setup
        self.db = db_io.Database()
        self.gpt = chat_gpt_control.Chat_GPT_Control()

    