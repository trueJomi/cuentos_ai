from pydantic import BaseModel, Field

class QuestionInput(BaseModel):
    id_token: str = Field("id_token del usuario")
    id: str = Field("id del cuento")
    type: str = Field("tipo de pregunta")
    paragrafth: list[int] = Field([
        "lista de parrafos a los que se le va a generar preguntas",
        "ejemplo: [1,2,3]",1,2,3
    ])
    cantidad: int = Field("cantidad de preguntas")
