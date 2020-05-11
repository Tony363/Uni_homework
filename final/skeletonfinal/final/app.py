# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template, url_for,request

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/",endpoint='index')
def hello():
    version = request.endpoint
    return render_template("jane_doe.html",version=version)

@app.route("/Assignment",endpoint='v1')
@app.route("/Class",endpoint='v2')
def Class():
    version = request.endpoint
    print(type(version))
    return render_template("class.html",version=version)

# @app.route("/Assignment")
# def Assignment():
#     return render_template("assignment.html")

@app.route("/resume")
def test():
    return render_template('index.html')

@app.route("/test1")
def test1():
    return render_template()
#start the server
if __name__ == "__main__":
    app.run()