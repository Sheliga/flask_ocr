import json
import os

import cv2
import pytesseract
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static', template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload') 

with open('config.json') as f:
    config = json.load(f)

pytesseract.pytesseract.tesseract_cmd = config['tesseract_path']
custom_config = r'--oem 3 --psm 6 -l por'


def extrair_texto_imagem(img):
    try:
        texto = pytesseract.image_to_string(img, config=custom_config)
    except Exception as e:
        print(f"Ocorreu um erro ao tentar extrair o texto da imagem: {str(e)}")
        alt_config = r'--oem 3 --psm 6'
        texto = pytesseract.image_to_string(img, config=alt_config)
        

    print("texto: " + texto)
    return texto

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    print("file -->", file)
    save_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(save_path)    
    print('save path',save_path)
    img = cv2.imread(save_path)
    texto = extrair_texto_imagem(img)
    return render_template('index.html', text=texto)

@app.route('/get-file/<filename>')
def get_file(filename):
    file = os.path.join(UPLOAD_FOLDER, filename+'.png')
    return send_file(file, mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True, port=3000)
