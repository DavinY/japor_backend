# Japor API

Here is the repository from Cloud Computing side. We use Django REST framework to make an API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

Migrate the database after installing the requirements.

```bash
python manage.py migrate
```

## Usage

Change database configuration

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #Change to your database engine
        'HOST': '/cloudsql/japor-application:asia-southeast2:japor-database', #Change to your connection name
        'USER': 'root', #Change to your database user
        'PASSWORD': '', #Change to your database password
        'NAME': 'japor_app', #Change to your database name
    }
}

```

Run Cloud SQL Proxy so the API can be run on local with database on cloud.
```bash
cloud_sql_proxy.exe -instances=japor-application:asia-southeast2:japor-database=tcp:3306
#Change instances to your connection name
```

Run the API.

```bash
python manage.py runserver
```
