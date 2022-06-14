# Flast API

## Add dependencies
```bash
pip install flask
pip install flask_restful
pip install flask_sqlalchemy
pip freeze --local > requirements.txt
```

## Add application and sqlite database
```bash
touch app.py
touch data.db
```

## Add crud books
```bash
touch models.py
touch views.py
```

## Run and Test server
```bash
python app.py
curl localhost:5000/books
```