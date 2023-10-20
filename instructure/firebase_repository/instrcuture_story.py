from instructure.firebase_repository.firebase_comon import save_data
from domain.models.story_entity import StoryModel

async def save_story(data:StoryModel, id:str):
    doc_dict = data.to_dict()
    await save_data(id,"Story",doc_dict)
    return data