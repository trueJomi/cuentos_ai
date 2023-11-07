from instructure.firebase_repository.firebase_comon import save_data
from domain.models.story_entity import StoryModel
from domain.models.story_complete_entity import StoryCompleteModel

async def save_story(data:StoryModel, id:str, uid:str):
    doc_dict = data.to_dict()
    await save_data(id,"Story",doc_dict,uid)
    return data

async def save_story_complete(data:StoryCompleteModel, id:str, uid:str):
    doc_dict = data.to_dict()
    await save_data(id,"Story",doc_dict,uid)
    return data