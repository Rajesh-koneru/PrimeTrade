from types import new_class

from fastapi import  APIRouter,HTTPException
from models.users import User
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.Users_schema import UserSignup,UserLogin
from starlette.templating import pass_context
from utils.authenticate import authenticate


from utils.password_hasing import hash_password,verify_password
from utils.JWT_auth import create_access_token


authRouter=APIRouter()
db: Session = SessionLocal()

@authRouter.post("/login")
def login(user:UserLogin):
   try:
       print(user.Email)
       auth=authenticate(user.password,user.Email)
       print("role",auth.get("role"))

       if auth:
           print("user loged in")
           # JWT token generation

           data={"usermail":user.Email,"role":auth.get("role")}
           token=create_access_token(data)

           if not token:
               raise HTTPException(status_code=500,detail="Token generation error")
           return {"msg":"user loged in successful","token":token,"tokentype":"bearer"}

       return {"msg":"user login failed"}


   except Exception as e:
       print(str(e))
       raise HTTPException(status_code=500,detail="Error occured")

@authRouter.post("/signin")
def signin(user:UserSignup):

    try:
        print(user.Email,user.username)
        exist_user = db.query(User).filter(User.email == user.Email).first()

        if  exist_user:
            print("user already exist")
            print(exist_user.username)

            raise HTTPException(status_code=401,detail="User already exist")

        if not user:
            print("User data is not received...")
            raise HTTPException(status_code=400, detail="User data not valid")


        hashPassword=hash_password(user.password)
        print("hash password is:",hashPassword)

        if not hashPassword:
            print("error in password hasing")
            raise HTTPException(status_code=401,detail="Error in password hashing")

        new_user=User(username=user.username,email=user.Email,password=hashPassword,role="user")
        db.add(new_user)
        return {"msg": "signin succesfull..."}

    except Exception as e:
        print("database error",str(e))
        raise HTTPException(status_code=400,detail=str(e))
    finally:
        db.commit()

