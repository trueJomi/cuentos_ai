import os

TOKEN_API = os.getenv("TOKEN_API")

class SendUrlInput:
    def __init__(self, url: str):
        self.url = url
    
    def to_dict(self):
        rest_message = {
            "url": self.url,
            "token": TOKEN_API
        }
        return rest_message