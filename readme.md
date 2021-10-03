# Extensions Yang Biasa Dipakai
1. Untuk membuat REST API + Open API Documentation secara otomatis dengan Flask : https://flask-restx.readthedocs.io/en/latest/
2. Untuk agar dapat menggunakan ORM : https://flask-sqlalchemy.palletsprojects.com/en/2.x/
3. Untuk proses migrasi ORM : https://flask-migrate.readthedocs.io/en/latest/

# Steps
1. Create virtual environment
```
$ python3 -m venv venv
$ source venv/bin/activated
```

2. Install Flask
```
$ pip install flask
```

3. Create simple application
```
from flask import Flask

api = Flask(__name__)

@api.get('/')
def index():
    return {"hello": "world!"}

if __name__ == "__main__":
    api.run(host="127.0.0.1", port=5000)
```

4. Running application
```
$ python app.py
```

5. Running application using Flask Command
```
$ export FLASK_APP=app.py
$ flask run
```

6. Running application using debuging mode
```
$ export FLASK_ENV=development
$ flask run
```

# Notes
Baca dokumentasi!