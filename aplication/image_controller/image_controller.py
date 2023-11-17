from fastapi import status, HTTPException

from aplication.image_controller import image_router
from domain.services.image_services import image_service, generate_3_images_service
from aplication.enpoints_models.image_input import ImageQuery
from domain.services.firebase_validate import validate_id_token
from aplication.enpoints_models.image_result import ImageResult
from aplication.enpoints_models.images_3_input import ImageGenerate3Input
from aplication.enpoints_models.images_3_result import ResponseImages3

@image_router.post(
        "/",
        status_code = status.HTTP_201_CREATED,
        response_model = ImageResult
    )
def create_image_controller(promp:ImageQuery):
    try:
        validate_id_token(promp.id_token)
    except ValueError as e :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Error: Unauthorized API"
        )
    try:
        data = image_service(promp.prompt)
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
        
@image_router.post(
        "/from-story",
        status_code = status.HTTP_201_CREATED,
        response_model = ResponseImages3
    )
async def create_image_3_story_controller(body:ImageGenerate3Input):
    try:
       uid = validate_id_token(body.id_token)
    except ValueError as e :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Error: Unauthorized API"
        )
    try:
        data = await generate_3_images_service(body.id, uid)
        return data.to_dict()
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )