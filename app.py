from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/live")
def live():
    return render_template("live.html")

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
