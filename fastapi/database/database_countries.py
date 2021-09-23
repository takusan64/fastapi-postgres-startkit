from database.database import DataBase

class DataBase_Countries(object):
  def __init__(self, host, port, user, password, database):
    self.db = DataBase(
      host=host,
      port=port,
      user=user,
      password=password,
      database=database
    )

  def get_country(self, country_id):
    sql = f"SELECT * FROM countries WHERE country_id={country_id};"
    try:
      result = self.db.fetchall(sql)
      return result
    except Exception:
      print("Can't connected DB")
      raise