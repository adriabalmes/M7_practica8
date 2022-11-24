# conn = psycopg2.connect("dbname=postgres user=postgresUser password=postgresPW")
# Crear conexion
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

#Crear cursor
cursor = conn.cursor()

#Ejecutar  MYSQL function utilizando execute()
cursor.execute("select version()")
data = cursor.fetchone()
print("Connection established to: ",data)

#Cerrando la conexion
conn.close()
Connection established : (2022)