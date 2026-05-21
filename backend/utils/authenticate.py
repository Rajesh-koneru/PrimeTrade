from database import SessionLocal
from pygments.lexers.asm import HsailLexer
from sqlalchemy import false
from sqlalchemy.orm import Session
from models.users import User
from utils.password_hasing import verify_password
from fastapi import HTTPException

is_authenticate=False
def authenticate(password,usermail):
    db:Session=SessionLocal()
    try:
        if not password or not usermail:
            print("password or mail are not valid..")
            raise HTTPException(status_code=400,detail="password or mail are not valid")

        check_user=db.query(User).filter(User.email==usermail).first()
        if not check_user:
            print("User details are not found..")
            raise HTTPException(status_code=404,detail="user not found")

        pwd_check=verify_password(password,check_user.password)
        if pwd_check:
            #Jwt token code here
            print("user login successful")
            is_authenticat=True
            return {"role":check_user.role,"status":True}
        return False
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500,detail="internal error")
