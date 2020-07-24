import json
import jsonschema
import sys

from flask import Flask, request, jsonify
from flask_jsonschema_validator import JSONSchemaValidator

import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from controller.camera import picture

app = Flask(__name__)
JSONSchemaValidator(
    app = app,
    root = "schemas"
)
ok = {
    'message': 'ok',
    'code': 200
}

def error_response(e) -> dict:
    code = 400
    res = {
        'code': code,
        'error': e.error,
        'message': e.message,
    }
    return jsonify(res), 400

@app.errorhandler(jsonschema.ValidationError)
def onValidationError(e):
    res = {
        'code': 400,
        'error': e.__class__.__name__,
        'message': 'Validation error: ' + str(e),
    }
    return jsonify(res), 400

@app.route('/ping')
def ping():
    return jsonify(ok), 200

@app.route('/picture', methods=['POST'])
@app.validate('picture', 'picture')
def take_picture():
    try:
        picture(request.json)
    except Exception as e:
        print(e)
        return error_response(e)
    return jsonify(ok), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5364)
