import firebase_admin
from firebase_admin import credentials,firestore_async

cred_firebase = credentials.Certificate("./domain/static/credentials_firebase.json")
fire = firebase_admin.initialize_app(cred_firebase)
db =  firestore_async.client()

async def save_data(id:str, path:str , data: dict):
    new_data = await  db.collection(f'User/{id}/{path}').add(data)
    return new_data