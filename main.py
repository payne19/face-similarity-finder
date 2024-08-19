import streamlit as st
from deepface import DeepFace
import tempfile
import os

st.title("Face Similarity Finder")

uploaded_file_1 = st.file_uploader("Please upload the first image", type=["jpg", "jpeg", "png"])
uploaded_file_2 = st.file_uploader("Please upload the second image", type=["jpg", "jpeg", "png"])

if uploaded_file_1 is not None and uploaded_file_2 is not None:
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_file_1, caption='First Image', use_column_width=True)
    with col2:
        st.image(uploaded_file_2, caption='Second Image', use_column_width=True)

def save_uploaded_file_to_temp(file):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(file.read())
    temp_file.close()
    return temp_file.name

if uploaded_file_1 is not None and uploaded_file_2 is not None:
    with st.spinner("Calculating similarity..."):
        temp_file_path_1 = save_uploaded_file_to_temp(uploaded_file_1)
        temp_file_path_2 = save_uploaded_file_to_temp(uploaded_file_2)

        result = DeepFace.verify(temp_file_path_1, temp_file_path_2)

        os.remove(temp_file_path_1)
        os.remove(temp_file_path_2)

        similarity_percentage = (1 - result['distance']) * 100
        st.success(f"The similarity between the two faces is {similarity_percentage:.2f}%")
