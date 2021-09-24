import config
from database.database import DataBase

db = DataBase(
  host = config.DB_HOST,
  port = config.DB_PORT,
  user = config.DB_USER,
  password = config.DB_PASSWORD,
  database = config.DATABASE
)

def get_country(country_id):
  try:
    country_data = sum(db.get_country(country_id), [])
    if country_data:
      res={
        "country_id":country_data[0],
        "country_code":country_data[1],
        "name_label":country_data[2]
      }
      return res
    else:
      print("No matching data found.")
      raise Exception
  except Exception:
    raise