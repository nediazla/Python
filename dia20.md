# Dia 20 - Virtual Environments

## Setting up Virtual Environments

Para comenzar un proyecto, sería recomendable tener un entorno virtual. Este nos permite crear un entorno aislado o independiente. Esto nos ayudará a evitar conflictos de dependencias entre proyectos. Si escribes "pip freeze" en tu terminal, verás todos los paquetes instalados en tu ordenador. Si usamos virtualenv, accederemos solo a los paquetes específicos de ese proyecto. Abre tu terminal e instala virtualenv.

```sh
xnoxos@ubuntu:~$ pip install virtualenv
```

Dentro de la carpeta ClassOfPython, crea la carpeta flask_project.

Después de instalar el paquete virtualenv, ve a la carpeta de tu proyecto y crea un entorno virtual escribiendo:

Para Mac/Linux:
```bash
xnoxos@ubuntu:~/Desktop/ClassOfPython/flask_project\$ virtualenv venv
```

Para Windows:
```sh
C:\Users\User\Documents\ClassOfPython\flask_project>python -m venv venv
```

Prefiero llamar al nuevo proyecto venv, pero puedes darle otro nombre. Comprobemos si el venv se creó usando el comando ls (o dir para el símbolo del sistema de Windows).

```sh
xnoxos@ubuntu:~/Desktop/ClassOfPython/flask_project$ ls
venv/
```

Para Mac/Linux:
```sh
xnoxos@ubuntu:~/Desktop/ClassOfPython/flask_project$ source venv/bin/activate
```

La activación del entorno virtual en Windows puede variar en Windows Power Shell y Git Bash.

Para Windows Power Shell:
```sh
C:\Users\User\Documents\ClasssOfPython\flask_project> venv\Scripts\activate
```

Para Windows Git bash:
```sh
C:\Users\User\Documents\ClassOfPython\flask_project> venv\Scripts\. activate
```

Después de escribir el comando de activación, el directorio de su proyecto comenzará con venv. Vea el ejemplo a continuación.

```sh
(venv) xnoxos@ubuntu:~/Desktop/ClassOfPython/flask_project$
```

Ahora, revisemos los paquetes disponibles en este proyecto escribiendo pip freeze. No verá ningún paquete.

Vamos a crear un pequeño proyecto Flask, así que instalemos el paquete Flask.

```sh
(venv) xnoxos@ubuntu:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

Ahora, escribamos pip freeze para ver una lista de paquetes instalados en el proyecto:

```sh
(venv) xnoxos@ubuntu:~/Desktop/ClassOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

Al terminar deberás desactivar el proyecto activo utilizando _desactivate_.

```sh
(venv) xnoxos@ubuntu:~/Desktop/ClassOfPython$ deactivate
```


Los módulos necesarios para trabajar con Flask están instalados. Ahora, tu directorio de proyecto está listo para un proyecto Flask. Debes incluir el archivo venv en tu archivo .gitignore para no subirlo a GitHub.

## 💻 Ejercicios: Día 20

1. Crea un directorio de proyecto con un entorno virtual basado en el ejemplo anterior.

🎉 ¡FELICIDADES! 🎉