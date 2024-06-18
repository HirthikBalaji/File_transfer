import streamlit as st
from ftplib import FTP

ftp = FTP("localhost")
ftp.login()
st.set_page_config(layout="wide")

option = st.selectbox("DIRECTORY", ["Music", "Downloads", "Movies", "Documents"])
if option:
    ftp.cwd("/")
    ftp.cwd(f"/{option}")
    file = ftp.nlst()
    l = []
    for i in file:
        l.append(str(i))
    file = st.selectbox("FILES", l)
