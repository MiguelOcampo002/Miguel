import streamlit as st
from PIL import Image

st.title ("LOC") 

st.header ("En este espacio podrás obtener información de La Otra Ciudad")

image=image.open("LOC_Logo_04.jpg")
st.image(image, caption="La Otra Ciudad, Logo")
st.write("Colectivo de jóvenes, very well")
