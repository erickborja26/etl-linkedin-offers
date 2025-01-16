import mysql.connector
from prefect import task

@task(name="Load en base de datos")
def task_load_linkedin(ofertas):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='datag3'
        )
        cursor = conn.cursor()

        query_tabla = """CREATE TABLE IF NOT EXISTS ofertas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            ubicacion VARCHAR(255),
            url VARCHAR(255)
        )"""
        cursor.execute(query_tabla)
        conn.commit()
        query_insertar = "INSERT INTO ofertas (nombre, ubicacion, url) VALUES (%s, %s, %s)"

        for oferta in ofertas:
            cursor.execute(query_insertar, (oferta['nombre'], oferta['ubicacion'], oferta['url']))
        
        conn.commit()
        cursor.close()
        conn.close()
        print(f"La data fue guardada en la base de datos")
    
    except mysql.connector.Error as error:
        print("Error detectado : {}".format(error))