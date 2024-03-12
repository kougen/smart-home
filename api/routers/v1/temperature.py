from fastapi import APIRouter


temperature_router = APIRouter(
    tags=["temperature"],
    prefix="/temperature",
)

@temperature_router.get("/")
async def read_temperature():
    return {"message": "Temperature v1"}
