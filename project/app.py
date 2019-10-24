from flask import Flask, render_template, url_for, request, redirect
from login import my_user

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def homepage():
    return render_template('home.html', user = my_user)

app.run(port=4995)
