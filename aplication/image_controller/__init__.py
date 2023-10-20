from fastapi import APIRouter

image_router = APIRouter(
    prefix='/images',
    tags=['images'],
)

