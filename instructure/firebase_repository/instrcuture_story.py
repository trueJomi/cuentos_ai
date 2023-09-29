from instructure.firebase_repository.firebase_comon import save_data
from domain.models.story import Story

async def save_story(data:Story, id:str):
    doc_dict = Story.to_dict()
    await save_data(id,"Story",doc_dict)
    return data