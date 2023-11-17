from firebase_admin.auth import verify_id_token

def validate_id_token(id_token:str) -> str:
    decoded_token = verify_id_token(id_token)
    uid = decoded_token['uid']
    return uid