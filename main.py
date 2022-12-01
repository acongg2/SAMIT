from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bson.json_util as json_util

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@lasti.gi8e0eg.mongodb.net/Samsat_Keliling")
db = client["BAPENDA"]

def parse_json(data):
    return json_util.dumps(data)

@app.route('/Samling', methods=["GET"])
def get_data():
    collection = client["BAPENDA"]["Samsat_Keliling"]
    datas = []
    for data in collection.find({}):
        datas.append(data)
    return parse_json(datas)
    client.close()


if __name__ == '__main__':
    app.run()


# db=client["BAPENDA"]
# db=client["Samsat Keliling"]

# if request.method == 'READ':
#         data = list(collection.find())
#         return Response(jsonify(data))