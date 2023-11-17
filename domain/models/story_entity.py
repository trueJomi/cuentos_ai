from datetime import datetime
from domain.models.image3_entity import Image3Model

class StoryModel():
    def __init__(
      self,
      tittle: str,
      introduction: list[str],
      middle: list[str],
      end: list[str],
      id:str,
      images:Image3Model=None,
    ):
        self.id = id
        self.title = tittle
        self.introduction = introduction
        self.middle = middle
        self.end = end
        self.date = datetime.now()
        self.images = images

    def __eq__(self, other:'StoryModel') -> bool:
        return self.id == other.id

    def to_dict(self) -> dict:
        if self.images:
            entity = {
                "title": self.title,
                "introduction": self.introduction,
                "middle": self.middle,
                "end": self.end,
                "images": self.images.to_dict(),
                "date":self.date
            }
        else:
            entity = {
                "title": self.title,
                "introduction": self.introduction,
                "middle": self.middle,
                "end": self.end,
                "date":self.date
            }
        return entity