# Dynamic Import Using exec (dynamic_import_exec.py)
# This is a simple example of dynamically importing a module using exec.
# This snippet imports the aiohttp.web module using exec.

# Importing a module dynamically using exec will cause type checkers to be unable to infer the type of the imported module.
# type: ignore

module_name = "aiohttp.web"
exec(f"import {module_name} as web")


async def example(request: web.Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return web.Response(text=f"headers: {headers} body: {body}")


app = web.Application()
app.add_routes([web.post("/", example)])
web.run_app(app)
