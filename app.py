import streamlit as st
from PIL import Image

st.title ("LOC") 

st.header ("En este espacio podrás obtener información de La Otra Ciudad")

image= Image.open('LOC.pn')
st.image(image, caption="La Otra Ciudad, Logo")
st.write("Colectivo de jóvenes, very well")
