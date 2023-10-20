from pydantic import BaseModel, Field

class ImageTextResult(BaseModel):
    introduction: str = Field("url de la imagen de la introduccion")
    middle: str = Field("url de la imagen del nudo")
    end: str = Field("url de la imagen del desenlace")