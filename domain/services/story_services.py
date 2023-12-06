from domain.utils.chat_gpt import ChatGpt
from domain.utils.decript_text import decript_text_introduccion, decript_text_middle, decript_text_end, decript_text_tittle
from domain.models.story_entity import StoryModel
from domain.repositorys import exist_url, send_data_image_3, save_story
from domain.models.image_entity_input import SendImageInputText
from domain.utils.create_prmpt_image import create_prompt
from concurrent.futures import ThreadPoolExecutor
import uuid


def create_cuento_with_pompt(entrada:str)-> StoryModel:
    context = ChatGpt("PROMPT_CREATE_CUENTO")
    text_raw= context.hadleMsgChat(f'prompt = {entrada}, respondeme con el texto con este promp')
    title = decript_text_tittle(text_raw)
    list_introduction = decript_text_introduccion(text_raw)
    list_middle = decript_text_middle(text_raw)
    list_end = decript_text_end(text_raw)
    uid = str(uuid.uuid4())
    data = StoryModel(title,list_introduction,list_middle,list_end,uid, entrada)
    return data

async def create_story_service(entrada:str, uid:str)-> StoryModel:
    data = create_story_complete_with_prompt(entrada)
    await save_story(data,uid,data.id)
    return data


def create_story_complete_with_prompt(prompt:str):
    cuento = create_cuento_with_pompt(prompt)
    try :
        exist_url()
        with ThreadPoolExecutor(max_workers=3) as executor:
            init_promise = executor.submit(create_prompt, cuento.introduction)
            middle_promise = executor.submit(create_prompt, cuento.middle)
            final_promise = executor.submit(create_prompt, cuento.end)
        init = init_promise.result()
        middle = middle_promise.result()
        final = final_promise.result()
        data = SendImageInputText(init,middle, final) 
        images = send_data_image_3( data )
        cuento.images=images
    except Exception as e:
        return cuento
    return cuento
