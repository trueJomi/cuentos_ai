import firebase_admin
from firebase_admin import credentials,firestore_async, storage

cred_firebase = credentials.Certificate("./domain/static/credentials_firebase.json")
fire = firebase_admin.initialize_app(cred_firebase)
db =  firestore_async.client()

store = storage.bucket( name="cuentos-ai.appspot.com", app=fire)

