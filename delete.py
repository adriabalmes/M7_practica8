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