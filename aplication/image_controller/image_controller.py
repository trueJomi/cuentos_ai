from fastapi import status, HTTPException

from aplication.image_controller import image_router
from domain.services.image_services import create_image
from domain.models.enpoints_models.image_input import ImageQuery

@image_router.post(
        "/",
        status_code = status.HTTP_201_CREATED,
        # response_model = ImagesResult
    )
def create_story_controller(promp:ImageQuery):
    try:
        data = create_image(promp.promp)
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
        
@image_router.post(
        "/history",
        status_code = status.HTTP_201_CREATED,
        # response_model = ImagesResult
    )
def create_story_controller(promp:ImageQuery):
    try:
        data = create_image(promp.promp)
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )