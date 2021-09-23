import psycopg2
import psycopg2.extras

class DataBase(object):
  def __init__(self, host, port, user, password, database):
    self.host = host
    self.port = port
    self.user = user
    self.password = password
    self.database = database

  # connect db
  def create_connection(self):
    # connect db
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

  def fetchone(self, sql):
    try:
      with self.create_connection() as connection:
        with connection.cursor() as cursor:
          cursor.execute(sql)
          return cursor.fetchone()
    except Exception as e:
      print(e.args)
      raise

  def fetchall(self, sql):
    try:
      with self.create_connection() as connection:
        with connection.cursor() as cursor:
          cursor.execute(sql)
          return cursor.fetchall()
    except Exception as e:
      print(e.args)
      raise

  def commit(self, sql):
    try:
      with self.create_connection() as connection:
        with connection.cursor() as cursor:
          cursor.execute(sql)
        connection.commit()
    except Exception as e:
      print(e.args)
      raise