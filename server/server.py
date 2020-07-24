import json
import jsonschema
import sys

from flask import Flask, request, jsonify, Response
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
ok = json.dumps({
    'message': 'ok',
    'code': 200
})

@app.errorhandler(jsonschema.ValidationError)
def onValidationError(e):
  res = json.dumps({
      'message': 'Validation error: ' + str(e),
      'code': 400
  })
  return Response(res , 400)

@app.route('/ping')
def ping():
    return Response(ok, 200)

@app.route('/picture', methods=['POST'])
@app.validate('picture', 'picture')
def take_picture():
    picture(request.json)
    return Response(ok, 200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5364)
