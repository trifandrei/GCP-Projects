import datetime
from flask import Flask, render_template
import os


app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')


imgFolder=os.path.join('static','img')
app.config['UPLOAD_FOLDER']= imgFolder

@app.route('/')
def root():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'hotel.jpg')
    return render_template("homepage.html", user_image=pic1)


@app.route('/prices')
def prices():
    return render_template("prices.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)