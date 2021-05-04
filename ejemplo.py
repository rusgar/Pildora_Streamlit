import streamlit as st


st.title(' Pildoraca chunga de Streamlit')

with st.echo():
    x=15
    
with st.echo():
    y=60

with st.echo():
    z = x+y
    st.write(z)  

