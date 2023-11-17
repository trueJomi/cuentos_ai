class QuestionModel:
    def __init__(self, id: int, question:str , response:str, type:str):
        self.id = id
        self.question = question
        self.response = response
        self.type = type
    
    def to_dict(self) -> dict:
        entity = {
            "id": self.id,
            "question": self.question,
            "response": self.response,
            "type": self.type
        }
        return entity