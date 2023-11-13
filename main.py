import streamlit as st
from PIL import Image

#Start the camera
with st.expander("Start the camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    #create a pilow image instance
    img = Image.open(camera_image)

    #convert the pilow image to gray scale
    gray_image = img.convert("L")

    #Render image
    st.image(gray_image)
