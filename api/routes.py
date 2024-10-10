# api/routes.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/transform', methods=['POST'])
def transform_data():
    data = request.json
    # Perform some transformation
    transformed_data = {k: v.upper() for k, v in data.items()}
    return jsonify(transformed_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
# api/routes.py (add this to the existing file)
import requests

@app.route('/external', methods=['GET'])
def call_external_service():
    response = requests.get('https://api.example.com/data')
    return jsonify(response.json())
