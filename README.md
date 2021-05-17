# HU-DSA-Project

## Semester 2 Project - Data Structurees & Algorithms

### Encryptor &nbsp;&nbsp;[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg) &nbsp;![GitHub release](https://img.shields.io/github/release/Jazz-hash/HU-PFun-Project)](https://github.com/Jazz-hash/HU-PFun-Project)

#### URL: [https://hu-encryptor.herokuapp.com/](https://hu-encryptor.herokuapp.com/)

#### Environment: &nbsp; [![Python](https://img.shields.io/badge/Python-3.2%20and%20above-blue.svg)](https://pypi.org/project/pip/)

#### Tested and verified by github actions: &nbsp; [![DSA Project](https://github.com/Jazz-hash/HU-DSA-Project/actions/workflows/main.yml/badge.svg)](https://github.com/Jazz-hash/HU-DSA-Project/actions/workflows/main.yml)

## Description

In cryptography, encryption is the process of transforming information (referred to as plaintext) using an algorithm (called cipher) to make it unreadable to anyone except those possessing special knowledge, usually referred to as a key. We are applying the same approach but not using any encrypting algorithm but instead of that making our own depending upon Data structures, sorting algorithms, and One-Hot-Encoding logic. Our algorithm will be connected to a web app that can be accessed through any OS and furthermore the user just has to upload text files and the rest is on us.

## Algorithm Logic

The algorithm we used to implement this logic:

- First we create a random, or user provides us, the key.
- Secondly, we start reading the file and convert the file to words. We then apply frequency algorithm and obtain the frequency that is most repetitive in the file.
- Then we do some special-secret stuff to the words having that frquency ( which we can't tell u for the security of our algorithm ) hiding the key inside that word and finally merge the words again. Giving up the encrypted secure text. This key can also be provided by the user.
  **Note**: This algorithm is just for knowledge purposes. We use DSA and python techniques to evolve the text in the encryption form. Don't use it for higher encryption purposes SHA-256 is always better than our algorithm.

## Components:

- Web UI ( Frontend )
- Algorithms - Sorting, Data structures ( Backend )

## Frameworks/Libraries used:

- Web is built on Python Web Framework - Flask
- Algorithms are written on core Python

## Challenges:

- The first challenge is to handle all the encryption with faster and scalable algorithms. Not to take a lot of time of the user by implementing a lot of code.
- Second challenge is to make a hybrid-responsive web app that will work on any platform.

## Project Goals:

- Our goal is to provide a faster and more secure encryption algorithm that will help people encrypt not just messages but whole paragraphs and even large text files at primary level (not advanced).
- Our secondary goal is to provide this algorithm to people on every platform by removing the operating systems' (windows/Linux/macOS/android/ios) limits and boundaries.

## Prerequisite

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

- python and pip ( version = "\*" )

  Visit [https://www.python.org/](https://www.python.org/) and download any version of python for your operating system.
  Open command prompt/powershell/terminal in default python environment.

  ```
  # For verification open command prompt or terminal and run
  python --version
  Output: Python 3.x.x
  ```

- pipenv ( version = "\*" )
  ```
  pip install pipenv
  # Again for verification
  pipenv --version
  Output: pipenv, version 2020.x.x
  ```

## Available Scripts

- Download Project files

  - Clone using git
    ```
    git clone https://github.com/Jazz-hash/HU-DSA-Project
    cd HU-DSA-Project/
    ```
    #### Or
  - Download the repository from [https://github.com/Jazz-hash/HU-DSA-Project](https://github.com/Jazz-hash/HU-DSA-Project) then move to the directory where you downloaded or cloned the repository and cd into project directory.

    `cd HU-DSA-Project-main/`

- Install dependencies via your powershell/terminal/cmd.
  ```
  pipenv install -r requirements.txt
  ```
- Launching in project's virtual environment
  ```
  pipenv shell
  ```
- Testing
  ```
  python test.py
  Output: Test Passed ! All libraries working.
  ```
- Importing variables
  - For linux users
    `export FLASK_APP=app/server.py && export FLASK_ENV=development`
  - For windows users
    `SET FLASK_APP=app/server.py ; SET FLASK_ENV=development`
- Now for the final step

  ```
  flask run
  Output:
   * Serving Flask app "app/server.py" (lazy loading)
   * Environment: development
   * Debug mode: on
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   * Restarting with inotify reloader
   * Debugger is active!
   * Debugger PIN: 164-091-533
  ```

- Open browser and enter address [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and hit enter.

### Magic happens !!

- Refer to **Application Usage** (given below) for instructions or go through the Project Manual located in **docs** folder on how to use this efficient tool.
- Docs: `cd <project-main-directory>/docs/`
  - Project-Report.pdf
  - Project-Manual.pdf
