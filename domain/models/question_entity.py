class QuestionModel:
    def __init__(self, reference:list[int] ,question:str , response:str, type:str, id: int=None):
        self.id = id
        self.reference = reference
        self.question = question
        self.response = response
        self.type = type
    
    def to_dict(self) -> dict:
        entity = {
            "id": self.id,
            "reference": self.reference,
            "question": self.question,
            "response": self.response,
            "type": self.type
        }
        if self.id is None:
            del entity["id"]
        return entity