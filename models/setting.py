from flask import Flask
# from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import env, psycopg2

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



app = Flask(__name__)

class ENVSetting:
	"""docstring for ENVSetting"""
	def __init__(self):
		# self.username = self.password = self.database = self.host = ''
		pass

	def getPsqlENV(self):
		""" This will return the postgres access credential """
		username = getattr(env, env.ENV+'_username')
		password = getattr(env, env.ENV+'_password')
		database = getattr(env, env.ENV+'_database')
		host = getattr(env, env.ENV+'_host')
		return database, username, password


env_get = ENVSetting()
database, username, password = env_get.getPsqlENV()

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://"+username+":"+password+"@localhost/"+database
# db = SQLAlchemy(app)
engine = create_engine("postgresql://"+username+":"+password+"@localhost/"+database, echo=True)
# Base = declarative_base(engine)
app.config['SQLALCHEMY_DATABASE_URI'] = engine
db = SQLAlchemy(app)













# class tasks(Base):
#     """"""
#     __tablename__ = 'tasks'
#     __table_args__ = {'autoload':True}
# 	user = db.relationship('users', backref = 'creator_id', lazy = 'dynamic') 

# def loadSession():
#     """"""
#     metadata = Base.metadata
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session