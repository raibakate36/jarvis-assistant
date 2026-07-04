from flask import Flask, render_template, request, jsonify
from chatbot import get_jarvis_reply
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    message = data["message"]

    start = time.perf_counter()

    reply = get_jarvis_reply(message)

    print("Jarvis processing time:", time.perf_counter() - start)

    print("Jarvis Reply:", reply)

    return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(debug=True)