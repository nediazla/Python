import requests


# Función para descargar la imagen
def descargar_imagen(url, nombre_archivo):
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            with open(nombre_archivo, 'wb') as file:
                file.write(response.content)
            print(f"Imagen descargada: {nombre_archivo}")
        else:
            print(f"Error al descargar la imagen {nombre_archivo}: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


# URL base
url_base = "https://academy.hackthebox.com/storage/modules/176/{}.png"

# Descargar imágenes de la 1 a la 200
for i in range(1, 201):
    url = url_base.format(i)
    nombre_archivo = f"imagen_{i}.png"
    descargar_imagen(url, nombre_archivo)
