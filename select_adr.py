import psycopg2
conexion = psycopg2.connect(database="postgres",
                        # Ip Servidor
                        host="localhost",
                        # Usuario
                        user="postgresUser",
                        # Contraseña
                        password="postgresPW",
                        # Puerto
                        port="5455")

cursor = conexion.cursor()

sql = "SELECT * FROM "Coches".vehiculo "


RESULTADO = cursor.fetchall()
for X in RESULTADO:
    print(X)

cursor.close()
conexion.close()
