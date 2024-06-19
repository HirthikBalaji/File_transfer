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

# List files on the FTP server
file = ftp.nlst()

# Initialize an empty list to store file options for selection
list_options = []

# Populate the list with filenames retrieved from the server
for i in file:
    list_options.append(i)

# Create a selectbox in Streamlit to choose a filename
option = st.selectbox("filename", list_options)

# Button to initiate file download
button = st.button("DOWNLOAD")
if button:

    # Display a spinner while downloading
    with st.spinner("DOWNLOADING!!"):

        # Open a local file and retrieve binary data from the FTP server
        with open(f"DATAPATH/{option}", 'wb') as f:
            ftp.retrbinary('RETR ' + option, f.write)

        # Display success message after successful download
        st.success("DONE DOWNLOAD!")

        # Show balloons animation to indicate success
        st.balloons()

close = st.button("CLOSE CONNECTION!")
if close:
    ftp.quit()
