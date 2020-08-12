from typing import List, Dict
from flask import Flask, request, current_app
import mysql.connector
import json

app = Flask(__name__)


def get_field(field="*") -> List[Dict]:
    config = {
        "user": "root",
        "password": "root",
        "host": "db",
        "port": "3306",
        "database": "wydb",
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(f"SELECT {field} FROM images")
    results = [{field: item} for item in cursor]
    cursor.close()
    connection.close()
    return results


def select_from(field, query):
    config = {
        "user": "root",
        "password": "root",
        "host": "db",
        "port": "3306",
        "database": "wydb",
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor = cursor()
    cursor.execute(f"SELECT {field} from images where {field} LIKE %{query}%")
    cursor.close()
    connection.close()
    return results


@app.route("/")
def home():
    return "Hello WAC!"


@app.route("/data")
def list_field() -> str:
    field = request.args.get("field") or "*"
    return json.dumps(get_field(field))


@app.route("/data/<field>")
def query():
    query = request.args.get(field)
    if query:
        return json.dumps(select_from(field, query))
    else:
        return "Sorry, bud"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
