# Manual Exhaustivo de Python y SQL

1. [Fundamentos de Python](#fundamentos-de-python) (Parte 1)
2. Python Intermedio (Parte 2)
3. Python Avanzado (Parte 3)
4. Fundamentos de SQL (Parte 4)
5. SQL Intermedio (Parte 5)
6. SQL Avanzado (Parte 6)
7. Integración Python-SQL (Parte 7)
8. Proyectos Prácticos (Parte 8)

## Fundamentos de Python

### 1. Instalación y Configuración

#### 1.1 Instalación de Python
```bash
# Windows
# 1. Descargar el instalador de python.org
# 2. Marcar "Add Python to PATH"
# 3. Instalar

# Linux
sudo apt update
sudo apt install python3
sudo apt install python3-pip

# macOS
brew install python3
```

#### 1.2 Entorno Virtual
```bash
# Crear entorno virtual
python -m venv mi_entorno

# Activar entorno virtual
# Windows
mi_entorno\Scripts\activate
# Linux/macOS
source mi_entorno/bin/activate

# Instalar paquetes
pip install nombre_paquete
```

### 2. Tipos de Datos Fundamentales

#### 2.1 Números
```python
# Enteros (int)
x = 5
y = -17
z = 1_000_000  # Separador de miles para legibilidad

# Punto flotante (float)
pi = 3.14159
e = 2.71828
científico = 1.23e-4

# Operaciones matemáticas avanzadas
import math

# Constantes matemáticas
print(math.pi)       # π
print(math.e)        # e (número de Euler)
print(math.inf)      # Infinito
print(math.nan)      # Not a Number

# Funciones matemáticas
print(math.ceil(3.7))    # 4 (redondeo hacia arriba)
print(math.floor(3.7))   # 3 (redondeo hacia abajo)
print(math.trunc(3.7))   # 3 (truncamiento)
print(math.gcd(12, 18))  # 6 (máximo común divisor)
print(math.factorial(5))  # 120 (factorial)

# Funciones trigonométricas
print(math.sin(math.pi/2))  # 1.0
print(math.cos(math.pi))    # -1.0
print(math.tan(math.pi/4))  # 1.0
print(math.degrees(math.pi)) # 180.0
print(math.radians(180))    # π

# Números complejos
z1 = 3 + 4j
z2 = complex(1, 2)
print(z1.real)       # 3.0
print(z1.imag)       # 4.0
print(abs(z1))       # 5.0 (magnitud)
print(z1.conjugate()) # 3 - 4j

# Operaciones con precisión decimal
from decimal import Decimal, getcontext
getcontext().prec = 28  # Establecer precisión
d1 = Decimal('1.1')
d2 = Decimal('2.2')
print(d1 + d2)      # Exactamente 3.3
```

#### 2.2 Strings (Cadenas de texto)
```python
# Creación de strings
simple = 'Texto con comillas simples'
doble = "Texto con comillas dobles"
triple = '''Texto con
múltiples líneas y
    preservando espacios'''

# Caracteres especiales
especiales = "Salto de línea:\n\tTabulación\n\"Comillas\""

# Métodos de formato avanzado
nombre = "Juan"
edad = 25
# f-strings con formato
print(f"{'Nombre:':<10} {nombre}")  # Alineación izquierda
print(f"{'Edad:':<10} {edad:04d}")  # Padding con ceros
print(f"Pi es {math.pi:.2f}")       # Dos decimales

# Format con nombres
mensaje = "Hola {nombre}, tienes {edad} años".format(
    nombre=nombre,
    edad=edad
)

# Format con posición
pos = "{1} tiene {0} años".format(edad, nombre)

# Format con alineación
tabla = "|{:<10}|{:^10}|{:>10}|".format('izq', 'centro', 'der')

# Métodos de strings avanzados
texto = "  Python Programming  "
print(texto.strip())          # Elimina espacios inicio/fin
print(texto.lstrip())         # Solo elimina espacios inicio
print(texto.rstrip())         # Solo elimina espacios final

# Búsqueda y reemplazo
texto = "Python es genial, Python es poderoso"
print(texto.count("Python"))  # 2
print(texto.find("genial"))   # 9
print(texto.rfind("Python"))  # 22 (busca desde el final)
print(texto.replace("Python", "JavaScript", 1))  # Reemplaza solo la primera ocurrencia

# Partición de strings
email = "usuario@ejemplo.com"
usuario, dominio = email.split('@')
print(texto.partition('es'))  # ('Python ', 'es', ' genial, Python es poderoso')

# Validación de strings
print("ABC123".isalnum())    # True (alfanumérico)
print("ABC".isalpha())       # True (solo letras)
print("123".isdecimal())     # True (solo números decimales)
print("Variable1".isidentifier()) # True (identificador válido)
print("   ".isspace())       # True (solo espacios)
print("Title".istitle())     # True (formato título)
print("MAYÚS".isupper())     # True (todo mayúsculas)
print("minus".islower())     # True (todo minúsculas)

# Codificación y decodificación
texto = "¡Hola, mundo!"
encoded = texto.encode('utf-8')
decoded = encoded.decode('utf-8')

# Unión de strings
palabras = ['Python', 'es', 'genial']
print(" ".join(palabras))    # Python es genial
print("-".join(palabras))    # Python-es-genial
```

#### 2.3 Booleanos y Operadores Lógicos
```python
# Valores booleanos
verdadero = True
falso = False

# Operadores de comparación
x = 5
y = 10
print(x == y)    # Igual a
print(x != y)    # Diferente de
print(x < y)     # Menor que
print(x <= y)    # Menor o igual que
print(x > y)     # Mayor que
print(x >= y)    # Mayor o igual que

# Operadores lógicos
a = True
b = False
print(a and b)   # AND lógico
print(a or b)    # OR lógico
print(not a)     # NOT lógico

# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(lista1 is lista3)      # True
print(lista1 is lista2)      # False
print(lista1 is not lista2)  # True

# Operadores de pertenencia
lista = [1, 2, 3, 4, 5]
print(3 in lista)           # True
print(6 not in lista)       # True

# Evaluación en cortocircuito
x = 5
y = 0
resultado = x != 0 and y/x > 0  # No causa error por división por cero

# Valores que se evalúan como False
print(bool(0))         # False
print(bool(""))        # False
print(bool([]))        # False
print(bool({}))        # False
print(bool(set()))     # False
print(bool(None))      # False

# Valores que se evalúan como True
print(bool(1))         # True
print(bool("texto"))   # True
print(bool([1, 2]))    # True
print(bool({1: 2}))    # True
print(bool({1, 2}))    # True
```

## Parte 2: Estructuras de Datos y Control de Flujo Avanzado

### 1. Estructuras de Datos Avanzadas

#### 1.1 Listas Avanzadas
```python
# Comprensión de listas avanzada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz for num in fila]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Comprensión con múltiples condiciones
números = [x for x in range(50) if x % 2 == 0 if x % 3 == 0]  # Números divisibles por 2 y 3

# Operaciones con listas
lista = [1, 2, 3, 4, 5]
# Slice con paso
print(lista[::2])    # [1, 3, 5]
print(lista[::-1])   # [5, 4, 3, 2, 1]

# Modificación por slice
lista[1:4] = [20, 30, 40]
print(lista)         # [1, 20, 30, 40, 5]

# Métodos avanzados
from collections import deque
cola = deque([1, 2, 3])
cola.append(4)       # Añade al final
cola.appendleft(0)   # Añade al inicio
cola.rotate(1)       # Rota elementos

# Ordenamiento personalizado
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"

personas = [
    Persona("Ana", 25),
    Persona("Juan", 30),
    Persona("María", 20)
]

# Ordenar por edad
personas.sort(key=lambda p: p.edad)
# Ordenar por nombre
personas.sort(key=lambda p: p.nombre)
# Ordenamiento múltiple
personas.sort(key=lambda p: (p.edad, p.nombre))
```

#### 1.2 Tuplas Avanzadas
```python
# Tuplas nombradas
from collections import namedtuple
Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(11, y=22)
print(p.x, p.y)      # 11 22

# Desempaquetado de tuplas
coords = [(1, 2), (3, 4), (5, 6)]
for x, y in coords:
    print(f"X: {x}, Y: {y}")

# Tuplas como claves de diccionario
matriz_dispersa = {
    (0, 0): 1,
    (1, 1): 2,
    (2, 2): 3
}

# Conversión y operaciones
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla + (4, 5))    # (1, 2, 3, 4, 5)
print(tupla * 2)         # (1, 2, 3, 1, 2, 3)
```

#### 1.3 Diccionarios Avanzados
```python
# Diccionarios por comprensión
cuadrados = {x: x**2 for x in range(5)}

# Combinación de diccionarios
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Python 3.5+
combinado = {**dict1, **dict2}
# Python 3.9+
combinado = dict1 | dict2

# DefaultDict
from collections import defaultdict
conteo = defaultdict(int)
palabras = ['manzana', 'pera', 'manzana', 'naranja']
for palabra in palabras:
    conteo[palabra] += 1

# OrderedDict
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

# Counter
from collections import Counter
letras = Counter('mississippi')
print(letras)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Métodos avanzados de diccionarios
d = {'a': 1, 'b': 2, 'c': 3}
# setdefault
valor = d.setdefault('d', 4)  # Obtiene o establece valor por defecto

# update con función
d.update(e=5, f=6)
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# Operaciones atómicas
valor = d.pop('a')      # Elimina y retorna valor
valor = d.popitem()     # Elimina y retorna último par (LIFO)
```

#### 1.4 Sets Avanzados
```python
# Creación de sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Operaciones de conjuntos
unión = set1 | set2             # Unión
intersección = set1 & set2      # Intersección
diferencia = set1 - set2        # Diferencia
diff_sim = set1 ^ set2          # Diferencia simétrica

# Comprensión de sets
vocales = {char for char in "hello world" if char in 'aeiou'}

# Operaciones de subconjuntos
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))    # True
print(b.issuperset(a))  # True
print(a.isdisjoint({4, 5}))  # True (no elementos en común)

# FrozenSet (inmutable)
fs = frozenset([1, 2, 3])

# Operaciones avanzadas
set1.update([6, 7])     # Actualiza con múltiples elementos
set1.intersection_update(set2)  # Actualiza con intersección
set1.difference_update(set2)    # Actualiza con diferencia
```

### 2. Control de Flujo Avanzado

#### 2.1 Bucles con Else
```python
# For con else
def encontrar_número(números, objetivo):
    for n in números:
        if n == objetivo:
            print(f"¡Encontrado {objetivo}!")
            break
    else:
        print(f"No se encontró {objetivo}")

# While con else
def esperar_valor(máximo_intentos):
    intentos = 0
    while intentos < máximo_intentos:
        valor = input("Ingrese un valor: ")
        if valor.lower() == 'salir':
            break
        intentos += 1
    else:
        print("Se agotaron los intentos")
```

#### 2.2 Comprehensions Avanzadas
```python
# Comprehensions anidadas
matriz = [[i+j for j in range(3)] for i in range(3)]
print(matriz)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Comprehensions con múltiples if
números = [x for x in range(100) 
          if x % 2 == 0 
          if x % 3 == 0 
          if x % 5 == 0]

# Dict comprehensions con condiciones
texto = "hello world"
freq = {char: texto.count(char) for char in texto if char != ' '}

# Set comprehensions con funciones
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = {x for x in range(100) if es_primo(x)}
```

#### 2.3 Context Managers
```python
# With statement básico
with open('archivo.txt', 'w') as f:
    f.write('Hola mundo')

# Creando context managers con clases
class MiContextManager:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        print(f"Entrando al contexto {self.nombre}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Saliendo del contexto {self.nombre}")
        if exc_type is not None:
            print(f"Se produjo una excepción: {exc_type}")
        return False  # No suprime excepciones

# Usando contextlib
from contextlib import contextmanager

@contextmanager
def tempdir():
    import tempfile
    import shutil
    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path)

# Múltiples context managers
with open('entrada.txt') as fin, open('salida.txt', 'w') as fout:
    fout.write(fin.read().upper())
```

[Continúa en la siguiente parte...]