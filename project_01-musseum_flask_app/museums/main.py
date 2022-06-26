import datetime
from flask import Flask, render_template,request,jsonify,redirect,url_for, make_response
from flask_login import UserMixin,LoginManager, login_required, login_user,current_user, logout_user
from google.cloud import datastore
import pdfkit
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "admin"
        self.password = "admin"

app = Flask(__name__,template_folder='app/templates/public',static_folder='app/static')
app.config['SECRET_KEY'] = 'best-secret'
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def root():
    client = datastore.Client()  
    query = client.query(kind="Museum")
    result=query.fetch() 
    try:
        list_items=[{"id": item.key.id, "name": item["name"], "location": item["location"], "address": item["address"]} for item in result]
    except:
        list_items=[]
    return render_template("appointment.html",value=list_items,len=len(list_items)) ,200

def max_app(id_museum,new_date):
    client = datastore.Client()  
    query = client.query(kind="Appointment")
    query.add_filter("museum","=",id_museum)
    query.add_filter("date","=",new_date)
    result=query.fetch() 
    c=0
    for a in result:
        c=c+1
    return c>=10

@app.route('/', methods=["POST"])
def post_root():

    new_name=request.form["name"]
    new_location=request.form["start_time"]
    new_address=request.form["stop_time"]
    new_date=request.form["date"]
    new_museum=request.form["museum"]

    client = datastore.Client()
    with client.transaction():
        incomplete_key = client.key("Appointment")
        new_entity = datastore.Entity(key=incomplete_key)
        new_entity.update(
        {
            "museum":new_museum,
            "name": new_name,
            "stat_time": new_location,
            "stop_time": new_address,
            "date": new_date
        }
        )
        if  max_app(new_museum,new_date) :
            return "Too many appointments for today ",401

        t1=datetime.datetime.strptime(new_location, '%H:%M').time() 
        t2=datetime.datetime.strptime(new_address, '%H:%M').time() 
        if t2<t1:
            return "Invalid interval!!",401
            
        client.put(new_entity)
    html = render_template("appointment_result.html")
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response ,200

@app.route('/admin', methods=["POST"])
def login_page():
    user=request.form["user"]
    password=request.form["pass"]
    if (user == "admin" and password == "admin"):
        user = User(1)
        login_user(user)
    return redirect(url_for('login'))

@app.route('/admin', methods=["GET"])
def login():
    return render_template("admin.html",login = current_user.is_authenticated)

@app.route('/admin/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/admin/add',methods=["POST"])
@login_required
def add_musemum():
    new_name=request.form["name"]
    new_location=request.form["location"]
    new_address=request.form["address"]

    client = datastore.Client()
    with client.transaction():
        incomplete_key = client.key("Museum")
        new_entity = datastore.Entity(key=incomplete_key)
        new_entity.update(
        {
            "name": new_name,
            "location": new_location,
            "address": new_address
        }
        )
        client.put(new_entity)
    return render_template("admin_add.html"),200

@app.route('/admin/add',methods=["GET"])
@login_required
def get_musemum():
    return render_template("admin_add.html"),200


@app.route('/admin/delete',methods=["GET"])
@login_required
def delete_musemum():
    client = datastore.Client()  
    query = client.query(kind="Museum")
    result=query.fetch() 
    try:
        list_items=[{"id": item.key.id, "name": item["name"], "location": item["location"], "address": item["address"]} for item in result]
    except:
        list_items=[]
    return render_template("admin_delete.html",value=list_items,len=len(list_items)) ,200

@app.route('/admin/delete', methods=['POST'])
@login_required
def deletemuseum():
    idmuseum=request.form["museum"]
    client = datastore.Client()  
    query = client.query(kind="Museum")
    result=query.fetch() 
    for item in result:
        if str(item.key.id) == str(idmuseum):
            client.delete(client.key("Museum",item.key.id))
            return "Museum deleted ",200
    return "Museum doesn't exist ", 404

@app.route('/admin/edit',methods=['POST'])
@login_required
def updatemuseumbyid():
    idmuseum=request.form["museum"]
    new_name=request.form["name"]
    new_location=request.form["location"]
    new_address=request.form["address"]

    client = datastore.Client()
    query = client.query(kind="Museum")
    result = query.fetch()
    for item in result:
        if str(item.key.id) == str(idmuseum): 
                complete_key = client.key("Museum", item.key.id)
                updated_entity = datastore.Entity(key=complete_key)
                updated_entity.update(
                {
                    "name": new_name,
                    "location": new_location,
                    "address": new_address
                }
                )
                client.put(updated_entity)
                return "Museum updated ",200
    return "Museum doesn't exist ", 404

@app.route('/admin/edit',methods=['GET'])
@login_required
def edit_museumbyid():
    client = datastore.Client()  
    query = client.query(kind="Museum")
    result=query.fetch() 
    try:
        list_items=[{"id": item.key.id, "name": item["name"], "location": item["location"], "address": item["address"]} for item in result]
    except:
        list_items=[]
    return render_template("admin_edit.html",value=list_items,len=len(list_items)) ,200


if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=8080, debug=True)