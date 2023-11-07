import firebase_admin
from firebase_admin import credentials,firestore_async

cred_firebase = credentials.Certificate("./domain/static/credentials_firebase.json")
fire = firebase_admin.initialize_app(cred_firebase)
db =  firestore_async.client()

async def save_data(id:str, path:str , data: dict, uid:str):
    new_data = await  db.collection(f'User/{id}/{path}').document(uid).set(data)
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

