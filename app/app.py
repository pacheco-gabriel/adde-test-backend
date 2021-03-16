# compose_flask/app.py
from flask import Flask
from flask import request
from Controllers.Clima import Clima
from flask_cors import CORS


app = Flask(__name__)

CORS(app, support_credentials=True)

@app.route('/')
@app.route('/<cidade>')
def index(cidade = ''):
    ip      = request.remote_addr;
    obClima = Clima(cidade, ip)
    return obClima.search()

@app.route('/favicon.ico')
def favicon():
    return "Favicon.ico"

if __name__ == "__main__":
    app.run()
