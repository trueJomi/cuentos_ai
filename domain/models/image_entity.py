class ImageModel:
        
    def __init__(self, id: str = "", path_storage: str= "", params: dict={}):
        self.id = id
        self.path_storage = path_storage
        self.params = params
    
    def to_dict(self):
        return {
            "id": self.id,
            "path_storage": self.path_storage,
            "params": self.params
        }
        