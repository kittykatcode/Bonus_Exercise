import streamlit as st
from PIL import Image

st.header('colour to grey image')

uploaded_image = st.file_uploader('Upload Image')

with st.expander('start Camera'):
    camera_image = st.camera_input('Camera')


if camera_image:
    img = Image.open(camera_image)
    gry_img = img.convert('L')
    st.image(gry_img)
if uploaded_image:
    img = Image.open(uploaded_image)
    gry_img = img.convert('L')
    st.image(gry_img)
