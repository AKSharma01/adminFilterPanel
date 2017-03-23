from setting import db
from flask_sqlalchemy import SQLAlchemy



class Users(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    display_name = db.Column(db.String(70), unique=True)
    email = db.Column(db.String(255), unique=True)    
    password = db.Column(db.String(60))
    reset_pin = db.Column(db.SMALLINT)
    is_banned = db.Column(db.Boolean, unique=False, default=False)
    is_god = db.Column(db.Boolean, unique=False, default=False)
    se = db.Column(db.Boolean, unique=False, default=False)
    is_active = db.Column(db.Boolean, unique=False, default=False)
    confirmation_code = db.Column(db.String(255))
    last_login_location = db.Column(db.JSON)
    is_password_change_required = db.Column(db.Boolean, default= None)
    created_at = db.Column(db.DateTime) 
    updated_at = db.Column(db.DateTime)
    slack_id = db.Column(db.String(30), unique = True)
    logo = db.Column(db.Text)


class Tasks(db.Model):
    """docstring for Tasks"""
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(255))
    description =  db.Column(db.Text) 
    creator_id = db.Column(db.String(100))
    is_assignee_group = db.Column(db.Boolean, unique=False, default=False)
    due_date = db.Column(db.DateTime) 
    seen = db.Column(db.DateTime)
    is_submitted = db.Column(db.Boolean, unique=False, default=False)
    is_completed = db.Column(db.Boolean, unique=False, default=False)
    submission_date = db.Column(db.DateTime)
    completion_date = db.Column(db.DateTime)
    priority_id = db.Column(db.Integer, default = 1)
    location = db.Column(db.String(255)) 
    status_id = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime) 
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    tna_item_id = db.Column(db.String(255)) 
    archived_at = db.Column(db.DateTime)
    created_from = db.Column(db.String(255)) 
    created_from_id = db.Column(db.String(255)) 
    google_calendar_id = db.Column(db.String(255)) 
    checklist = db.Column(db.JSON)
    line_id = db.Column(db.String(255)) 
    style_id = db.Column(db.String(255)) 
    customer_id = db.Column(db.String(255)) 
    need_approval = db.Column(db.Boolean, unique=False)
    is_approved = db.Column(db.Boolean, unique=False, default=False)
    starter_id    =  db.Column(db.Text) 
    submitter_id  =  db.Column(db.Text) 
    schema_version = db.Column(db.String(255))
    user_relation = db.relationship('Users', backref='emailid', lazy='dynamic')

