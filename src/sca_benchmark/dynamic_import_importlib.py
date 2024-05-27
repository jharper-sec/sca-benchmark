# Dynamic Import Using importlib (dynamic_import_importlib.py)
# This is a simple example of dynamically importing a module using importlib.import_module.
# This snippet imports the aiohttp.web module using importlib.import_module.

# Importing a module dynamically using importlib.import_module will cause type checkers to be unable to infer the type of the imported module.
# type: ignore

import importlib

web = importlib.import_module("aiohttp.web")


async def example(request: web.Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return web.Response(text=f"headers: {headers} body: {body}")


app = web.Application()
app.add_routes([web.post("/", example)])
web.run_app(app)
