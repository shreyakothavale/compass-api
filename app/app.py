from flask import Flask, request, jsonify
import app.compass as compass

app = Flask(__name__)


@app.route('/')
def index():
    return 'Compass'

@app.route('/upload', methods=['PUT'])
def upload():
    try:
        compass.save(request.json)
        return jsonify({
            'message': 'Map uploaded'
        }), 200
    except:
        return jsonify({
            'message': 'Failed to upload map'
        }), 400

@app.route('/download', methods=['GET'])
def download():
    data = compass.load()
    return jsonify({
        'data': data
    }) 
