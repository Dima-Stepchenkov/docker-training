from flask import Flask
import os
import logging

app = Flask(__name__)

# Настройка логирования
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/flask.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

@app.route('/')
def hello():
    app.logger.info('Handling request to /')
    return "Hello from Flask (via Nginx proxy!)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
