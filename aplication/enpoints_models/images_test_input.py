from pydantic import BaseModel, Field

class ImageTextResult(BaseModel):
    id_test: str = Field("url de la imagen de la introduccion")
    token: str = Field("url de la imagen del nudo")