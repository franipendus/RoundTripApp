import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Deal Information')

st.write("### Your deals:")
num = st.number_input('Deal Administrator ID', min_value=1, max_value=50, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/d/dealadmin/deals/{num}').json()
st.table(results)

if st.button('Post an Deal'):
    st.write('finish this')


st.write("### Want the information about a specific deal?")
num = st.number_input('Deal ID', min_value=1, max_value=100, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/d/dealadmin/dealinfospecific/{num}').json()
st.table(results)