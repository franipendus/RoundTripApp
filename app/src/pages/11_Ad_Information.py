import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Ad Information')
if st.button('Post an Ad'):
    st.switch_page('pages/13_Post_Ad.py')

if st.button('Delete an Ad'):
    st.switch_page('pages/14_Delete_Ad.py')

st.write("### Your ads:")
id = st.session_state['id']
results = requests.get(f'http://api:4000/a/advertisers/adinfo/{id}').json()
st.table(results)


st.write("### Want the information about a specific ad?")
num = st.number_input('Ad ID', min_value=1, max_value=10, value= 1,                  
                    label_visibility="visible")
results = requests.get(f'http://api:4000/a/advertisers/adinfospecific/{id}/{num}').json()
st.table(results)