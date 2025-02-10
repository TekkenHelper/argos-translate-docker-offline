from flask import Flask, jsonify, request
import argostranslate.package
import argostranslate.translate
import os
app = Flask(__name__)

@app.route('/translate', methods=['GET','POST'])
def translate():
    _from = request.args.get('from')
    _to = request.args.get('to')
    _content = request.args.get('content')
    argostranslate.package.install_from_path("/argos-language-packs/translate-"+_from+
                                             "_"+_to+"-1_9.argosmodel")
    _result = argostranslate.translate.translate(_content, _from, _to)
    _jsonRes='{"result":"'+_result+'"}'

    if  request.args.get('responseType') == 'jsonp':
        # _jsonRes = "document.getElementById('"+request.args.get('domId')+"').innerText="+'\'{"code":200,"result":"'+_result+'"}\''
        # _jsonRes=f'{request.args.get("callback")}('+  +')"
        _jsonRes = request.args.get('domId')+".push("+'\'{"code":200,"result":"'+_result+'"}\')'

    print(_jsonRes)
    return _jsonRes,200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Use port 5000 inside the container