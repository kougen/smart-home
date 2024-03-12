from lib import start_multiple_versions
import sys
import uvicorn
from routers.v1.base import root as root_router_v1

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


if __name__ == "__main__":
    start_multiple_versions()
