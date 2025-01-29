# Dia 5: dictionaries

## Diccionarios

Un diccionario es una colección de datos de tipo par (clave: valor) modificables (mutables) y no ordenados.

### Creación de un diccionario

Para crear un diccionario, utilizamos llaves, {} o la función incorporada *dict()*.

```python
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

**Example:**

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Spain',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
    }
```

El diccionario anterior muestra que un valor puede ser cualquier tipo de datos: cadena, booleano, lista, tupla, conjunto o un diccionario.

### Longitud del diccionario

Comprueba la cantidad de pares "clave: valor" en el diccionario.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Ejemplo:**

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Spain',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
    }
print(len(person)) # 7
```

### Acceso a los elementos del diccionario

Podemos acceder a los elementos del diccionario consultando su nombre de clave.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
```

**Ejemplo:**

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Spain',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
    }
print(person['first_name']) # Nelson
print(person['country'])    # Spain
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
```

Acceder a un elemento por el nombre de la clave genera un error si la clave no existe. Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get. El método get devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Spain',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
    }
print(person.get('first_name')) # Nelson
print(person.get('country'))    # Spain
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### Cómo agregar elementos a un diccionario

Podemos agregar nuevos pares de clave y valor a un diccionario

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

**Ejemplo:**

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Spain',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'        }
}
person['job_title'] = 'Instructor'person['skills'].append('HTML')
print(person)
```

### Modificación de elementos en un diccionario

Podemos modificar elementos en un diccionario

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
```

**Ejemplo:**

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Spain',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
    }
person['first_name'] = 'Eyob'person['age'] = 252
```

### Comprobación de claves en un diccionario

Utilizamos el operador *in* para comprobar si una clave existe en un diccionario

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Eliminación de pares de clave y valor de un diccionario

- *pop(key)*: elimina el elemento con el nombre de clave especificado:
- *popitem()*: elimina el último elemento
- *del*: elimina un elemento con el nombre de clave especificado

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
```

**Ejemplo:**

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Spain',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
    }
person.pop('first_name')        # Removes the firstname 
itemperson.popitem()                # Removes the address 
itemdel person['is_married']        # Removes the is_married item
```

### Cambio del diccionario a una lista de elementos

El método *items()* cambia el diccionario a una lista de tuplas.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())
```

### Limpiar un diccionario

Si no queremos los elementos de un diccionario, podemos limpiarlos utilizando el método *clear()*

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Eliminar un diccionario

Si no usamos el diccionario podemos eliminarlo por completo

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copiar un diccionario

Podemos copiar un diccionario utilizando el método *copy()*. Al utilizar la copia podemos evitar la mutación del diccionario original.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
```

### Obtención de claves de diccionario como una lista

El método *keys()* nos proporciona todas las claves de un diccionario como una lista.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)  
```

### Obtención de valores de diccionario como una lista

El método *values* nos proporciona todos los valores de un diccionario como una lista.

```python
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values) 
```

🌕 Eres asombroso. Ahora estás supercargado con el poder de los diccionarios. Acabas de completar los desafíos del día 5 y estás 5 pasos adelante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 5

1. Crea un diccionario vacío llamado perro
2. Agrega nombre, color, raza, patas, edad al diccionario perro
3. Crea un diccionario de estudiantes y agrega nombre, apellido, género, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario
4. Obtén la longitud del diccionario de estudiantes
5. Obtén el valor de habilidades y verifica el tipo de datos, debe ser una lista
6. Modifica los valores de las habilidades agregando una o dos habilidades
7. Obtén las claves del diccionario como una lista
8. Obtén los valores del diccionario como una lista
9. Cambia el diccionario a una lista de tuplas usando el método *items()*
10. Elimina uno de los elementos del diccionario
11. Elimina uno de los diccionarios

🎉 ¡FELICITACIONES! 🎉