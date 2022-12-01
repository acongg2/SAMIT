from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@lasti.gi8e0eg.mongodb.net/?retryWrites=true&w=majority")
db = client["BAPENDA"]

@app.route('/Samling', methods=["GET"])
def get_data():
    data = client["BAPENDA"]["Samsat Keliling"]
    records = data.find({})
    json_obj = json.dumps(records)
    return jsonify(json_obj)
    client.close()


if __name__ == '__main__':
    app.run()


# db=client["BAPENDA"]
# db=client["Samsat Keliling"]

# if request.method == 'READ':
#         data = list(collection.find())
#         return Response(jsonify(data))