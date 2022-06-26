from flask import Flask, render_template


app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')


@app.route('/')
def root():
    return "hi"


if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)