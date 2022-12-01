#UPDATE nombre_tabla SET columna1 = 'nuevo_valor' WHERE columna1 = 'valor1'; 
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

#METODO INSERT#####################################################################################################################
#Creamos la sentencia sql

#cambiamos el nombre
sql = 'UPDATE persona SET nombre = %s WHERE id = %s'

#le pedimos los datos al usuario
nombre =input('introduce el nuevo nombre: ')

id =input(('introduce la id de la persona a actualizar: '))
#recogemos los datos en una variable

datos = (nombre, id)

cursor.execute(sql,datos)

#guardamos el registro
con.commit()

#esto (rowcount) lo que hace es contar los registros, es decir las filas
registrosactualizados = cursor.rowcount

#mostramos un mensaje
print(f'registro insertado: {registrosactualizados}')

#cerramos la conexion
cursor.close()
con.close()

