# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI

from routers import auth,Users,Admin
from database import engine,Base
from models.users import User

app=FastAPI()
Base.metadata.create_all(bind=engine)
print("database connected...")
app.include_router(auth.authRouter)
app.include_router(Users.userRouter)
app.include_router(Admin.AdminRouter)


