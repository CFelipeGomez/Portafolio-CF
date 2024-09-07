#Conceptos cubiertos: API, acciones API, consultas básicas.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados (normalmente estos datos estarían en una base de datos)
tareas = [
    {"id": 1, "titulo": "Aprender Python", "completado": False},
    {"id": 2, "titulo": "Construir una API", "completado": False}
]

# Ruta para obtener todas las tareas (GET)
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    """
    Devuelve la lista de tareas.
    Utiliza el método GET para obtener los recursos.
    """
    return jsonify(tareas)

# Ruta para obtener una tarea específica (GET)
@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    """
    Devuelve una tarea específica basada en el ID.
    Si no se encuentra, devuelve un error 404.
    """
    tarea = next((tarea for tarea in tareas if tarea["id"] == id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(tarea)

# Ruta para crear una nueva tarea (POST)
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    """
    Crea una nueva tarea.
    El cuerpo de la solicitud debe contener un JSON con los datos.
    """
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": request.json['titulo'],
        "completado": False
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

# Ruta para actualizar una tarea existente (PUT)
@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    """
    Actualiza una tarea existente basada en el ID.
    El cuerpo de la solicitud debe contener un JSON con los datos.
    """
    tarea = next((tarea for tarea in tareas if tarea["id"] == id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    tarea["titulo"] = request.json.get('titulo', tarea['titulo'])
    tarea["completado"] = request.json.get('completado', tarea['completado'])
    return jsonify(tarea)

# Ruta para eliminar una tarea (DELETE)
@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    """
    Elimina una tarea basada en el ID.
    Si no se encuentra, devuelve un error 404.
    """
    tarea = next((tarea for tarea in tareas if tarea["id"] == id), None)
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404

    tareas.remove(tarea)
    return jsonify({"message": "Tarea eliminada correctamente"}), 200

# Ejecución del servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
