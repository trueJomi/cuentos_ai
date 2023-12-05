from datetime import datetime
from domain.models.image_entity import ImageModel

class EvaluationModel():

    def __init__(
        self,
        title: str,
        introduction: list[str],
        middle: list[str],
        end: list[str],
        id:str,
        image:ImageModel=None,
        date:datetime=None
        ):
            self.id = id
            self.title = title
            self.introduction = introduction
            self.middle = middle
            self.end = end
            if date:
                self.date = date
            else:
                self.date = datetime.now()
            self.image = image

    def __eq__(self, other:'EvaluationModel') -> bool:
        return self.id == other.id

    def to_dict(self) -> dict:
        entity = {
            "title": self.title,
            "introduction": self.introduction,
            "middle": self.middle,
            "end": self.end,
            "date":self.date
        }
        if self.image is not None:
            entity["image"]  = self.image.to_dict()
        return entity