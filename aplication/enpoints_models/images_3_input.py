from pydantic import BaseModel 

class ImageGenerate3Input(BaseModel):
    id: int
    id_token: str