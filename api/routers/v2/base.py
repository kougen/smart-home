from fastapi import APIRouter


root = APIRouter()

@root.get("/", tags=["root"])
async def read_root():
    return {"message": "Hello World v2"}
