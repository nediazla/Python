import requests
from bs4 import BeautifulSoup

# URL base
base_url = "https://academy.hackthebox.com/module/108/section/"


# Función para descargar la página
def descargar_pagina(seccion_numero):
    # Genera la URL completa
    url = f"{base_url}{seccion_numero}"

    try:
        # Realiza la solicitud GET
        respuesta = requests.get(url)

        # Si la respuesta es exitosa (código 200)
        if respuesta.status_code == 200:
            # Guardar la página en un archivo
            with open(f"{seccion_numero}.html", 'w', encoding='utf-8') as archivo:
                archivo.write(respuesta.text)
            print(f"Página {seccion_numero} descargada con éxito.")
        else:
            print(f"Error al descargar la página {seccion_numero}: {respuesta.status_code}")
    except Exception as e:
        print(f"Hubo un error al descargar la página {seccion_numero}: {e}")


# Descargar páginas desde 1000 hasta 5000
for i in range(1000, 5001):
    descargar_pagina(i)
