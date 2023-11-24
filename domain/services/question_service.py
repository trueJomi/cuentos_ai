import asyncio
from instructure.firebase_repository.instrcuture_story import get_story
from instructure.firebase_repository.instructure_question import save_question
from domain.utils.transform import concat_list
from concurrent.futures import ThreadPoolExecutor
from domain.utils.questions_generate import generate_question, validate_type

async def generate_question_service(type: str, paragrafth:list[int] , cantidad:int, uid:str, id:str):
    validate_type(type)
    story = await get_story(uid, id)
    paragrafths_concat = concat_list(story, paragrafth)
    preguntas = generate_question(paragrafths_concat,cantidad, type, paragrafth)
    tasks = []
    for pregunta in preguntas:
        task  = save_question(pregunta, uid, id)
        tasks.append(task)
    await asyncio.gather(*tasks)

    quesions_dict = [pregunta.to_dict() for pregunta in preguntas]
    return  quesions_dict