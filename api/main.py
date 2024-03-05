import uvicorn
from fastapi import FastAPI
from lib import get_versions
import sys
import routers.root_router_v1 as root_router_v1

description = """

API for the smart home system.

## API

- `/api/` - API root

### Description

This API is used to control the smart home system. It can be used to control the lights, the temperature, and other custom devices.

"""

tags_metadata = [
    {
        "name": "Root",
        "description": "The root of the API",
    },
]


app = FastAPI(
    title="Smart Home API",
    description=description,
    version="0.1.0",
    openapi_tags=tags_metadata,
    servers=get_versions(),
)

app.include_router(root_router_v1.root, prefix="/api")
app.include_router(root_router_v1.root, prefix="/api/v1")
app.include_router(root_router_v1.root, prefix="/api/latest")


if __name__ == "__main__":
    port = 80
    if sys.argv[1] == "port":
        port = int(sys.argv[2])
    uvicorn.run(app, host="0.0.0.0", port=port)
