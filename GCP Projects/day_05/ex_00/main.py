from flask import Flask, render_template
import os


app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')

imgFolder=os.path.join('static','img')
app.config['UPLOAD_FOLDER']= imgFolder

@app.route('/')
def root():
    return ""


@app.route('/hello_to_training')
def hello():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'],'cat1.png')
    return render_template("index.html", user_image=pic1)

if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)