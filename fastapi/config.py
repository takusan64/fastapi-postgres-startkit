import os
from os.path import join, dirname
from dotenv import load_dotenv
from urllib.parse import urlparse

# loading .env file
env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)

# use function
def number_check(num=None):
  if isinstance(int(num), int):
    return int(num)
  return None

# Register Env Param
try:
  DB_HOST = os.environ.get('DB_HOST') or 'pgsql'
  DB_PORT = number_check(os.environ.get('DB_PORT')) or 5432
  DB_USER = os.environ.get('DB_USER') or 'postgres'
  DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'postgres'
  DATABASE = os.environ.get('DATABASE') or 'postgres'
except Exception:
  print("defined param error： check .env file")
  raise