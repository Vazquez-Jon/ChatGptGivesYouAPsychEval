## Jonathan Vazquez
## gpt_control.py
##
## Desc: Class to get response from gpt-3

import openai

class GPT_Control():
    def __init__(self) -> None:
        self.api_key = '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'
        

    ## Func to get psych eval
    def get_psycheval(self, input):
        openai.api_key = self.api_key

        response = openai.Completion.create(
            model             = "text-davinci-003",
            prompt            = input,
            temperature       = 0.95,
            max_tokens        = 3000,
            top_p             = 1.0,
            frequency_penalty = 0.0,
            presence_penalty  = 0.0
        )

        return response['choices'][0]['text']