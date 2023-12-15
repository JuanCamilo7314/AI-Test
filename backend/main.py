from flask import Flask, request, jsonify
from flask_cors import CORS
from modelo import summarize_text

app = Flask(__name__)
CORS(app)
def summarize_text_api(text):
    try:
        ordered_summary = summarize_text(text)
        return jsonify({'resumen_organizado': ordered_summary})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/resumir_texto', methods=['POST'])
def procesar_texto():
    try:
        data = request.get_json()
        texto = data['texto']
        return summarize_text_api(texto)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)