from fastapi import APIRouter


lights_router = APIRouter(
    tags=["lights"],
    prefix="/lights",
)

@lights_router.get("/")
async def read_lights():
    return {"message": "Lights v1"}
