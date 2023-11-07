from copy import copy
from domain.utils.chat_gpt import ChatGpt
from firebase_admin.auth import verify_id_token
from domain.repositorys import save_story
from domain.utils.decript_text import decript_text_introduccion, decript_text_middle, decript_text_end, decript_text_tittle
from domain.models.story_entity import StoryModel
import uuid


def create_story_service(entrada:str)-> StoryModel:
    context = ChatGpt("PROMPT_CREATE_CUENTO")
    text_raw= context.hadleMsgChat(f'prompt = {entrada}, respondeme con el texto con este promp')
    tittle = decript_text_tittle(text_raw)
    list_introduction = decript_text_introduccion(text_raw)
    list_middle = decript_text_middle(text_raw)
    list_end = decript_text_end(text_raw)
    uid = str(uuid.uuid4())
    data = StoryModel(tittle,list_introduction,list_middle,list_end,uid)
    return data

async def create_cuento_with_pomp(entrada:str, id_token:str)-> StoryModel:
    # decoded_token = verify_id_token(id_token)
    # uid = decoded_token['uid']
    data = create_story_service(entrada)
    await save_story(data,"ulpoOHsuhXfhvF4TPUrmkmSi3tQ2",data.id)
    return data  