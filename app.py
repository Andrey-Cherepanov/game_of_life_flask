from flask import Flask
from flask import render_template
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route("/")
def index():
    GameOfLife(width=20, height=20)
    return render_template("index.html")

@app.route("/live")
def live():
    life = GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    else:
        life.counter+=1
    return render_template("live.html",
                            life=life)

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
