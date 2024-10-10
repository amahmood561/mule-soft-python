# Python MuleSoft-like Integration

This project demonstrates a MuleSoft-like integration using Python. It features a simple REST API, orchestration with Celery, and integration with external services. The project showcases skills in API development, data transformation, task orchestration, and testing.

## Features
- RESTful API using Flask
- Background task processing with Celery
- Integration with external APIs using the Requests library
- Configuration management
- Unit testing with unittest

## Prerequisites
- Python 3.8+
- Redis (for Celery message broker)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-mulesoft-integration.git
   cd python-mulesoft-integration
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start Redis (if not already running):
   ```bash
   redis-server
   ```

4. Start the Celery worker:
   ```bash
   celery -A orchestration.tasks worker --loglevel=info
   ```

5. Run the Flask API:
   ```bash
   python api/routes.py
   ```

## API Endpoints

### 1. Data Transformation
Transforms the input data by converting all values to uppercase.

- **Endpoint**: `/transform`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "john",
    "city": "new york"
  }
  ```
- **Response**:
  ```json
  {
    "name": "JOHN",
    "city": "NEW YORK"
  }
  ```

#### Example cURL Request
```bash
curl -X POST http://127.0.0.1:5000/transform \
-H "Content-Type: application/json" \
-d '{"name": "john", "city": "new york"}'
```

### 2. External Service Call
Calls an external API and returns the response data.

- **Endpoint**: `/external`
- **Method**: `GET`
- **Response** (example):
  ```json
  {
    "data": {
      "id": 1,
      "value": "example data"
    }
  }
  ```

#### Example cURL Request
```bash
curl -X GET http://127.0.0.1:5000/external
```

### 3. Background Data Processing
Submits data for background processing via Celery. The data is reversed (e.g., "hello" becomes "olleh").

- **Endpoint**: `/process`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "message": "hello"
  }
  ```
- **Response**:
  ```json
  {
    "task_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "status": "Processing started"
  }
  ```

#### Example cURL Request
```bash
curl -X POST http://127.0.0.1:5000/process \
-H "Content-Type: application/json" \
-d '{"message": "hello"}'
```

### Checking Task Status
You can check the status of the background task using the task ID.

- **Endpoint**: `/task/<task_id>`
- **Method**: `GET`
- **Response** (example):
  ```json
  {
    "task_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "status": "Completed",
    "result": {
      "message": "olleh"
    }
  }
  ```

#### Example cURL Request
```bash
curl -X GET http://127.0.0.1:5000/task/d290f1ee-6c54-4b01-90e6-d701748f0851
```

## Configuration
You can customize settings in the `config/settings.py` file. For example, you can change the external API URL:
```python
API_URL = "https://api.example.com"
```

## Running Tests
Run unit tests to ensure the project is functioning correctly:
```bash
python -m unittest discover tests
```

## Contributing
Feel free to submit issues, fork the repository, and send pull requests!

