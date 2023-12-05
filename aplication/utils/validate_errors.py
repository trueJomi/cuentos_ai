from domain.services.firebase_validate import validate_id_token
from fastapi import status, HTTPException 

def validate_errors(fun):
    def function_decorator(*args, **kwargs):
        try:
            validate_id_token(kwargs.id_token)
        except Exception as e :
            raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail=f"Unauthorized API"
        )
        try:
            return fun(*args, **kwargs)
        except Exception as e :
            raise HTTPException(
                status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"{e}"
            )
    return function_decorator