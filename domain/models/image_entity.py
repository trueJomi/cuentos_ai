from instructure.images_respository.images_url import get_url

class ImageModel:
        
    def __init__(self, id: str, path_storage: str, params: dict):
        self.id = id
        self.path_storage = path_storage
        self.params = params
        self.url = get_url(id)
    
    def to_dict(self):
        return {
            "id": self.id,
            "path_storage": self.path_storage,
            "params": self.params,
            "url": self.url
        }
        