from instructure.firebase_repository.firebase_comon import get_data,update_data
from domain.models.image_entity import ImageModel

def save_image(id:str, path:str , intro: ImageModel, middle:ImageModel, end:ImageModel, uid:str):
    data = get_data(id,path,uid)
    if(data["images"]):
        raise Exception("Ya existe una imagen")
    else:
        dict_intro = intro.to_dict()
        dict_middle = middle.to_dict()
        dict_end = end.to_dict()
        update_data(id,path,{
                "images": {
                    "introduction":dict_intro,
                    "middle":dict_middle,
                    "end":dict_end
                }
            },uid)
        return data

