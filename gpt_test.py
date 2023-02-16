## Jonathan Vazquez
## gpt_test.py
##
## Desc: Simple function used to see if the gpt_control.py class works

import gpt_control

gpt = gpt_control.GPT_Control()

print(gpt.get_psych_eval('What is dark matter?')+'/n')
print(gpt.get_psych_eval('What are farts made of?')+'/n')