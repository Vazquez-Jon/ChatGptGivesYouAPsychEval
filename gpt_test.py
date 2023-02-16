## Jonathan Vazquez
## gpt_test.py
##
## Desc: Simple function used to see if the gpt_control.py class works

import gpt_control

gpt = gpt_control.GPT_Control()

print("Give me a psych eval based on someone that talks in the following way.\n This gonna happen to @lasercats one day\n This picture made me go braindead\n Yeah Joel, why won't you tell them that?\n@Colonel Custard just realized that since new raid is 48hrs now, if we get it done early we can try to take you through it on sat if you want\n @Colonel Custard just realized that since new raid is 48hrs now, if we get it done early we can try to take you through it on sat if you want")
print(gpt.get_psycheval("Give me a psych eval based on someone that talks in the following way.\n This gonna happen to @lasercats one day\n This picture made me go braindead\n Yeah Joel, why won't you tell them that?\n @Colonel Custard just realized that since new raid is 48hrs now, if we get it done early we can try to take you through it on sat if you want\n @Colonel Custard just realized that since new raid is 48hrs now, if we get it done early we can try to take you through it on sat if you want"))
print(gpt.get_psycheval('What are farts made of?'))