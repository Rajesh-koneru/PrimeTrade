from http.client import HTTPException

from fastapi import FastAPI,APIRouter,HTTPException
from fastapi.params import Depends
from utils.role_config import require_role
from models.users import User
from models.products import products

from database import SessionLocal
from sqlalchemy.orm import Session
from schemas.Users_schema import ProductResponse

userRouter=APIRouter()
db:Session=SessionLocal()

api1="/api/v1"
#api2="/api/v2"

@userRouter.get("/profile")
def get_profile(current_user=Depends(require_role(["user","admin"]))):
    user_data=db.query(User).filter(User.email==current_user["id"]).first()
    if user_data is  None:
        print("user details are found..")
        raise HTTPException(status_code=404,detail="Profile is not found")
    # extracting user information
    user_obj={"name":user_data.username,"email":user_data.email,"created_on":user_data.create_data}
    print(user_obj)
    return {"msg":"welcome user","data":user_obj}



# getting all the products from the db
@userRouter.get("/api/v1/products/all",response_model=list[ProductResponse])
def get_allProducts(user=Depends(require_role(["admin","user"]))):
    product_data=db.query(products).all()
    return product_data


# getting single product by id

@userRouter.get("/api/v1/products/{id}",response_model=ProductResponse)
def product_ById(id:int,user=Depends(require_role(["admin","user"]))):

    product=db.query(products).filter(products.Id==id).first()

    if not product:
        print("product is not available")
        raise HTTPException(status_code=404,detail="Product is not found")
    return product

#searching product by its name
@userRouter.get("/api/v1/product",response_model=list[ProductResponse])
def product_ByName(name:str,user=Depends(require_role(["admin","user"]))):
    print(name)
    products_all = db.query(products).filter(
        products.prod_name.ilike(f"%{name}%")
    ).all()

    print("all the products with name match...",[x.prod_name for x in products_all])
    return products_all




