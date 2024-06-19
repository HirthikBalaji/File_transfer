import streamlit as st
from ftplib import FTP
import pickle

# Set the page configuration to wide layout
st.set_page_config(layout="wide")

# Input fields for FTP connection details
host = st.text_input("host")
user = st.text_input("User")
password = st.text_input("Password", type='password')

# Data dictionary to store connection details
data = {
    'host': host,
    'user': user,
    'password': password
}

# Button to initiate the connection
conn = st.button("CONNECT!")
if conn:
    try:
        # Attempt to establish FTP connection using provided credentials
        ftp = FTP(host)
        ftp.login(user, password)

        # If connection successful, save connection details to a temporary file
        with open("temp.bin", 'wb') as file:
            pickle.dump(data, file)

        # Close FTP connection
        ftp.quit()

        # Display success message if login is successful
        st.success("LOGGED IN")

        # Display links to downloader and uploader pages
        st.page_link("pages/downloader.py", label="DOWNLOAD!")
        st.page_link("pages/uploader.py", label="UPLOAD!")

    except Exception as e:
        # Display error message if connection or login fails

        st.error(e)


