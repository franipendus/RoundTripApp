import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Ad Information')

st.write("### Your ads:")
num = st.number_input('Advertiser ID', min_value=1, max_value=5, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/a/advertisers/adinfo/{num}').json()
st.table(results)

if st.button('Post an Ad'):
    st.write('finish this')


st.write("### Want the information about a specific ad?")
num = st.number_input('Ad ID', min_value=1, max_value=10, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/a/advertisers/adinfospecific/{num}').json()
st.table(results)