from fastapi import APIRouter


tags_metadata = [
    {
        "name": "Root",
        "description": "The root of the API",
    },
    {
        "name": "Lights",
        "description": "Control the lights in the smart home",
    },
    {
        "name": "Temperature",
        "description": "Control the temperature in the smart home",
    },
    {
        "name": "Custom Devices",
        "description": "Control custom devices in the smart home",
    }
]

root = APIRouter(
    tags=["Root"],
)

lights_router = APIRouter(
    tags=["Lights"],
    prefix="/lights",
)

temperature_router = APIRouter(
    tags=["Temperature"],
    prefix="/temperature",
)

devices_router = APIRouter(
    tags=["Custom Devices"],
    prefix="/devices",
)


root.include_router(lights_router)
root.include_router(temperature_router)
root.include_router(devices_router)

@root.get("/")
async def read_root():
    return {"message": "Hello World v1"}


@lights_router.get("/")
async def read_lights():
    return {"message": "Lights v1"}


@temperature_router.get("/")
async def read_temperature():
    return {"message": "Temperature v1"}

@devices_router.get("/")
async def read_devices():
    return {"message": "Custom Devices v1"}




