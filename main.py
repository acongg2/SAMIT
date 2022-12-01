from flask import Flask, render_template
from pymongo import MongoClient
import bson.json_util as json_util

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@lasti.gi8e0eg.mongodb.net/Samsat_Keliling")
db = client["BAPENDA"]

def parse_json(data):
    return json_util.dumps(data)

@app.route('/api/Samling', methods=["GET"])
def get_data():
    collection = client["BAPENDA"]["Samsat_Keliling"]
    datas = []
    for data in collection.find({}):
        datas.append(data)
    return parse_json(datas)


if __name__ == '__main__':
    app.run()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/samling')
def samling():
    return render_template('./pages/samling.html')