from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8084"}})

@app.route('/get-data', methods=['GET'])
def get_data():
    try:
        conn = sqlite3.connect('/var/lib/sqlite/app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sample_table LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        if result:
            return jsonify({"message": result[1]})
        else:
            return jsonify({"error": "No data found"}), 404
    except sqlite3.OperationalError as e:
        print(str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
