from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.json_util import dumps
from datetime import datetime
from bson.objectid import ObjectId


app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://mongo:27017/todo_db"

mongo = PyMongo(app)


@app.route('/')
def index():
    todos = list(mongo.db.todos.find())
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task', '')
    if not task:
        return redirect(url_for('index'))
    todo = {
        'task': task,
        'date_created': datetime.utcnow(),
        'completed': False
    }
    mongo.db.todos.insert_one(todo)
    return redirect(url_for('index'))

@app.route('/update/<id>', methods=['POST'])
def update_todo(id):
    print(f"Update called with id: {id}, data: {request.form}") 
    updated_task = request.form.get('task', '').strip()
    completed = request.form.get('completed', 'off') == 'on'  # Check if the checkbox is checked
    if not updated_task:
        return redirect(url_for('index'))  # Redirect back if task is empty

    mongo.db.todos.update_one(
        {'_id': ObjectId(id)},  # Match by _id
        {'$set': {'task': updated_task, 'completed': completed}}
    )
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['POST'])
def delete_todo(id):
    try:
        mongo.db.todos.delete_one({'_id': ObjectId(id)})  # Deletes the todo by its ID
        print(f"Todo with id {id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting todo with id {id}: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

