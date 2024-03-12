from fastapi import APIRouter


devices_router = APIRouter(
    tags=["custom devices"],
    prefix="/devices",
)

@devices_router.get("/")
async def read_devices():
    return {"message": "Custom Devices v1"}
