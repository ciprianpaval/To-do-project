from werkzeug.security import generate_password_hash, check_password_hash

from main import db


class ProjectModel(db.Model):
    __tablename__ = 'projects'

    projectID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(255), unique=True, nullable=False)
    project_manager = db.Column(db.String(255), unique=True, nullable=False)
    tasks = db.relationship('TaskModel', backref=db.backref('projects'))

    def __init__(self, project_name, project_manager):
        self.project_name = project_name
        self.project_manager = project_manager

    def get_id(self):
        return self.projectID

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_projectID(cls, projectID):
        return cls.query.filter_by(projectID=projectID).first()

    @classmethod
    def find_by_project_name(cls, project_name):
        return cls.query.filter_by(project_name=project_name)


class TaskModel(db.Model):
    __tablename__ = "tasks"

    taskID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_description = db.Column(db.String(255), unique=True, nullable=True)
    status = db.Column(db.String(255), unique=False, nullable=True)
    projectID = db.Column(db.Integer, db.ForeignKey('projects.projectID'), nullable=True)

    def __init__(self, task_description, status, projectID):
        self.task_description = task_description
        self.status = status
        self.projectID = projectID

    def get_id(self):
        return self.taskID

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_taskID(cls, taskID):
        return cls.query.filter_by(taskID=taskID).first()

    @classmethod
    def find_by_projectID(cls, projectID):
        return cls.query.filter_by(projectID=projectID)

    @classmethod
    def find_by_taskID_projectID(cls, taskID, projectID):
        return cls.query.filter_by(projectID=projectID).filter_by(taskID=taskID).first()


class UserModel(db.Model):
    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), unique=True, nullable=True)
    user_password = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = generate_password_hash(user_password)

    def get_id(self):
        return self.userID

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_user_name(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()

    @classmethod
    def find_by_user_id(cls, userID):
        return cls.query.filter_by(userID=userID).first()

    @classmethod
    def find_by_project_name(cls, project_name):
        return cls.query.filter_by(project_name=project_name)

    def verify_password(self, password):
        return check_password_hash(self.user_password, password)
