from fastapi import APIRouter
from .temperature import temperature_router
from .lights import lights_router
from .devices import devices_router

root = APIRouter()

@root.get("/", tags=["root"])
async def read_root():
    return {"message": "Hello World v1"}

root.include_router(temperature_router)
root.include_router(lights_router)
root.include_router(devices_router)
