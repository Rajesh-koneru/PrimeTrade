from pydantic import BaseModel

class Products_request(BaseModel):
    prod_Id:str
    prod_name:str
    prod_cost:int
    prod_disc:str
    prod_status:str
    prod_count:int

    class Config:
        from_attributes = True
class product_update_data(BaseModel):
    change_colum:str
    change_data:str