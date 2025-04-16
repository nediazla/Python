# 🌴 API de Destinos Turísticos

API RESTful desarrollada con Flask + MongoDB para registrar y consultar lugares para vacacionar.

## 🧪 Rutas disponibles

- `GET /api/v1/destinos`
- `GET /api/v1/destinos/<id>`
- `POST /api/v1/destinos`
- `PUT /api/v1/destinos/<id>`
- `DELETE /api/v1/destinos/<id>`

## 🚀 Cómo ejecutar localmente

1. Instala dependencias:
```bash
pip install -r requirements.txt
```

2. Crea un archivo `.env` o define la variable de entorno `MONGODB_URI`.

3. Ejecutá la API:
```bash
python vacation_api.py
```

## 🌐 Despliegue en Replit o Render

- Usá `MONGODB_URI` como variable de entorno.
- Comando de inicio: `python vacation_api.py`
