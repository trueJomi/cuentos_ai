from instructure.config.config import db
import instructure.firebase_repository.firebase_comon


async def save_data(id:str, path:str , data: dict, uid:str):
    new_data = await  db.collection(f'User/{id}/{path}').document(uid).set(data)
    return new_data

async def save_data_with_id(id:str, path:str , data: dict):
    new_data = await  db.collection(f'User/{id}/{path}').add(data)
    return new_data

async def update_data(id:str, path:str , data: dict, uid:str):
    update_data = await  db.collection(f'User/{id}/{path}').document(uid).update(data)
    return update_data

async def get_data(id:str, path:str, uid:str) -> dict:
    data = await db.collection(f'User/{id}/{path}').document(uid).get()
    if (data.exists):
        dict_data = data.to_dict()
        dict_data["id"] = data.id
        return dict_data
    else:
        raise Exception("No existe el documento")

