from app import app
from models import db,User,Task



with app.app_context():
    # clear existing data
    Task.query.delete()
    User.query.delete()
    db.session.commit()
    # create an empty list 
    users = []
    tasks= []
    # add user instances to the list
    users.append(User(name = "karanja",email = "karanja@gmail.com")) 
    users.append(User(name = "Martin",email = "Martin@gmail.com"))
    users.append(User(name = "Bradley",email = "Bradley@gmail.com"))

    # add task instances
    tasks.append(Task(title="rent",description="pay rent "))
    tasks.append(Task(title="fees",description="pay fees "))
    tasks.append(Task(title="tokens",description="pay power"))
    
    # add the users in the list 
    db.session.add_all(users+tasks)

    db.session.commit()