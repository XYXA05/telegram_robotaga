import openai

class test0_chat():
    def __init__(self, prompt):
        self.prompt = prompt
        self.model = "text-davinci-003"
        self.max_tokens = 150
        self.top_p = 1
        self.stop = None
        self.temperature = 0.5

    def get_response(self):
        response = openai.Completion.create(
            engine=self.model,
            prompt=self.prompt,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            stop=self.stop,
            temperature=self.temperature,
        )
        return response.choices[0].text.strip()


class test1_chat():
    def __init__(self, prompt):
        self.prompt = prompt
        self.model = "text-davinci-003"
        self.max_tokens = 200   
        self.top_p = 1
        self.frequency_penalty = 0
        self.presence_penalty = 0.6
        #self.stop = None,
        self.temperature = 0.9


    def get_response(self):
        response = openai.Completion.create(
            engine=self.model,
            prompt=self.prompt,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            #stop=self.stop,
            temperature=self.temperature,
        )
        return response.choices[0].text.strip()
    
class text():
    def __init__(self, prompt):
        self.prompt = prompt

    def get_response(self):
        prepared_text = self.prompt
        return prepared_text

import random
class random_text():

    def __init__(self, prompt):
        self.prompt = prompt

    def get_response(self):
        prepared_text =  self.parse_spintax(self.prompt)
        return prepared_text

    def parse_spintax(self, text):
        while '{' in text:
            start = text.find('{')
            end = text.find('}')
            
            if start != -1 and end != -1:
                spintax = text[start + 1:end]
                options = spintax.split('|')
                selected_option = random.choice(options)
                text = text[:start] + selected_option + text[end + 1:]
        
        return text
    

model_map = {
    'test0': test0_chat,
    'test1': test1_chat,
    'text_zagatovga':text,
    'spintaxst': random_text
}