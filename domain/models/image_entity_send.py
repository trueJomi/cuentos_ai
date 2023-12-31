import os

TOKEN_API = os.getenv("TOKEN_API")

class SendQueryIamgeEntity: 
    def __init__(self, prompt):
        self.prompt = prompt
    
    def to_dict(self):
        rest_message = {
            "prompt": self.prompt,
            "token": TOKEN_API
        }
        return rest_message