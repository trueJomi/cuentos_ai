from pydantic import BaseModel, Field

class ImageResult(BaseModel):
    id: str = Field("id de imagen")
    path_storage: str = Field("path la imagen")
    params: dict = Field({})