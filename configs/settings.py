import os

DEBUG = os.getenv('DEBUG', 'True') == 'True'
BROKER_URL = os.getenv('BROKER_URL', 'redis://localhost:6379/0')
