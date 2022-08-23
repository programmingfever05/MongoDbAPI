from flask_pymongo import PyMongo
import flask
import pymongo
import dns
from flask import request
import os

app = flask.Flask(__name__)

@app.route("/get_yml_file/<filename>", methods = ["GET","POST"])
def get_yml_file(filename):
    
    if filename.split(".")[1] != "yml":
        return "Please select yml file."
    else:
        directory = os.getcwd()
        file = directory +"\\"+ filename

        with open(file) as f:
            data = f.read()
            
            return data

@app.route("/get_jinja_file/<filename>", methods = ["GET","POST"])
def get_jinja_file(filename):
    
    if filename.split(".")[1] != "html":
        return "Please select jinja file."
    else:
        directory = os.getcwd()
        file = directory +"\\"+ filename

        with open(file) as f:
            data = f.read()
            
            return data

if __name__ == "__main__":
    app.run(debug=True)
