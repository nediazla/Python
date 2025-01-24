# Ejercicio 1: Concatenar las cadenas 'Class', 'Of', 'Python' en una sola cadena 'clases de python'
cadena1 = 'Class' + ' ' + 'Of' + ' ' + 'Python'
print(cadena1.lower())  # 'clases de python'

# Ejercicio 2: Concatenar las cadenas 'Coding', 'For', 'All' en una sola cadena 'Coding For All'
cadena2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(cadena2)

# Ejercicio 3: Declarar una variable llamada company y asignarle el valor inicial "Coding For All"
company = "Coding For All"

# Ejercicio 4: Imprimir la variable company utilizando *print()*
print(company)

# Ejercicio 5: Imprimir la longitud de la cadena company utilizando el método *len()* y *print()*
print(len(company))

# Ejercicio 6: Cambiar todos los caracteres a mayúsculas utilizando el método *upper()*
print(company.upper())

# Ejercicio 7: Cambiar todos los caracteres a minúsculas utilizando el método *lower()*
print(company.lower())

# Ejercicio 8: Usar los métodos capitalize(), title(), swapcase() para dar formato al valor de la cadena *Coding For All*
print(company.capitalize())  # 'Coding for all'
print(company.title())  # 'Coding For All'
print(company.swapcase())  # 'cODING fOR aLL'

# Ejercicio 9: Cortar (slice) la primera palabra de la cadena *Coding For All*
print(company[0:6])  # 'Coding'

# Ejercicio 10: Verificar si la cadena *Coding For All* contiene la palabra Coding usando el método index, find u otros métodos.
print(company.find('Coding'))  # 0 (posición inicial de "Coding")

# Ejercicio 11: Reemplazar la palabra coding en la cadena ‘Coding For All’ por Python.
print(company.replace('Coding', 'Python'))  # 'Python For All'

# Ejercicio 12: Cambiar Python for Everyone a Python for All utilizando el método replace u otros métodos.
cadena3 = 'Python for Everyone'
print(cadena3.replace('Everyone', 'All'))  # 'Python for All'

# Ejercicio 13: Dividir la cadena ‘Coding For All’ usando el espacio como separador (split()).
print(company.split())  # ['Coding', 'For', 'All']

# Ejercicio 14: “Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon” dividir la cadena en la coma.
cadena4 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(cadena4.split(', '))  # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Ejercicio 15: ¿Cuál es el carácter en el índice 0 de la cadena *Coding For All*?
print(company[0])  # 'C'

# Ejercicio 16: ¿Cuál es el último índice de la cadena *Coding For All*?
print(len(company) - 1)  # 14

# Ejercicio 17: ¿Qué carácter está en el índice 10 de la cadena “Coding For All”?
print(company[10])  # 'A'

# Ejercicio 18: Crear un acrónimo o abreviatura para el nombre ‘Python For Everyone’.
print(''.join([word[0] for word in 'Python For Everyone'.split()]))  # 'PFE'

# Ejercicio 19: Crear un acrónimo o abreviatura para el nombre ‘Coding For All’.
print(''.join([word[0] for word in 'Coding For All'.split()]))  # 'CFA'

# Ejercicio 20: Usar index para determinar la posición de la primera ocurrencia de C en Coding For All.
print(company.index('C'))  # 0

# Ejercicio 21: Usar index para determinar la posición de la primera ocurrencia de F en Coding For All.
print(company.index('F'))  # 7

# Ejercicio 22: Usar rfind para determinar la posición de la última ocurrencia de l en Coding For All People.
company2 = "Coding For All People"
print(company2.rfind('l'))  # 13

# Ejercicio 23: Usar index o find para encontrar la posición de la primera ocurrencia de la palabra ‘because’ en la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’
oracion = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(oracion.find('porque'))  # 36

# Ejercicio 24: Usar rindex para encontrar la posición de la última ocurrencia de la palabra because en la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’
print(oracion.rfind('porque'))  # 52

# Ejercicio 25: Cortar (slice) la frase ‘porque porque porque’ de la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’
print(oracion[36:52])  # 'porque porque porque'

# Ejercicio 26: Encontrar la posición de la primera ocurrencia de la palabra ‘porque’ en la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’
print(oracion.find('porque'))  # 36

# Ejercicio 27: Cortar (slice) la frase ‘porque porque porque’ de la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’
print(oracion[36:52])  # 'porque porque porque'

# Ejercicio 28: ¿Empieza ‘Coding For All’ con una subcadena *Coding*?
print(company.startswith('Coding'))  # True

# Ejercicio 29: ¿Termina ‘Coding For All’ con una subcadena *coding*?
print(company.endswith('coding'))  # False

# Ejercicio 30: Eliminar los espacios a la izquierda y derecha de la cadena dada.
cadena5 = "   Coding For All   "
print(cadena5.strip())  # 'Coding For All'

# Ejercicio 31: ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier()?
print('ClassOfPython'.isidentifier())  # True
print('Class_of_python'.isidentifier())  # True

# Ejercicio 32: Unir la lista con un hash con espacio entre las cadenas.
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(librerias))  # 'Django # Flask # Bottle # Pyramid # Falcon'

# Ejercicio 33: Usar la secuencia de escape de nueva línea para separar las siguientes oraciones.
print("py\nEstoy disfrutando de este desafío. Solo me pregunto qué será lo próximo.")

# Ejercicio 34: Usar una secuencia de escape de tabulación para escribir las siguientes líneas.
print("py\tNombre\tEdad\tPaís\tCiudad\nNelson\t250\tEspaña\tCaceres")

# Ejercicio 35: Usar el método de formato de cadenas para mostrar lo siguiente.
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# Ejercicio 36: Realice lo siguiente utilizando métodos de formato de cadena:
print("8 + 6 = {}".format(8 + 6))
print("8 - 6 = {}".format(8 - 6))
print("8 * 6 = {}".format(8 * 6))
print("8 / 6 = {:.2f}".format(8 / 6))
print("8 % 6 = {}".format(8 % 6))
print("8 // 6 = {}".format(8 // 6))
print("8 ** 6 = {}".format(8 ** 6))
