[![Build Status](http://kseniaglivko.teamcity.com/app/rest/builds/buildType:(id:PythonApiTests_Build)/statusIcon)](https://kseniaglivko.teamcity.com/viewType.html?buildTypeId=PythonApiTests_Build&guest=1)
# Python api tests

Api tests in Python

The project uses:
1. Python
2. Requests
3. Allure for reports
4. CI (GitHub actions)


Testing application (write with Flask):

git: https://github.com/berpress/flask-restful-api

url: https://stores-tests-api.herokuapp.com

Swagger: https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0


### How to start

Use python 3.9 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

or install poetry https://python-poetry.org/, then

```
poetry install
```

and add pre-commit
```
pre-commit install
```

### Run all tests

```
pytest
```
