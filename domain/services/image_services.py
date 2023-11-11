from domain.models.image_entity_send import SendQueryIamgeEntity
from instructure.images_respository.images_generate import send_data_image_1
from domain.models.image_entity import ImageModel





def image_service(prompt:str):
    message_api= SendQueryIamgeEntity(prompt)
    json_image = send_data_image_1(message_api)
    imageData = ImageModel(json_image["id"], json_image["path_storage"], json_image["params"])
    return imageData.to_dict()