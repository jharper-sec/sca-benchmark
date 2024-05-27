# Import All Functions and Classes (import_all.py)
# This is a simple example of importing all functions and classes from a module.
# This snippet imports all functions and classes from the aiohttp.web module.

from aiohttp.web import *  # type: ignore


async def example(request: Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return Response(text=f"headers: {headers} body: {body}")


app = Application()
app.add_routes([post("/", example)])
run_app(app)
