from flask import Flask, jsonify, request
import argostranslate.package
import argostranslate.translate
import os
app = Flask(__name__)


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        # Get data from the JSON body
        data = request.json
        _from = data.get('from')
        _to = data.get('to')
        _content = data.get('content')
    else:
        # Fallback to GET parameters for backward compatibility
        _from = request.args.get('from')
        _to = request.args.get('to')
        _content = request.args.get('content')

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
    app.run(debug=True, host='0.0.0.0', port=5000)  # Use port 5000 inside the container
