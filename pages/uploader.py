import streamlit as st
import pickle
from ftplib import FTP
with open("temp.bin", "rb") as f:
    data = pickle.load(f)
user = data['user']
host = data['host']
password = data['password']

ftp = FTP(host)
ftp.login(user, password)

files = st.file_uploader("UPLOAD FILES", accept_multiple_files=True)
button = st.button("UPLOAD!")
if button:
    if files:
        for file in files:
            with st.spinner("uploading..."):
                st.write(file.name)
                ftp.storbinary(f'STOR {str(file.name)}', file)
            st.success(f"done uploading {str(file.name)}!")
        st.balloons()
