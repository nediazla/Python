
## 📊 Tipos de Datos en MySQL

### 🔢 Numéricos

| Tipo            | Descripción                      | Ejemplo               |
| --------------- | -------------------------------- | --------------------- |
| `INT`           | Entero (±2,147,483,647)          | `edad INT`            |
| `TINYINT`       | Entero pequeño (±127)            | `activo TINYINT(1)`   |
| `SMALLINT`      | Entero pequeño (±32,767)         | `puntuación SMALLINT` |
| `BIGINT`        | Entero grande                    | `saldo BIGINT`        |
| `DECIMAL(10,2)` | Números decimales precisos       | `precio DECIMAL(8,2)` |
| `FLOAT`         | Números decimales menos precisos | `promedio FLOAT`      |

---

### 📜 Texto

| Tipo         | Descripción                           | Ejemplo               |
| ------------ | ------------------------------------- | --------------------- |
| `VARCHAR(n)` | Cadena variable hasta `n` caracteres  | `nombre VARCHAR(100)` |
| `CHAR(n)`    | Cadena fija de `n` caracteres         | `codigo CHAR(5)`      |
| `TEXT`       | Texto largo (hasta 65,535 caracteres) | `comentarios TEXT`    |

---

### 📅 Fechas y Tiempos

| Tipo        | Descripción                        | Ejemplo                |
| ----------- | ---------------------------------- | ---------------------- |
| `DATE`      | Fecha (YYYY-MM-DD)                 | `nacimiento DATE`      |
| `TIME`      | Hora (HH:MM:SS)                    | `hora_ingreso TIME`    |
| `DATETIME`  | Fecha y hora (YYYY-MM-DD HH:MM:SS) | `fecha DATETIME`       |
| `TIMESTAMP` | Fecha y hora con zona horaria      | `registrado TIMESTAMP` |
| `YEAR`      | Año (YYYY)                         | `año YEAR`             |

---

### 🆔 Identificadores y Booleans

| Tipo      | Descripción                                      | Ejemplo                             |
| --------- | ------------------------------------------------ | ----------------------------------- |
| `BOOLEAN` | Alias de `TINYINT(1)` (0 = falso, 1 = verdadero) | `activo BOOLEAN`                    |
| `ENUM`    | Lista de valores permitidos                      | `estado ENUM('activo', 'inactivo')` |