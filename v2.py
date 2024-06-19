import streamlit as st
from ftplib import FTP

ftp = FTP("localhost")
ftp.login()
st.set_page_config(layout="wide")

option = st.selectbox("DIRECTORY", ftp.nlst())
st.write(option)
button = st.button("Download")
if button:
    with st.spinner(f'Downloading.. {option}'):
        ftp.retrbinary("RETR " + option, open(option, 'wb').write)
