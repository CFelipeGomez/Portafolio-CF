#Conceptos cubiertos: Bases de datos No-SQL, conexión con MongoDB usando pymongo,
#operaciones CRUD (Create, Read, Update, Delete).

#Explicación: En este código, se trabaja con MongoDB (No-SQL) y se muestran las operaciones básicas de crear, 
#leer, actualizar y eliminar documentos dentro de una colección. 
#Esto introduce conceptos importantes para bases de datos No-SQL.

#Instalar pymongo (pip install pymongo)

from pymongo import MongoClient

def conectar_mongodb():
    """
    Esta función se conecta a una base de datos MongoDB local y realiza operaciones CRUD básicas.
    """
    cliente = MongoClient('mongodb://localhost:27017/')
    db = cliente['mi_base_no_sql']
    coleccion = db['usuarios']

    # Crear (Insertar)
    coleccion.insert_one({'nombre': 'Claudio', 'edad': 30})
    coleccion.insert_one({'nombre': 'Boberto', 'edad': 24})

    # Leer (Consultar)
    usuarios = coleccion.find()
    for usuario in usuarios:
        print(usuario)

    # Actualizar
    coleccion.update_one({'nombre': 'Claudio'}, {'$set': {'edad': 31}})

    # Eliminar
    coleccion.delete_one({'nombre': 'Boberto'})

    cliente.close()

if __name__ == "__main__":
    conectar_mongodb()
