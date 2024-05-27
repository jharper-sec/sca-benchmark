# Using Built-in Functions (built_in_functions.py)
# This is a simple example of using built-in functions to import modules.
# This snippet imports the aiohttp and aiohttp.web modules using built-in functions.

# Importing modules using built-in functions will cause type checkers to be unable to infer the type of the imported module.
# type: ignore

globals()["aiohttp"] = __import__("aiohttp")
globals()["aiohttp.web"] = __import__("aiohttp.web")


async def example(request: aiohttp.web.Request):
    headers = dict(request.headers)
    body = await request.content.read()
    print(f"headers: {headers} body: {body}")
    return aiohttp.web.Response(text=f"headers: {headers} body: {body}")


app = aiohttp.web.Application()
app.add_routes([aiohttp.web.post("/", example)])
aiohttp.web.run_app(app)
