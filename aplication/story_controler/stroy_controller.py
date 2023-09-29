from fastapi import status, HTTPException

from aplication.story_controler import router
from domain.models.story_input import PrompQuery
from domain.services.story_services import create_cuento_with_pomp
from domain.models.story import Story

@router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
    response_model=Story
    )
def create_story(promp:PrompQuery):
    try:
        data = create_cuento_with_pomp(promp.promp, promp.id_token)
        return data.to_dict()
    except Exception as e :
        print(e.__str__)
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    