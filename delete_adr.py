import psycopg2
conexion = psycopg2.connect(database="postgresDB",
                        host="localhost",
                        user="postgresUser",
                        password="postgresPW",
                        port="5455")
                        
cursor = con.cursor()

sql = 'DELETE FROM persona WHERE id=%s'

id = input('id to delete: ')


info = id

cursor.execute(sql,info)

con.commit()



cursor.close()
conexion.close()