from fastapi import APIRouter
from google.cloud import datastore
from pydantic import BaseModel


class User(BaseModel):
    name: str


router = APIRouter()


@router.get("/hello")
async def hello():
    return {"message": "hello, world."}


@router.post("/user")
async def create_user(user: User):
    client = datastore.Client()
    key = client.key("User")
    entity = datastore.Entity(key)
    entity.update({"name": user.name})
    client.put(entity)

    return 200
