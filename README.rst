***Steps***

1. `poetry new --name agify --src python-tutorial`

2. `poetry add requests click`

3. `poetry add --dev pytest ipdb ipython`

4. `poetry install`

5. `touch src/agify/agify.py`

6. add function to agify.py

7. add


```ini
[tool.poetry.scripts]
agify = "agify.agify:run"
```
to pyproject.toml

8. `poetry run agify`