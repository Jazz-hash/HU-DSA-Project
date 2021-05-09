# ? imports ( Flask )
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import string    
import random

import re


from utils.encryption import init as initEncryption

UPLOAD_FOLDER = 'uploads'
KEY_LENGTH = 10
FILENAME = "test.txt"

# ? Creating app with Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        key = request.form.get("key")
        key = key if key != "" else generateKey()
        print(key)
        if uploaded_file.filename != '':
            file = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], file))
            encrypted = ""
            with open(f"{UPLOAD_FOLDER}/{FILENAME}", "r") as fileReader:
                encrypted = initEncryption(fileReader.read(), key)
            with open(f"{UPLOAD_FOLDER}/{FILENAME}", "w") as fileWriter:
                fileWriter.write(encrypted)
            return redirect(url_for("result", key=key, filename=FILENAME))  
            # uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))

        
    return render_template('index.htm')

@app.route("/result", methods=["GET"])
def result():
    key = request.args.get("key")
    filename = request.args.get("filename")
    if key == "":
        return redirect(url_for('index'))
    return render_template("result.htm",  key=key, filename=filename)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_file(uploads, as_attachment=True)
    # return send_from_directory(directory=uploads, filename=filename)


def encrypt(filename, key):
    print(filename, key)
    return "file"


def generateKey():
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = KEY_LENGTH))    
    key = str(ran)
    return key