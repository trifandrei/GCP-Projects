import datetime
from flask import Flask, render_template
import os


app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')



@app.route('/')
def root():
    return ""


@app.route('/hello_to_training/<name>')
def hello(name):
    return render_template("index.html", value=str(name.capitalize()))

if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)