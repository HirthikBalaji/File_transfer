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
file = ftp.nlst()
l = []
for i in file:
    l.append(i)
option = st.selectbox("filename", l)
button = st.button("DOWNLOAD")
if button:
    with st.spinner("DOWNLOADING!!"):
        with open(option, 'wb') as f:
            ftp.retrbinary('RETR ' + option, f.write)
        st.success("DONE DOWNLOAD!")
        st.balloons()
