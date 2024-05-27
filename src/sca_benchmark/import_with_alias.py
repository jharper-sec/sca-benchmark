# Import with Alias (import_with_alias.py)
# This is a simple example of importing a module with an alias.
# This snippet imports the aiohttp.web module with an alias.

import aiohttp.web as web


async def example(request: web.Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return web.Response(text=f"headers: {headers} body: {body}")


app = web.Application()
app.add_routes([web.post("/", example)])
web.run_app(app)  # type: ignore
