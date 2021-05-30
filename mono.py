# Testing heroku deployment
from os import device_encoding, name
from typing import ItemsView
from flask import Flask
from datetime import datetime
from flask import render_template,request, redirect, url_for

# custom modules
from insertpc import *
from amazon import *


data= []
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/reviews',methods = ['POST','GET'])
def reviews():
    devdata = []
    if request.method == 'POST':
        name = request.form["dn"]
        asin = request.form["asn"]
        ram = request.form["ram"]
        rom = request.form["rom"]
        color = request.form["color"]
        # devdata = [{'name':name,'asin':asin,'ram':ram,'rom':rom,'color':color}]
        devdata.append(str(name))
        devdata.append(str(asin))
        devdata.append(int(ram))
        devdata.append(int(rom))
        devdata.append(str(color))
        # return redirect(url_for("device", data = devdata))
        # this pass the value of the return element to the device page
        return redirect(url_for("device",data = dbinsert(devdata)))
    elif request.method == 'GET':
        return render_template("reviews.html")

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        devicecode = request.form["pc"]
        data = (user,devicecode)
        return redirect(url_for("device",ddata=data))
        # return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/<data>")
def device(data):
    return render_template("device.html",data = data)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}!"

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("admin",name="Mono!"))



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)