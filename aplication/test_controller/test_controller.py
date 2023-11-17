from fastapi import status, HTTPException


from aplication.test_controller import test_router
from aplication.enpoints_models.story_complete_result import StoryComplete
from aplication.enpoints_models.story_input import PrompQuery
from tests.test_api import test_service_3_resturn

@test_router.post(
    "/story/all",
    status_code = status.HTTP_201_CREATED,
    response_model=StoryComplete
    )
def test_create_story_complete_controller():
    try:
        data = test_service_3_resturn()
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
