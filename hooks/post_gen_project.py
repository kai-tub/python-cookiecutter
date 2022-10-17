from pathlib import Path
from packaging.version import Version, parse

pyproject_path = Path("pyproject.toml")
assert pyproject_path.exists()

test_path = Path(".github/workflows/test.yml")
assert test_path.exists()

min_python = parse("{{cookiecutter.min_supported_python}}")
max_python = parse("{{cookiecutter.max_supported_python}}")

if max_python < min_python:
    raise ValueError(
        "Maximum Python version cannot be smaller than minimum Python version!"
    )

if min_python.major != max_python.major:
    raise ValueError("Do not support different major versions as of now!")

if min_python == max_python:
    python_version = f"{min_python.major}.{min_python.minor}"
    pyproject_python_str = python_version
    test_matrix_str = python_version
else:
    # pyproject_python_str = f">={min_python.major}.{min_python.minor}, <{max_python.major}.{max_python.minor + 1}"
    # Disable the upper bound for Python version, as it has caused more issues
    pyproject_python_str = f">={min_python.major}.{min_python.minor}"
    # assume max_minor > min_minor
    test_matrix_str = ",".join(
        f'"{min_python.major}.{m}"'
        for m in range(min_python.minor, max_python.minor + 1)
    )

pyproject_data = pyproject_path.read_text()
pyproject_data = pyproject_data.replace(r"{PYTHON_VERSIONS_HOOK}", pyproject_python_str)
pyproject_path.write_text(pyproject_data)

test_data = test_path.read_text()
test_data = test_data.replace(r"{PYTHON_MATRIX_HOOK}", test_matrix_str)
test_path.write_text(test_data)
