# Modifying sys.path (sys_path_import.py)
# This is a simple example of modifying the sys.path to import a module.
# This snippet imports the aiohttp.web module by modifying the sys.path.

import sys
import os

# Add the local_libs directory to sys.path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "local_libs"))
)

# Now import aiohttp from the local_libs directory
from aiohttp import web


async def example(request: web.Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return web.Response(text=f"headers: {headers} body: {body}")


app = web.Application()
app.add_routes([web.post("/", example)])

if __name__ == "__main__":
    web.run_app(app)  # type: ignore
