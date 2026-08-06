from flask import Flask, request, jsonify
from gemini import analyze_logs

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    logs = data.get("logs")

    result = analyze_logs(logs)

    return jsonify({"analysis": result})


if __name__ == "__main__":
    app.run(debug=True)
