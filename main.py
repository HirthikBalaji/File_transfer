import os

import streamlit as st

st.set_page_config(layout="wide")
st.header("WELCOME!")

Data = os.listdir("DATAPATH")
option = st.selectbox(
    label="Available files...",
    options=tuple(Data))
with open(f"DATAPATH/{option}",'rb') as file:
    st.download_button(label="DOWNLOAD",data=file,file_name=option)
files = st.file_uploader(label="UPLOAD FILES",accept_multiple_files=True)
submit_btn = st.button("Submit")
if submit_btn:
    for file in files:
        with open(f"DATAPATH/{file.name}", "wb") as file_obj:
            file_obj.write(file.getvalue())