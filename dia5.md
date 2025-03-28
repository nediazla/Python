# Dia 5: Lists

## Lists

Hay cuatro tipos de datos de colección en Python:

- Lista: es una colección ordenada y modificable. Permite miembros duplicados.
- Tupla: es una colección ordenada e inmutable. Permite miembros duplicados.
- Conjunto: es una colección desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
- Diccionario: es una colección desordenada, modificable e indexada. No hay miembros duplicados.

Una lista es una colección de diferentes tipos de datos que está ordenada y es modificable. Una lista puede estar vacía o puede tener elementos de diferentes tipos de datos.

### Cómo crear una lista

En Python podemos crear listas de dos maneras:

- Usando la función incorporada de lista

```python
# syntaxlst = list()
```

```python
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

- Usando corchetes, []

```python
# syntaxlst = []
```

```python
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

Listas con valores iniciales. Usamos *len()* para encontrar la longitud de una lista.

```python
fruits = ['banana', 'orange', 'mango', 'lemon'] 
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot'] 
animal_products = ['milk', 'meat', 'butter', 'yoghurt']  
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB'] 
countries = ['Espana', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)  # Corregido el nombre aquí
print('Number of web technologies:', len(web_techs))  # Corregido el nombre aquí
print('Countries:', countries)
print('Number of countries:', len(countries))
```

```python
Fruits: ['banana', 'orange', 'mango', 'lemon']
# Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
# Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
# Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
# Number of web technologies: 7
Countries: ['Espana', 'Estonia', 'Denmark', 'Sweden', 'Norway']
# Number of countries: 5
```

- Las listas pueden tener elementos de diferentes tipos de datos.

```python
lst = ['Nelson', 250, True, {'country': 'Espana', 'city': 'Helsinki'}]
```

### Acceso a elementos de lista mediante indexación positiva

Accedemos a cada elemento de una lista mediante su índice. El índice de una lista comienza desde 0. La siguiente imagen muestra claramente dónde comienza el índice.

![30-Days-Of-Pythonimageslist_index.png](img/30-Days-Of-Pythonimageslist_index.png)

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

# Accediendo al primer elemento usando su índice
first_fruit = fruits[0]
print(first_fruit)  # banana

# Accediendo al segundo elemento
second_fruit = fruits[1]  # Corregido el nombre de la variable
print(second_fruit)  # orange

# Accediendo al último elemento directamente con su índice
last_fruit = fruits[3]
print(last_fruit)  # lemon

# Accediendo al último elemento usando el índice calculado
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)  # lemon
```

### Acceso a elementos de lista mediante indexación negativa

La indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al penúltimo elemento.

![30-Days-Of-Pythonimageslist_negative_indexing.png](img/30-Days-Of-Pythonimageslist_negative_indexing.png)

List negative indexing

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```
### Desempaquetando elementos de la lista

```python
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

```python
# Primer ejemplo de desempaquetado
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)    # banana
print(second_fruit)   # orange
print(third_fruit)    # mango
print(rest)           # ['lemon', 'lime', 'apple']

# Segundo ejemplo de desempaquetado
listfirst, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listfirst)      # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4, 5, 6, 7, 8, 9]
print(tenth)          # 10

# Tercer ejemplo de desempaquetado
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Espana', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)        # Germany
print(fr)        # France
print(bg)        # Belgium
print(sw)        # Sweden
print(scandic)   # ['Denmark', 'Espana', 'Norway', 'Iceland']
print(es)        # Estonia
```

### Segmentación de elementos de una lista

- Indexación positiva: podemos especificar un rango de índices positivos especificando el inicio, el final y el paso; el valor de retorno será una nueva lista. (valores predeterminados para inicio = 0, fin = len(lst) - 1 (último elemento), paso = 1)

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

# Acceder a todos los elementos de la lista
all_fruits = fruits[0:4]  # Devuelve todos los elementos: ['banana', 'orange', 'mango', 'lemon']
print(all_fruits)

# Esto también devolverá todos los elementos de la lista
all_fruits = fruits[0:]  # Si no se especifica el índice final, toma todos los elementos
print(all_fruits)

# Acceder a un subgrupo (de índice 1 a 3, sin incluir el índice 3)
orange_and_mango = fruits[1:3]  # Devuelve ['orange', 'mango']
print(orange_and_mango)

# Acceder a los elementos desde el índice 1 hasta el final
orange_mango_lemon = fruits[1:]  # Devuelve ['orange', 'mango', 'lemon']
print(orange_mango_lemon)

# Acceder a cada segundo elemento
orange_and_lemon = fruits[::2]  # Devuelve ['banana', 'mango']
print(orange_and_lemon)
```

- Indexación negativa: podemos especificar un rango de índices negativos especificando el inicio, el final y el paso, el valor de retorno será una nueva lista.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

# Acceder a todos los elementos desde el índice -4 hasta el final
all_fruits = fruits[-4:]  # Devuelve ['banana', 'orange', 'mango', 'lemon']
print(all_fruits)

# Acceder a un subgrupo entre los índices -3 y -1 (sin incluir el último índice)
orange_and_mango = fruits[-3:-1]  # Devuelve ['orange', 'mango']
print(orange_and_mango)

# Acceder a todos los elementos desde el índice -3 hasta el final
orange_mango_lemon = fruits[-3:]  # Devuelve ['orange', 'mango', 'lemon']
print(orange_mango_lemon)

# Invertir la lista usando un paso negativo
reverse_fruits = fruits[::-1]  # Devuelve ['lemon', 'mango', 'orange', 'banana']
print(reverse_fruits)
```

### Modificación de listas

Una lista es una colección ordenada de elementos que se puede modificar o cambiar. Vamos a modificar la lista de frutas.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

# Cambiar el primer elemento
fruits[0] = 'avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']

# Cambiar el segundo elemento
fruits[1] = 'apple'
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']

# Cambiar el último elemento
last_index = len(fruits) - 1  # Calcular el índice del último elemento
fruits[last_index] = 'lime'  # Cambiar el último elemento a 'lime'
print(fruits)  # ['avocado', 'apple', 'mango', 'lime']
```

### Comprobación de elementos en una lista

Comprobación de un elemento para ver si es miembro de una lista mediante el operador *in*. Vea el ejemplo a continuación.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

# Verificar si 'banana' está en la lista
does_exist = 'banana' in fruits
print(does_exist)  # True

# Verificar si 'lime' está en la lista
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### Cómo agregar elementos a una lista

Para agregar un elemento al final de una lista existente, utilizamos el método *append()*.

```python
# syntaxlst = list()
lst.append(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

### Inserción de elementos en una lista

Podemos utilizar el método *insert()* para insertar un único elemento en un índice específico de una lista. Tenga en cuenta que los demás elementos se desplazan hacia la derecha. El método *insert()* toma dos argumentos: índice y un elemento para insertar.

```python
# syntaxlst = ['item1', 'item2']
lst.insert(index, item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

### Eliminar elementos de una lista ***

El método remove elimina un elemento específico de una lista

```python
# syntaxlst = ['item1', 'item2']
lst.remove(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list

fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

### Eliminación de elementos mediante Pop

El método *pop()* elimina el índice especificado (o el último elemento si no se especifica el índice):

```python
# syntaxlst = ['item1', 'item2']
lst.pop()       # last itemlst.pop(index)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### Eliminar elementos con Del

La palabra clave *del* elimina el índice especificado y también se puede utilizar para eliminar elementos dentro del rango del índice. También puede eliminar la lista por completo.

```python
# syntaxlst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

# Eliminar el primer elemento de la lista
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']

# Eliminar el segundo elemento (índice 1) de la lista
del fruits[1]
print(fruits)  # ['orange', 'lemon', 'kiwi', 'lime']

# Eliminar un rango de elementos entre los índices 1 y 3 (sin incluir el índice 3)
del fruits[1:3]  # Elimina 'lemon' y 'kiwi'
print(fruits)  # ['orange', 'lime']

# Eliminar la lista completa
del fruits
print(fruits)  # Esto generará un error porque 'fruits' ya no está definida
```

### Borrado de elementos de la lista

El método *clear()* vacía la lista:

```python
# syntaxlst = ['item1', 'item2']
lst.clear()
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

### Copiar una lista

Es posible copiar una lista reasignándola a una nueva variable de la siguiente manera: list2 = list1. Ahora, list2 es una referencia de list1, cualquier cambio que hagamos en list2 también modificará la original, list1. Pero hay muchos casos en los que no queremos modificar la original, sino que preferimos tener una copia diferente. Una forma de evitar el problema anterior es usar *copy()*.

```python
# syntaxlst = ['item1', 'item2']
lst_copy = lst.copy()
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### Unir listas

Existen varias formas de unir o concatenar dos o más listas en Python.

- Operador más (+)

```python
# syntaxlist3 = list1 + list2
```

```python
# Concatenación de números enteros
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Concatenación de frutas y verduras
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- Unir mediante el método extend()
El método extend() permite añadir una lista a una lista. Vea el ejemplo a continuación.

```python
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

```python
# Extender num1 con num2
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)  # Numbers: [0, 1, 2, 3, 4, 5, 6]

# Extender negative_numbers con zero y positive_numbers
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)  # Agrega el 0
negative_numbers.extend(positive_numbers)  # Agrega los números positivos
print('Integers:', negative_numbers)  # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Extender fruits con vegetables
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)  # Agrega las verduras
print('Fruits and vegetables:', fruits)  # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### Conteo de elementos en una lista

El método *count()* devuelve la cantidad de veces que aparece un elemento en una lista:

```python
# syntaxlst = ['item1', 'item2']
lst.count(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### Búsqueda del índice de un elemento

El método *index()* devuelve el índice de un elemento de la lista:

```python
# syntaxlst = ['item1', 'item2']
lst.index(item)
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))  # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # 2        # 2, the first occurrence
```

### Invertir una lista

El método *reverse()* invierte el orden de una lista.

```python
# syntaxlst = ['item1', 'item2']
lst.reverse()
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

```python
# syntaxlst = ['item1', 'item2']
lst.sort()                # ascendinglst.sort(reverse=True)    # descending
```

**Example:**

```python
# Ordenar frutas alfabéticamente
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)  # ['banana', 'lemon', 'mango', 'orange']

# Ordenar frutas en orden descendente
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']

# Ordenar edades en orden ascendente
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]

# Ordenar edades en orden descendente
ages.sort(reverse=True)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]
```

sorted(): returns the ordered list without modifying the original list
**Example:**

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']# Reverse orderfruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
```

### Ordenar elementos de una lista

Para ordenar listas podemos utilizar el método *sort()* o las funciones integradas *sorted()*. El método *sort()* reordena los elementos de la lista en orden ascendente y modifica la lista original. Si un argumento del método *sort()* reverse es igual a true, ordenará la lista en orden descendente.

- `sort()`: este método modifica la lista original

🌕 Eres diligente y ya has logrado mucho. Acabas de completar los desafíos del día 5 y estás 5 pasos adelante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 5

### Ejercicios: Nivel 1

1. Declara una lista vacía
2. Declara una lista con más de 5 elementos
3. Encuentra la longitud de tu lista
4. Obtén el primer elemento, el elemento del medio y el último elemento de la lista
5. Declara una lista llamada mixed_data_types, pon tu(nombre, edad, altura, estado civil, dirección)
6. Declara una variable de lista llamada it_companies y asigna los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
7. Imprima la lista usando *print()*
8. Imprima el número de empresas en la lista
9. Imprima la primera, la segunda y la última empresa
10. Imprima la lista después de modificar una de las empresas
11. Agregue una empresa de TI a it_companies
12. Inserte una empresa de TI en el medio de la lista de empresas
13. Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
14. Una las it_companies con una cadena ‘#; ’
15. Verifique si una determinada empresa existe en la lista it_companies.
16. Ordena la lista usando el método sort()
17. Invierte la lista en orden descendente usando el método reverse()
18. Elimina las primeras 3 empresas de la lista
19. Elimina las últimas 3 empresas de la lista
20. Elimina la empresa o empresas de TI del medio de la lista
21. Elimina la primera empresa de TI de la lista
22. Elimina la empresa o empresas de TI del medio de la lista
23. Elimina la última empresa de TI de la lista
24. Elimina todas las empresas de TI de la lista
25. Destruye la lista de empresas de TI
26. Une las siguientes listas:

```python
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

```

1. Después de unir las listas en cuestión 26. Copia la lista unida y asígnala a una variable full_stack, luego inserta Python y SQL después de Redux.

### Ejercicios: Nivel 2

1. La siguiente es una lista de 10 edades de estudiantes:

```bash
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

```

- Ordena la lista y encuentra la edad mínima y máxima
- Agrega la edad mínima y la edad máxima nuevamente a la lista
- Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
- Encuentra la edad promedio (suma de todos los elementos dividida por su número)
- Encuentra el rango de las edades (máxima menos mínima)
- Compara el valor de (mín - promedio) y (máx - promedio), usa el método *abs()*
1. Encuentra el país o los países del medio en la [lista de países](https://github.com/nediazla/Python/blob/main/data/countries.py)
2. Divide la lista de países en Dos listas iguales si es par o no, un país más para la primera mitad.
3. [‘China’, ‘Rusia’, ‘EE. UU.’, ‘España’, ‘Suecia’, ‘Noruega’, ‘Dinamarca’]. Desglosa los tres primeros países y el resto como países escandinavos.

🎉 ¡FELICIDADES! 🎉
