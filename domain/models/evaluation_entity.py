from datetime import datetime
from domain.models.image_entity import ImageModel
from domain.models.story_entity import StoryModel

class EvaluationModel(StoryModel):

    def __init__(self, title: str, introduction: list[str], middle: list[str], end: list[str], id: str, input: str = None, image: ImageModel = None, date: datetime = None):
        super().__init__(title, introduction, middle, end, id, input, None, date)
        self.image: ImageModel = image
        
    
    def __eq__(self, other:'EvaluationModel') -> bool:
        return self.id == other.id

    def to_dict(self) -> dict:
        entity = super().to_dict()
        if self.image is not None:
            entity["image"]  = self.image.to_dict()
        return entity