import psycopg2
import psycopg2.extras

class DataBase(object):
  def __init__(self, host, port, user, password, database):
    self.host = host
    self.port = port
    self.user = user
    self.password = password
    self.database = database

  # create connect db
  def create_connection(self):
    connection = psycopg2.connect(
      host=self.host,
      port=self.port,
      user=self.user,
      password=self.password,
      database=self.database
    )
    connection.set_client_encoding('utf-8')
    connection.cursor_factory=psycopg2.extras.DictCursor
    return connection

  # print postgres version
  def connect_check(self):
    try:
      with self.create_connection() as connection:
        with connection.cursor() as cursor:
          sql="SELECT version();"
          cursor.execute(sql)
          result = cursor.fetchall()
          print(result)
          print("Connected DB")
    except Exception as e:
      print("Can't connected DB")
      print(e.args)
      raise

  # get country data
  def get_country(self, country_id):
    try:
      with self.create_connection() as connection:
        with connection.cursor() as cursor:
          sql = f"SELECT * FROM countries WHERE country_id={country_id};"
          cursor.execute(sql)
          return cursor.fetchall()
    except Exception as e:
      print(e.args)
      raise