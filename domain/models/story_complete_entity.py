from domain.models.story_entity import StoryModel
from domain.models.image_entity import ImageModel

class StoryCompleteModel(StoryModel):
    def __init__(self, init_data:StoryModel, image_1:ImageModel, iamge_2:ImageModel, iamge_3:ImageModel):
        super().__init__(init_data.title,init_data.introduction,init_data.middle,init_data.end,init_data.id)
        self.images =  {
            "introduction":image_1.to_dict(),
            "middle":iamge_2.to_dict(),
            "end":iamge_3.to_dict()
        }
    
    def to_dict(self) -> dict:
        entity = {
            "title": self.title,
            "introduction": self.introduction,
            "middle": self.middle,
            "end": self.end,
            "images":{
                "introduction":self.images["introduction"],
                "middle":self.images["middle"],
                "end":self.images["end"]
            },
            "date":self.date
        }
        return entity