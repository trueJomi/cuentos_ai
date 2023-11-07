from fastapi import FastAPI
import os
import uvicorn
from aplication.story_controler.stroy_controller import story_router
from aplication.image_controller.image_controller import image_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from domain.utils.chat_gpt import ChatGpt
from domain.utils.create_prmpt_image import create_prompt
from domain.services.image_services import image_service

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(story_router)
app.include_router(image_router)

@app.get("/")
def home():
    with ThreadPoolExecutor(max_workers=1) as executor:
        prompt_promise = executor.submit(create_prompt,["Al llegar a la casa de la abuelita, el lobo amigable se despidió de Caperucita y continuó su camino. Caperucita entró alegremente en la acogedora casita y encontró a su abuelita esperándola con una amplia sonrisa. Emocionada, Caperucita le contó a su abuelita sobre su inesperado encuentro con el amigable lobo. Desde aquel día, Caperucita y el lobo se convirtieron en grandes amigos. Juntos, visitaban constantemente a la abuelita, llenando su hogar de risas y alegría. Caperucita aprendió que, a veces, las apariencias pueden ser engañosas y que aquellos que parecen peligrosos pueden convertirse en amigos en busca de compañía.","Moraleja:Este cuento nos enseña la importancia de no juzgar a los demás por su apariencia y de abrir nuestro corazón a nuevas amistades. A veces, los aparentes peligros se convierten en valiosas lecciones de vida y en la oportunidad de crear lazos de amistad inesperados. Con su capa roja como símbolo de amistad y valentía, Caperucita Roja y el lobo amable demostraron que la empatía y la amistad genuina pueden romper barreras y transformar vidas."])
    prompt = prompt_promise.result()
    return {
        "prompt":prompt
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=4200, workers=4,  reload=True)
