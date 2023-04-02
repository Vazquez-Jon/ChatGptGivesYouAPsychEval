## Jonathan Vazquez
## responses.py
##
## Desc: Used to generate response for when bot was called

import re

## Desc: Use to clean a message that has a mention(the id and not weird disc mention)
## clean_mentions(message)
## message: the message to clean as a str
## Return: [clean string, id, if str has an id]
def clean_mentions(message: str):
    ## Regex used to find discord's formatting of mentions in the message str
    regex_dirty = "<@!?[0-9]+>"
    ## Regex to find the id in the weird format str
    regex_clean = "[0-9]+"

    ## Get the weird mention format str from the message
    id_dirty = re.search(regex_dirty, message)

    ## No match so there is no id's
    if( id_dirty.group() == None ):
        return [message, None, False]

    ## Get the id from the weird mention format str
    id_clean = re.search(regex_clean, id_dirty.group())

    clean_msg = message.replace(id_dirty.group(), "")
    ## Above line will leave a double space so get rid of it
    clean_msg = message.replace("  ", " ")
    
    ## Extracted id so just get rid of it in message to get "peval descriptor"
    ## Return message w/o weird str, extracted id, wether or not str had id
    return [clean_msg, int(id_clean), True]


def parse(author_userid: int, message: str, ctrl) -> str:
    lower_message = clean_mentions(message.lower())
    ## TODO Take care of when someone uses gpt peval @someone

    p_message = lower_message[0][4:]
    tag = lower_message[0][:3]
    userid = author_userid

    ## Message includes a mention so use that user id
    if (lower_message[2]):
        p_message = lower_message[0][4:9]
        userid = lower_message[1]

    response = None

    ## Bot was called
    if tag == 'gpt':
        
        ## Help was called for
        if p_message == 'help':
            response = 'Type: **gpt peval** for a psych eval'

        ## A psych eval was requested
        elif p_message == 'peval':
            try:
                gpt_input = ctrl.db.get_gptin(userid)
                response  = ctrl.gpt.get_psycheval(gpt_input)
            except Exception as e:
                print(e)
                response = 'User has no chracter defining messages, try typing some more meaningful messages!'

        ## Someone tried to use a command but was typed incorrectly. Is here so you dont save useless messages
        else:
            response = 'Error: I do not know what that command was.'



    return response