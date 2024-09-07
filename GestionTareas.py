#Conceptos cubiertos: Operaciones CRUD con SQLite, estructura de clases y objetos.

#Explicación: Aquí se introduce el uso de clases y objetos para encapsular la lógica de negocio. 
#El programa gestiona una lista de tareas en una base de datos SQLite, y se realizan todas las operaciones CRUD.

import sqlite3

class TareasDB:
    def __init__(self):
        self.conexion = sqlite3.connect('tareas.db')
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                               id INTEGER PRIMARY KEY,
                               descripcion TEXT,
                               completada BOOLEAN)''')

    def agregar_tarea(self, descripcion):
        self.cursor.execute("INSERT INTO tareas (descripcion, completada) VALUES (?, ?)", (descripcion, False))
        self.conexion.commit()

    def listar_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        return self.cursor.fetchall()

    def completar_tarea(self, id_tarea):
        self.cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (id_tarea,))
        self.conexion.commit()

    def eliminar_tarea(self, id_tarea):
        self.cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()

if __name__ == "__main__":
    db = TareasDB()

    # Agregar una tarea
    db.agregar_tarea("Aprender Python")

    # Listar todas las tareas
    tareas = db.listar_tareas()
    for tarea in tareas:
        print(tarea)

    # Completar una tarea
    db.completar_tarea(1)

    # Eliminar una tarea
    db.eliminar_tarea(1)

    db.cerrar()
