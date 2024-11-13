import streamlit as st
st.slider('Grau de satisfação', 0,100)
numero=st.slider ('Selecionar um número', min_value=0, max_value=100)
st.text('Seu número é' + str(numero))
