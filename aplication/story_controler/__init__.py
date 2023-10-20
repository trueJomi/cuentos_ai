from fastapi import APIRouter

story_router = APIRouter(
    prefix='/story',
    tags=['story'],
)