from pydantic import BaseModel, Field

class ImageResult(BaseModel):
    id: str = Field("id de imagen")
    url: str = Field("url de la imagen")
    params: str = Field("paramtros que tine l imagen")