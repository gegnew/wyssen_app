from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)

def get_field(field="*") -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'wydb'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(f"SELECT {field} FROM images")
    results = [{field: item} for item in cursor]
    cursor.close()
    connection.close()
    return results

@app.route('/data')
def query() -> str:
    field = request.args.get("field") or "*"
    return json.dumps(get_field(field))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
