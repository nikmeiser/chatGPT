
import os
import openai

class OpenAiClient:
    def __init__(self, engine='davinci', temperature=1.0):
        self.api_key = os.environ.get('OPENAI_API_KEY')
        self.engine = engine
        self.max_tokens = 100
        self.n = 1
        self.temperature = temperature

    def set_engine(self, new_engine):
        self.engine = new_engine

    def set_temperature(self, new_temperature):
        if new_temperature >= 0.0 and new_temperature <= 2:
            self.temperature = new_temperature
        else:
            raise ValueError("Invalid temperature value. Value must be between 0.0 and 2.0")
