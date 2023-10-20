from domain.utils.base64_to_image import to_image
from instructure.storage_repository.storage_image import upload_file

img_name="eb0f49c1-50ec-4c76-9fcd-41eaa796366d"

def test_tranform_base64_to_image():
    with open('tests/static/bin.txt', 'rb') as file:
        image_bytes = file.read()
        array_bytes= bytearray(image_bytes)
        image = to_image(array_bytes)
    assert type(image['id']) is str
    assert type(image['direction']) is str

def test_save_image():
    url = upload_file(f"domain/static/temp/{img_name}.png", img_name)
    assert type(url) is str