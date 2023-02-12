import random

def parse(username, message: str, ctrl) -> str:
    lower_message = message.lower()


    p_message = lower_message[3:]
    tag = lower_message[:3]

    ## Bot was called
    if tag == 'gpt':
        
        ## Help was called for
        ## TODO Make this useful
        if p_message == 'help':
            return 'Make this useful'

        if p_message == 'psych eval':
            return 'pysch eval'


    return ''