from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid token"
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("usermail")
        role = payload.get("role")
        print(role)

        if user_id is None:
            print("user value is none")
            raise HTTPException(status_code=405,detail="user is invalid")

    except JWTError:
        print("JWT token error")
        raise HTTPException(status_code=400,detail="token error")

    # fetch user from DB
    user = {
        "id": user_id,
        "role": role
    }

    return user