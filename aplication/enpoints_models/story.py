from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Story(BaseModel):
  id: Optional[str] = Field("opcional: depende si se crea o se pide")
  title: str= Field("Titulo del cuento")
  introduction: list[str] = Field(["primer parrafo de la introduccion","segundo parrafo de la introduccion"])
  middle: list[str] = Field(["primer parrafo del nudo","segundo parrafo del nudo"])
  end: list[str] = Field(["primer parrafo del desenlace","segundo parrafo del desenlace"])
  date:datetime  = datetime.now()