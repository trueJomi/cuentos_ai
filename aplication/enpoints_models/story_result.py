from pydantic import BaseModel, Field 
from datetime import datetime

class Story(BaseModel):
  id: str = Field( default=None, examples=["opcional: depende si se crea o se pide"] )
  title: str= Field(default=None, examples=["Titulo del cuento"])
  introduction: list[str] = Field(default=None, examples=[["primer parrafo de la introduccion","segundo parrafo de la introduccion"]])
  middle: list[str] = Field(default=None, examples=[["primer parrafo del nudo","segundo parrafo del nudo"]])
  images: dict = Field(default=None, examples=[
      {
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
    }
  ])
  end: list[str] = Field(default=None, examples=[["primer parrafo del desenlace","segundo parrafo del desenlace"]])
  date:datetime  = Field(default=datetime.now(), examples=["2021-08-01T00:00:00.000Z"])