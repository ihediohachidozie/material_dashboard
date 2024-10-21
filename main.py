import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_sC4ctxQYGG36oJKqBG2@pg-22dfbb48-ihediohachidozie-43e4.g.aivencloud.com:17394/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()