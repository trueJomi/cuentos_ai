from pydantic import BaseModel, Field

class ResponseImages3(BaseModel):
    introduction: dict = Field({
        "id":"id",
        "path_storage": "ubicacion de la imagen",
        "params":{}
    })
    middle: dict = Field({
        "id":"id",
        "path_storage": "ubicacion de la imagen",
        "params":{}
    })
    end: dict = Field({
        "id":"id",
        "path_storage": "ubicacion de la imagen",
        "params":{}
    })