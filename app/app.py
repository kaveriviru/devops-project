from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword")
    )


@app.route("/")
def home():
    return "Hello! Python application is running."


@app.route("/health")
def health():
    return jsonify(status="UP")


@app.route("/db-check")
def db_check():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify(
            status="UP",
            database="PostgreSQL",
            version=version[0]
        )

    except Exception as e:
        return jsonify(
            status="DOWN",
            error=str(e)
        ), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)