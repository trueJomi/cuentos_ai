from instructure.config.config import store

def get_url(id:str):
    image =store.blob(f"images/{id}.png")
    image.make_public()
    return image.public_url