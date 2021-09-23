from database.database import DataBase

class DataBase_Util(object):
  def __init__(self, host, port, user, password, database):
    self.db = DataBase(
      host=host,
      port=port,
      user=user,
      password=password,
      database=database
    )

  def connect_check(self):
    sql="SELECT version();"
    try:
      result = self.db.fetchall(sql)
      print(result)
      print("Connected DB")
    except Exception:
      print("Can't connected DB")
      raise