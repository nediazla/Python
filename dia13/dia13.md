# Dia 13: python datetime

## Python *datetime*

Python tiene un módulo *datetime* para gestionar la fecha y la hora.

```python
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

Con los comandos integrados dir o help es posible conocer las funciones disponibles en un determinado módulo. Como puedes ver, en el módulo datetime hay muchas funciones, pero nos centraremos en *date*, *datetime*, *time* y *timedelta*. Veámoslas una por una.

### Obtener información de *datetime*

```python
from datetime import datetime

# Obtener la fecha y hora actual
now = datetime.now()

# Asignar los componentes de la fecha y hora a variables individuales
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

# Obtener el timestamp (segundos desde el 1 de enero de 1970)
timestamp = now.timestamp()

# Mostrar los resultados
print(day, month, year, hour, minute)
print('timestamp', timestamp)

# Mostrar la fecha en formato personalizado
print(f'{day}/{month}/{year}, {hour}:{minute}')  # Ejemplo: 8/7/2021, 7:38

```

La marca de tiempo o marca de tiempo Unix es la cantidad de segundos transcurridos desde el 1 de enero de 1970 UTC.

### Formato de la salida de fecha con *strftime*

```python
from datetime import datetime

# Crear un objeto datetime para el 1 de enero de 2020
new_year = datetime(2020, 1, 1)

# Obtener los componentes individuales de la fecha y hora
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second

# Mostrar los valores de los componentes
print(day, month, year, hour, minute)  # 1 1 2020 0 0

# Mostrar la fecha en un formato personalizado
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

```

El formato de fecha y hora mediante el método strftime y la documentación se pueden encontrar [aquí](https://strftime.org/).

```python
from datetime import datetime

# Obtener la fecha y hora actuales
now = datetime.now()

# Formatear la hora actual
t = now.strftime("%H:%M:%S")
print("time:", t)

# Formatear la fecha y hora en formato mm/dd/YY H:M:S
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)

# Formatear la fecha y hora en formato dd/mm/YY H:M:S
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)

```

Aquí se encuentran todos los símbolos de tiempo que utilizamos para dar formato a la hora. Un ejemplo de todos los formatos de este módulo

![](30-Days-Of-Pythonimagesstrftime.png)

## strftime

### Convertir una cadena en hora con *strptime*

A continuación, se incluye una [documentación](https://www.programiz.com/python-programming/datetime/strptimet) que ayuda a comprender el formato.

```python
from datetime import datetime

# Definir la cadena de fecha
date_string = "5 December, 2019"
print("date_string =", date_string)

# Convertir la cadena a un objeto datetime usando strptime
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

```

### Usando la fecha de datetime

```python
from datetime import date

# Crear un objeto de fecha con el 1 de enero de 2020
d = date(2020, 1, 1)
print(d)

# Obtener la fecha actual usando la función today()
print('Current date:', d.today())  # Esto debería ser '2023-02-23' (dependiendo de la fecha en la que lo ejecutes)

# Crear un objeto de fecha con la fecha actual
today = date.today()

# Mostrar el año, mes y día de la fecha actual
print("Current year:", today.year)    # Ejemplo: 2023
print("Current month:", today.month)  # Ejemplo: 2
print("Current day:", today.day)      # Ejemplo: 23

```

### Objetos de tiempo para representar el tiempo

```python
from datetime import time

# Crear un objeto time con los valores predeterminados (hora=0, minuto=0, segundo=0)
a = time()
print("a =", a)

# Crear un objeto time con hora, minuto y segundo específicos
b = time(10, 30, 50)
print("b =", b)

# Crear un objeto time usando parámetros con nombre
c = time(hour=10, minute=30, second=50)
print("c =", c)

# Crear un objeto time con hora, minuto, segundo y microsegundo
d = time(10, 30, 50, 200555)
print("d =", d)
```

### Diferencia entre dos puntos en el tiempo usando

```python
from datetime import date, datetime

# Definir la fecha de hoy y la del Año Nuevo
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)

# Calcular la diferencia entre las dos fechas
time_left_for_newyear = new_year - today
print('Time left for new year:', time_left_for_newyear)  # 27 days, 0:00:00

# Definir las fechas y horas específicas (incluyendo la hora)
t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)

# Calcular la diferencia entre las dos fechas y horas
diff = t2 - t1
print('Time left for new year:', diff)  # 26 days, 23:01:00
```

### Diferencia entre dos puntos en el tiempo usando timedelta

```python
from datetime import timedelta

# Crear dos objetos timedelta con diferentes valores
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)

# Calcular la diferencia entre t1 y t2
t3 = t1 - t2

# Imprimir el resultado
print("t3 =", t3)

```

🌕 Eres extraordinario. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 13

1. Obtén el día, mes, año, hora, minuto y marca de tiempo actuales del módulo datetime
2. Formatea la fecha actual con este formato: “%m/%d/%Y, %H:%M:%S”)
3. Hoy es 5 de diciembre de 2019. Cambia esta cadena de tiempo a time.
4. Calcula la diferencia horaria entre ahora y el año nuevo.
5. Calcula la diferencia horaria entre el 1 de enero de 1970 y ahora.
6. Piensa, ¿para qué puedes usar el módulo datetime? Ejemplos:
- Análisis de series temporales
- Para obtener una marca de tiempo de cualquier actividad en una aplicación
- Agregar publicaciones en un blog

🎉 ¡FELICITACIONES! 🎉

[Tareas](tareas.py)