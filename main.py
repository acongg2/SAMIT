from flask import Flask, jsonify, request
import mysql.connector

# Intitialise the app
app = Flask(__name__)

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="samsat_keliling"
    )

# Create a cursor  
cursor = db.cursor()

# Endpoint Get
@app.get("/api/getSamlingInfo/loc=Bandung")
def getSamlingInfo():
    cursor.execute("SELECT * FROM data_samling WHERE kota_kabupaten like '%Bandung%'")
    return jsonify(cursor.fetchall())
