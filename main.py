# from typing import Optional
# from fastapi import FastAPI, Depends, HTTPException, status, Response, Request, status
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# from fastapi.security import OAuth2PasswordRequestForm
# import mysql.connector
# from pymongo import MongoClient

# # Intitialise the app
# app = FastAPI()

# mongodb_URI = 'mongodb+srv://admin:admin@lasti.gi8e0eg.mongodb.net/?retryWrites=true&w=majority'
# port = 3306
# client = MongoClient(mongodb_URI, port)
# db = client["User"]

# @app.get("/api/getSamlingInfo/loc=Bandung")
# async def getSamlingInfo():
#     mycol = db["BAPENDA"]
#     myquery = { "location": "Bandung" }
#     mydoc = mycol.find(myquery)
#     for x in mydoc:
#         return x


from flask import Flask, jsonify, render_template, request, Response, redirect, url_for
from flask_pymongo import PyMongo
import bson

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Lasti"
mongo = PyMongo(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/api/getSamlingInfo/loc=Bandung")
def getSamlingInfo():
    mycol = mongo.db.BAPENDA
    myquery = { "location": "Bandung" }
    mydoc = mycol.find(myquery
    for x in mydoc:
        return x


# @app.route('/')
# def home():
#     return render_template('home.html')

# if __name__ == '__main__':
#     app.run(debug=False)

# db=client["BAPENDA"]
# db=client["Samsat Keliling"]

# if request.method == 'READ':
#         data = list(collection.find())
#         return Response(jsonify(data))