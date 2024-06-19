import streamlit as st
from ftplib import FTP

ftp = FTP("localhost")
ftp.login()
st.set_page_config(layout="wide")

option = st.selectbox("DIRECTORY", ftp.nlst())
st.write(option)
st.markdown(f'<a href="http://192.168.1.6:21/{option}">Hi!</a>', unsafe_allow_html=True)