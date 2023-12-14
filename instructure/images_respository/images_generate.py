import os
import re
import requests
from domain.models.image_entity_send import SendQueryIamgeEntity
from domain.models.image_entity_input import SendImageInputText
from domain.utils.dalle_image import Dalle2
from domain.models.image_url_input import SendUrlInput
from domain.models.image_entity import ImageModel
from domain.models.image3_entity import Image3Model

API_URL = os.getenv("URL_API")

def send_data_image_1(message_api:SendQueryIamgeEntity) -> ImageModel:
    response =requests.post(
        f"{API_URL}/getImage/",
        headers={
            'Content-Type': 'application/json',
        },
        json=message_api.to_dict())
    if (response.status_code >= 400):
        raise Exception(response.json()["detail"])
    json_image = response.json()
    image = ImageModel(**json_image)
    return image

def send_data_image_3(message_api:SendImageInputText) -> Image3Model:
    response =requests.post(
        f"{API_URL}/get3Images/",
        headers={
            'Content-Type': 'application/json',
        },
        json=message_api.to_dict())
    if (response.status_code >= 400):
        raise Exception(response.json()["detail"])
    json_image = response.json()
    introducton_image =ImageModel(
        **json_image["introduction"]
    )
    middle_image = ImageModel(
        **json_image["middle"]
        )
    end_image = ImageModel(
        **json_image["end"]
    )
    images = Image3Model(introducton_image,middle_image,end_image)
    return images
    
def generate_dalle_image(prompt:str):
    image_dalle = Dalle2()
    url=image_dalle(prompt)
    return url

def save_image_dalle(meesage_api:SendUrlInput):
    response = requests.post(
        f"{API_URL}/saveImage/",
        headers={
            'Content-Type': 'application/json',
        },
        json=meesage_api.to_dict())
    if (response.status_code >= 400):
        raise Exception(response.json()["detail"])
    return response.json()

def exist_url():
    response = requests.get(
        f'{API_URL}/exist/',
    )
    if (response.status_code >= 400):
        return False
    if response.json()["message"]== "ok":
        return True
    else:
        return False
