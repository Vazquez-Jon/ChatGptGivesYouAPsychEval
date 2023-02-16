## Jonathan Vazquez
## api_control.py
## 
## Desc: Class that will handle interacting with database and gpt. Also will do initial setup for both api's

import db_io
import gpt_control

## TODO Make it so the classes take in api keys so you dont have to hard code it 
class API_Control():
    def __init__(self) -> None:
        ## Database setup
        self.db = db_io.Database()
        self.gpt = gpt_control.GPT_Control()

    