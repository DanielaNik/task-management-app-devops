import os

DB_CONFIG = {
    'dbname' : os.environ.get('POSTGRES_DB'),
    'user' : os.environ.get('POSTGRES_USER'),
    'password' : os.environ.get('POSTGRES_PASSWORD'),
    'host' : os.environ.get('POSTGRES_HOST'),
    'port' : os.environ.get('POSTGRES_PORT')
}

if DB_CONFIG['dbname'] is None:
    raise RuntimeError("Environment variable POSTGRES_DB is missing")

if DB_CONFIG['user'] is None:
    raise RuntimeError("Environment variable POSTGRES_USER is missing")

if DB_CONFIG['password'] is None:
    raise RuntimeError("Environment variable POSTGRES_PASSWORD is missing")
