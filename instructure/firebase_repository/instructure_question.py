from instructure.firebase_repository.firebase_comon import save_data_with_id
from domain.models.question_entity import QuestionModel

async def save_question(data:QuestionModel, id:str, uid_story:str):
    response = await save_data_with_id(id,f"Story/{uid_story}/Question",data.to_dict())
    return response