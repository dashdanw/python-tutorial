***Steps***

1. `poetry new --name agify --src python-tutorial`

1. `poetry add requests click`

1. `poetry add --dev pytest ipdb ipython`

1. `poetry install`

1. `touch src/agify/agify.py`

1. add function to agify.py

1. add


```ini
[tool.poetry.scripts]
agify = "agify.agify:run"
```
to pyproject.toml

1. `poetry run agify`