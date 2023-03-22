import os
import random
import string

def crear_carpetas(cantidad):
    """
    Crea una cantidad específica de carpetas con nombres aleatorios en la carpeta raíz del disco principal.
    """
    # Obtiene la ruta de la carpeta raíz del disco principal
    raiz = os.path.abspath(os.sep)
    for i in range(cantidad):
        # Genera un nombre de carpeta aleatorio
        nombre_carpeta = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        # Crea la carpeta en la ruta especificada
        os.mkdir(os.path.join(raiz, nombre_carpeta))
        print(f"Carpeta {nombre_carpeta} creada en {raiz}")

cantidad = 5
crear_carpetas(cantidad)
