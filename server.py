from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_event():
    data = request.get_json()
    print("📥 Received:", data)
    return jsonify({"status": "ok"})

@app.route('/', methods=['GET'])
def home():
    return "✅ Server is running"

if __name__ == '__main__':
    app.run()