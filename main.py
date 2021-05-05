import streamlit as st
import numpy as np
import pandas as pd
import webbrowser


st.title(' Pildorica de Streamlit')

st.sidebar.date_input('Date input')
st.sidebar.time_input('Time entry')
url = 'https://github.com/rusgar/Pildora_Streamlit/'

if st.sidebar.button('Github'):
    webbrowser.open_new_tab(url)
    

DATE_TIME = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(100000)

# hour = 10
# hour = st.selectbox('selecciona la hora', range(0,24),1)
hour = st.slider ('selecciona la hora', 0,24,10,1)
data = data [data[DATE_TIME].dt.hour == hour ]

if st.checkbox('Vista de datos'):
     st.subheader('Datos de solo %sh'% hour)   
     st.write(data)

st.subheader('Datos por minutos a %sh'% hour)
st.bar_chart(np.histogram(data[DATE_TIME].dt.minute, bins = 60, range = (0,60))[0])

st.subheader('Mapa de datos a %sh'% hour)  
st.map (data)
