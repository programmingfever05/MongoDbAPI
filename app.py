from flask_pymongo import PyMongo
import flask
import pymongo
import dns
from flask import request
import os

app = flask.Flask(__name__)

@app.route("/get_file_data/<filename>", methods = ["GET","POST"])
def getData(filename):
    
    if filename.split(".")[1] == "yml" or filename.split(".")[1] == "html":
        directory = os.getcwd()
        file = directory +"\\"+ filename

        with open(file) as f:
            data = f.read()
            
            return data
    else:
        return "Please select yml or jinja file."

if __name__ == "__main__":
    app.run(debug=True)
