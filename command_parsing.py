import random

def parse(message: str) -> str:
    lower_message = message.lower()


    p_message = lower_message[3:]
    tag = lower_message[:3]

    ## Bot was called
    if tag == 'gpt':
        
        ## help weas called for
        ## TODO actually make this informative
        if p_message == 'help':
            return 'Make this useful'

        if p_message == 'psych eval':
            return 'pysch eval'


    return 'Nothing to respond to'