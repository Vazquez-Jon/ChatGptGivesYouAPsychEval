## Jonathan Vazquez
## responses.py
##
## Desc: Used to generate response for when bot was called

def parse(username, message: str, ctrl) -> str:
    lower_message = message.lower()


    p_message = lower_message[4:]
    tag = lower_message[:3]

    response = None

    ## Bot was called
    if tag == 'gpt':
        
        ## Help was called for
        ## TODO Make this useful
        if p_message == 'help':
            response = 'Type: **gpt psych eval** for a psych eval'

        ## A psych eval was requested
        elif p_message == 'psych eval':
            try:
                gpt_input = ctrl.db.get_gptin(username)
                response  = ctrl.gpt.get_psycheval(gpt_input)
            except Exception as e:
                print(e)
                response = 'User has no chracter defining messages, try typing some more meaningful messages!'

        ## Someone tried to use a command but was typed incorrectly. Is here so you dont save useless messages
        else:
            response = 'Error: I do not know what that command was.'



    return response