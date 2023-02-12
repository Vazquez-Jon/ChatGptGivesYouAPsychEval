import random

def parse(username, message: str, db) -> str:
    lower_message = message.lower()


    p_message = lower_message[3:]
    tag = lower_message[:3]

    ## Bot was called
    if tag == 'gpt':
        
        ## Help weas called for
        if p_message == 'help':
            return 'help'

        if p_message == 'psych eval':
            return 'pysch eval'


    return 'Nothing to respond to'