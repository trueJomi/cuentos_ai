import asyncio
from domain.services.story_services import create_cuento_with_pompt
from domain.utils.create_prmpt_image import create_prompt
from instructure.images_respository.images_generate import send_data_image_1
from instructure.firebase_repository.instructure_evaluate import save_evaluation, save_question_evalaute
from domain.utils.questions_generate import generate_evaluation_question
from domain.models.evaluation_entity import EvaluationModel
from aplication.utils.validate_errors import validate_errors


def create_evaluation_story_complete_with_prompt(prompt:str):
    cuento = create_cuento_with_pompt(prompt)
    story = [*cuento.introduction,*cuento.middle, *cuento.end]
    image_prompt = create_prompt(story) 
    image = send_data_image_1(image_prompt)
    questions = generate_evaluation_question(story)
    class_evaluation = EvaluationModel(cuento.title, cuento.introduction, cuento.middle, cuento.end, cuento.id, image)
    return {
        'evaluation':class_evaluation,
        'questions':questions,
    }

async def create_evaluation_story_complete_service(prompt:str, uid:str) -> EvaluationModel :
    parts_data = create_evaluation_story_complete_with_prompt(prompt)
    data = parts_data['evaluation'] 
    preguntas = parts_data['questions']
    await save_evaluation(data,uid,data.id)
    tasks = []
    for pregunta in preguntas:
        task  = save_question_evalaute(pregunta, uid, data.id)
        tasks.append(task)
    await asyncio.gather(*tasks)
    return data
