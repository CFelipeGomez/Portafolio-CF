#Conceptos cubiertos: Funciones, bucles, condicionales, manejo de errores.

#Explicación: Este código utiliza una función para verificar si un número es primo. 
#Se introducen conceptos básicos de condicionales, bucles, y manejo de excepciones.

# Función para verificar si un número es primo
def es_primo(numero):
    """
    Esta función recibe un número y determina si es primo.
    Un número primo es divisible solo por sí mismo y por 1.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitamos un número al usuario
try:
    numero = int(input("Introduce un número: "))
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
except ValueError:
    print("Por favor, introduce un número entero válido.")