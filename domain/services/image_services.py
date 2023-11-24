from domain.models.image_entity_send import SendQueryIamgeEntity
from instructure.images_respository.images_generate import send_data_image_1, send_data_image_3
from domain.models.image_entity_input import SendImageInputText
from instructure.firebase_repository.instrcuture_story import get_story
from concurrent.futures import ThreadPoolExecutor
from domain.utils.create_prmpt_image import create_prompt

def image_service(prompt:str):
    message_api= SendQueryIamgeEntity(prompt)
    image = send_data_image_1(message_api)
    return image.to_dict()

async def generate_3_images_service(id:int, uid:str):
    story = await get_story(id,uid)
    if (story.images):
        raise Exception("Ya existen images en este cuento")
    with ThreadPoolExecutor(max_workers=3) as executor:
        init_promise = executor.submit(create_prompt, story.introduction)
        middle_promise = executor.submit(create_prompt, story.middle)
        final_promise = executor.submit(create_prompt, story.end)
    init = init_promise.result()
    middle = middle_promise.result()
    final = final_promise.result()
    message_api= SendImageInputText(init,middle,final)
    images = send_data_image_3(message_api)
    return images