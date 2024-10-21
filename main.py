import psycopg

def main():
     conn = psycopg.connect('postgres://avnadmin:AVNS_sC4ctxQYGG36oJKqBG2@pg-22dfbb48-ihediohachidozie-43e4.g.aivencloud.com:17394/defaultdb?sslmode=require')

     query_sql = 'SELECT VERSION()'

     cur = conn.cursor()
     cur.execute(query_sql)

     version = cur.fetchone()[0]
     print(version)


if __name__ == "__main__":
  main()

# import pymysql

# timeout = 10
# connection = pymysql.connect(
#   charset="utf8mb4",
#   connect_timeout=timeout,
#   cursorclass=pymysql.cursors.DictCursor,
#   db="defaultdb",
#   host="mysql-278e137c-ihediohachidozie-43e4.g.aivencloud.com",
#   password="AVNS_inDXGPRK7q1hHmYLHr_",
#   read_timeout=timeout,
#   port=17394,
#   user="avnadmin",
#   write_timeout=timeout,
# )
  
# try:
#   cursor = connection.cursor()
#   cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
#   cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
#   cursor.execute("SELECT * FROM mytest")
#   print(cursor.fetchall())
# finally:
#   connection.close()