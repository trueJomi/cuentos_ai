from fastapi import status, HTTPException

from aplication.story_controler import story_router
from aplication.enpoints_models.story_input import PrompQuery
from domain.services.story_services import create_story_service
from aplication.enpoints_models.story_result import Story
from domain.services.firebase_validate import validate_id_token
from domain.services.evaluate_service import create_evaluation_story_complete_service
@story_router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
    response_model= Story
    )
async def create_story_controller(promp:PrompQuery):
    try:
        uid = validate_id_token(promp.id_token)
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Unauthorized API"
        )
    try:
        data = await create_story_service(promp.prompt, uid)
        dict_data = data.to_dict()
        dict_data["id"] = data.id
        return dict_data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}"
        )
        
@story_router.post(
    "/evaluation",
    status_code = status.HTTP_201_CREATED,
    response_model= Story
    )
async def create_story_evaluation( body:PrompQuery ):
    # try:
    uid = validate_id_token(body.id_token)
    # except Exception as e :
    #      raise HTTPException(
    #           status_code= status.HTTP_401_UNAUTHORIZED,
    #           detail=f"Unauthorized API"
    #      )
    # try:
    data = await create_evaluation_story_complete_service(body.prompt, uid)
    dict_data = data.to_dict()
    dict_data["id"] = data.id
    return dict_data
    # except Exception as e :
    #     raise HTTPException(
    #         status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail=f"{e}"
    #     ) 
    