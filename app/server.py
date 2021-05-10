# ? imports ( Flask )
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import string    
import random

import re

# from utils.decryption import init as initDecryption
from utils.encryption import init as initEncryption

UPLOAD_FOLDER = 'uploads'
KEY_LENGTH = 10
FILENAME = "test.txt"

# def encrypt(filename, key):
#     print(filename, key)
#     return "file"

def generateKey():
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = KEY_LENGTH))    
    key = str(ran)
    return key

# def getWordsFromLineList(sentences):
#     wordsList = []
#     for sentence in sentences:
#         wordsList += re.sub('['+string.punctuation+']', '', sentence).split()
#     return wordsList

# def countFrequency(wordsList):
#     wordsWithFrequencies = {}
#     for word in wordsList:
#         wordsWithFrequencies[word] = wordsWithFrequencies.get(word, 0) + 1
#     return list(wordsWithFrequencies.items())

# def countFrequencyLength(wordsWithFrequencies):
#     frequencies = {}
#     for word, frequency in wordsWithFrequencies:
#         frequencies[frequency] = frequencies.get(frequency, 0) + 1
#     return list(frequencies.items())

# def bubble_sort(lst):
#     if len(lst) == 1:
#         return print(lst)
        
#     for i in range(len(lst) - 1): 
#         for j in range(0, len(lst) - i -1): 
#             if lst[j][1] < lst[j + 1][1]: 
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j] 
#     return lst

# def replaceWords(words, maximumFrequencyOccurence, key):
#     replacements = {}
#     for word, frequency in words:
#         if frequency == maximumFrequencyOccurence:
#             wordASCII = ""
#             for letter in word:
#                 wordASCII += "{0:03d}".format(ord(letter))
#             newWord = str(ord(key[0])) + key[:len(key) // 2] + str(wordASCII) + key[len(key) // 2:] + str(ord(key[-1]))
#             replacements[word] = newWord
#     return replacements
    
# def replaceInput(words, replacedWords):
#     for word, replacement in replacedWords.items():
#         if word in words:
#             index = words.index(word)
#             words[index] = replacement
#     return words

# def returnEncryptedData(encryptedWords):
#     return " ".join(encryptedWords)


# def initEncryption(data, key):
#     if type(data) == list:
#         data = "".join(data)

#     if not key:
#         key = generateKey()
    
#     sentences = data.lower().split(".")[:-1]

#     words = getWordsFromLineList(sentences)
#     wordsWithFrequencies = countFrequency(words)
#     frequencies = countFrequencyLength(wordsWithFrequencies)
#     maximumFrequencyOccurence = bubble_sort(frequencies)[0][0]
#     replacedWords = replaceWords(wordsWithFrequencies, maximumFrequencyOccurence, key)
#     encryptedWords = replaceInput(words, replacedWords)
#     encryptedData = returnEncryptedData(encryptedWords)

#     return encryptedData


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
            path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER']) + f"/{FILENAME}"
            with open(path, "r") as fileReader:
                encrypted = initEncryption(fileReader.read(), key)
            with open(path, "w") as fileWriter:
                fileWriter.write(encrypted)
            return redirect(url_for("result", key=key, filename=FILENAME))  
            # uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))
    return render_template('index.htm')

@app.route("/result", methods=["GET"])
def result():
    key = request.args.get("key")
    filename = request.args.get("filename")
    path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER']) + f"/{FILENAME}"
    decrypted = ""
    with open(path, "r") as fileReader:
        pass
        # decrypted = initDecryption(fileReader.read(), key)
    print(decrypted)
    if key == "":
        return redirect(url_for('index'))
    return render_template("result.htm",  key=key, filename=filename)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER']) + f"/{filename}"
    return send_file(uploads, as_attachment=True)

