from domain.models.image_entity_send import SendQueryIamgeEntity
import domain.repositorys
from domain.utils.create_prmpt_image import create_prompt
from concurrent.futures import ThreadPoolExecutor
from instructure.images_respository.images_generate import send_data_image_1
from instructure.images_respository.images_generate import send_data_image_3
from domain.repositorys import save_story_complete
from domain.models.image_entity_input import SendImageInputText
from domain.services.story_services import create_story_service
from domain.models.image_entity import ImageModel
from domain.models.story_complete_entity import StoryCompleteModel




def image_service(prompt:str):
    message_api= SendQueryIamgeEntity(prompt)
    json_image = send_data_image_1(message_api)
    return {
        "info_image":json_image["params"],
        "id":json_image['id'],
        "path_storage":json_image['path_storage']
    }
    
def create_image_3_service(prompt:str, id_token:str):
    # decoded_token = verify_id_token(id_token)
    # uid = decoded_token['uid']
    cuento = create_story_service(prompt)
    with ThreadPoolExecutor(max_workers=3) as executor:
        init_promise = executor.submit(create_prompt, cuento.introduction)
        middle_promise = executor.submit(create_prompt, cuento.middle)
        final_promise = executor.submit(create_prompt, cuento.end)
    init = init_promise.result()
    middle = middle_promise.result()
    final = final_promise.result()
    data = SendImageInputText(init,middle, final)
    
    json_image = send_data_image_3( data )
    introducton_image =ImageModel(json_image["introducction"]["id"], json_image["introducction"]["path_storage"], json_image["introducction"]["params"])
    middle_image = ImageModel(json_image["middle"]["id"], json_image["middle"]["path_storage"], json_image["middle"]["params"])
    end_image = ImageModel(json_image["end"]["id"], json_image["end"]["path_storage"], json_image["end"]["params"])
    
    data_complete = StoryCompleteModel(cuento, introducton_image, middle_image, end_image)
    save_story_complete(data_complete,"ulpoOHsuhXfhvF4TPUrmkmSi3tQ2",data_complete.id)
    return data_complete.to_dict()