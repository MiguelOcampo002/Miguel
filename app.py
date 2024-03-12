import streamlit as st
from PIL import Image

st.title ("La Otra Ciudad") 

st.header ("En este espacio podrás obtener información de La Otra Ciudad")

image= Image.open('LOC.png')
st.image(image, caption="La Otra Ciudad, Logo")
st.write("Colectivo de jóvenes, very well")
st.write("Ingresa al link para visualizar data [link] (https://demo.thingsboard.io/dashboards/5ee36a30-e0a2-11ee-8542-2546a9cc72d5")
