from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "service": "AI Football Shorts Video Generator",
        "message": "Backend is working!"
    })

@app.route("/generate", methods=["POST"])
def generate_video():
    return jsonify({
        "status": "received",
        "message": "Video generation request received."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
