from flask import make_response
from flask_restful import Resource, reqparse
from main import *
from models import *


class ProjectsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('project_name', type=str, required=True, help='This field cannot  be left empty')
    parser.add_argument('project_manager', type=str, required=True, help='This field cannot  be left empty')

    def post(self):
        try:
            data = ProjectsResource.parser.parse_args()
            project = ProjectModel(data['project_name'], data['project_manager'])
            project.save_to_db()
            return make_response(jsonify({
                'projectID': project.projectID,
                'project_name': project.project_name,
                'project_manager': project.project_manager
            }), 201)
        except Exception as error:
            return str(error)

    def delete(self, projectID=None):
        try:
            project = ProjectModel.find_by_projectID(projectID=projectID)
            if project is not None:
                TaskModel.find_by_projectID(projectID=projectID).delete()
                db.session.commit()
                project.delete_from_db()
                return {'status': 'succces'}, 200
            else:
                return {'status': 'not found'}, 404
        except Exception as error:
            return str(error)

    def put(self, projectID=None):
        try:
            data = ProjectsResource.parser.parse_args()
            project = ProjectModel.find_by_projectID(projectID=projectID)
            if not project:
                project = ProjectModel(data['project_name'], data['project_manager'])
            else:
                if data['project_manager'] is not None:
                    project.project_manager = data['project_manager']
                if data['project_name'] is not None:
                    project.project_name = data['project_name']
            project.save_to_db()
            return make_response(jsonify({
                'projectID': project.projectID,
                'project_name': project.project_name,
                'project_manager': project.project_manager
            }), 200)
        except Exception as error:
            return str(error)

    def get(self, projectID=None):
        if projectID is None:
            try:
                projects = ProjectModel.query.all()
                projects_list = [{
                    'projectID': proj.projectID,
                    'project_name': proj.project_name,
                    'project_manager': proj.project_manager
                } for proj in projects]
                return {
                           'projects': projects_list
                       }, 200

            except Exception as error:
                return str(error)
        else:
            try:
                project = ProjectModel.find_by_projectID(projectID=projectID)
                return {
                    'projectID': project.projectID,
                    'project_name': project.project_name,
                    'project_manager': project.project_manager
                }, 200

            except Exception as error:
                return str(error)


class TasksResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('task_description', type=str, required=False, help='This field cannot  be left empty')
    parser.add_argument('projectID', type=int, required=False, help='This field cannot  be left empty')

    def post(self, projectID):
        try:
            data = TasksResource.parser.parse_args()
            status = 'todo'
            request_status = request.get_json()
            task_description = request_status.get('task_description')
            projectID = request_status.get('projectID')
            task = TaskModel(task_description, status, projectID)
            task.save_to_db()
            return make_response(jsonify({
                'taskID': task.taskID,
                'task_description': task.task_description,
                'status': task.status,
                'projectID': task.projectID,
            }), 201)
        except Exception as error:
            return str(error)

    def delete(self, taskID=None, projectID=None):
        try:
            task = TaskModel.find_by_taskID_projectID(taskID=taskID, projectID=projectID)
            if task is not None:
                task.delete_from_db()
                return {'status': 'succces'}, 200
            else:
                return {'status': 'not found'}, 404
        except Exception as error:
            return str(error)

    def put(self, projectID=None, taskID=None):
        try:
            data = TasksResource.parser.parse_args()
            request_status = request.get_json()
            status = request_status.get('status')
            task = TaskModel.find_by_taskID_projectID(taskID=taskID, projectID=projectID)
            if not task:
                task = TaskModel(data['task_description'], status=status, projectID=projectID)
            else:
                if data['task_description'] is not None:
                    task.task_description = data['task_description']
                if status is not None:
                    task.status = status
            task.save_to_db()
            return make_response(jsonify({
                'taskID': task.taskID,
                'task_description': task.task_description,
                'status': task.status,
                'projectID': task.projectID,
            }), 200)
        except Exception as error:
            return str(error)

    def get(self, taskID=None, projectID=None):
        if taskID is None:
            try:
                tasks = TaskModel.find_by_projectID(projectID=projectID)
                tasks_list = [{
                    'taskID': task.taskID,
                    'task_description': task.task_description,
                    'status': task.status,
                    'projectID': task.projectID,
                } for task in tasks]
                return {
                           'tasks': tasks_list
                       }, 200
            except Exception as error:
                return str(error)
        else:
            try:
                task = TaskModel.find_by_taskID_projectID(taskID=taskID, projectID=projectID)
                if not task:
                    return {'not found'}, 404
                return {
                    'taskID': task.taskID,
                    'task_description': task.task_description,
                    'status': task.status,
                    'projectID': task.projectID,
                }, 200

            except Exception as error:
                return str(error)


class UsersResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('user_name', type=str, required=False, help='This field cannot  be left empty')
    parser.add_argument('user_password', type=str, required=False, help='This field cannot  be left empty')

    def post(self):
        try:
            data = UsersResource.parser.parse_args()
            user = UserModel(data['user_name'], data['user_password'])
            user.save_to_db()
            return make_response(jsonify({
                'userID': user.userID,
                'user_name': user.user_name
            }), 201)
        except Exception as error:
            return str(error)

    def delete(self, userID=None):
        try:
            user = UserModel.find_by_user_id(userID=userID)
            if user is not None:
                user.delete_from_db()
                return {'status': 'succces'}, 200
            else:
                return {'status': 'not found'}, 404
        except Exception as error:
            return str(error)

    def put(self, userID=None):
        try:
            data = UsersResource.parser.parse_args()
            user = UserModel.find_by_user_id(userID=userID)
            if not user:
                user = UserModel(data['user_name'], data['user_password'])
            else:
                if data['user_name'] is not None:
                    user.user_name = data['user_name']
                if data['user_password'] is not None:
                    user.user_password = data['user_password']
            user.save_to_db()
            return make_response(jsonify({
                'userID': user.userID,
                'user_name': user.user_name
            }), 200)
        except Exception as error:
            return str(error)

    def get(self, userID=None):
        if userID is None:
            try:
                users = UserModel.query.all()
                users_list = [{
                    'userID': user.userID,
                    'user_name': user.user_name
                } for user in users]
                return {
                           'users': users_list
                       }, 200

            except Exception as error:
                return str(error)
        else:
            try:
                user = UserModel.find_by_user_id(userID=userID)
                return {
                    'userID': user.userID,
                    'user_name': user.user_name
                }, 200

            except Exception as error:
                return str(error)