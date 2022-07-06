import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import cv2 
import pytesseract

app = Flask(__name__, static_folder='static', template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload') 

def extrairTextoImagem(img):
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    return text


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)    
    print(savePath)
    img = cv2.imread(savePath)
    texto = extrairTextoImagem(img)
    return render_template('index.html',text = texto)

@app.route('/get-file/<filename>')
def getFile(filename):
    file = os.path.join(UPLOAD_FOLDER, filename+'.png')
    return send_file(file, mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True, port=3000)