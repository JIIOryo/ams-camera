import json
import jsonschema
from flask import Flask, request, jsonify, Response
from flask_jsonschema_validator import JSONSchemaValidator

from controller.camera import picture

app = Flask(__name__)
JSONSchemaValidator(
    app = app,
    root = "schemas"
)
empty_response = {}

@app.errorhandler(jsonschema.ValidationError)
def onValidationError(e):
  res = json.dumps({
      'message': 'Validation error: ' + str(e),
      'code': 400
  })
  return Response(res , 400)

@app.route('/ping')
def ping():
    return jsonify(empty_response)

@app.route('/picture', methods=['POST'])
@app.validate('picture', 'picture')
def take_picture():
    picture(request.json)
    return empty_response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5364)
