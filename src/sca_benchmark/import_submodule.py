# Import Submodule (import_submodule.py)
# This is a simple example of importing a submodule from a package.
# This snippet imports the aiohttp.web module from the aiohttp package.


import aiohttp.web


async def example(request: aiohttp.web.Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return aiohttp.web.Response(text=f"headers: {headers} body: {body}")


app = aiohttp.web.Application()
app.add_routes([aiohttp.web.post("/", example)])
aiohttp.web.run_app(app)  # type: ignore
