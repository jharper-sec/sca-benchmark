# Relative Import (relative_import/parent_module.py and relative_import/sibling_module.py)
# This is a simple example of a relative import.
# This snippet defines a parent_function that reads the request headers and body and returns a response.

# relative_import/parent_module.py
from aiohttp.web import Response, Request


async def parent_function(request: Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return Response(text=f"headers: {headers} body: {body}")
