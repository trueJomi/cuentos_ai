from fastapi import status, HTTPException

from aplication.image_controller import image_router
from domain.services.image_services import image_service
from aplication.enpoints_models.image_input import ImageQuery
from domain.services.firebase_validate import validate_id_token
from aplication.enpoints_models.image_result import ImageResult

@image_router.post(
        "/",
        status_code = status.HTTP_201_CREATED,
        response_model = ImageResult
    )
def create_image_controller(promp:ImageQuery):
    # try:
    #     validate_id_token(promp.id_token)
    # except ValueError as e :
    #     raise HTTPException(
    #         status_code= status.HTTP_401_UNAUTHORIZED,
    #         detail=f"Error: Unauthorized API"
    #     )
    try:
        data = image_service(promp.prompt)
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
        
