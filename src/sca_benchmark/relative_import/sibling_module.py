# Relative Import (relative_import/parent_module.py and relative_import/sibling_module.py)
# This is a simple example of a relative import.
# This snippet imports the parent_module module from the sibling_module module.

# relative_import/sibling_module.py
from .parent_module import parent_function
from aiohttp.web import Application, post, run_app  # type: ignore

app = Application()
app.add_routes([post("/", parent_function)])
run_app(app)
