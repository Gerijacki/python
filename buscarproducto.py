import requests
from bs4 import BeautifulSoup

def buscar_precios(producto):
    """
    Busca los precios de un producto en diferentes tiendas en línea.
    """
    tiendas = ["https://www.amazon.com", "https://www.pccomponentes.com/", "https://www.mediamarkt.es/"]
    for tienda in tiendas:
        try:
            pagina = requests.get(tienda, params={"q": producto})
            soup = BeautifulSoup(pagina.content, "html.parser")
            precio = soup.find("span", class_="a-price-whole").get_text()
            print(f"En {tienda} el precio de {producto} es {precio}")
        except:
            print(f"No se encontró el precio de {producto} en {tienda}.")

buscar_precios("iphone 11")
