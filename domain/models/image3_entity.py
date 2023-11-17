from domain.models.image_entity import ImageModel

class Image3Model:
        
    def __init__(self, introducction:ImageModel, middle:ImageModel, end:ImageModel):
        self.introduction = introducction
        self.middle = middle
        self.end = end
    
    def to_dict(self):
        return {
            "introduction":self.introduction.to_dict(),
            "middle":self.middle.to_dict(),
            "end":self.end.to_dict()
        }