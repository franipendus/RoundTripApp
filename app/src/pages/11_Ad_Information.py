import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Ad Information')

# shows user their posted ads 
st.write("### Your ads:")
id = st.session_state['id']
results = requests.get(f'http://api:4000/a/advertisers/adinfo/{id}').json()
st.table(results)

# shows information about a specific ad for the user 
st.write("### Want the information about a specific ad?")
options = requests.get(f'http://api:4000/a/advertisers/adids/{id}').json()

ids = []

for i in options:
    ids.append(int(i['Ad ID'])) 


num = st.selectbox('Ad ID', 
                       ids,                  
                    label_visibility="visible")



results = requests.get(f'http://api:4000/a/advertisers/adinfospecific/{id}/{num}').json()
st.table(results)