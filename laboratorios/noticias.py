import requests
from bs4 import BeautifulSoup

def obtener_titulos_noticias(url):

    respuesta = requests.get(url)

    if  respuesta.status_code == 200:

        soup = BeautifulSoup(respuesta.content, 'html.parser')
        titulos = soup.find_all(['h2', 'a'])
        titulos_articulos = set()

        for titulo in titulos:
            texto_titulo = titulo.get_text().strip()
            if texto_titulo:
                titulos_articulos.add(texto_titulo)

        titulos_articulos = sorted(titulos_articulos)


        print('Tirulos de los articulos encontrados: ')
        for idx, titulo in enumerate(titulos_articulos, start=1):
            print(f'{idx} - {titulo}')

    else:
        print(f'Error al acceder a la pagina: {respuesta.status_code}')

url = 'https://www.formula1.com/'

obtener_titulos_noticias(url)