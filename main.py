import aplication.questions_controller
from fastapi import FastAPI
import pytest
import uvicorn
from aplication.story_controler.stroy_controller import story_router
from aplication.image_controller.image_controller import image_router
from aplication.questions_controller.question_controller import question_router
from aplication.controller_prueba.controller_prueba import test_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="API Cuentos",
    description="API para crear cuentos con imagenes ",
    version="0.7.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://cuentos-ai.web.app',
        'http://localhost:5173',
        'https://api.cuentos-ai.tech',
        'https://cuentos-ai.firebaseapp.com',
        'http://api.cuentos-ai.tech/',
        'https://cuentos-ai.tech/',
        'https://www.cuentos-ai.tech/'
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['*'],
)

app.include_router(story_router)
app.include_router(image_router)
app.include_router(question_router)
app.include_router(test_router)


if __name__ == "__main__":
    pytest.main()
    uvicorn.run("main:app", reload=True, port=4200, workers=4)
