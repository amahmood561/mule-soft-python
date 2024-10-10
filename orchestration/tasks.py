# orchestration/tasks.py
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_data(data):
    # Perform some complex processing
    return {k: v[::-1] for k, v in data.items()}
