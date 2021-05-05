import streamlit as st


st.title(' Pildorica de Streamlit')

with st.echo():
    x=35
    
with st.echo():
    y=110

with st.echo():
    z = x+y
    st.write(z)
     
with st.echo():
    z = x*y
    st.write(z)

