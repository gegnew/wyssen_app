from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def get_images() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'wydb'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM images')
    results = [[_id, sum, path, title, crop] for (_id, sum, path, title, crop) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'images': get_images()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
