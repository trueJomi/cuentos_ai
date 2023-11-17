from pydantic import BaseModel, Field 
from typing import Optional
from datetime import datetime

class StoryComplete(BaseModel):
  id: Optional[str] = Field("opcional: depende si se crea o se pide")
  title: str= Field("Titulo del cuento")
  introduction: list[str] = Field(["primer parrafo de la introduccion","segundo parrafo de la introduccion"])
  middle: list[str] = Field(["primer parrafo del nudo","segundo parrafo del nudo"])
  images: dict = Field({
        "introduction":{
            "id": "id de imagen",
            "path_storage": "direccion del storage",
            "url": "url de la imagen",
            "params": "paramtros que tiene l imagen"
        },
        "middle":{
            "id": "id de imagen",
            "url": "url de la imagen",
            "path_storage": "direccion del storage",
            "params": "paramtros que tiene l imagen"
        },
        "end":{
            "id": "id de imagen",
            "url": "url de la imagen",
            "path_storage": "direccion del storage",
            "params": "paramtros que tiene l imagen"
        }
  })
  end: list[str] = Field(["primer parrafo del desenlace","segundo parrafo del desenlace"])
  date:datetime  = datetime.now()