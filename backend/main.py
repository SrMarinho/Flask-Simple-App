from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import routes

app = Flask(__name__)
# CORS(app, origins=['http://127.0.0.1:8081'])
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(routes.bp)

if __name__ == '__main__':
    app.run()