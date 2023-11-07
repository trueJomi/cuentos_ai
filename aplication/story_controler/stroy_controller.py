from fastapi import status, HTTPException

from aplication.story_controler import story_router
from aplication.enpoints_models.story_input import PrompQuery
from domain.services.story_services import create_cuento_with_pomp
from aplication.enpoints_models.story import Story

@story_router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
    response_model=Story
    )
async def create_story_controller(promp:PrompQuery):
    try:
        data = await create_cuento_with_pomp(promp.promp, promp.id_token)
        return data.to_dict()
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {e}"
        )
    