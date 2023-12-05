from datetime import datetime
from domain.models.image3_entity import Image3Model

class StoryModel():
    def __init__(
      self,
      title: str,
      introduction: list[str],
      middle: list[str],
      end: list[str],
      id:str,
      input:str=None,
      images:Image3Model=None,
      date:datetime=None
    ):
        self.id = id
        self.title = title
        self.introduction = introduction
        self.middle = middle
        self.end = end
        self.input = input
        if date:
            self.date = date
        else:
            self.date = datetime.now()
        self.images = images

    def __eq__(self, other:'StoryModel') -> bool:
        return self.id == other.id

    def to_dict(self) -> dict:
        entity = {
            "title": self.title,
            "introduction": self.introduction,
            "middle": self.middle,
            "end": self.end,
            "input": self.input,
            "date":self.date
        }
        if self.images is not None:
            entity["images"]  = self.images.to_dict()
        return entity