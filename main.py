from fastapi import FastAPI
import uvicorn
from aplication.story_controler.stroy_controller import story_router
from aplication.image_controller.image_controller import image_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

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

if __name__ == "__main__":
    uvicorn.run(app, port=4200)
