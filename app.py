from flask import Flask, request, jsonify, render_template
from translate import Translator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/write')
def write():
    return render_template('index.html')

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data['text']
    target_language = data['target_language']

    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)

    return jsonify({'translatedText': translation})

if __name__ == '__main__':
    app.run(debug=True)
