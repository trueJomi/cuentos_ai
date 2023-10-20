import os
from dotenv import load_dotenv

load_dotenv()


class ChatGpt:
    __queue:list[dict]=[]
    
    def __init__(self):
        import openai
        self.__openai = openai
        self.__openai.api_key= os.getenv("OPENAI_API_KEY")
        with open( "./domain/static/PROM-BASE.txt", mode='r', encoding='utf-8') as file:
            self.__queue.append({"role": "system", "content": file.read()})
        
    @property
    def queue(self):
        return self.__queue
    
    def hadleMsgChat(self,message:str)->str:
        self.__queue.append(
            {"role": "user", "content": message},
        )
        chatResponse = self.__openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=self.__queue,
        )
        reply = chatResponse.choices[0].message.content
        return reply


