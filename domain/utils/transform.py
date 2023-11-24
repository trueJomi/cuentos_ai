from domain.models.story_entity import StoryModel

def concat_list(data:StoryModel, array_pargraphs:list[int]):
    arrayconcat = data.introduction + data.middle + data.end
    paragrafts = []
    for i in array_pargraphs:
        paragrafts.append(arrayconcat[i])    
    return arrayconcat


