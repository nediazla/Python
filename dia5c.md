# Dia 5: sets

## Sets (set)

Un set es una colección de elementos. Permítanme llevarlos de regreso a su lección de matemáticas de la escuela primaria o secundaria. La definición matemática de un sets se puede aplicar también en Python. Un setes una colección de elementos distintos no ordenados y no indexados. En Python, un set se usa para almacenar elementos únicos y es posible encontrar la *unión*, *intersección*, *diferencia*, *diferencia simétrica*, *subset*, *superset*y *setdisjunto* entre sets.

### Creación de un set

Usamos la función incorporada *set()*.

- Creación de un setvacío

```python
# syntaxst = set()
```

- Creando un setcon elementos iniciales

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

**Ejemplo:**

```python
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### Obtención de la longitud de un set

Utilizamos el método **len()** para encontrar la longitud de un set.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**Example:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

### Acceso a elementos de un set

Utilizamos bucles para acceder a los elementos. Veremos esto en la sección de bucles

### Comprobación de un elemento

Para comprobar si un elemento existe en una lista, utilizamos el operador de pertenencia *in*.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### Cómo agregar elementos a un set

Una vez que se crea un set, no podemos cambiar ningún elemento y también podemos agregar elementos adicionales.

- Agregue un elemento usando *add()*

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**Ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

- Agregar varios elementos mediante update()
La función update() permite agregar varios elementos a un set. La función update() toma como argumento una lista.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**Ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### Eliminar elementos de un set

Podemos eliminar un elemento de un setmediante el método *remove()*. Si no se encuentra el elemento, el método *remove()* generará errores, por lo que es bueno verificar si el elemento existe en el setdado. Sin embargo, el método *discard()* no genera ningún error.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

Los métodos pop() eliminan un elemento aleatorio de una lista y devuelven el elemento eliminado.

**Ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
```

Si estamos interesados en el artículo eliminado.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
```

### Borrar elementos de un set

Si queremos borrar o vaciar el set, utilizamos el método *clear*.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**Ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### Eliminar un set

Si queremos eliminar el set en sí, utilizamos el operador *del*.

```python
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**Ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### Conversión de lista a set

Podemos convertir una lista a un sety un seta una lista. Al convertir una lista a un setse eliminan los duplicados y solo se reservan los elementos únicos.

### Conversión de lista a set

Podemos convertir una lista a un set y un set a una lista. Al convertir una lista a un setse eliminan los duplicados y solo se reservan los elementos únicos.

```python
# syntaxl
st = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

**Ejemplo:**

```python
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### Unir sets

Podemos unir dos setsutilizando el método *union()* o *update()*.

- union()
Este método devuelve un nuevo set

```python
# syntaxst1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

**Ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

- update()
Este método inserta un seten un setdado

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

**Ejemplo:**

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)
```

### Búsqueda de elementos de intersección

La intersección devuelve un setde elementos que se encuentran en ambos sets. Vea el ejemplo

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```

**Ejemplo:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```

### Comprobación de subsetsy supersets

Un setpuede ser un subseto un supersetde otros sets:

- Subset: *issubset()*
- Superset: *issuperset*

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**Ejemplo:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### Comprobación de la diferencia entre dos sets

Devuelve la diferencia entre dos sets.

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)
st1.difference(st2) 
```

**Example:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### Hallar la diferencia simétrica entre dos sets

Devuelve la diferencia simétrica entre dos sets. Esto significa que devuelve un setque contiene todos los elementos de ambos sets, excepto los elementos que están presentes en ambos sets, matemáticamente: (A) ∪ (B)

```python
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}

st2.symmetric_difference(st1)
```

**Ejemplo:**

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon) 
```

### Unión de sets

Si dos setsno tienen un elemento o elementos en común, los llamamos setsdisjuntos. Podemos comprobar si dos sets son joint o disjoint usandog *isdisjoint()*

```python
# syntaxst1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

**Example:**

```python
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)
```

🌕 Eres una estrella en ascenso. Acabas de completar los desafíos del día 7 y estás 7 pasos adelante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 5

```python
# set
sit_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Ejercicios: Nivel 1

1. Halla la longitud del setit_companies
2. Añade ‘Twitter’ a it_companies
3. Inserta varias empresas de TI a la vez en el setit_companies
4. Elimina una de las empresas del setit_companies
5. ¿Cuál es la diferencia entre eliminar y descartar?

### Ejercicios: Nivel 2

1. Une A y B
2. Halla la intersección de A y B
3. ¿Es A un subsetde B?
4. ¿Son A y B setsdisjuntos?
5. Une A con B y B con A
6. ¿Cuál es la diferencia simétrica entre A y B?
7. Elimina los sets por completo

### Ejercicios: Nivel 3

1. Convierte las edades en un sety compara la longitud de la lista y el set, ¿cuál es más grande?
2. Explica la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y set.
3. *Soy profesor y me encanta inspirar y enseñar a la gente.* ¿Cuántas palabras únicas se han utilizado en la oración? Utiliza los métodos split y set para obtener las palabras únicas.

🎉 ¡FELICITACIONES! 🎉