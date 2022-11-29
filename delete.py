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

sql = "DELETE FROM Coches.vehiculo WHERE marca = %s"
adr = ("audi", )


mycursor.execute(sql, adr)

conn.commit()

print(mycursor.rowcount, "registro deleted")