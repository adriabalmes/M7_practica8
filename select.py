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

mycursor.execute('SELECT * FROM "Coches".vehiculo')

result = mycursor.fetchall()

for all in result:
    print(all)

#cerramos la conexion
mycursor.close()
conn.close()