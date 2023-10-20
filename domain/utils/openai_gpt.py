from openai.error import InvalidRequestError
import os


class OpenAiGPT:
    __queue:list[dict]=[]
    
    def __init__(self):
        import openai
        self.__openai= openai
        self.__openai.api_key= os.getenv("OPENAI_API_KEY")
        
    @property
    def queue(self):
        return self.__queue
    
    def hadleMsgChat(self,message:str)->str:    
        self.__queue.append(
            {"role": "user", "content": message},
        )
        chatResponse = self.__openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.__queue,
        )
        reply = chatResponse.choices[0].message.content
        return reply
