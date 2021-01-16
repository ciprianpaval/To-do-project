from projects import *


@app.route('/login', methods=['POST'])
def login():
    signin_json = request.get_json()
    if not signin_json:
        return jsonify({'msg': 'Missing JSON'}), 400

    username = signin_json.get('user_name')
    password = signin_json.get('user_password')

    if not username:
        return jsonify({'msg': 'Missing username'}), 400

    if not password:
        return jsonify({'msg': 'Missing password'}), 400

    user = UserModel.find_by_user_name(user_name=username)
    if user:
        if user.verify_password(password):
            return jsonify({'msg': 'Success login'}), 200
        else:
            return jsonify({'msg': 'Wrong'}), 401
    else:
        return jsonify({'msg': 'not found'}), 404


@app.route('/signup', methods=['POST'])
def signup():
    signup_json = request.get_json()
    if not signup_json:
        return jsonify({'msg': 'Missing JSON'}), 400

    username = signup_json.get('user_name')
    password = signup_json.get('user_password')

    if not username:
        return jsonify({'msg': 'Missing username'}), 400

    if not password:
        return jsonify({'msg': 'Missing password'}), 400
    try:
        user = UserModel(user_name=username, user_password=password)
        user.save_to_db()
        return jsonify({'status': 'succes'})

    except Exception as error:
        return str(error)


api.add_resource(ProjectsResource, '/projects', '/projects/<int:projectID>')
api.add_resource(TasksResource, '/tasks/<int:projectID>/<int:taskID>', '/tasks/<int:projectID>')
api.add_resource(UsersResource, '/users', '/users/<int:userID>')

if __name__ == '__main__':
    app.run(debug=True)
