import domain.utils.questions_generate
from fastapi import status, HTTPException

from aplication.questions_controller import question_router
from domain.services.firebase_validate import validate_id_token
from aplication.enpoints_models.question_input import QuestionInput
from domain.services.question_service import generate_question_service, generate_evaluation_question_serivice
from aplication.enpoints_models.story_result import Story
from aplication.enpoints_models.images_3_input import ImageGenerate3Input

@question_router.post(
    "/",
    status_code = status.HTTP_201_CREATED,
    )
async def create_story_question_literal(body:QuestionInput):
    try:
        uid = validate_id_token(body.id_token)
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Unauthorized API"
        )
    try:
        data = await generate_question_service(body.type, body.paragrafth, body.cantidad, uid, body.id)
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}"
        )
        
@question_router.post(
    "/evaluation",
    status_code = status.HTTP_201_CREATED,
)
async def create_question_evaluation(body:ImageGenerate3Input):
    try:
        uid = validate_id_token(body.id_token)
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Unauthorized API"
        )
    try:
        data = await generate_evaluation_question_serivice(uid, body.id)
        return data
    except Exception as e :
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}"
        )
        