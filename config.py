import os

DB_CONFIG = {
    'dbname' : os.environ.get('DB_NAME'),
    'user' : os.environ.get('DB_USER'),
    'password' : os.environ.get('DB_PASSWORD'),
    'host' : os.environ.get('DB_HOST'),
    'port' : os.environ.get('DB_PORT')
}

if DB_CONFIG['dbname'] is None:
    raise RuntimeError("Environment variable DB_NAME is missing")

if DB_CONFIG['user'] is None:
    raise RuntimeError("Environment variable DB_USER is missing")

if DB_CONFIG['password'] is None:
    raise RuntimeError("Environment variable DB_PASSWORD is missing")