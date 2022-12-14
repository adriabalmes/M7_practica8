#modificaciones de adrbranch
# conn = psycopg2.connect("dbname=postgres user=postgresUser password=postgresPW")
# Crear conexion
import psycopg2
                        # Base de datos
con = psycopg2.connect(database="postgresDB",
                        # Ip Servidor
                        host="localhost",
                        # Usuario
                        user="postgresUser",
                        # Contraseña
                        password="postgresPW",
                        # Puerto
                        port="5455")
                        
#Crear cursor
cursor = con.cursor()

#Creamos la sentencia sql
# sql = 'INSERT INTO VEHICULO (marca, modelo, combustible, color, transmision, puertas, plazas) VALUES(%s,%s,%s,%s,%s,%s,%s))'

# Sentencia sql DELETE
sql = 'DELETE FROM "Coches".vehiculo WHERE id=%s'


#le pedimos los datos al usuario
id = input('introduce la id a borrar: ')

#recogemos los datos en una variable
datos = id

mycursor.execute(sql,datos)

#guardamos el registro
conn.commit()

#esto (rowcount) lo que hace es contar los registros, es decir las filas
registrosEliminados = mycursor.rowcount

#mostramos un mensaje
print(f'registro eliminado: {registrosEliminados}')

#cerramos la conexion
mycursor.close()
conn.close()