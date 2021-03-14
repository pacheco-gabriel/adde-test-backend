# compose_flask/app.py
from flask import Flask
from Controllers.Clima import Clima

app = Flask(__name__)

@app.route('/<cidade>')
def index(cidade):
    obClima = Clima(cidade)
    return obClima.search()


if __name__ == "__main__":
    app.run()
