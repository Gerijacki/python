import os

def limpiador_de_archivos(directorio):
    """
    Elimina todos los archivos con una extensión específica en un directorio dado.
    """
    ext = input("Ingrese la extensión de archivo que desea eliminar (ej: .txt, .pdf): ")
    for archivo in os.listdir(directorio):
        if archivo.endswith(ext):
            os.remove(os.path.join(directorio, archivo))
            print(f"Archivo {archivo} eliminado.")
    print("Limpieza de archivos completada.")

limpiador_de_archivos("/ruta/a/tu/directorio")
