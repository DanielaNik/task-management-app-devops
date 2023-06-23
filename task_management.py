import sys
import psycopg2
from contextlib import closing
from flask import Flask, request, jsonify
from config import DB_CONFIG

app = Flask(__name__)

# Database configuration
DB_NAME = DB_CONFIG['dbname']
DB_USER = DB_CONFIG['user']
DB_PASSWORD = DB_CONFIG['password']
DB_HOST = DB_CONFIG['host']
DB_PORT = DB_CONFIG['port']

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/favicon.ico')
def favicon():
    # Return the favicon.ico file
    return app.send_static_file('favicon.ico')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        with closing(psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM task")
                tasks = cursor.fetchall()
                return jsonify({'tasks': tasks})
    except psycopg2.Error as e:
        print("Error retrieving tasks:", e)
        sys.exit(1)

@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        task_name = request.json['name']
        task_details = request.json['details']
        due_date = request.json.get('dueDate')
        is_finished = request.json.get('isFinished', False)
        with closing(psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO task (name, details, dueDate, isFinished) VALUES (%s, %s, %s, %s)", (task_name, task_details, due_date, is_finished))
                conn.commit()
                return jsonify({'message': 'Task created successfully'})
    except (psycopg2.Error, KeyError) as e:
        print("Error creating task:", e)
        sys.exit(1)

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    try:
        with closing(psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM task WHERE id = %s", (task_id,))
                task = cursor.fetchone()
                if task:
                    return jsonify({'task': task})
                else:
                    return jsonify({'message': 'Task not found'})
    except psycopg2.Error as e:
        print("Error retrieving task:", e)
        sys.exit(1)

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        task_name = request.json['name']
        task_details = request.json['details']
        due_date = request.json.get('dueDate')
        is_finished = request.json.get('isFinished', False)
        with closing(psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("UPDATE task SET name = %s, details = %s, dueDate = %s, isFinished = %s WHERE id = %s", (task_name, task_details, due_date, is_finished, task_id))
                conn.commit()
                return jsonify({'message': 'Task updated successfully'})
    except (psycopg2.Error, KeyError) as e:
        print("Error updating task:", e)
        sys.exit(1)

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        with closing(psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM task WHERE id = %s", (task_id,))
                conn.commit()
                return jsonify({'message': 'Task deleted successfully'})
    except psycopg2.Error as e:
        print("Error deleting task:", e)
        sys.exit(1)

if __name__ == '__main__':
    app.run(debug=True)
