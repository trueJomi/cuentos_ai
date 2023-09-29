from fastapi import FastAPI
from aplication.story_controler.stroy_controller import router as story_router

app = FastAPI()

app.include_router(story_router)
