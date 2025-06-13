from flask import Flask,make_response
from flask_migrate import Migrate
from models import db,User,Task

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///task.db"

# save on memory avoid building up too much data
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# iniatialize the db(connect db to app)
db.init_app(app)

migration = Migrate(app,db)

@app.route('/')
def index():
    response = make_response(
        '<h1>Welcome to the Tasks directory</h1>',200
    )
    return response

# get the user by id
@app.route('/users/<int:id>')
def user_by_name(id):
    user = User.query.filter(User.id== 
    id).first()

# returning the message as a json by turning the object to a dictionary
    if user:
       response_body = {
           "id":user.id,
           "name":user.name,
           "email":user.email
           
           }
       response_status = 200
    else:
        response_body = f"<p>User {user} Not found</p>"   
        response_status = 404
    response = make_response(response_body,response_status)
    return response

@app.route('/tasks/<string:title>')
def get_task_by_title(title):
    task = Task.query.filter(Task == title)

    if task:
        response_body = f"<h1>This is your task{task.name}</h1>"
        response_status = 200
    else:
        response_body = f"<p>{title} Not found</p>"
        response_status = 404
    response = make_response(response_body,response_status)
    return        

if __name__ =="__main__":
    app.run(port=5555,debug=True)
