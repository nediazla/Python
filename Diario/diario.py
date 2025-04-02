

# Lista de datos: cada sublista contiene información de una persona: [Nombre, País, Ciudad]
data = [
    ['Asabeneh', 'Finland', 'Helsink'],  # Nota: "Helsink" podría ser un error tipográfico, normalmente se escribe "Helsinki"
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

# Creación de un DataFrame de pandas a partir de la lista de datos
# Se especifican los nombres de las columnas: 'Names', 'Country' y 'City'
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])

# Imprime el DataFrame resultante
print(df)
