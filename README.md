# Packaging a DRF application in Docker
The application is packaged in 3 containers:
 - DB: PostgreSQL Database
 - Web: Django RF application, Gunicorn
 - Nginx: Web server and static files
 Includes two volumes:
 - Static
 - Media

### Files structure

infra_sp2
├── api_yamdb/
│    ├── api/ <-- API App dir
│    ├── api_yamdb/
│    │   ├── __init__.py
│    │   ├── settings.py
│    │   ├── urls.py
│    │   └── wsgi.py
│    ├── reviews/ <-- Reviews app dir
│    ├── static <-- Project static files
│    │   └── redoc.yaml
│    ├── templates
│    │   └── redoc.html
|    ├── Dockerfile 
│    ├── manage.py
|    └── requirements.txt 
├── infra/ <-- Directory with infrastructure deployment files
│    ├── nginx/ 
│    │   └── default.conf
│    ├── .env
|    └── docker-compose.yaml
├── tests/ 
├── .gitignore
├── pytest.ini
├── README.md
└── setup.cfg


### Dependencies

```
requests==2.26.0
django==2.2.16
djangorestframework==3.12.4
djangorestframework-simplejwt==5.1.0
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
django-filter==21.1
gunicorn==20.0.4
psycopg2-binary==2.9.2
```

## Launch the project:

Clone the repository and go to it:

```
git clone https://github.com/web2cap/infra_sp2.git
```

```
cd infra_sp2/infra
```

#### Preparing the .env file

Create an environment variable file in infra_sp2/infra
```
touch .ent
```
Populate the .env file using the template:

```
ST_SECRET_KEY = "" # Django SECRET_KEY
DB_ENGINE=django.db.backends.postgresql_psycopg2 # DB Adapter
DB_NAME= # Database name
POSTGRES_USER= # DB Login
POSTGRES_PASSWORD= # DB Password
DB_HOST=db # Container name
DB_PORT=5432 # DB Port
```


Run Docker-compose

```
docker-compose up -d --build 
```

Make migrations and collect static files:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input 
```

You can create Django super-user:

```
docker-compose exec web python manage.py createsuperuser
```

And you can upload test data to database:

```
docker-compose exec web python manage.py loaddata
```
### This DRF Project Page

https://github.com/web2cap/api_yamdb

### API Documentation

http://127.0.0.1/redoc/

### Avtor:

* Koshelev Pavel