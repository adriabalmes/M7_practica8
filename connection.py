# conn = psycopg2.connect("dbname=postgres user=postgresUser password=postgresPW")

import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgresUser",
                        password="postgresPW",
                        port="5455")