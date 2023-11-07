from fastapi import status, HTTPException

from aplication.enpoints_models.story_input import PrompQuery
from aplication.image_controller import image_router
from domain.services.image_services import image_service, create_image_3_service
from aplication.enpoints_models.image_input import ImageQuery

@image_router.post(
        "/",
        status_code = status.HTTP_201_CREATED,
        # response_model = ImagesResult
    )
def create_story_controller(promp:ImageQuery):
    try:
        data = image_service(promp.prompt)
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
async def create_story_controller(promp:PrompQuery):
    try:
        data = create_image_3_service(promp.promp, promp.id_token)
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )