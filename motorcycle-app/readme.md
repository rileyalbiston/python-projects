# Flask Motorcycle Web App 

## App Environment

* Flask
* PostgreSQL
* Virtualenvironment

**Flask Modules:**

* flask-sqlalchemy
* psycop2

## Inital Setup

> mkdir motorcycle-app

> cd motorcycle-app

> echo # Flask Motorcycle Web App > readme.md

motorcycle-app> virtualenv venv

motorcycle-app> venv\scripts\activate

motorcycle-app>pip install Flask

motorcycle-app> pip freeze > requirements.txt

motorcycle-app>echo main program file content > main.py

Add the following to the hello.py file:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

## Run the Development Server

motorcycle-app> python main.py

## Flask Modules

motorcycle-app> pip install flask-sqlalchemy psycopg2

motorcycle-app> pip freeze > requirements.txt