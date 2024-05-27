# Using imp Module (Deprecated) (dynamic_import_imp.py)
# This is a simple example of dynamically importing a module using the imp module.
# This snippet imports the aiohttp.web module using the imp module.

# The imp module is deprecated since Python 3.4. It is recommended to use importlib.import_module instead.
# type: ignore

import imp
import os


# Function to dynamically load a module
def load_module(module_name):
    fp, pathname, description = imp.find_module(module_name)
    try:
        module = imp.load_module(module_name, fp, pathname, description)
    finally:
        if fp:
            fp.close()
    return module


# Load the top-level aiohttp module
aiohttp = load_module("aiohttp")

# Find and load the aiohttp.web submodule
submodule_name = "web"
fp, pathname, description = imp.find_module(
    submodule_name, [os.path.dirname(aiohttp.__file__)]
)
aiohttp_web = imp.load_module(f"aiohttp.{submodule_name}", fp, pathname, description)

# Now you can use aiohttp.web components
Application = aiohttp_web.Application
Request = aiohttp_web.Request
Response = aiohttp_web.Response
run_app = aiohttp_web.run_app


async def example(request: Request):
    headers = dict(request.headers)
    body = await request.content.read()
    return Response(text=f"headers: {headers} body: {body}")


app = Application()
app.add_routes([aiohttp_web.post("/", example)])

if __name__ == "__main__":
    run_app(app)
