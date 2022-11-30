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

# Sentencia sql INSERT
sql = "INSERT INTO Coches.vehiculo (id, marca, modelo, combustible, color, transmision, puertas, plazas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
val = [
    # id   marca  modelo combustible color  transmission  puertas plazas
    (1, 'audi', 'a4' , 'diesel', 'rojo', 'automatica', '5', '5')
]

mycursor.executemany(sql, val)

conn.commit()

print(mycursor.rowcount, "registro deleted")

#Cerrando la conexion
conn.close()