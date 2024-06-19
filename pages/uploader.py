import streamlit as st
import pickle
from ftplib import FTP

# Set the page configuration to wide layout
st.set_page_config(layout="wide")

# Load saved FTP connection details from 'temp.bin' file
with open("temp.bin", "rb") as f:
    data = pickle.load(f)

# Extract connection details from loaded data
user = data['user']
host = data['host']
password = data['password']

# Establish FTP connection using loaded credentials
ftp = FTP(host)
ftp.login(user, password)

# File uploader in Streamlit UI for uploading files
files = st.file_uploader("UPLOAD FILES", accept_multiple_files=True)

# Button to initiate file upload
button = st.button("UPLOAD!")

if button:
    if files:
        for file in files:

            # Display a spinner while uploading each file
            with st.spinner("uploading..."):

                # Write the contents of the file to the FTP server
                ftp.storbinary(f'STOR {str(file.name)}', file)

            # Display success message after successful upload
            st.success(f"done uploading {str(file.name)}!")

        # Show balloons animation to indicate successful upload(s)
        st.balloons()

close = st.button("CLOSE CONNECTION!")
if close:
    ftp.quit()