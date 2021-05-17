# Put your app in here.
import operations as ops
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def calc_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(ops.add(a,b))

@app.route('/sub')
def calc_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(ops.sub(a,b))

@app.route('/mult')
def calc_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(ops.mult(a,b))

@app.route('/div')
def calc_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(ops.div(a,b))


# Single Route code
funcs = {"add": ops.add, "sub": ops.sub, "mult": ops.mult, "div": ops.div}

@app.route('/math/<operation>')
def calc_val(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(funcs[operation](a,b))