from alembic.util import status
from fastapi import FastAPI,APIRouter,HTTPException
from fastapi.params import Depends
from utils.role_config import require_role
from schemas.Admin_Schema import Products_request,product_update_data
from sqlalchemy.orm import Session

from database import SessionLocal
from models.products import products

AdminRouter=APIRouter()
db:Session=SessionLocal()

@AdminRouter.get("/admin/profile")
def get_profile(current_user=Depends(require_role(["admin"]))):

    return {"msg":"welcome admin","data":current_user}


@AdminRouter.post("/api/v1/admin/product/add")
def Product_add(product:Products_request,user=Depends(require_role(["admin"]))):
    try:
        print("the product name",product.prod_name)
        if product is None:
            print("product details are not received.")
            raise HTTPException(status_code=400,detail="product details are not received..")
        new_prod=products(prod_Id=product.prod_Id,prod_name=product.prod_name,prod_cost=product.prod_cost
                          ,prod_disc=product.prod_disc,prod_count=product.prod_count,prod_status=product.prod_status)

        # adding data into db
        db.add(new_prod)
        return {"msg":"product added successfully..."}
    except Exception as e:
        print(str(e))
        return {"error":str(e)}
    finally:
        db.commit()
        db.close()


#updating product
@AdminRouter.post("/api/v1/admin/product/update")
def product_update(data:Products_request,user=Depends(require_role(["admin"]))):
    try:
        print(data.prod_name)
        if not data:
            print("data is not received")
            raise HTTPException(status_code=404,detail="update data is not received...")
        update_data = data.dict(exclude_unset=True)
        db.query(products).filter(products.prod_Id==data.prod_Id).update(update_data)
        db.commit()
        return {"msg":"data updated"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=400,detail="data is not updated..")
    finally:
        db.close()

# deleting the product by id
@AdminRouter.delete("/api/v1/product/delete")
def Delete_product(prod_id:str,user=Depends(require_role(["admin"]))):
    try:
        prod=db.query(products).filter(products.prod_Id==prod_id).first()
        if not prod:
            print("user is not found")
            raise HTTPException(status_code=404,detail="data not found")

        # deleting the user
        db.delete(prod)
        db.commit()
        return {"msg":"product deleted..."}
    except Exception as e:
        print(str(e))
        return{"error":str(e)}
    finally:
        db.close()










