#!/usr/bin/env python3

import pickle
import os
from ftplib import FTP
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

with open("temp.bin", "rb") as f:
    data = pickle.load(f)

# Extract connection details from loaded data
user = data['user']
host = data['host']
password = data['password']

@app.route('/uploader.py', methods=['POST'])
def upload_file():
    ftp_server = host
    ftp_user = user
    ftp_password = password

    ftp = FTP(ftp_server)
    ftp.login(ftp_user, ftp_password)

    uploaded_file = request.files['file']
    filename = uploaded_file.filename
    file_path = os.path.join('/path/to/ftp/directory/', filename)

    with open(file_path, 'wb') as file:
        uploaded_file.save(file_path)
        ftp.storbinary('STOR ' + filename, open(file_path, 'rb'))

    ftp.quit()
    return 'File uploaded successfully!'


if __name__ == '__main__':
    app.run(debug=True)
