from datetime import datetime

class StoryModel():
    def __init__(
      self,
      tittle: str,
      introduction: list[str],
      middle: list[str],
      end: list[str],
      id:str | None = None
    ):
        self.id = id
        self.tittle = tittle
        self.introduction = introduction
        self.middle = middle
        self.end = end
        self.date = datetime.now()

    def __eq__(self, other:'StoryModel') -> bool:
        return self.id == other.id

    def to_dict(self) -> dict:
        if self.id:
            entity = {
                "id": self.id,
                "tittle": self.tittle,
                "introduction": self.introduction,
                "middle": self.middle,
                "end": self.end,
                "date":self.date
            }
            return entity
        else:
            entity = {
                "tittle": self.tittle,
                "introduction": self.introduction,
                "middle": self.middle,
                "end": self.end,
                "date":self.date
            }
            return entity