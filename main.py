import streamlit as st
from ftplib import FTP
import pickle
st.set_page_config(layout="wide")
host = st.text_input("host")
user = st.text_input("User")
password = st.text_input("Password", type='password')
data = {
    'host': host,
    'user': user,
    'password': password
}
conn = st.button("CONNECT!")
if conn:
    try:
        ftp = FTP(host)
        ftp.login(user, password)
        with open("temp.bin", 'wb') as file:
            pickle.dump(data, file)
        ftp.quit()
        st.success("LOGGED IN")
        st.page_link("pages/downloader.py", label="DOWNLOAD!")
        st.page_link("pages/uploader.py", label="UPLOAD!")
    except Exception as e:
        st.error(e)


