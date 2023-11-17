from fastapi import FastAPI
import os
import uvicorn
from aplication.story_controler.stroy_controller import story_router
from aplication.image_controller.image_controller import image_router
from aplication.test_controller.test_controller import test_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from tests.test_api import test_service_3_resturn

load_dotenv()

app = FastAPI(
    title="API Cuentos",
    description="API para crear cuentos con imagenes ",
    version="0.7.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(story_router)
app.include_router(image_router)
app.include_router(test_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True , port=4200, workers=4)
