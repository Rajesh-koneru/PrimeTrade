from pydantic import BaseModel,EmailStr

class UserSignup(BaseModel):
    username :str
    Email:EmailStr
    password:str


class UserLogin(BaseModel):
    Email:EmailStr
    password:str



class ProductResponse(BaseModel):
    prod_Id :str
    prod_name:str
    prod_cost:int
    prod_disc:str
    prod_count:int
    prod_status:str

    class Config:
        from_attributes = True