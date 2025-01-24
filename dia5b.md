# Dia 5: Tuples

## 

```python
# syntaxempty_tuple = ()
# or using the tuple constructorempty_tuple = tuple()
```

## Tuplas

Una tupla es una colección de diferentes tipos de datos que está ordenada y no se puede cambiar (inmutable). Las tuplas se escriben entre corchetes, (). Una vez que se crea una tupla, no podemos cambiar sus valores. No podemos usar los métodos add, insert, remove en una tupla porque no es modificable (mutable). A diferencia de list, tuple tiene pocos métodos. Métodos relacionados con las tuplas:

- tuple(): para crear una tupla vacía
- count(): para contar la cantidad de un elemento específico en una tupla
- index(): para encontrar el índice de un elemento específico en una tupla
- operator: para unir dos o más tuplas y crear una nueva tupla

### Creación de una tupla

- Tupla vacía: creación de una tupla vacía
    
    ```python
    # syntax
    tpl = ('item1', 'item2','item3')
    # or using the tuple constructor
    empty_tuple = tuple()
    ```
    
- Tuple con valor inicial
    
```python
# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
```
### Longitud de la tupla

Utilizamos el método *len()* para obtener la longitud de una tupla.

```python
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Acceso a elementos de tupla

- Indexación positiva
De manera similar al tipo de datos de lista, utilizamos indexación positiva o negativa para acceder a los elementos de tupla.
    
![30-Days-Of-Pythonimagestuples_index.png](img/30-Days-Of-Pythonimagestuples_index.png)

```python
# Syntaxtpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1last_fruit = fruits[las_index]
```

- Indexación negativa
La indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al segundo último y el negativo de la longitud de la lista/tupla se refiere al primer elemento.
    
![30-Days-Of-Pythonimagestuple_negative_indexing.png](img/30-Days-Of-Pythonimagestuple_negative_indexing.png)
    

```python
# Syntaxtpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
```

### Segmentación de tuplas

Podemos segmentar una subtupla especificando un rango de índices donde comenzar y donde terminar en la tupla; el valor de retorno será una nueva tupla con los elementos especificados.

- Rango de índices positivos

```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
```

- Range of Negative Indexes

```python
 # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # all items
  middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
```

```python
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # all items
  orange_mango = fruits[-3:-1]  # doesn't include item at index 3
  orange_to_the_rest = fruits[-3:]
```

### Cambio de tuplas a listas

Podemos cambiar tuplas a listas y listas a tuplas. Una tupla es inmutable; si queremos modificar una tupla, debemos convertirla en una lista.

```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### Comprobación de un elemento en una tupla

Podemos comprobar si un elemento existe o no en una tupla utilizando *in*, que devuelve un valor booleano.

```python
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

### Unir tuplas

Podemos unir dos o más tuplas usando el operador +

```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

### Eliminación de tuplas

No es posible eliminar un solo elemento de una tupla, pero sí es posible eliminar la tupla misma mediante *del*.

```python
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

🌕 Eres muy valiente, has llegado hasta aquí. Acabas de completar los desafíos del día 6 y estás 6 pasos adelante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 5

### Ejercicios: Nivel 1

1. Crea una tupla vacía
2. Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
3. Une las tuplas de hermanos y hermanas y asígnalas a los hermanos
4. ¿Cuántos hermanos tienes?
5. Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members

### Ejercicios: Nivel 2

1. Desempaqueta los hermanos y los padres de family_members
2. Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
3. Cambia la tupla about food_stuff_tp a una lista food_stuff_lt
4. Recorta el elemento o los elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.
5. Separe los tres primeros elementos y los tres últimos elementos de la lista food_staff_lt
6. Elimine la tupla food_staff_tp por completo
7. Verifique si existe un elemento en la tupla:
    - Verifique si "Estonia" es un país nórdico
    - Verifique si "Islandia" es un país nórdico
    
```python
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
```
    

🎉 ¡FELICIDADES! 🎉