from pydantic import BaseModel 

class ImageGenerate3Input(BaseModel):
    id: str
    id_token: str