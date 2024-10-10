# api/routes.py
from flask import Flask, request, jsonify
from orchestration.tasks import process_data_task
import requests

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform_data():
    data = request.json
    # Perform a simple transformation
    transformed_data = {k: v.upper() for k, v in data.items()}
    return jsonify(transformed_data)

@app.route('/external', methods=['GET'])
def call_external_service():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    return jsonify(response.json())

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    # Trigger background processing
    task = process_data_task.delay(data)
    return jsonify({"task_id": task.id, "status": "Processing started"})

@app.route('/task/<task_id>', methods=['GET'])
def get_task_status(task_id):
    from celery.result import AsyncResult
    task_result = AsyncResult(task_id)
    result = task_result.result if task_result.successful() else None
    return jsonify({
        "task_id": task_id,
        "status": task_result.status,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
