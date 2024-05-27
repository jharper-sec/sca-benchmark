# Basic Import (basic_import.py)
# This is a simple example of importing a module.
# This snippet imports the aiohttp.web module.

from aiohttp import web


async def example(request: web.Request):
    headers = dict(request.headers)
    body = await request.content.read()
    print(f"headers: {headers} body: {body}")
    return web.Response(text=f"headers: {headers} body: {body}")


app = web.Application()
app.add_routes([web.post("/", example)])
web.run_app(app)  # type: ignore
