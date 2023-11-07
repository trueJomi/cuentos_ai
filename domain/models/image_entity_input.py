import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_API = os.getenv("TOKEN_API")

class SendImageInputText:
    def __init__(self, init,middle, final):
        self.init = init
        self.middle = middle
        self.final = final
        
    def to_dict(self):
        rest_message = {
            "init": self.init,
            "middle": self.middle,
            "final": self.final,
            "token": TOKEN_API
        }
        return rest_message