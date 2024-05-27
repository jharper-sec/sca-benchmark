# Import Specific Functions or Classes (import_specific.py)
# This is a simple example of importing specific functions or classes from a module.
# This snippet imports the Application, Request, Response, post, and run_app functions from the aiohttp.web module.

from aiohttp.web import Application, Request, Response, post, run_app  # type: ignore


async def example(request: Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return Response(text=f"headers: {headers} body: {body}")


app = Application()
app.add_routes([post("/", example)])
run_app(app)
