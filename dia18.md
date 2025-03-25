# Dia 18:clases y objetos

## Clases y objetos

Python es un lenguaje de programación orientado a objetos. Todo en Python es un objeto, con sus propiedades y métodos. Un número, cadena, lista, diccionario, tupla, conjunto, etc. utilizado en un programa es un objeto de una clase incorporada correspondiente. Creamos una clase para crear un objeto. Una clase es como un constructor de objetos, o un "plano" para crear objetos. Instanciamos una clase para crear un objeto. La clase define los atributos y el comportamiento del objeto, mientras que el objeto, por su parte, representa a la clase.

Hemos estado trabajando con clases y objetos desde el principio de este reto sin saberlo. Cada elemento en un programa Python es un objeto de una clase. Comprobemos si todo en python es una clase:

```python
xnoxos@ubuntu:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### Crear una clase

Para crear una clase necesitamos la palabra clave **class** seguida del nombre y dos puntos. El nombre de la clase debe ser **CamelCase**.

```bash
# syntaxclass ClassName:
  code goes here
```

**Ejemplo:**

```python
class Person:
  passprint(Person)
```

```bash
<__main__.Person object at 0x10804e510>
```

### Crear un objeto

Podemos crear un objeto llamando a la clase.

```python
p = Person()
print(p)
```

### Constructor de clase

En los ejemplos anteriores, hemos creado un objeto a partir de la clase Persona. Sin embargo, una clase sin constructor no es realmente útil en aplicaciones reales. Usemos la función constructor para hacer nuestra clase más útil. Al igual que la función constructora en Java o JavaScript, Python también tiene una función constructora **init**() incorporada. La función constructora **init** tiene el parámetro self que es una referencia a la instancia actual de la clase**Examples:**

```python
class Person:
    def __init__(self, name):
        # self permite asociar el parámetro con la clase
        self.name = name  # Asigna el valor del parámetro 'name' al atributo 'name' de la instancia

# Crear una instancia de la clase Person con el nombre 'Nelson'
p = Person('Nelson')

# Imprimir el atributo 'name' de la instancia 'p'
print(p.name)

# Imprimir la representación por defecto de la instancia 'p'
print(p)
```

Añadamos más parámetros a la función constructora.

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        # Inicializa los atributos de la clase con los valores pasados
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

# Crear una instancia de la clase Person con valores específicos
p = Person('Nelson', 'Diaz', 250, 'Finland', 'Helsinki')

# Imprimir los atributos de la instancia 'p'
print(p.firstname)  # Imprime: Nelson
print(p.lastname)   # Imprime: Diaz
print(p.age)        # Imprime: 250
print(p.country)    # Imprime: Finland
print(p.city)       # Imprime: Helsinki
```

### Métodos de Objeto

Los objetos pueden tener métodos. Los métodos son funciones que pertenecen al objeto.

**Ejemplo:**

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

# Crear una instancia de la clase Person
p = Person('Nelson', 'Diaz', 250, 'Finland', 'Helsinki')

# Imprimir la información de la persona usando el método 'person_info'
print(p.person_info())
```

### Métodos por defecto de objetos

Algunas veces, puedes querer tener valores por defecto para los métodos de tus objetos. Si damos valores por defecto para los parámetros en el constructor, podemos evitar errores cuando llamamos o instanciamos nuestra clase sin parámetros. Veamos como se ve:

**Ejemplo:**

```python
class Person:
    def __init__(self, firstname='Nelson', lastname='Diaz', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

# Crear una instancia con los valores predeterminados
p1 = Person()
print(p1.person_info())

# Crear una instancia con valores personalizados
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

```

### Método para Modificar los Valores por Defecto de una Clase

En el siguiente ejemplo, la clase persona, todos los parámetros del constructor tienen valores por defecto. Además tenemos el parámetro skills, al que podemos acceder mediante un método. Creemos el método add_skill para añadir habilidades a la lista de habilidades.

```python
class Person:
    def __init__(self, firstname='Nelson', lastname='Diaz', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []  # Lista para almacenar las habilidades de la persona

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)  # Añade una habilidad a la lista de habilidades

# Crear una instancia con los valores predeterminados
p1 = Person()
print(p1.person_info())

# Agregar habilidades a p1
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')

# Crear una instancia con valores personalizados
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

# Imprimir las habilidades de cada persona
print(p1.skills)  # Imprimirá las habilidades de p1
print(p2.skills)  # Imprimirá las habilidades de p2 (vacío por ahora)
```

### Herencia

Usando la herencia podemos reutilizar el código de la clase padre. La herencia nos permite definir una clase que hereda todos los métodos y propiedades de la clase padre. La clase padre o super o clase base es la clase que da todos los métodos y propiedades. La clase hija es la clase que hereda de otra o clase padre. Creemos una clase estudiante heredando de la clase persona.

```python
class Person:
    def __init__(self, firstname='Nelson', lastname='Diaz', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []  # Lista para almacenar las habilidades de la persona

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)  # Añade una habilidad a la lista de habilidades

# Clase Student que hereda de Person
class Student(Person):
    pass  # La clase Student hereda todos los métodos y atributos de Person

# Crear instancias de Student
s1 = Student('Eyob', 'Diaz', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')

# Imprimir la información de s1
print(s1.person_info())

# Agregar habilidades a s1
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')

# Imprimir las habilidades de s1
print(s1.skills)

# Imprimir la información de s2
print(s2.person_info())

# Agregar habilidades a s2
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')

# Imprimir las habilidades de s2
print(s2.skills)
```

No llamamos al constructor **init**() en la clase hija. Si no lo llamamos entonces todavía podemos acceder a todas las propiedades de la clase padre. Pero si llamamos al constructor podemos acceder a las propiedades del padre llamando a *super*.

Podemos añadir un nuevo método a la clase hija o podemos sobreescribir los métodos de la clase padre creando el mismo nombre de método en la clase hija. Cuando añadimos la función **init**(), la clase hija ya no heredará la función **init**() de la clase padre.

### Sobreescribir el método padre

```python
class Person:
    def __init__(self, firstname='Nelson', lastname='Diaz', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []  # Lista para almacenar las habilidades de la persona

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)  # Añade una habilidad a la lista de habilidades

# Clase Student que hereda de Person
class Student(Person):
    def __init__(self, firstname='Nelson', lastname='Diaz', age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        # No redefinimos la variable gender dentro del método
        pronoun = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {pronoun} lives in {self.city}, {self.country}.'

# Crear instancias de Student
s1 = Student('Eyob', 'Diaz', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')

# Imprimir la información de s1
print(s1.person_info())

# Agregar habilidades a s1
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')

# Imprimir las habilidades de s1
print(s1.skills)

# Imprimir la información de s2
print(s2.person_info())

# Agregar habilidades a s2
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')

# Imprimir las habilidades de s2
print(s2.skills)
```

Podemos utilizar la función incorporada super() o el nombre del padre Persona para heredar automáticamente los métodos y propiedades de su padre. En el ejemplo anterior anulamos el método padre. El método hijo tiene una característica diferente, puede identificar, si el género es masculino o femenino y asignar el pronombre apropiado(He/She).

🌕 Ahora, usted está completamente cargado con un super poder de programación. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 18

### Ejercicios: Nivel 1

1. Python tiene el módulo llamado *estadística* y podemos usar este módulo para hacer todos los cálculos estadísticos. Sin embargo, para aprender a hacer función y reutilizar función vamos a intentar desarrollar un programa, que calcule la medida de tendencia central de una muestra (media, mediana, moda) y medida de variabilidad (rango, varianza, desviación típica). Además de esas medidas, encuentre el mínimo, máximo, recuento, percentil y distribución de frecuencias de la muestra. Puedes crear una clase llamada Estadística y crear todas las funciones que hacen cálculos estadísticos como métodos para la clase Estadística. Comprueba la salida más abajo.

```python
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```bash
# you output should look like thisprint(data.describe())Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### Ejercicios: Nivel 2

1. Cree una clase llamada CuentaPersona. Tiene las propiedades nombre, apellidos, ingresos, gastos y los métodos total_ingresos, total_gastos, información_cuenta, añadir_ingresos, añadir_gastos y saldo_cuenta. Ingresos es un conjunto de ingresos y su descripción. Lo mismo ocurre con los gastos.

🎉 ¡ENHORABUENA! 🎉

[Tetris](laboratorios/tetris.py)