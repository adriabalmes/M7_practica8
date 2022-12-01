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

def execute_query(conn, query):

        mycursor.execute(query)
        conn.commit()
        print("Query successful")

create_table_vehiculos = """
CREATE TABLE IF NOT EXISTS "Coches".vehiculo
    (
        id integer NOT NULL DEFAULT nextval('"Coches".vehiculo'::regclass),
        marca text COLLATE pg_catalog."default" NOT NULL,
        modelo text COLLATE pg_catalog."default" NOT NULL,
        combustible text COLLATE pg_catalog."default" NOT NULL,
        color text COLLATE pg_catalog."default" NOT NULL,
        transmision text COLLATE pg_catalog."default" NOT NULL,
        puertas text COLLATE pg_catalog."default" NOT NULL,
        plazas text COLLATE pg_catalog."default" NOT NULL,
        CONSTRAINT id_pkey PRIMARY KEY (marca)
    )
"""

insert_table_vehiculos = """
INSERT INTO "Coches".vehiculo(
        id, marca, modelo, combustible, color, transmision, puertas, plazas)
        VALUES ( 1, 'audi', 'a4' , 'diesel', 'rojo', 'automatica', '5', '5'),
        (2, 'bmw', 'x4', 'gasolina', 'verde', 'automatica', '5', '5'),
        (3, 'citroen', 'c5', 'gasolina', 'negro', 'manual', '5', '5'),
        (4, 'dacia', 'duster', 'gasolina', 'azul', 'manual', '5', '5'),
        (5, 'peugeot', '208', 'gasolina', 'azul', 'manual', '3', '4'),
        (6, 'renault', 'arkana', 'electrico', 'amarillo', 'manual', '5', '5'),
        (7, 'seat', 'leon', 'gasolina', 'verde', 'manual', '5', '5');
"""

execute_query(conn, create_table_vehiculos)
execute_query(conn, insert_table_vehiculos)

#cerramos la conexion
mycursor.close()
conn.close()