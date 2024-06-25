from flask import Flask, request, render_template, jsonify
from PIL import Image
import pytesseract
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        text = pytesseract.image_to_string(Image.open(file_path))
        return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
