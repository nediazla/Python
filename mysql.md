## Introducción a MySQL 
A nivel teórico, existen 3 lenguajes para el manejo de bases de datos: DDL (Data Definition Language) Que es el lenguaje de definición de datos. Es el lenguaje que se usa para crear bases de datos y tablas, y para modificar sus estructuras, así como los permisos y privilegios. 
Este lenguaje trabaja sobre unas tablas especiales llamadas diccionario de datos. 

DML (Data Manipulation Language) que es el lenguaje de manipulación de datos. Es el que se usa para modificar y obtener datos desde las bases de datos. 

DCL (Data Control Language) que es el lenguaje de control de datos, que incluye una serie de comandos que permiten al administrador controlar el acceso a los datos contenidos en la base de datos. 

A continuación vamos a ver las instrucciones más básicas en MySQL divididas en secciones. Pero antes de empezar te enseñaremos 2 auxiliares que te vendrán bien para comprobar los resultados de lo que vayas haciendo; 

`SELECT * FROM nombretabla;` se usa para ver el resultado de una tabla con todos sus registros. 
`DESCRIBE nombretabla;` se usa para ver la estructura de una tabla.

## Crear una base de datos

`CREATE DATABASE;` 
`SHOW DATABASES;` 
`USE prueba;` 

Desde el punto de vista de SQL, una base de datos es sólo un conjunto de relaciones (o tablas). A nivel de sistema operativo, cada base de datos se guarda en un directorio diferente. 
Por tanto, crear una base de datos es una tarea muy simple. Claro que, en el momento de crearla, la base de datos estará vacía, es decir, no contendrá ninguna tabla. 
Para crear una base de datos se usa una sentencia CREATE DATABASE:

```mysql
mysql>CREATE DATABASE prueba;
Query OK, 1 row affected (0.03 sec)
```

Para saber cuántas bases de datos existen en nuestro sistema usamos la sentencia SHOW DATABASES:

```mysql
mysql>SHOW DATABASES; 
+--------------------+ 
| Database           | 
+--------------------+ 
| mysql              | 
| prueba             | 
| test               | 
+--------------------+ 
3 rows in set (0.00 sec)
```

A partir de ahora, en los próximos capítulos, trabajaremos con esta base de datos, por lo tanto la seleccionaremos como base de datos por defecto.. Para seleccionar una base de datos concreta se usa el comando USE que no es exactamente una sentencia SQL, sino más bien de una opción de MySQL. Esto nos permitirá obviar el nombre de la base de datos en consultas:

```mysql
mysql>USE prueba; 
Database changed
```

## Crear una tabla 

`CREATE TABLE … `
`SHOW TABLES; `

Veamos ahora la sentencia CREATE TABLE que sirve para crear tablas. La sintaxis de esta sentencia es muy compleja, pero empezaremos con ejemplos sencillos. 
En su forma más simple, la sentencia CREATE TABLE creará una tabla con las columnas que indiquemos. Crearemos, como ejemplo, una tabla que nos permitirá almacenar nombres de personas y sus fechas de nacimiento. Deberemos indicar el nombre de la tabla y los nombres y tipos de las columnas:

```mysql
mysql> USE prueba 
Database changed 
mysql>CREATE TABLE gente (nombre VARCHAR(40), fecha DATE); 
Query OK, 0 rows affected (0.53 sec)
```

