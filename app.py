from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('new.html')

@app.route('/add', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        tasks.append({'task': task, 'completed': False})
    return jsonify(tasks)

@app.route('/toggle', methods=['POST'])
def toggle_task():
    index = request.json.get('index')
    if index is not None and 0 <= index < len(tasks):
        tasks[index]['completed'] = not tasks[index]['completed']
    return jsonify(tasks)

@app.route('/delete', methods=['POST'])
def delete_task():
    index = request.json.get('index')
    if index is not None and 0 <= index < len(tasks):
        del tasks[index]
    return jsonify(tasks)

@app.route('/clear', methods=['POST'])
def clear_completed():
    global tasks
    tasks = [task for task in tasks if not task['completed']]
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)