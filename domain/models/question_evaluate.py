from domain.models.question_entity import QuestionModel

class QuestionEvaluateModel():
    def __init__(self,question:str , response:int, type:str,options:list[str]=None,id: int=None):
        self.id = id
        self.question = question
        self.response = response
        self.type = type
        self.options = options
    
    def to_dict(self) -> dict:
        entity = {
            "id": self.id,
            "question": self.question,
            "response": self.response,
            "type": self.type,
            "options": self.options
        }
        if id is not None:
            entity["id"] = self.id
            
        return entity