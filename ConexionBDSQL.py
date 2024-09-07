#Conceptos cubiertos: Bases de datos SQL, conexión con SQLite en Python, consultas básicas.

#Explicación: Este código muestra cómo conectar una base de datos SQLite, crear una tabla, 
#insertar registros y consultar los datos. Se utiliza SQLite por ser una base de datos ligera y fácil de manejar.

import sqlite3

def crear_base_datos():
    """
    Esta función crea una base de datos SQLite y una tabla de ejemplo llamada 'usuarios'.
    """
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    # Creación de una tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                      id INTEGER PRIMARY KEY,
                      nombre TEXT,
                      edad INTEGER)''')

    # Insertamos algunos registros
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Claudio', 30)")
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Boberto', 24)")
    conexion.commit()

    # Consultamos los datos
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

    conexion.close()

if __name__ == "__main__":
    crear_base_datos()
