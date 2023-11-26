from domain.models.story_entity import StoryModel

def concat_list(data:StoryModel, array_pargraphs:list[int]):
    arrayconcat = [*data.introduction,*data.middle, *data.end]
    sort_array = sorted(array_pargraphs)
    paragrafts = []
    for i in sort_array:
        paragrafts.append(arrayconcat[i])
    return paragrafts


