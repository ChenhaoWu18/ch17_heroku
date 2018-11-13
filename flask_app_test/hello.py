#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 12:02:37 2018

@author: wuchenhao
"""
####**********
##task1
########******
#from flask import Flask
#app = Flask("MyApp")
#
#@app.route("/")
#def hello():
#    return "Hello World using flask"
#
#app.run(debug=True)

####**********
##task1_new page
########******
#from flask import Flask
#app = Flask("MyApp")
#
#@app.route("/bio")
#def hello():
#    return "Hello World using flask"
#
#app.run(debug=True)

####**********
##task2
########******
#from flask import Flask, render_template
#
#app = Flask("MyApp")
#
#@app.route("/bio")
#def hello():
#    return "Hello World using flask"
#
#app.run(debug=True)

####**********
##task4
########******
#from flask import Flask, render_template
#
#app = Flask("MyApp")
#
#@app.route("/")
#
#def hello():
#    return "Hello World using flask"
#
#@app.route("/<name>")
#
#def hello_someone(name):
#		return render_template("hello.html", name=name.title())
#
#app.run(debug=True)

####**********
##task5
########******
from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")

def hello():
    return "Hello World using flask"

@app.route("/<name>")

def hello_someone(name):
		return render_template("hello_2.html", name=name.title())
    
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print (form_data["email"])
    return "All OK"

app.run(debug=True)

