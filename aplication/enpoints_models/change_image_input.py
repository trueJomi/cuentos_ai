from pydantic import BaseModel 
from typing import Optional

class ImageChangeInput(BaseModel):
    id: int
    prompt: Optional[str]
    id_token: str
    part: str