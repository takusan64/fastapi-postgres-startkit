import config
from database.database_countries import DataBase_Countries

db_countries = DataBase_Countries(
  host = config.DB_HOST,
  port = config.DB_PORT,
  user = config.DB_USER,
  password = config.DB_PASSWORD,
  database = config.DATABASE
)

def get_country(country_id):
  try:
    country_data = sum(db_countries.get_country(country_id), [])
    if country_data:
      res={
        "country_id":country_data[0],
        "country_code":country_data[1],
        "name_label":country_data[2]
      }
      return res
    else:
      print("Can't get data.")
      raise Exception
  except Exception:
    raise