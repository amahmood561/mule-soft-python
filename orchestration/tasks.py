# orchestration/tasks.py
from celery import Celery
import time

app = Celery('tasks', broker='redis://localhost:6379/0')

# Configure the Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_data_task(data):
    # Simulate a time-consuming data processing task
    time.sleep(5)  # Simulate processing delay
    # Reverse each string in the data
    processed_data = {k: v[::-1] for k, v in data.items()}
    return processed_data
