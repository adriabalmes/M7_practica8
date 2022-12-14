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
# sql = 'INSERT INTO VEHICULO (marca, modelo, combustible, color, transmision, puertas, plazas) VALUES(%s,%s,%s,%s,%s,%s,%s))'

sql = "INSERT INTO persona (id, nombre, apellido, edad) VALUES (%s, %s, %s, %s)"
# val = [
#     # id   marca  modelo combustible color  transmission  puertas plazas
#     (1, 'audi', 'a4' , 'diesel', 'rojo', 'automatica', '5', '5')
# ]

#le pedimos los datos al usuario
id = input('introduce la id: ')

nombre = input('introduce el nombre: ')

apellido = input('introduce el apellido: ')

edad = input('introduce la edad: ')

#recogemos los datos en una variable

datos = (id, nombre, apellido, edad)

cursor.execute(sql,datos)

#guardamos el registro
con.commit()

#esto (rowcount) lo que hace es contar los registros, es decir las filas
registros = cursor.rowcount

#mostramos un mensaje
print(f'registro insertado: {registros}')

#cerramos la conexion
cursor.close()
con.close()

#METODO delete#####################################################################################################################
