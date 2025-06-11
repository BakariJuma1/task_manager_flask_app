from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String,Column,Integer,MetaData,DateTime
from datetime import datetime,timedelta

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer(),primary_key=True)
    name = Column(String(80))
    email = Column(String(),unique=True)

class Task(db.Model):

    __tablename__ = "Tasks"
    
    id = Column(Integer(),primary_key=True)
    title = Column(String(80))
    description = Column(String())
    due_date = Column(DateTime,default=lambda: datetime.now()+ timedelta(days=5))