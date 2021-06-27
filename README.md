# flask_db

## overview
- alembic
- flask-sqlalchemy
- flask-marshmallow

## how to
- Install
```
pipenv install
pipenv shell
```

- Create db
```
alembic upgrade head
```

- Add row
```
flask job hello
```

- Set up a server
```
python app.py
```

- Access
```
http://127.0.0.1:5000/api/users
```

## update models
```
alembic revision --autogenerate -m 'update'
alembic upgrade head
```
