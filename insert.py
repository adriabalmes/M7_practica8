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
sql = 'INSERT INTO "Coches".vehiculo (id, marca, modelo, combustible, color, transmision, puertas, plazas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
# val = [
#     # id   marca  modelo combustible color  transmission  puertas plazas
#     (1, 'audi', 'a4' , 'diesel', 'rojo', 'automatica', '5', '5')
# ]

#le pedimos los datos al usuario
id = input('introduce la id: ')

marca = input('introduce la marca: ')

modelo = input('introduce el modelo: ')

combustible = input('introduce el combustible: ')

color = input('introduce el color: ')

transmision = input('introduce la transmision: ')

puertas = input('introduce las puertas: ')

plazas = input('introduce las plazas: ')

#recogemos los datos en una variable

datos = (id, marca, modelo, combustible, color, transmision, puertas, plazas)

mycursor.execute(sql,datos)

#guardamos el registro
conn.commit()


print(mycursor.rowcount, "registro deleted")
=======
#esto (rowcount) lo que hace es contar los registros, es decir las filas
registros = mycursor.rowcount

#mostramos un mensaje
print(f'registro insertado: {registros}')

#cerramos la conexion
mycursor.close()
conn.close()

