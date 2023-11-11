from pydantic import BaseModel, Field
 
class PrompQuery(BaseModel):
    prompt: str = Field("un cuento basado en caperucita roja que tenga por lo menos 5 parrafos")
    id_token: str = Field("1234567890")