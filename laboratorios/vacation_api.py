# 📦 Importamos librerías necesarias
from flask import Flask, request, jsonify, Response
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os
from dotenv import load_dotenv  # <-- IMPORTANTE

load_dotenv()  # <-- Carga las variables desde .env

# 🔐 URI de MongoDB tomada de la variable de entorno
MONGODB_URI = os.environ.get("MONGODB_URI")

client = pymongo.MongoClient(MONGODB_URI)
db = client["vacation_db"]
destinos = db.destinos

# 🏠 Ruta principal para probar si la API funciona
@app.route('/')
def index():
    return jsonify({"message": "Bienvenido a la API de destinos turísticos"}), 200

# 📖 GET - Obtener todos los destinos
@app.route('/api/v1/destinos', methods=['GET'])
def obtener_destinos():
    datos = list(destinos.find())
    return Response(dumps(datos), mimetype="application/json")

# 🔍 GET - Obtener un destino por ID
@app.route('/api/v1/destinos/<id>', methods=['GET'])
def obtener_destino(id):
    destino = destinos.find_one({"_id": ObjectId(id)})
    if destino:
        return Response(dumps(destino), mimetype="application/json")
    return jsonify({"error": "Destino no encontrado"}), 404

# ➕ POST - Agregar un nuevo destino
@app.route('/api/v1/destinos', methods=['POST'])
def agregar_destino():
    data = request.get_json()
    data['created_at'] = datetime.now()
    result = destinos.insert_one(data)
    return jsonify({"message": "Destino agregado", "id": str(result.inserted_id)}), 201

# ✏️ PUT - Editar un destino
@app.route('/api/v1/destinos/<id>', methods=['PUT'])
def editar_destino(id):
    data = request.get_json()
    result = destinos.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.modified_count:
        return jsonify({"message": "Destino actualizado"})
    return jsonify({"error": "Destino no encontrado o sin cambios"}), 404

# ❌ DELETE - Eliminar un destino
@app.route('/api/v1/destinos/<id>', methods=['DELETE'])
def eliminar_destino(id):
    result = destinos.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "Destino eliminado"})
    return jsonify({"error": "Destino no encontrado"}), 404

# ▶️ Iniciar la app Flask
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render y Replit usan PORT automático
    app.run(debug=True, host='0.0.0.0', port=port)
