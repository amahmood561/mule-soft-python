# main.py

from multiprocessing import Process
from api.routes import app  # Import the Flask app
from orchestration.tasks import app as celery_app  # Import the Celery app
import os

def start_flask_app():
    """Starts the Flask API server."""
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)

def start_celery_worker():
    """Starts the Celery worker."""
    celery_app.worker_main(['worker', '--loglevel=info'])

if __name__ == '__main__':
    # Create separate processes for Flask and Celery
    flask_process = Process(target=start_flask_app)
    celery_process = Process(target=start_celery_worker)

    # Start both processes
    flask_process.start()
    print("Flask API server started...")

    celery_process.start()
    print("Celery worker started...")

    # Join the processes to keep them running
    flask_process.join()
    celery_process.join()
