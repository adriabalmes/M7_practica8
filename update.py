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

#Creamos la sentencia sql

#cambiamos la marca
sql = 'UPDATE "Coches".vehiculo SET marca = %s WHERE id = %s'

#le pedimos los datos del vehiculo
marca =input('introduce la nueva marca: ')

id =input(('introduce la id del coche a actualizar: '))
#recogemos los datos en una variable

datos = (marca, id)

mycursor.execute(sql,datos)

#guardamos el registro
conn.commit()

#esto (rowcount) lo que hace es contar los registros, es decir las filas
registrosactualizados = mycursor.rowcount

#mostramos un mensaje
print(f'registro actualizado: {registrosactualizados}')

#cerramos la conexion
mycursor.close()
conn.close()