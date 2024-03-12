from fastapi import FastAPI
import uvicorn
from routers.v1.base import root as root_router_v1
from routers.v2.base import root as root_router_v2
import threading

tags_metadata = [
    {
        "name": "root",
        "description": "The root of the API",
    },
    {
        "name": "lights",
        "description": "Control the lights in the smart home",
    },
    {
        "name": "temperature",
        "description": "Control the temperature in the smart home",
    },
    {
        "name": "custom devices",
        "description": "Control custom devices in the smart home",
    }
]


def get_versions():
    return [
        {"url": "/", "version": "v1", "tags": tags_metadata, "description": "The first version of the API", "port": 8000},
        {"url": "/", "version": "v2", "tags": tags_metadata, "description": "The second version of the API", "port": 8001},
    ]


def get_root_router(version: str):
    if version == "v1":
        return root_router_v1
    elif version == "v2":
        return root_router_v2
    else:
        return root_router_v1

def start_version(version: dict):
    description = version["description"]
    siblig_servers = []
    for v in get_versions():
        siblig_servers.append({"url": f"http://localhost:{v['port']}", "description": v["description"]})
    port = version["port"]
    app = FastAPI(
        title="Smart Home API",
        description=description,
        version=version["version"],
        openapi_tags=version["tags"],
        servers=siblig_servers
    )
    app.include_router(get_root_router(version["version"]))
    uvicorn.run(app, host="0.0.0.0", port=port)

def start_multiple_versions():
    versions = get_versions()
    threads = []
    for version in versions:
        t = threading.Thread(target=start_version, args=(version,))
        threads.append(t)
        t.start()
