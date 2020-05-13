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
    return render_template("intro.html",version=version)

@app.route("/Description")
def Description():
    return render_template('description.html')

@app.route("/Portfolio")
def Portfolio():
    return render_template("portfolio.html")
#start the server
if __name__ == "__main__":
    app.run()