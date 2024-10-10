# config/settings.py
import os

DEBUG = os.getenv('DEBUG', 'True') == 'True'
API_URL = os.getenv('API_URL', 'https://api.example.com')
