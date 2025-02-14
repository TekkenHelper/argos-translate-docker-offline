from flask import Flask, request, jsonify
import argostranslate.package
import argostranslate.translate
import json  # Import the json module for escaping

app = Flask(__name__)

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        # Check the Content-Type header to determine how to retrieve data
        if request.is_json:
            # If the request is JSON, use request.json
            data = request.json
            _from = data.get('from')
            _to = data.get('to')
            _content = data.get('content')
        else:
            # If the request is form data, use request.form
            _from = request.form.get('from')
            _to = request.form.get('to')
            _content = request.form.get('content')
    else:
        # Fallback to GET parameters for backward compatibility
        _from = request.args.get('from')
        _to = request.args.get('to')
        _content = request.args.get('content')

    # Validate that all required parameters are present
    if not all([_from, _to, _content]):
        return jsonify({"error": "Missing required parameters: 'from', 'to', or 'content'"}), 400

    # Install the language pack if not already installed
    argostranslate.package.install_from_path(f"/argos-language-packs/translate-{_from}_{_to}-1_9.argosmodel")

    # Perform the translation
    _result = argostranslate.translate.translate(_content, _from, _to)

    # Prepare the JSON response
    _jsonRes = {"result": _result}

    # Print the response for debugging
    print(_jsonRes)

    # Return the response as JSON
    return jsonify(_jsonRes), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
