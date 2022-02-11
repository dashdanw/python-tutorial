Presentation
https://docs.google.com/presentation/d/1SUq8zVAMNEeGbWLLztEPLZM8LzYnwBMW42jpQHuNAqE/edit?usp=sharing

***Some Setup Steps***

1. `poetry new --name agify --src python-tutorial`

2. `poetry add requests click`

3. `poetry add --dev pytest ipdb ipython`

4. `poetry install`

6. add function to agify.py

7. add
```
[tool.poetry.scripts] agify = "agify.agify:run"
```
to pyproject.toml

8. `poetry run agify`