from flask import Flask,make_response,jsonify
from flask_migrate import Migrate
from models import db,User,Task
from dotenv import load_dotenv


app = Flask(__name__)
app.config.from_prefixed_env()

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
def user_by_id(id):
    user = User.query.filter(User.id== 
    id).first()

# returning the message as a json by turning the object to a dictionary
# changed to use serializer wich is automatic
    if user:
       response_body = user.to_dict()
       response_status = 200
    else:
        response_body = f"<p>User {user} Not found</p>"   
        response_status = 404
    response = make_response(response_body,response_status)
    return response

@app.route('/tasks/<string:title>')
def get_task_by_title(title):
    task = Task.query.filter_by(title=title).all()

    if task:
        response_body = [t.to_dict() for t in task]
        response_status = 200
    else:
        response_body = {'message':f'Task with title"{title}" not found'}
        response_status = 404
    response = make_response(response_body,response_status)
    return response

if __name__ =="__main__":
    app.run(port=5555,debug=True)
