## Jonathan Vazquez
## responses.py
##
## Desc: Used to generate response for when bot was called

def parse(username, message: str, ctrl) -> str:
    lower_message = message.lower()


    p_message = lower_message[4:]
    tag = lower_message[:3]

    response = ''

    ## Bot was called
    if tag == 'gpt':
        
        ## Help was called for
        ## TODO Make this useful
        if p_message == 'help':
            response = 'Make this useful'

        ## TODO Add gpt get_pyscheval
        if p_message == 'psych eval':
            gpt_input = ctrl.db.get_gptin(username)
            response  = ctrl.gpt.get_pyscheval(gpt_input)

        ## Someone tried to use a command but was typed incorrectly. Is here so you dont save useless messages
        response = 'Error: I do not know what that command was.'



    return response