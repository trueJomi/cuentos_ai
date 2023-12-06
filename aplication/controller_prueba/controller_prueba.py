from fastapi import status, HTTPException


from aplication.controller_prueba import test_router
from tests.static.data import prueba_service_3_return
from aplication.enpoints_models.story_result import Story

@test_router.post(
    "/story/all",
    status_code = status.HTTP_201_CREATED,
    response_model=Story
    )
def test_create_story_complete_controller():
    try:
        data = prueba_service_3_return()
        return data.to_dict()
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )

@test_router.post(
    "/question/all",
    status_code = status.HTTP_201_CREATED,
    response_model=Story
    )
def test_create_story_complete_controller():
    try:
        data = prueba_service_3_return()
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
