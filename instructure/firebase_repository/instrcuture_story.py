from instructure.firebase_repository.firebase_comon import save_data, get_data
from domain.models.story_entity import StoryModel
from domain.models.image_entity import ImageModel
from domain.models.image3_entity import Image3Model

async def save_story(data:StoryModel, id:str, uid:str):
    doc_dict = data.to_dict()
    await save_data(id,"Story",doc_dict,uid)
    return data

async def save_story_complete(data:StoryModel, id:str, uid:str):
    doc_dict = data.to_dict()
    await save_data(id,"Story",doc_dict,uid)
    return data

async def get_story(id:str, uid:str) -> StoryModel:
    data = await get_data(id,"Story",uid)
    story = StoryModel(**data)
    story.images = None
    try:
        intro_image = ImageModel(**data["images"]["introduction"])
        middle_image = ImageModel(**data["images"]["middle"])
        end_image = ImageModel(**data["images"]["end"])
        images = Image3Model(intro_image,middle_image,end_image)
        story.images = images
    except Exception as e:
        return story
    return story