# SCA Benchmark: Imports in Python

This project demonstrates various methods for statically and dynamically importing dependencies in Python. It includes examples of using normal import methods using the `import` keyword as well the `import`, `importlib`, and deprecated `imp` modules to load a vulnerable version of the `aiohttp.web` module. The purpose is to benchmark and evaluate the efficacy of software composition analysis (SCA) tools, specifically regarding the reachability of code within dependencies.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/sca_benchmark.git
   cd sca_benchmark
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install .
   ```
   