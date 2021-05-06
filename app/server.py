# ? imports ( Flask )
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'app/uploads'

# ? Creating app with Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        key = request.form.get("key")
        print(key)
        if uploaded_file.filename != '':
            file = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file))
            new_file = encrypt(file, key)
            return redirect(url_for("result"))  
            # uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))
    return render_template('index.htm')

@app.route("/result", methods=["GET"])
def result():
    return render_template("result.htm")

def encrypt(filename, key):
    print(filename, key)
    return "file"


def generate_key():
    return