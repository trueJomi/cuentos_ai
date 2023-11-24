from fastapi import APIRouter

question_router = APIRouter(
    prefix='/question',
    tags=['questions'],
)