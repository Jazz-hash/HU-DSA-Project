# ? imports ( Flask )
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import string    
import random
import re
from flask_mail import Mail, Message

# Setting constansts
UPLOAD_FOLDER = 'uploads'
KEY_LENGTH = 12
FILENAME = "test.txt"

# ? Creating app with Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# setting smtp sever variables
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'travellingdiaries2019@gmail.com'
app.config['MAIL_PASSWORD'] = 'Travel1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def generateKey():
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = KEY_LENGTH))    
    key = str(ran)
    return key

def removePunctuation(data):
    data = re.sub(r"[,.;@#?!&$]+\ *", " ", data)
    return data

def getWordsFromLineList(data):
    return data.split(" ")

def countFrequency(wordsList):
    wordsWithFrequencies = {}
    for word in wordsList:
        wordsWithFrequencies[word] = wordsWithFrequencies.get(word, 0) + 1
    return list(wordsWithFrequencies.items())

def countFrequencyLength(wordsWithFrequencies):
    frequencies = {}
    for word, frequency in wordsWithFrequencies:
        frequencies[frequency] = frequencies.get(frequency, 0) + 1
    return list(frequencies.items())

def bubble_sort(lst):
    if len(lst) == 1:
        return print(lst)
        
    for i in range(len(lst) - 1): 
        for j in range(0, len(lst) - i -1): 
            if lst[j][1] < lst[j + 1][1]: 
                lst[j], lst[j + 1] = lst[j + 1], lst[j] 
    return lst

def replaceWords(words, maximumFrequencyOccurence, key):
    replacements = {}
    for word, frequency in words:
        if frequency == maximumFrequencyOccurence:
            wordASCII = ""
            for letter in word:
                wordASCII += "{0:03d}".format(ord(letter))
            newWord = "{0:03d}".format(ord(key[0])) + key[:len(key) // 2] + str(wordASCII) + key[len(key) // 2:] + "{0:03d}".format(ord(key[-1]))
            replacements[word] = newWord
    return replacements
    
def replaceInput(words, replacedWords):
    for word, replacement in replacedWords.items():
        if word in words:
            index = words.index(word)
            words[index] = replacement
    return words

def returnEncryptedData(encryptedWords):
    return " ".join(encryptedWords)


def initEncryption(data, key):
    if type(data) == list:
        data = "".join(data)

    if not key:
        key = generateKey()
    data = removeDetails(data, "Decryption")
    print(data)
    
    data = removePunctuation(data)
    words = getWordsFromLineList(data)
    wordsWithFrequencies = countFrequency(words)
    print(wordsWithFrequencies)
    frequencies = countFrequencyLength(wordsWithFrequencies)
    maximumFrequencyOccurence = bubble_sort(frequencies)[0][0]
    replacedWords = replaceWords(wordsWithFrequencies, maximumFrequencyOccurence, key)
    encryptedWords = replaceInput(words, replacedWords)
    encryptedData = returnEncryptedData(encryptedWords)

    return encryptedData

def replace(word, replacements):
    word = word[:3].replace(replacements[0], "") + word[3:-3] +  word[-3:].replace(replacements[-1], "")
    for replacement in replacements[1:-1]:
        word = word.replace(replacement, "")
    return word

def enQueue(queue, item, priority = 0):
    queue.append((item, priority))

def removeKey(words, key):
    if len(key) < 12:
        return None
    keyLessWords = []
    key0 = "{0:03d}".format(ord(key[0]))
    key1 = key[:len(key) // 2]
    key2 = key[len(key) // 2:]
    key3 = "{0:03d}".format(ord(key[-1]))
    print(key1, key2)
    
    for word in words:
        priority = 0
        if word[:3] == key0 and key1 == word[3:9]:
            word = replace(word, [key0, key1, key2, key3])
            priority = 1
        enQueue(keyLessWords, word, priority)
    return keyLessWords
    
def checkDecryption(keyLessWords):
    keyError = True
    for word, level in keyLessWords:
        if level == 1:
            keyError = False
    return keyError

def convertEncryptedToWords(encrypted):
    if checkDecryption(encrypted):
        return None
    words = []
    for word, level in encrypted:
        if level == 1:
            word = "".join([str(chr(int(word[i:i+3]))) for i in range(0, len(word), 3)])
        words.append(word)
    return words
        
def wordsToFile(words):
    return " ".join(words)

def initDecryption(encrypted, key):
    encrypted = removeDetails(encrypted, "Encryption")
    words = encrypted.lower().split(" ")[:-1]
    keyLessWords = removeKey(words, key)
    print(keyLessWords)
    if keyLessWords:
        print(keyLessWords, "0000000000000")
        replacedWords = convertEncryptedToWords(keyLessWords)  
        if replacedWords:
            result = wordsToFile(replacedWords)
            return result
    return None

def removeDetails(result, type):
    copyrightLine = f"\n\n\n  {type} by Encryptor - visit https://hu-encryptor.herokuapp.com/ to encrypt/decrypt more files !!  \n\n\n"
    result = result.replace(copyrightLine, "")
    return result

def addDetails(result, type):
    copyrightLine = f"\n\n\n  {type} by Encryptor - visit https://hu-encryptor.herokuapp.com/ to encrypt/decrypt more files !!  \n\n\n"
    return result + copyrightLine


# Routes

# Index route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        _type = request.form.get("type")
        print(_type) 

        # Encryption
        if _type == "encryption":
            uploaded_file = request.files['eFile']
            key = request.form.get("key")
            if key == "":
                key = generateKey()
            print(key)
            if uploaded_file.filename != '':
                # saving file in uploads dir
                file = secure_filename(uploaded_file.filename)
                uploaded_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], file))
                encrypted = ""
                path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER']) + f"/{file}"
                # reading file
                with open(path, "r") as fileReader:
                    # applying encryption
                    encrypted = initEncryption(fileReader.read(), key)
                    # adding footer of our app
                if encrypted:
                    encrypted = addDetails(encrypted, "Encryption")
                    # re-writting file
                with open(path, "w") as fileWriter:
                    fileWriter.write(encrypted)
                    # return result route with key and filename
                return redirect(url_for("result", key=key, filename=file))
        
        # Decryption
        else:
            uploaded_file = request.files['dFile']
            key = request.form.get("dKey")
            if uploaded_file.filename != '':
                file = secure_filename(uploaded_file.filename)
                print(file)
                # saving file in uploads dir
                uploaded_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], file))
                decrypted = ""
                path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER']) + f"/{file}"
                # print(path, "-------------------------------------")
                # reading file
                with open(path, "r") as fileReader:
                    decrypted = initDecryption(fileReader.read(), key)
                    # adding footer of our app
                if decrypted:
                    decrypted = addDetails(decrypted, "Decryption")
                    # checking if key is right or wrong
                if decrypted == "" or not decrypted:
                    # return error route
                    return redirect(url_for('error'))
                    # re-writting file
                with open(path, "w") as fileWriter:
                    fileWriter.write(decrypted)
                    # return result route with key and filename
                return redirect(url_for("result", key=key, filename=file))  
        return redirect(url_for('index'))
    return render_template('index.htm')

# Result route
@app.route("/result", methods=["GET"])
def result():
    key = request.args.get("key")
    filename = request.args.get("filename")
    if key == "":
        # if not key return to index
        return redirect(url_for('index'))
    # return result page with key and filename
    return render_template("result.htm",  key=key, filename=filename)

# Download route
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER']) + f"/{filename}"
    # download file 
    return send_file(uploads, as_attachment=True)

# Error route
@app.route("/error", methods=["GET"])
def error():
    # render error page
    return render_template("error.htm")

# Mailing route
@app.route("/sendMail")
def sendMail():
    # sending mail with smtp server

    key = request.args.get("key")
    filename = request.args.get("filename")
    msg = Message('Your file is ready', sender = 'travellingdiaries2019@gmail.com', recipients = ['jazzelmehmood6@gmail.com'])
    msg.body = f"Key = {key} \nEnjoy !!"
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER']) + f"/{filename}"
    print(uploads)
    with app.open_resource(uploads) as fp:        
        msg.attach("file.txt", "text/txt", fp.read())
    mail.send(msg)
    return redirect(url_for('index'))