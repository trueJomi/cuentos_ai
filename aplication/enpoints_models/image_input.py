from pydantic import BaseModel, Field

class ImageQuery(BaseModel):
    prompt: str = Field("kid sidown chair in beach")
    id_token: str = Field("1234567890")