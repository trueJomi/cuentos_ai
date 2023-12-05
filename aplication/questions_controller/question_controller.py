from fastapi import status, HTTPException

from aplication.questions_controller import question_router
from aplication.enpoints_models.story import Story
from domain.services.firebase_validate import validate_id_token
from aplication.enpoints_models.question_input import QuestionInput
from domain.services.question_service import generate_question_service

@question_router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
    )
async def create_story_question_literal(body:QuestionInput):
    # try:
    uid = validate_id_token(body.id_token)
    # except Exception as e :
    #     raise HTTPException(
    #         status_code= status.HTTP_401_UNAUTHORIZED,
    #         detail=f"Unauthorized API"
    #     )
    # try:
    data = await generate_question_service(body.type, body.paragrafth, body.cantidad, uid, body.id)
    return data
    # except Exception as e :
    #     raise HTTPException(
    #         status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail=f"{e}"
    #     )
        