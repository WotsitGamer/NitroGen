from flask import Flask
app = Flask(__name__)

@app.get("/")
def index():
    return "HEY"
app.run(host='0.0.0.0', port=80, debug=True)