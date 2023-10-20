import os
from domain.models.image_entity_send import SendQueryIamgeEntity
import requests
from domain.utils.base64_to_image import to_image

API_URL = os.getenv("URL_API")

def create_image(prompt:str):
    message_api= SendQueryIamgeEntity(prompt)
    response =requests.post(
        f"{API_URL}/sdapi/v1/txt2img",
        headers={
            'Content-Type': 'application/json',
        },
        json=message_api.to_dict())
    json_image = response.json()
    image_str = json_image["images"][0]
    image = to_image(image_str)
    return {
        "info_image":json_image["parameters"],
        "id":image['id'],
        "ubication":image['direction']
    }