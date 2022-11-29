import psycopg2
# Base de datos
conn = psycopg2.connect(database="postgres",
                        # Ip Servidor
                        host="localhost",
                        # Usuario
                        user="postgresUser",
                        # Contraseña
                        password="postgresPW",
                        # Puerto
                        port="5455")

mycursor = conn.cursor()

sql = "UPDATE Coches.vehiculo SET marca = %s WHERE address = %s"
val = ("audi", "renault")

mycursor.executemany(sql, val)

conn.commit()

print(mycursor.rowcount, "registro actualizado")