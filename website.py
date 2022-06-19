from flask import Flask
import subprocess
subprocess.Popen(["python", "threadsnitro.py"])
app = Flask(__name__)

@app.get("/")
def index():
    return "HEY"
app.run()